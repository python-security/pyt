# Make a regex for redirect(word), no quotes or anything.
# Run it on every file, see what it outputs, the ones that it is successful for we run PyT on.
# redirect(url_for('helpTopics'))

import csv 
import os
import re
import subprocess
from collections import namedtuple


# Part 1, make regex

# test_strings = [
# 	"redirect(url_for('helpTopics'))", # 1
# 	"redirect(hey)", # 2
# 	"redirect", # 3
# 	"hhredirect", # 4
# 	"return redirect(foo)", # 5
# 	"redirect(", # 6
# 	"redirect()", # 7
# 	"return redirect(request.GET.get('redirect',
					# '/taskManager/'))" # 8
# ]

# for i, string in enumerate(test_strings):
# 	match = re.match(".*redirect\([a-zA-Z0-9_]+\)", string)
# 	if match:
# 		print(str(i + 1)+" was a match.")
# 	request_as_arg = re.match(".*redirect\(request.*\)", string)	
# 	if request_as_arg:
# 		print(str(i + 1)+" was a match to request_as_arg.")

first_regex_vulns = set()
second_regex_vulns = set()

def test_match_with_regex(string, file_name):
	global first_regex_vulns
	global second_regex_vulns

	if string.strip().startswith('#'):
		return False

	variable_as_arg = re.match(".*redirect\([a-zA-Z0-9_]+\).*", string)
	if variable_as_arg:
		print(string + " was a match to variable_as_arg.")
		first_regex_vulns.add(
			VulnerabilityConfig(
				file_name=file_name,
				line_matching_regex=string.strip()
			)
		)
		return True

	request_as_arg = re.match(".*redirect\(request.*\).*", string)	
	if request_as_arg:

		# Maybe some guy on Hackerone would argue it was a vuln, but it's much lamer.
		just_the_referrer = re.match(".*redirect\(request\.referrer\).*", string)
		if just_the_referrer:
			return False

		just_the_url = re.match(".*redirect\(request\.url\).*", string)
		if just_the_url:
			return False

		print(string + " was a match to request_as_arg.")
		second_regex_vulns.add(
			VulnerabilityConfig(
				file_name=file_name,
				line_matching_regex=string.strip()
			)
		)
		return True

	return False


# Part 2, grab repos and run the regex on them.
# https://github.com/mattmakai/choose-your-own-adventure-presentations.git, /cyoa/views.py

def get_repo_name(url):
    """Obtains the repo name repo URL.
    This allows for local file saving, as compared to the URL, which indicates WHERE to clone from.

    :type url: string
    """
    # e.g. 'git@github.com:pre-commit/pre-commit-hooks' -> pre-commit-hooks
    name = url.split('/')[-1]

    # The url_or_path will still work without the `.git` suffix.
    if name.endswith('.git'):
        return name[:-4]

    return name


RepoConfig = namedtuple(
    'RepoConfig',
    [
        'repo_url',
        'controller_file'
    ]
)

VulnerabilityConfig = namedtuple(
    'VulnerabilityConfig',
    [
        'file_name',
        'line_matching_regex'
    ]
)

repo_config = RepoConfig(
	"https://github.com/mattmakai/choose-your-own-adventure-presentations.git",
	"/cyoa/views.py"
)


def clone_from_github(repo_config):

	import os
	import signal
	from subprocess import Popen, PIPE, TimeoutExpired
	from time import monotonic as timer

	start = timer()
	with Popen('git clone '+repo_config.repo_url, shell=True, stdout=PIPE, preexec_fn=os.setsid) as process:
		try:
			output = process.communicate(timeout=1)[0]
		except TimeoutExpired:
			os.killpg(process.pid, signal.SIGINT) # send signal to the process group
			output = process.communicate()[0]
		except subprocess.CalledProcessError as e:
			error_msg = e.output.decode('ascii')

			# Ignore this message, because it's expected if the repo has already been cloned.
			match = re.match(r"fatal: destination path '[^']+' already exists", error_msg)
			if not match:
				raise
			print("Repo destination already existed.")
	print('Elapsed seconds: {:.2f}'.format(timer() - start))

	# # Clone from Github
	# try:
	#     subprocess.check_output([
	#         'git',
	#         'clone',
	#         repo_config.repo_url,
	#     ],
	#     stderr=subprocess.STDOUT,
	#     timeout=2)



