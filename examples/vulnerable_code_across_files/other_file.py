import subprocess

def return_constant_string(easy_to_find_in_logs):
    no_vuln = "This is not a vuln"
    return no_vuln

def return_the_arg(easy_to_find_in_logs):
    hehe = 'bar' + easy_to_find_in_logs
    return hehe

def shell_the_arg(easy_to_find_in_logs):
    subprocess.call(easy_to_find_in_logs, shell=True)
