#!/bin/env python
import sys
from antlr4 import *
from antlr.DanceList_MedLex import DanceList_MedLex as DanceList_MedLexer
from antlr.DanceList_Med import DanceList_Med as DanceList_MedParser
 
def main(argv):
    tree = getTree(argv[1])
    print(tree.toStringTree().replace('\\n', '\n'))

def getTree(filename):
    input = FileStream(filename)
    lexer = DanceList_MedLexer(input)
    stream = CommonTokenStream(lexer)
    parser = DanceList_MedParser(stream)
    tree = parser.r()
    return tree

def process_dance_source(tree):
    source_data = {}
    # title, editor, home_url, base_url
    for metadatum in tree.pair():
        key = metadatum.ID().symbol.text
        value = metadatum.VALUE().symbol.text
        source_data[key] = value;
    # events
    source_events = [event.eventData().VALUE().symbol.text for event in tree.event()]
    source_data['events'] = source_events
    # dances
    def process_dance(dance_node):
        dance = {}
        # lo, ti, au, fo
        for metadatum in dance_node.pair():
            key = metadatum.ID().symbol.text
            value = metadatum.VALUE().symbol.text
            dance[key] = value
        # ev
        dance_events = [event.eventData().VALUE().symbol.text for event in dance_node.event2()]
        dance['ev'] = dance_events
        return dance
    
    dances = map(process_dance, tree.dance())
    source_data['dances'] = dances
    return source_data

if __name__ == '__main__':
    main(sys.argv)
