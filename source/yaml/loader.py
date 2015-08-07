from .antlr_gen.YAMLLexer import YAMLLexer as Lexer
from .antlr_gen.YAMLParser import YAMLParser as Parser
from .IndentTokenFilter import IndentTokenFilter
from antlr4 import CommonTokenStream, FileStream

class Loader:
    def __init__(self, inputstream=None):
        self.input = inputstream
        self.lexer = Lexer(self.input)
        self.filter = IndentTokenFilter(self.lexer)
        self.cts = CommonTokenStream(self.filter)
        self.parser = Parser(self.cts)

    def set_input(self, inputstream):
        self.input = inputstream
        self.lexer.inputStream = self.input
        self.reset()

    def reset(self):
        self.lexer.reset()
        self.filter.reset()
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
