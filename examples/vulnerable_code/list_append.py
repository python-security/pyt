import os

from flask import request


def func():
    TAINT = request.args.get("TAINT")

    cmd = []
    cmd.append("echo")
    cmd.append(TAINT)

    os.system(" ".join(cmd))
