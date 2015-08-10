#!/bin/env python
import sys
import yaml, tsv
from pprint import pprint

def main(argv):
    format_choices = {"yaml": yaml, "tsv": tsv}
    remaining_format_choices = set(format_choices.keys())
    format = guess_format(argv[1])
    remaining_format_choices.remove(format)
    while True:
        try:
            data = format_choices[format].load_file(argv[1])
        except Exception as e:
            if len(remaining_format_choices) > 0:
                # Load failed; try another format
                format = remaining_format_choices.pop()
            else:
                # Out of formats; fail
                raise e
        else:
            # Successful load
            break
    pprint(data)

def guess_format(filename):
    f = open(filename)
    line = f.readline()
    # Find first non-empty line
    while len(line) <= 1 and line != "":
        line = f.readline()
    if line == "":
        # Default to tsv if file empty
        return "tsv"
    elif line.startswith("#<"):
        return "tsv"
    elif line.find(":") != -1:
        return "yaml"
    else:
        # If no noticable pattern, just use tsv
        return "tsv"

if __name__ == '__main__':
    main(sys.argv)
