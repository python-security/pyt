import json


def get_vulnerabilities_not_in_baseline(
	vulnerabilities,
	baseline_file
):
	baseline = json.load(open(baseline_file))
	output = list()
	for vuln in vulnerabilities:
		if vuln.as_dict() not in baseline['vulnerabilities']:
			output.append(vuln)
	return(output)
