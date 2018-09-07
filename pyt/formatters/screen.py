"""This formatter outputs the issues as color-coded text."""
from ..vulnerabilities.vulnerability_helper import SanitisedVulnerability, UnknownVulnerability

RESET = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
DANGER = '\033[31m'
GOOD = '\033[32m'
HIGHLIGHT = '\033[45;1m'
RED_ON_WHITE = '\033[31m\033[107m'


def color(string, color_string):
    return color_string + str(string) + RESET


def report(
    vulnerabilities,
    fileobj,
    print_sanitised,
):
    """
    Prints issues in color-coded text format.

    Args:
        vulnerabilities: list of vulnerabilities to report
        fileobj: The output file object, which may be sys.stdout
    """
    n_vulnerabilities = len(vulnerabilities)
    unsanitised_vulnerabilities = [v for v in vulnerabilities if not isinstance(v, SanitisedVulnerability)]
    n_unsanitised = len(unsanitised_vulnerabilities)
    n_sanitised = n_vulnerabilities - n_unsanitised
    heading = "{} vulnerabilit{} found{}.\n".format(
        'No' if n_unsanitised == 0 else n_unsanitised,
        'y' if n_unsanitised == 1 else 'ies',
        " (plus {} sanitised)".format(n_sanitised) if n_sanitised else "",
    )
    vulnerabilities_to_print = vulnerabilities if print_sanitised else unsanitised_vulnerabilities
    with fileobj:
        for i, vulnerability in enumerate(vulnerabilities_to_print, start=1):
            fileobj.write(vulnerability_to_str(i, vulnerability))

        if n_unsanitised == 0:
            fileobj.write(color(heading, GOOD))
        else:
            fileobj.write(color(heading, DANGER))


def vulnerability_to_str(i, vulnerability):
    lines = []
    lines.append(color('Vulnerability {}'.format(i), UNDERLINE))
    lines.append('File: {}'.format(color(vulnerability.source.path, BOLD)))
    lines.append(
        'User input at line {}, source "{}":'.format(
            vulnerability.source.line_number,
            color(vulnerability.source_trigger_word, HIGHLIGHT),
        )
    )
    lines.append('\t{}'.format(color(vulnerability.source.label, RED_ON_WHITE)))
    if vulnerability.reassignment_nodes:
        previous_path = None
        lines.append('Reassigned in:')
        for node in vulnerability.reassignment_nodes:
            if node.path != previous_path:
                lines.append('\tFile: {}'.format(node.path))
                previous_path = node.path
            label = node.label
            if (
                isinstance(vulnerability, SanitisedVulnerability) and
                node.label == vulnerability.sanitiser.label
            ):
                label = color(label, GOOD)
            lines.append(
                '\t  Line {}:\t{}'.format(
                    node.line_number,
                    label,
                )
            )
    if vulnerability.source.path != vulnerability.sink.path:
        lines.append('File: {}'.format(color(vulnerability.sink.path, BOLD)))
    lines.append(
        'Reaches line {}, sink "{}"'.format(
            vulnerability.sink.line_number,
            color(vulnerability.sink_trigger_word, HIGHLIGHT),
        )
    )
    lines.append('\t{}'.format(
        color(vulnerability.sink.label, RED_ON_WHITE)
    ))
    if isinstance(vulnerability, SanitisedVulnerability):
        lines.append(
            'This vulnerability is {}{} by {}'.format(
                color('potentially ', BOLD) if not vulnerability.confident else '',
                color('sanitised', GOOD),
                color(vulnerability.sanitiser.label, BOLD),
            )
        )
    elif isinstance(vulnerability, UnknownVulnerability):
        lines.append(
            'This vulnerability is unknown due to "{}"'.format(
                color(vulnerability.unknown_assignment.label, BOLD),
            )
        )
    return '\n'.join(lines) + '\n\n'