file_not_found_error_count = 0
boom_count = 0
possible_files = set()
unique_files = set()
possible_lines_first = set()
possible_lines_second = set()
def run_regex_on_repo_config(repo_config):
	# global vars
	global boom_count
	global file_not_found_error_count
	global possible_files
	global unique_files

	folder_name = get_repo_name(repo_config.repo_url)

	# The csv has some files that start with a slash, so we need to remove it.
	# path_to_file = os.path.join(folder_name, repo_config.controller_file)
	path_to_file = repo_config.controller_file
	if path_to_file in unique_files:
		return

	unique_files.add(path_to_file)
	try:
		with open(path_to_file) as foo:
			print("opened ", path_to_file)
			old_boom_count = boom_count
			for line in foo:
				if test_match_with_regex(line, file_name=path_to_file):
					print(path_to_file + " matches the regexes")
					print("Boom.")
					possible_files.add(path_to_file)
					boom_count = boom_count + 1
					break
			if old_boom_count == boom_count:
				print(path_to_file + " does not match the regexes")
	except FileNotFoundError:
		file_not_found_error_count = file_not_found_error_count + 1
		print("FileNotFoundError on ", path_to_file)


# See if the file matches the regex
# Print Success.
# Open flask_open_source_apps.csv,


# # BEGIN REGEX CODE
# FLASK_APPS_CSV = 'flask_open_source_apps.csv'
# flask_csv_reader = csv.reader(open(FLASK_APPS_CSV), delimiter=",")
# row_count = 0
# for row in flask_csv_reader:
# 	row_count = row_count + 1
# 	path_to_file = row[1].strip()
# 	repo_config = RepoConfig(
# 		repo_url=row[0].strip(),
# 		controller_file=path_to_file[1:] if path_to_file.startswith('/') else path_to_file
# 	)
# 	print("repo_config is ", repo_config)
# 	clone_from_github(repo_config)
# 	run_regex_on_repo_config(repo_config)

# print("file_not_found_error_count is", str(file_not_found_error_count))
# print("row_count is", str(row_count))
# print("boom_count is", str(boom_count))
# print("len(unique_files) is ", len(unique_files))
# print("len(possible_files) is ", len(possible_files))
# # End real code

# # print("possible_lines_first is ", possible_lines_first)
# for first_regex_vuln in first_regex_vulns:
# 	print("first_regex_vuln is", first_regex_vuln)
# for second_regex_vuln in second_regex_vulns:
# 	print("second_regex_vuln is", second_regex_vuln)
# # print("possible_lines_second is ", possible_lines_second)
# # END REGEX CODE











# I could generate a new CSV?
# Let me see where the current one gets us on boom_count
# So it gets us nowhere.



# FileNotFoundError on  flaskRestCrud/flaskRestCrud/project/__init__.py
# repo_config is  RepoConfig(repo_url='https://github.com/mustafawm/Flask-LocationApp', controller_file='Flask-LocationApp/routes.py')
# Cloning into 'Flask-LocationApp'...
# remote: Counting objects: 49, done.
# remote: Total 49 (delta 0), reused 0 (delta 0), pack-reused 49
# Unpacking objects: 100% (49/49), done.
# Checking connectivity... done.
# Elapsed seconds: 0.44
# FileNotFoundError on  Flask-LocationApp/Flask-LocationApp/routes.py
# repo_config is  RepoConfig(repo_url='https://github.com/Original-heapsters/FlaskPortal', controller_file='FlaskPortal/Portal_Main/app.py')
# Cloning into 'FlaskPortal'...
# remote: Counting objects: 253, done.
# remote: Total 253 (delta 0), reused 0 (delta 0), pack-reused 253
# Receiving objects: 100% (253/253), 186.70 KiB | 0 bytes/s, done.
# Resolving deltas: 100% (121/121), done.
# Checking connectivity... done.
# Elapsed seconds: 0.40
# FileNotFoundError on  FlaskPortal/FlaskPortal/Portal_Main/app.py
# repo_config is  RepoConfig(repo_url='https://github.com/neilmaldy/flask_upload', controller_file='flask_upload/test.py')
# Cloning into 'flask_upload'...
# remote: Counting objects: 20, done.
# remote: Total 20 (delta 0), reused 0 (delta 0), pack-reused 20
# Unpacking objects: 100% (20/20), done.
# Checking connectivity... done.
# Elapsed seconds: 0.35
# FileNotFoundError on  flask_upload/flask_upload/test.py
# file_not_found_error_count is 728
# row_count is 728

