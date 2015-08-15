#!/bin/env python
import sys
import hybrid_loader as hyb
from pprint import pprint

def main(argv):
    data = hyb.load_file(argv[1])
    pprint(data)

if __name__ == '__main__':
    main(sys.argv)
