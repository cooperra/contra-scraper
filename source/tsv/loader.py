from .antlr_gen.TSVLexer import TSVLexer as Lexer
from .antlr_gen.TSVParser import TSVParser as Parser
from antlr4 import CommonTokenStream, FileStream
from collections import OrderedDict

class Loader:
    def __init__(self, inputstream=None):
        self.input = inputstream
        self.lexer = Lexer(self.input)
        self.cts = CommonTokenStream(self.lexer)
        self.parser = Parser(self.cts)

    def set_input(self, inputstream):
        self.input = inputstream
        self.lexer.inputStream = self.input
        self.reset()

    def reset(self):
        self.lexer.reset()
        self.cts.reset()
        self.parser.reset()

    def load(self):
        tree = self.parser.r()
        return self.tree2dict(tree)

    def load_file(self, filename):
        self.set_input(FileStream(filename))
        return self.load()

    @staticmethod
    def tree2dict(tree):
        data = {}
        metadata = OrderedDict()
        for metadatum in tree.pair():
            key = metadatum.ID().symbol.text
            value = metadatum.VALUE().symbol.text
            if key not in metadata:
                # first occurence; just assign directly
                metadata[key] = value;
            else:
                # we've already have value(s) with this key, 
                # so append to list of existing values
                if type(metadata[key]) is not list:
                    # this is the second value, so we need to
                    # convert existing lone value to list of itself
                    metadata[key] = [metadata[key]]
                # append new value to list
                metadata[key].append(value)
        data['metadata'] = metadata
        data['rows'] = [[f.symbol.text for f in row.FIELD()] for row in tree.row()]
        return data
