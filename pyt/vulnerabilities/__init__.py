import json

from ..analysis.lattice import Lattice
from .trigger_definitions_parser import parse
from .vulnerabilities import find_vulnerabilities_in_cfg


def find_vulnerabilities(
    cfg_list,
    ui_mode,
    vulnerability_files
):
    """Find vulnerabilities in a list of CFGs from a trigger_word_file.

    Args:
        cfg_list(list[CFG]): the list of CFGs to scan.
        ui_mode(UImode): determines if we interact with the user or trim the nodes in the output, if at all.
        vulnerability_files(VulnerabilityFiles): contains trigger words and blackbox_mapping files

    Returns:
        A list of vulnerabilities.
    """
    vulnerabilities = list()
    definitions = parse(vulnerability_files.triggers)

    with open(vulnerability_files.blackbox_mapping) as infile:
        blackbox_mapping = json.load(infile)
    for cfg in cfg_list:
        find_vulnerabilities_in_cfg(
            cfg,
            definitions,
            Lattice(cfg.nodes),
            ui_mode,
            blackbox_mapping,
            vulnerabilities
        )
    with open(vulnerability_files.blackbox_mapping, 'w') as outfile:
        json.dump(blackbox_mapping, outfile, indent=4)

    return vulnerabilities
