import json


def get_vulnerabilities_not_in_baseline(vulnerabilities, baseline):
	baseline = json.load(open(baseline))
	output = list()
	vulnerabilities =[vuln for vuln in vulnerabilities]
	for vuln in vulnerabilities:
		if vuln.as_dict() not in baseline['vulnerabilities']:
			output.append(vuln)
	return(output)
