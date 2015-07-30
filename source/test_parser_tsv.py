#!/bin/env python
import sys
from antlr4 import FileStream, CommonTokenStream
from tsv import *
 
def main(argv):
    tree = getTree(argv[1])
    print(tree.toStringTree().replace('\\n', '\n'))
    print(process_dance_source(tree))

def getTree(filename):
    input = FileStream(filename)
    lexer = TSVLexer(input)
    stream = CommonTokenStream(lexer)
    parser = TSVParser(stream)
    tree = parser.r()
    return tree

def process_dance_source(tree):
    source_data = {}
    # title, subtitle, editor, home_url, base_url, date_entered, date_modified, publisher, date_published, isbn, thanks
    for metadatum in tree.pair():
        key = metadatum.ID().symbol.text
        value = metadatum.VALUE().symbol.text
        source_data[key] = value;
    # events #TODO -- add multiple as list
    #source_events = [event.eventData().VALUE().symbol.text for event in tree.event()]
    #source_data['events'] = source_events
    # dances
    rows = [[f.symbol.text for f in row.FIELD()] for row in tree.row()]
    source_data['rows'] = rows
    return source_data

if __name__ == '__main__':
    main(sys.argv)
