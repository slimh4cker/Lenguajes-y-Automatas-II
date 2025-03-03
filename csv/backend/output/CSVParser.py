# Generated from CSV.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,4,46,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,4,0,13,
        8,0,11,0,12,0,14,1,0,1,0,1,1,1,1,1,2,1,2,1,2,5,2,24,8,2,10,2,12,
        2,27,9,2,1,2,1,2,1,3,1,3,1,3,5,3,34,8,3,10,3,12,3,37,9,3,3,3,39,
        8,3,1,3,1,3,1,4,3,4,44,8,4,1,4,0,0,5,0,2,4,6,8,0,0,45,0,10,1,0,0,
        0,2,18,1,0,0,0,4,20,1,0,0,0,6,38,1,0,0,0,8,43,1,0,0,0,10,12,3,2,
        1,0,11,13,3,6,3,0,12,11,1,0,0,0,13,14,1,0,0,0,14,12,1,0,0,0,14,15,
        1,0,0,0,15,16,1,0,0,0,16,17,5,0,0,1,17,1,1,0,0,0,18,19,3,4,2,0,19,
        3,1,0,0,0,20,25,3,8,4,0,21,22,5,2,0,0,22,24,3,8,4,0,23,21,1,0,0,
        0,24,27,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,28,1,0,0,0,27,25,
        1,0,0,0,28,29,5,3,0,0,29,5,1,0,0,0,30,35,3,8,4,0,31,32,5,2,0,0,32,
        34,3,8,4,0,33,31,1,0,0,0,34,37,1,0,0,0,35,33,1,0,0,0,35,36,1,0,0,
        0,36,39,1,0,0,0,37,35,1,0,0,0,38,30,1,0,0,0,38,39,1,0,0,0,39,40,
        1,0,0,0,40,41,5,3,0,0,41,7,1,0,0,0,42,44,5,1,0,0,43,42,1,0,0,0,43,
        44,1,0,0,0,44,9,1,0,0,0,5,14,25,35,38,43
    ]

class CSVParser ( Parser ):

    grammarFileName = "CSV.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "','" ]

    symbolicNames = [ "<INVALID>", "TEXT", "COMMA", "NEWLINE", "WS" ]

    RULE_file = 0
    RULE_header = 1
    RULE_non_empty_row = 2
    RULE_row = 3
    RULE_field = 4

    ruleNames =  [ "file", "header", "non_empty_row", "row", "field" ]

    EOF = Token.EOF
    TEXT=1
    COMMA=2
    NEWLINE=3
    WS=4

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class FileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def header(self):
            return self.getTypedRuleContext(CSVParser.HeaderContext,0)


        def EOF(self):
            return self.getToken(CSVParser.EOF, 0)

        def row(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSVParser.RowContext)
            else:
                return self.getTypedRuleContext(CSVParser.RowContext,i)


        def getRuleIndex(self):
            return CSVParser.RULE_file

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFile" ):
                listener.enterFile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFile" ):
                listener.exitFile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFile" ):
                return visitor.visitFile(self)
            else:
                return visitor.visitChildren(self)




    def file_(self):

        localctx = CSVParser.FileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_file)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.header()
            self.state = 12 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 11
                self.row()
                self.state = 14 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0)):
                    break

            self.state = 16
            self.match(CSVParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HeaderContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def non_empty_row(self):
            return self.getTypedRuleContext(CSVParser.Non_empty_rowContext,0)


        def getRuleIndex(self):
            return CSVParser.RULE_header

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeader" ):
                listener.enterHeader(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeader" ):
                listener.exitHeader(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHeader" ):
                return visitor.visitHeader(self)
            else:
                return visitor.visitChildren(self)




    def header(self):

        localctx = CSVParser.HeaderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_header)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.non_empty_row()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Non_empty_rowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSVParser.FieldContext)
            else:
                return self.getTypedRuleContext(CSVParser.FieldContext,i)


        def NEWLINE(self):
            return self.getToken(CSVParser.NEWLINE, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSVParser.COMMA)
            else:
                return self.getToken(CSVParser.COMMA, i)

        def getRuleIndex(self):
            return CSVParser.RULE_non_empty_row

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNon_empty_row" ):
                listener.enterNon_empty_row(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNon_empty_row" ):
                listener.exitNon_empty_row(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNon_empty_row" ):
                return visitor.visitNon_empty_row(self)
            else:
                return visitor.visitChildren(self)




    def non_empty_row(self):

        localctx = CSVParser.Non_empty_rowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_non_empty_row)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.field()
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 21
                self.match(CSVParser.COMMA)
                self.state = 22
                self.field()
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 28
            self.match(CSVParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(CSVParser.NEWLINE, 0)

        def field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSVParser.FieldContext)
            else:
                return self.getTypedRuleContext(CSVParser.FieldContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSVParser.COMMA)
            else:
                return self.getToken(CSVParser.COMMA, i)

        def getRuleIndex(self):
            return CSVParser.RULE_row

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRow" ):
                listener.enterRow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRow" ):
                listener.exitRow(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRow" ):
                return visitor.visitRow(self)
            else:
                return visitor.visitChildren(self)




    def row(self):

        localctx = CSVParser.RowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_row)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 30
                self.field()
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 31
                    self.match(CSVParser.COMMA)
                    self.state = 32
                    self.field()
                    self.state = 37
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 40
            self.match(CSVParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(CSVParser.TEXT, 0)

        def getRuleIndex(self):
            return CSVParser.RULE_field

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField" ):
                listener.enterField(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField" ):
                listener.exitField(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField" ):
                return visitor.visitField(self)
            else:
                return visitor.visitChildren(self)




    def field(self):

        localctx = CSVParser.FieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_field)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 42
                self.match(CSVParser.TEXT)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