# path_to_file = 'Flask_SQLite/draw_member.py'
# with open(path_to_file) as foo:
# 	print("opened ", path_to_file)
# 	old_boom_count = boom_count
# 	for line in foo:
# 		print("line is ", line)
# 		if test_match_with_regex(line):
# 			print(path_to_file + " matches the regexes")
# 			print("Boom.")
# 			boom_count = boom_count + 1
# 			break
# 	if old_boom_count == boom_count:
# 		print(path_to_file + " does not match the regexes")



# file_not_found_error_count is 79
# row_count is 812
# boom_count is 34
# So how what was it 34/(812-79)
# # 4.6 percent matched the regexess
# # 34/733

# len(unique_files) is  20/(547-66) -> 20/481
# len(possible_files) is  20
# ~4.1 percent matched the regexes


# possible_files is  {'simple-web-proxy/app.py',
# 					'multunus-puzzle/src/app.py',
# 					'FLASKHW/directory.py',
# 					'flask-pastebin/pastebin.py',
# 					'python-indieweb/indieweb.py',
# 					'flask-oauthlib/flask_oauthlib/provider/oauth1.py',
# 					'flaskoktaapp/flaskoktaapp/__init__.py',
# 					'flask_shortener/app.py',
# 					'flask_upload/test.py',
# 					'twitter/hello.py',
# 					'rdflib-web/rdflib_web/lod.py',
# 					'cheapskate/cheapskate.py',
# 					'honest_site/run.py',
# 					'okta-pysaml2-example/app.py',
# 					'pandaflask_old/pandachrome.py',
# 					'oauth-flask-template/auth.py',
# 					'Flaskly/flaskly.py',
# 					'hb2_flask/hb2_flask.py',
# 					'social_project_flask/app.py',
# 					'Flask_SQLite/draw_member.py',
# 					'python-bookmark-service/app.py',
# 					'Flask_OAuth2/app.py',
# 					'cs125-fooddy-flask/fooddy2.py',
# 					'examples-flask/example_basic.py'
# 				   }
# Line matching regex 1 is return redirect(foo)
# Line matching regex 1 is return redirect(UPLOAD_ONION_URL)
# Line matching regex 1 is return redirect(target)
# Line matching regex 1 is return redirect(uri)
# Line matching regex 1 is return redirect(authorization_url)
# Line matching regex 1 is return redirect(link)
# Line matching regex 1 is return redirect(redirect_to)
# Line matching regex 1 is return redirect(url)
# Line matching regex 1 is return redirect(url)
# Line matching regex 1 is return redirect(link_target)
# Line matching regex 1 is return redirect(uri)
# Line matching regex 1 is return redirect(next_url)
# Line matching regex 1 is return redirect(url)
# Line matching regex 1 is return redirect(next)

# Line matching regex 2 is return redirect(request.url)
# Line matching regex 2 is return redirect(request.referrer or url_for('index'))
# Line matching regex 2 is return(redirect(request.referrer))
# Line matching regex 2 is # redirect(request.args.get('next') or url_for('index')) #allows login page to act as in between
# Line matching regex 2 is return redirect(request.referrer)
# Line matching regex 2 is return redirect(request.form["next"])
# Line matching regex 2 is return redirect(request.args.get("next") or url_for("index"))


# Finally I was left with the output:
# first_regex_vulns
# 	file_name='flaskoktaapp/flaskoktaapp/__init__.py',
# 	line_matching_regex='return redirect(url)'

