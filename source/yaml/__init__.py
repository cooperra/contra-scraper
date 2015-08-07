from .antlr_gen.YAMLLexer import YAMLLexer
from .antlr_gen.YAMLParser import YAMLParser
from .IndentTokenFilter import IndentTokenFilter
from .loader import Loader

def load_file(filename):
    loader = Loader()
    return loader.load_file(filename)
