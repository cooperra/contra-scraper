from .antlr_gen.TSVLexer import TSVLexer
from .antlr_gen.TSVParser import TSVParser
from .loader import Loader

def load_file(filename):
    loader = Loader()
    return loader.load_file(filename)
