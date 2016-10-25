class Block:
    def __init__(self, url, vulnerabilities):
        self.url = url
        self.vulnerabilities = vulnerabilities


def contains_block(blocks, block):
    for b in blocks:
        try:
            if block[1].strip() in b:
                return True
        except:
            return False
    return False


def get_blocks(filename):
    blocks = list()
    block = list()
    with open(filename, 'r') as fd:
        for line in fd:
            if not line.strip():
                blocks.append(block)
                block = list()
            else:
                block.append(line)
    return blocks

ha = set()
def has_vulnerability(block):
    ha.add(tuple(block))
    for entry in block:
        if 'vulnera' in entry:
            return True
    return False


def count_vulnerable_repos(blocks):
    counter = 0
    for block in blocks:
        if has_vulnerability(block):
            counter += 1
    return counter


def get_repos(filename):
    repos = set()
    with open(filename, 'r') as fd:
        for line in fd:
            if 'https' in line:
                repos.add(line)
    return repos


if __name__ == '__main__':
    filename = 'scan.pyt'
    print(get_repos(filename))
    print(len(get_repos(filename)))
    blocks = get_blocks(filename)
    print(count_vulnerable_repos(blocks))
    print(len(ha))
