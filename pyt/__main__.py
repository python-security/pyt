"""The comand line module of PyT."""

import os
import sys

from .analysis.constraint_table import initialize_constraint_table
from .analysis.fixed_point import analyse
from .cfg import make_cfg
from .core.ast_helper import generate_ast
from .core.project_handler import (
    get_directory_modules,
    get_modules
)
from .formatters import (
    json,
    text
)
from .usage import parse_args
from .vulnerabilities import (
    find_vulnerabilities,
    get_vulnerabilities_not_in_baseline,
    UImode
)
from .web_frameworks import (
    FrameworkAdaptor,
    is_django_view_function,
    is_flask_route_function,
    is_function,
    is_function_without_leading_
)


def discover_files(directory_path, excluded_files):
    file_list = []
    excluded_list = excluded_files.split(",")

    for root, dirs, files in os.walk(directory_path):
        for f in files:
            fullpath = os.path.join(root, f)
            if os.path.splitext(fullpath)[1] == '.py' and fullpath.split("/")[-1] not in excluded_list:
                file_list.append(fullpath)

    return(file_list)


def main(command_line_args=sys.argv[1:]):
    args = parse_args(command_line_args)

    ui_mode = UImode.NORMAL
    if args.interactive:
        ui_mode = UImode.INTERACTIVE
    elif args.trim_reassigned_in:
        ui_mode = UImode.TRIM

    path = os.path.normpath(args.filepath)
    directory_path = os.path.normpath(args.recursive)
    excluded_files = args.excluded_paths
    test = discover_files(directory_path, excluded_files) #just for see files in directory
    print(test)

    if args.ignore_nosec:
        nosec_lines = set()
    else:
        file = open(path, 'r')
        lines = file.readlines()
        nosec_lines = set(
            lineno for
            (lineno, line) in enumerate(lines, start=1)
            if '#nosec' in line or '# nosec' in line
        )

    if args.project_root:
        directory = os.path.normpath(args.project_root)
    else:
        directory = os.path.dirname(path)
    project_modules = get_modules(directory)
    local_modules = get_directory_modules(directory)

    tree = generate_ast(path)

    cfg = make_cfg(
        tree,
        project_modules,
        local_modules,
        path
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
    analyse(cfg_list)
    vulnerabilities = find_vulnerabilities(
        cfg_list,
        ui_mode,
        args.blackbox_mapping_file,
        args.trigger_word_file,
        nosec_lines
    )

    if args.baseline:
        vulnerabilities = get_vulnerabilities_not_in_baseline(
            vulnerabilities,
            args.baseline
        )

    if args.json:
        json.report(vulnerabilities, args.output_file)
    else:
        text.report(vulnerabilities, args.output_file)


if __name__ == '__main__':
    main()
