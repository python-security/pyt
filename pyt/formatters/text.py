"""This formatter outputs the issues as plain text."""


def report(
    vulnerabilities,
    fileobj
):
    """
    Prints issues in text format.

    Args:
        vulnerabilities: list of vulnerabilities to report
        fileobj: The output file object, which may be sys.stdout
    """
    number_of_vulnerabilities = len(vulnerabilities)
    with fileobj:
        if number_of_vulnerabilities == 0:
            fileobj.write('No vulnerabilities found.\n')
        elif number_of_vulnerabilities == 1:
            fileobj.write('%s vulnerability found:\n' % number_of_vulnerabilities)
        else:
            fileobj.write('%s vulnerabilities found:\n' % number_of_vulnerabilities)

        for i, vulnerability in enumerate(vulnerabilities, start=1):
            fileobj.write('Vulnerability {}:\n{}\n\n'.format(i, vulnerability))
