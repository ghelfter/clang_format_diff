""" Module for running an instance of the formatter. """

import subprocess

# Set the constant for timeout processes. This unit is in milliseconds.
TIMEOUT_CONSTANT = 20.0

def run_format(filepath, format_exe, tmp_path=None):
    out_path = None

    try:
        results = subprocess.run(format_exe, timeout=TIMEOUT_CONSTANT, stdout=subprocess.PIPE)
    except subprocess.TimeoutExpired:
        # Return None on error - diff command timed out for some reason
        return None

    if results.returncode == 0:
        pass

    return out_path
