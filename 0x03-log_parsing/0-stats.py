#!/usr/bin/python3
"""
- Module writes a script that reads stdin line by line and computes metrics
"""

import sys


if __name__ == '__main__':

    file_size = 0
    line_count = 0
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stat = {x: 0 for x in codes}

    def display_stats(stat: dict, file_size: int) -> None:
        print("File size: {:d}".format(file_size))
        for x, y in sorted(stat.items()):
            if y:
                print("{}: {}".format(x, y))

    try:
        for line in sys.stdin:
            line_count += 1
            split_parts = line.split()
            try:
                status_code = split_parts[-2]
                if status_code in stat:
                    stat[status_code] += 1
            except BaseException:
                pass
            try:
                file_size += int(split_parts[-1])
            except BaseException:
                pass
            if line_count % 10 == 0:
                display_stats(stat, file_size)
        display_stats(stat, file_size)
    except KeyboardInterrupt:
        display_stats(stat, file_size)
        raise
