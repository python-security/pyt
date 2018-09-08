"""The comand line module of PyT."""

import logging
import os
import sys
from collections import defaultdict

from .analysis.constraint_table import initialize_constraint_table
from .analysis.fixed_point import analyse
from .cfg import make_cfg
from .core.ast_helper import generate_ast
from .core.project_handler import (
    get_directory_modules,
    get_modules
)
from .usage import parse_args
from .vulnerabilities import (
    find_vulnerabilities,
    get_vulnerabilities_not_in_baseline
)
from .vulnerabilities.vulnerability_helper import SanitisedVulnerability
from .web_frameworks import (
    FrameworkAdaptor,
    is_django_view_function,
    is_flask_route_function,
    is_function,
    is_function_without_leading_
)

log = logging.getLogger(__name__)


def discover_files(targets, excluded_files, recursive=False):
    included_files = list()
    excluded_list = excluded_files.split(",")
    for target in targets:
        if os.path.isdir(target):
            for root, _, files in os.walk(target):
                for file in files:
                    if file.endswith('.py') and file not in excluded_list:
                        fullpath = os.path.join(root, file)
                        included_files.append(fullpath)
                        log.debug('Discovered file: %s', fullpath)
                if not recursive:
                    break
        else:
            if target not in excluded_list:
                included_files.append(target)
                log.debug('Discovered file: %s', target)
    return included_files


def retrieve_nosec_lines(
    path
):
    file = open(path, 'r')
    lines = file.readlines()
    return set(
        lineno for
        (lineno, line) in enumerate(lines, start=1)
        if '#nosec' in line or '# nosec' in line
    )


def main(command_line_args=sys.argv[1:]):  # noqa: C901
    args = parse_args(command_line_args)

    logging_level = (
        logging.ERROR if not args.verbose else
        logging.WARN if args.verbose == 1 else
        logging.INFO if args.verbose == 2 else
        logging.DEBUG
    )
    logging.basicConfig(level=logging_level, format='[%(levelname)s] %(name)s: %(message)s')

    files = discover_files(
        args.targets,
        args.excluded_paths,
        args.recursive
    )

    nosec_lines = defaultdict(set)

    if args.project_root:
        directory = os.path.normpath(args.project_root)
        project_modules = get_modules(directory, prepend_module_root=args.prepend_module_root)

    cfg_list = list()
    for path in sorted(files):
        log.info("Processing %s", path)
        if not args.ignore_nosec:
            nosec_lines[path] = retrieve_nosec_lines(path)

        if not args.project_root:
            directory = os.path.dirname(path)
            project_modules = get_modules(directory, prepend_module_root=args.prepend_module_root)

        local_modules = get_directory_modules(directory)
        tree = generate_ast(path)

        cfg = make_cfg(
            tree,
            project_modules,
            local_modules,
            path,
            allow_local_directory_imports=args.allow_local_imports
        )
        cfg_list = [cfg]

        framework_route_criteria = is_flask_route_function
        if args.adaptor:
            if args.adaptor.lower().startswith('e'):
                framework_route_criteria = is_function
            elif args.adaptor.lower().startswith('p'):
                framework_route_criteria = is_function_without_leading_
            elif args.adaptor.lower().startswith('d'):
                framework_route_criteria = is_django_view_function

        # Add all the route functions to the cfg_list
        FrameworkAdaptor(
            cfg_list,
            project_modules,
            local_modules,
            framework_route_criteria
        )

    initialize_constraint_table(cfg_list)
    log.info("Analysing")
    analyse(cfg_list)
    log.info("Finding vulnerabilities")
    vulnerabilities = find_vulnerabilities(
        cfg_list,
        args.blackbox_mapping_file,
        args.trigger_word_file,
        args.interactive,
        nosec_lines
    )

    if args.baseline:
        vulnerabilities = get_vulnerabilities_not_in_baseline(
            vulnerabilities,
            args.baseline
        )

    args.formatter.report(vulnerabilities, args.output_file, not args.only_unsanitised)

    has_unsanitised_vulnerabilities = any(
        not isinstance(v, SanitisedVulnerability)
        for v in vulnerabilities
    )
    if has_unsanitised_vulnerabilities:
        sys.exit(1)


if __name__ == '__main__':
    main()
