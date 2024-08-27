import subprocess

def execute(script: str) -> None:
    exec(open(script, "r").read())