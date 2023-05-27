import subprocess


def foo() -> None:
    pass


subprocess.Popen([], preexec_fn=foo)  # [subprocess-popen-preexec-fn]
