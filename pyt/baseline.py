import json

def get_vulnerabilities_not_in_baseline(vulnerabilities, baseline):
	baseline = json.load(open(baseline))

	output = list()
	vulnerabilities =[vuln.as_dict() for vuln in vulnerabilities]
	for vuln in vulnerabilities:
		if vuln not in baseline['vulnerabilities']:
			output.append(vuln)
	return(output)
