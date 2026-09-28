"""WorkCode utilities for BlendTwril.

Provides small helpers for running Windows CMD commands and Python code.
"""

import subprocess
import sys

VERSION = "1.0.0"


def run_cmd(command):
    """Run a Windows CMD command and return its exit code."""
    if not command:
        return 0
    result = subprocess.run(command, shell=True)
    return result.returncode


def run_python(code):
    """Execute a Python code string in a fresh main-style namespace."""
    if not code:
        return 0

    try:
        exec(code, {"__name__": "__main__"})
        return 0
    except Exception as error:
        print(f"Python error: {error}")
        return 1


def open_cmd():
    """Open a Windows Command Prompt window."""
    return subprocess.Popen(["cmd.exe"])


def open_python():
    """Open the current Python interpreter."""
    return subprocess.Popen([sys.executable])


if __name__ == "__main__":
    print(f"WorkCode {VERSION}")
    print("Usage:")
    print("  workcode.py cmd <command>")
    print("  workcode.py python <code>")

    if len(sys.argv) >= 3:
        mode = sys.argv[1].lower()
        value = " ".join(sys.argv[2:])

        if mode == "cmd":
            raise SystemExit(run_cmd(value))
        elif mode == "python":
            raise SystemExit(run_python(value))
