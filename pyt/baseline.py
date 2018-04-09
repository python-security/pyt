from pprint import pprint
import json


def isSame(res, base):
	if res == base:
		return(True)
	return(False)

def compare(results, baseline):

	baseline = json.load(open(baseline))
	#results = json.load(open(results))
	result = {'generated_at':results["generated_at"], 'vulnerabilities':[]}

	if "generated_at" in results and baseline:
		if not isSame(results["generated_at"], baseline["generated_at"]):
			pprint(results["generated_at"])

	if "vulnerabilities" in results and baseline:
		if not isSame(results["vulnerabilities"], baseline["vulnerabilities"]):
			for i in range(len(results["vulnerabilities"])):
				if results["vulnerabilities"][i] not in baseline["vulnerabilities"]:
					result["vulnerabilities"].append(results["vulnerabilities"][i])

	result = json.dumps(result, indent=4)
	print(result)
