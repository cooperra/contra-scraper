#!/bin/env python
import sys
import tsv
 
def main(argv):
    data = tsv.load_file(argv[1])
    print(data)

if __name__ == '__main__':
    main(sys.argv)
