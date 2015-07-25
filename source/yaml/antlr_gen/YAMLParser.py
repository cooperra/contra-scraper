# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .YAMLParserListener import YAMLParserListener
else:
    from YAMLParserListener import YAMLParserListener
def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\f")
        buf.write("\60\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3")
        buf.write("\2\3\3\6\3\21\n\3\r\3\16\3\22\3\4\3\4\3\4\3\4\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\7\5!\n\5\f\5\16\5$\13\5\3\5\3")
        buf.write("\5\5\5(\n\5\3\5\5\5+\n\5\3\6\3\6\3\6\3\6\2\2\7\2\4\6\b")
        buf.write("\n\2\2/\2\f\3\2\2\2\4\20\3\2\2\2\6\24\3\2\2\2\b*\3\2\2")
        buf.write("\2\n,\3\2\2\2\f\r\5\4\3\2\r\16\7\2\2\3\16\3\3\2\2\2\17")
        buf.write("\21\5\6\4\2\20\17\3\2\2\2\21\22\3\2\2\2\22\20\3\2\2\2")
        buf.write("\22\23\3\2\2\2\23\5\3\2\2\2\24\25\7\4\2\2\25\26\7\5\2")
        buf.write("\2\26\27\5\b\5\2\27\7\3\2\2\2\30\31\7\3\2\2\31\32\7\f")
        buf.write("\2\2\32\33\5\4\3\2\33\34\7\13\2\2\34+\3\2\2\2\35\36\7")
        buf.write("\3\2\2\36\"\7\f\2\2\37!\5\n\6\2 \37\3\2\2\2!$\3\2\2\2")
        buf.write("\" \3\2\2\2\"#\3\2\2\2#%\3\2\2\2$\"\3\2\2\2%+\7\13\2\2")
        buf.write("&(\7\n\2\2\'&\3\2\2\2\'(\3\2\2\2()\3\2\2\2)+\7\3\2\2*")
        buf.write("\30\3\2\2\2*\35\3\2\2\2*\'\3\2\2\2+\t\3\2\2\2,-\7\7\2")
        buf.write("\2-.\5\b\5\2.\13\3\2\2\2\6\22\"\'*")
        return buf.getvalue()


class YAMLParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"':'", u"'  '", 
                     u"'-'" ]

    symbolicNames = [ u"<INVALID>", u"EOL", u"ID", u"COLON", u"IND", u"DASH", 
                      u"HASHCOMMENT", u"WS", u"VALUE", u"DEDENT", u"INDENT" ]

    RULE_r = 0
    RULE_obj = 1
    RULE_pair = 2
    RULE_value = 3
    RULE_listItem = 4

    ruleNames =  [ "r", "obj", "pair", "value", "listItem" ]

    EOF = Token.EOF
    EOL=1
    ID=2
    COLON=3
    IND=4
    DASH=5
    HASHCOMMENT=6
    WS=7
    VALUE=8
    DEDENT=9
    INDENT=10

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class RContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def obj(self):
            return self.getTypedRuleContext(YAMLParser.ObjContext,0)


        def EOF(self):
            return self.getToken(YAMLParser.EOF, 0)

        def getRuleIndex(self):
            return YAMLParser.RULE_r

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, YAMLParserListener ):
                listener.enterR(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, YAMLParserListener ):
                listener.exitR(self)




    def r(self):

        localctx = YAMLParser.RContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_r)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.obj()
            self.state = 11
            self.match(YAMLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ObjContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YAMLParser.PairContext)
            else:
                return self.getTypedRuleContext(YAMLParser.PairContext,i)


        def getRuleIndex(self):
            return YAMLParser.RULE_obj

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, YAMLParserListener ):
                listener.enterObj(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, YAMLParserListener ):
                listener.exitObj(self)




    def obj(self):

        localctx = YAMLParser.ObjContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_obj)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 13
                self.pair()
                self.state = 16 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==YAMLParser.ID):
                    break

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

        def ID(self):
            return self.getToken(YAMLParser.ID, 0)

        def COLON(self):
            return self.getToken(YAMLParser.COLON, 0)

        def value(self):
            return self.getTypedRuleContext(YAMLParser.ValueContext,0)


        def getRuleIndex(self):
            return YAMLParser.RULE_pair

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, YAMLParserListener ):
                listener.enterPair(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, YAMLParserListener ):
                listener.exitPair(self)




    def pair(self):

        localctx = YAMLParser.PairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.match(YAMLParser.ID)
            self.state = 19
            self.match(YAMLParser.COLON)
            self.state = 20
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOL(self):
            return self.getToken(YAMLParser.EOL, 0)

        def INDENT(self):
            return self.getToken(YAMLParser.INDENT, 0)

        def obj(self):
            return self.getTypedRuleContext(YAMLParser.ObjContext,0)


        def DEDENT(self):
            return self.getToken(YAMLParser.DEDENT, 0)

        def listItem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YAMLParser.ListItemContext)
            else:
                return self.getTypedRuleContext(YAMLParser.ListItemContext,i)


        def VALUE(self):
            return self.getToken(YAMLParser.VALUE, 0)

        def getRuleIndex(self):
            return YAMLParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, YAMLParserListener ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, YAMLParserListener ):
                listener.exitValue(self)




    def value(self):

        localctx = YAMLParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.state = 40
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.match(YAMLParser.EOL)
                self.state = 23
                self.match(YAMLParser.INDENT)
                self.state = 24
                self.obj()
                self.state = 25
                self.match(YAMLParser.DEDENT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.match(YAMLParser.EOL)
                self.state = 28
                self.match(YAMLParser.INDENT)
                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==YAMLParser.DASH:
                    self.state = 29
                    self.listItem()
                    self.state = 34
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 35
                self.match(YAMLParser.DEDENT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 37
                _la = self._input.LA(1)
                if _la==YAMLParser.VALUE:
                    self.state = 36
                    self.match(YAMLParser.VALUE)


                self.state = 39
                self.match(YAMLParser.EOL)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ListItemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DASH(self):
            return self.getToken(YAMLParser.DASH, 0)

        def value(self):
            return self.getTypedRuleContext(YAMLParser.ValueContext,0)


        def getRuleIndex(self):
            return YAMLParser.RULE_listItem

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, YAMLParserListener ):
                listener.enterListItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, YAMLParserListener ):
                listener.exitListItem(self)




    def listItem(self):

        localctx = YAMLParser.ListItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_listItem)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(YAMLParser.DASH)
            self.state = 43
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx




