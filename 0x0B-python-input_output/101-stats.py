#!/usr/bin/python3

"""Define function read from stdin"""

import sys

status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
code_counts = {code: 0 for code in status_codes}
total_size = 0
line_count = 0


def print_stats():
    """Print size of file"""
    print("File size: {}".format(total_size))
    for code in sorted(code_counts.keys()):
        if code_counts[code] > 0:
            print("{}: {}".format(code, code_counts[code]))


try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        size = int(parts[-1])
        total_size += size
        code = int(parts[-2])
        if code in code_counts:
            code_counts[code] += 1
        if line_count % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    print_stats()
    raise

print_stats()
