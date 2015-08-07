#!/bin/env python
import sys
import yaml
 
def main(argv):
    data = yaml.load_file(argv[1])
    print(data)

if __name__ == '__main__':
    main(sys.argv)
