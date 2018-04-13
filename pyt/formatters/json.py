"""This formatter outputs the issues in JSON."""

import json
from datetime import datetime


def report(
    vulnerabilities,
    fileobj
):
    """
    Prints issues in JSON format.
    Args:
        vulnerabilities: list of vulnerabilities to report
        fileobj: The output file object, which may be sys.stdout
    """
    TZ_AGNOSTIC_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
    time_string = datetime.utcnow().strftime(TZ_AGNOSTIC_FORMAT)

    machine_output = {
        'generated_at': time_string,
        'vulnerabilities': [vuln.as_dict() for vuln in vulnerabilities]
    }

    result = json.dumps(
        machine_output,
        indent=4
    )

    with fileobj:
        fileobj.write(result)
