#!/bin/env python
import sys
import tsv
from pprint import pprint
 
def main(argv):
    data = tsv.load_file(argv[1])
    pprint(data)

if __name__ == '__main__':
    main(sys.argv)