# 	file_name='flask-pastebin/pastebin.py',
# 	line_matching_regex='return redirect(next_url)'

# 	file_name='flask_shortener/app.py',
# 	line_matching_regex='return redirect(link_target)'

# 	file_name='oauth-flask-template/auth.py',
# 	line_matching_regex='return redirect(next)'

# 	file_name='social_project_flask/app.py',
# 	line_matching_regex='return redirect(next_url)'

# 	file_name='flask-oauthlib/flask_oauthlib/provider/oauth1.py',
# 	line_matching_regex='return redirect(uri)'

# 	file_name='cs125-fooddy-flask/fooddy2.py',
# 	line_matching_regex='return redirect(auth_uri)')

# 	file_name='python-indieweb/indieweb.py',
# 	line_matching_regex='return redirect(url)'

# 	file_name='multunus-puzzle/src/app.py',
# 	line_matching_regex='return redirect(redirect_to)'

# 	file_name='hb2_flask/hb2_flask.py',
# 	line_matching_regex='return redirect(target)'

# 	file_name='Flask_OAuth2/app.py',
# 	line_matching_regex='return redirect(uri)'

# 	file_name='examples-flask/example_basic.py',
# 	line_matching_regex='return redirect(authorization_url)'

# 	file_name='Flaskly/flaskly.py',
# 	line_matching_regex='return redirect(link)'

# 	file_name='honest_site/run.py',
# 	line_matching_regex='return redirect(UPLOAD_ONION_URL)'

# 	file_name='cheapskate/cheapskate.py',
# 	line_matching_regex='return redirect(url)'

# 	file_name='okta-pysaml2-example/app.py',
# 	line_matching_regex='return redirect(url)'

# 	file_name='python-bookmark-service/app.py',
# 	line_matching_regex='return redirect(url)'

# second_regex_vulns
	# file_name='simple-web-proxy/app.py',
	# line_matching_regex='return redirect(request.args.get("next") or url_for("index"))'

	# file_name='twitter/hello.py',
	# line_matching_regex="return redirect(request.referrer or url_for('index'))"

	# file_name='pandaflask_old/pandachrome.py',
	# line_matching_regex='return redirect(request.form["next"])'

# 17 matching the first regex (5 'url', 2 'next_url', 2 'uri' and others)
# We cannot tell if they are vulnerable from looking at them.

# 3 matching the second_regex


interesting_files = set([
	'flaskoktaapp/flaskoktaapp/__init__.py', 
	'flask-pastebin/pastebin.py',
	'flask_shortener/app.py',
	'oauth-flask-template/auth.py',
	'social_project_flask/app.py',
	'flask-oauthlib/flask_oauthlib/provider/oauth1.py',
	'cs125-fooddy-flask/fooddy2.py',
	'python-indieweb/indieweb.py',
	'multunus-puzzle/src/app.py',
	'hb2_flask/hb2_flask.py',
	'Flask_OAuth2/app.py',
	'examples-flask/example_basic.py',
	'Flaskly/flaskly.py',
	'honest_site/run.py',
	'cheapskate/cheapskate.py',
	'okta-pysaml2-example/app.py',
	'python-bookmark-service/app.py',
	'simple-web-proxy/app.py',
	'twitter/hello.py',
	'pandaflask_old/pandachrome.py'
])

print("len of interesting_files is ", len(interesting_files))
for file in interesting_files:
	print('file is ', file)


flaskoktaapp/flaskoktaapp/__init__.py
# Ret

# Reports 0 vulns, (with edited flask trigger words)
# https://github.com/gene1wood/flaskoktaapp/blob/master/flaskoktaapp/__init__.py#L204
# although we don't currently have a Post-only Flask option.

#1 of 20, GOOD: true negative, not reported.
#2 of 20, 
# of 20, 
# of 20, 
# of 20, 
# of 20, 
# of 20, 
# of 20, 
# of 20, 
# of 20, 
# of 20, 
# of 20, 
# of 20, 
# of 20, 
# of 20, 












