# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .TSVParserListener import TSVParserListener
else:
    from TSVParserListener import TSVParserListener
def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\13")
        buf.write("\"\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\7\2\13\n\2\f\2\16\2")
        buf.write("\16\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\7")
        buf.write("\4\33\n\4\f\4\16\4\36\13\4\3\4\3\4\3\4\2\2\5\2\4\6\2\2")
        buf.write("!\2\f\3\2\2\2\4\21\3\2\2\2\6\27\3\2\2\2\b\13\5\4\3\2\t")
        buf.write("\13\5\6\4\2\n\b\3\2\2\2\n\t\3\2\2\2\13\16\3\2\2\2\f\n")
        buf.write("\3\2\2\2\f\r\3\2\2\2\r\17\3\2\2\2\16\f\3\2\2\2\17\20\7")
        buf.write("\2\2\3\20\3\3\2\2\2\21\22\7\b\2\2\22\23\7\n\2\2\23\24")
        buf.write("\7\t\2\2\24\25\7\13\2\2\25\26\7\3\2\2\26\5\3\2\2\2\27")
        buf.write("\34\7\5\2\2\30\31\7\6\2\2\31\33\7\5\2\2\32\30\3\2\2\2")
        buf.write("\33\36\3\2\2\2\34\32\3\2\2\2\34\35\3\2\2\2\35\37\3\2\2")
        buf.write("\2\36\34\3\2\2\2\37 \7\3\2\2 \7\3\2\2\2\5\n\f\34")
        return buf.getvalue()


class TSVParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"<INVALID>", u"'#'", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"'<'", u"'>'" ]

    symbolicNames = [ u"<INVALID>", u"EOL", u"HASH", u"FIELD", u"SEP", u"HASHCOMMENT", 
                      u"LT", u"GT", u"ID", u"VALUE" ]

    RULE_r = 0
    RULE_pair = 1
    RULE_row = 2

    ruleNames =  [ "r", "pair", "row" ]

    EOF = Token.EOF
    EOL=1
    HASH=2
    FIELD=3
    SEP=4
    HASHCOMMENT=5
    LT=6
    GT=7
    ID=8
    VALUE=9

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class RContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(TSVParser.EOF, 0)

        def pair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TSVParser.PairContext)
            else:
                return self.getTypedRuleContext(TSVParser.PairContext,i)


        def row(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TSVParser.RowContext)
            else:
                return self.getTypedRuleContext(TSVParser.RowContext,i)


        def getRuleIndex(self):
            return TSVParser.RULE_r

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSVParserListener ):
                listener.enterR(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSVParserListener ):
                listener.exitR(self)




    def r(self):

        localctx = TSVParser.RContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_r)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==TSVParser.FIELD or _la==TSVParser.LT:
                self.state = 8
                token = self._input.LA(1)
                if token in [TSVParser.LT]:
                    self.state = 6
                    self.pair()

                elif token in [TSVParser.FIELD]:
                    self.state = 7
                    self.row()

                else:
                    raise NoViableAltException(self)

                self.state = 12
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 13
            self.match(TSVParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PairContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(TSVParser.LT, 0)

        def ID(self):
            return self.getToken(TSVParser.ID, 0)

        def GT(self):
            return self.getToken(TSVParser.GT, 0)

        def VALUE(self):
            return self.getToken(TSVParser.VALUE, 0)

        def EOL(self):
            return self.getToken(TSVParser.EOL, 0)

        def getRuleIndex(self):
            return TSVParser.RULE_pair

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSVParserListener ):
                listener.enterPair(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSVParserListener ):
                listener.exitPair(self)




    def pair(self):

        localctx = TSVParser.PairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self.match(TSVParser.LT)
            self.state = 16
            self.match(TSVParser.ID)
            self.state = 17
            self.match(TSVParser.GT)
            self.state = 18
            self.match(TSVParser.VALUE)
            self.state = 19
            self.match(TSVParser.EOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RowContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FIELD(self, i:int=None):
            if i is None:
                return self.getTokens(TSVParser.FIELD)
            else:
                return self.getToken(TSVParser.FIELD, i)

        def EOL(self):
            return self.getToken(TSVParser.EOL, 0)

        def SEP(self, i:int=None):
            if i is None:
                return self.getTokens(TSVParser.SEP)
            else:
                return self.getToken(TSVParser.SEP, i)

        def getRuleIndex(self):
            return TSVParser.RULE_row

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSVParserListener ):
                listener.enterRow(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSVParserListener ):
                listener.exitRow(self)




    def row(self):

        localctx = TSVParser.RowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_row)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self.match(TSVParser.FIELD)
            self.state = 26
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==TSVParser.SEP:
                self.state = 22
                self.match(TSVParser.SEP)
                self.state = 23
                self.match(TSVParser.FIELD)
                self.state = 28
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 29
            self.match(TSVParser.EOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx




