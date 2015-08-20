#!/bin/env python
import sys
import os
sys.path.insert(0, os.path.realpath(__file__).rpartition('/')[0].rpartition('/')[0])
import source
from pprint import pprint

def main(argv):
    data = source.load_file(argv[1])
    pprint(data)

if __name__ == '__main__':
    main(sys.argv)
