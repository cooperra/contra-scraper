#!/bin/env python
import sys
from antlr4 import FileStream, CommonTokenStream
from yaml import *
 
def main(argv):
    tree = getTree(argv[1])
    print(tree.toStringTree().replace('\\n', '\n'))
    print(tree2dict(tree))

def getTree(filename):
    input = FileStream(filename)
    lexer = YAMLLexer(input)
    filteredSource = IndentTokenFilter(lexer)
    stream = CommonTokenStream(filteredSource)
    parser = YAMLParser(stream)
    tree = parser.r()
    return tree

def tree2dict(tree):
    def obj2dict(obj_node):
        obj_dict = {}
        for p in obj_node.pair():
            key = p.ID().symbol.text
            value = get_value(p.value())
            obj_dict[key] = value
        return obj_dict
    def get_value(val):
        if val.obj():
            return obj2dict(val.obj())
        elif val.VALUE():
            return val.VALUE().symbol.text
        elif val.listItem():
            return [get_value(item.value()) for item in val.listItem()]
    return obj2dict(tree.obj())


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
