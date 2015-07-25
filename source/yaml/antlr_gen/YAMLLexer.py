# Generated from java-escape by ANTLR 4.5
from antlr4 import *
from io import StringIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2\f")
        buf.write("^\b\1\b\1\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6")
        buf.write("\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2")
        buf.write("\6\2\35\n\2\r\2\16\2\36\3\3\6\3\"\n\3\r\3\16\3#\3\4\3")
        buf.write("\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\7\7\63")
        buf.write("\n\7\f\7\16\7\66\13\7\3\7\3\7\3\7\3\7\3\b\6\b=\n\b\r\b")
        buf.write("\16\b>\3\b\3\b\3\t\6\tD\n\t\r\t\16\tE\3\t\7\tI\n\t\f\t")
        buf.write("\16\tL\13\t\3\n\3\n\3\n\3\n\3\n\3\13\7\13T\n\13\f\13\16")
        buf.write("\13W\13\13\3\f\7\fZ\n\f\f\f\16\f]\13\f\2\2\r\5\3\7\4\t")
        buf.write("\5\13\6\r\7\17\b\21\t\23\n\25\2\27\13\31\f\5\2\3\4\6\4")
        buf.write("\2\f\f\17\17\5\2C\\aac|\4\2\13\13\"\"\5\2\13\f\17\17\"")
        buf.write("\"c\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\3\21\3\2\2\2\3\23\3\2\2\2\3\25")
        buf.write("\3\2\2\2\4\27\3\2\2\2\4\31\3\2\2\2\5\34\3\2\2\2\7!\3\2")
        buf.write("\2\2\t%\3\2\2\2\13)\3\2\2\2\r,\3\2\2\2\17\60\3\2\2\2\21")
        buf.write("<\3\2\2\2\23C\3\2\2\2\25M\3\2\2\2\27U\3\2\2\2\31[\3\2")
        buf.write("\2\2\33\35\t\2\2\2\34\33\3\2\2\2\35\36\3\2\2\2\36\34\3")
        buf.write("\2\2\2\36\37\3\2\2\2\37\6\3\2\2\2 \"\t\3\2\2! \3\2\2\2")
        buf.write("\"#\3\2\2\2#!\3\2\2\2#$\3\2\2\2$\b\3\2\2\2%&\7<\2\2&\'")
        buf.write("\3\2\2\2\'(\b\4\2\2(\n\3\2\2\2)*\7\"\2\2*+\7\"\2\2+\f")
        buf.write("\3\2\2\2,-\7/\2\2-.\3\2\2\2./\b\6\2\2/\16\3\2\2\2\60\64")
        buf.write("\7%\2\2\61\63\n\2\2\2\62\61\3\2\2\2\63\66\3\2\2\2\64\62")
        buf.write("\3\2\2\2\64\65\3\2\2\2\65\67\3\2\2\2\66\64\3\2\2\2\67")
        buf.write("8\5\5\2\289\3\2\2\29:\b\7\3\2:\20\3\2\2\2;=\t\4\2\2<;")
        buf.write("\3\2\2\2=>\3\2\2\2><\3\2\2\2>?\3\2\2\2?@\3\2\2\2@A\b\b")
        buf.write("\3\2A\22\3\2\2\2BD\n\5\2\2CB\3\2\2\2DE\3\2\2\2EC\3\2\2")
        buf.write("\2EF\3\2\2\2FJ\3\2\2\2GI\n\2\2\2HG\3\2\2\2IL\3\2\2\2J")
        buf.write("H\3\2\2\2JK\3\2\2\2K\24\3\2\2\2LJ\3\2\2\2MN\5\5\2\2NO")
        buf.write("\3\2\2\2OP\b\n\4\2PQ\b\n\5\2Q\26\3\2\2\2RT\5\13\5\2SR")
        buf.write("\3\2\2\2TW\3\2\2\2US\3\2\2\2UV\3\2\2\2V\30\3\2\2\2WU\3")
        buf.write("\2\2\2XZ\5\13\5\2YX\3\2\2\2Z]\3\2\2\2[Y\3\2\2\2[\\\3\2")
        buf.write("\2\2\\\32\3\2\2\2][\3\2\2\2\r\2\3\4\36#\64>EJU[\6\7\3")
        buf.write("\2\b\2\2\6\2\2\t\3\2")
        return buf.getvalue()


class YAMLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    VALUE_M = 1
    UNUSED = 2

    EOL = 1
    ID = 2
    COLON = 3
    IND = 4
    DASH = 5
    HASHCOMMENT = 6
    WS = 7
    VALUE = 8
    DEDENT = 9
    INDENT = 10

    modeNames = [ u"DEFAULT_MODE", u"VALUE_M", u"UNUSED" ]

    literalNames = [ u"<INVALID>",
            "':'", "'  '", "'-'" ]

    symbolicNames = [ u"<INVALID>",
            "EOL", "ID", "COLON", "IND", "DASH", "HASHCOMMENT", "WS", "VALUE", 
            "DEDENT", "INDENT" ]

    ruleNames = [ "EOL", "ID", "COLON", "IND", "DASH", "HASHCOMMENT", "WS", 
                  "VALUE", "EOL2", "DEDENT", "INDENT" ]

    grammarFileName = "YAMLLexer.g4"

    def __init__(self, input=None):
        super().__init__(input)
        self.checkVersion("4.5")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


