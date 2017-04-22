class Repo:
    def __init__(self, url=None, vulnerabilities=None):
        self.url = url
        self.vulnerabilities = vulnerabilities


class Vulnerability:
    def __init__(self):
        self.filename = None
        self.source = None
        self.sink = None
        self.source_line = None
        self.sink_source = None


def parse_vulnerabilities(file_descriptor):
    vulnerabilities = list()
    vulnerability = Vulnerability()
    for line in file_descriptor:
        next_line = next(file_descriptor)
        if line.strip() == '' and 'Vulnerability:' not in next_line:
            return vulnerabilities
        elif line.strip() == '':
            vulnerabilities.append(vulnerability)
            vulnerability = Vulnerability()
        else:
            if 'File:' in line:
                vulnerability.filename = line.split(':')[1].strip()
            elif ' > User input at line' in line:
                vulnerability.source = line.split('"')[-2]
                vulnerability.source_line = next_line
            elif ' > reaches line' in line:
                vulnerability.source = line.split('"')[-2]
                vulnerability.source_line = next_line


def get_repos(filename):
    repos = list()
    repo = Repo()
    previous_line = None
    with open(filename, 'r') as fd:
        for line in fd:
            next_line = next(fd)
            if not line.strip() == '' or 'Vulnera' in next_line:
                if 'https://' in line:
                    repo.url = line.strip()
                elif 'Vulnera' in next_line:
                    repo.vulnerabilities = parse_vulnerabilities(fd)
            elif next_line.strip() == '':
                    continue
            else:
                repos.append(repo)
                repo = Repo()
            previous_line = line
    return repos


def get_urls(filename):
    with open(filename, 'r') as fd:
        return sorted({line for line in fd if 'https' in line})


if __name__ == '__main__':
    filename = 'scan_results/archived_26_10_scan.pyt'
    filename = 'scan_results/test.pyt'
    repos = get_repos(filename)
    print([b.url for b in repos])
    print(len(repos))
