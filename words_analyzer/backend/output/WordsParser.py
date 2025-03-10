# Generated from Words.g4 by ANTLR 4.13.2
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
        4,1,7,33,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,4,0,9,8,0,11,0,12,0,10,
        1,0,1,0,1,1,1,1,1,1,5,1,18,8,1,10,1,12,1,21,9,1,1,1,4,1,24,8,1,11,
        1,12,1,25,1,2,4,2,29,8,2,11,2,12,2,30,1,2,0,0,3,0,2,4,0,1,1,0,2,
        7,34,0,8,1,0,0,0,2,14,1,0,0,0,4,28,1,0,0,0,6,9,3,2,1,0,7,9,3,4,2,
        0,8,6,1,0,0,0,8,7,1,0,0,0,9,10,1,0,0,0,10,8,1,0,0,0,10,11,1,0,0,
        0,11,12,1,0,0,0,12,13,5,0,0,1,13,1,1,0,0,0,14,15,5,1,0,0,15,19,5,
        2,0,0,16,18,5,6,0,0,17,16,1,0,0,0,18,21,1,0,0,0,19,17,1,0,0,0,19,
        20,1,0,0,0,20,23,1,0,0,0,21,19,1,0,0,0,22,24,3,4,2,0,23,22,1,0,0,
        0,24,25,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,3,1,0,0,0,27,29,7,
        0,0,0,28,27,1,0,0,0,29,30,1,0,0,0,30,28,1,0,0,0,30,31,1,0,0,0,31,
        5,1,0,0,0,5,8,10,19,25,30
    ]

class WordsParser ( Parser ):

    grammarFileName = "Words.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "':'" ]

    symbolicNames = [ "<INVALID>", "MONTH", "COLON", "WORD", "PUNCTUATION", 
                      "NUMBER", "WHITESPACE", "NEWLINE" ]

    RULE_texto = 0
    RULE_seccion_mes = 1
    RULE_otro = 2

    ruleNames =  [ "texto", "seccion_mes", "otro" ]

    EOF = Token.EOF
    MONTH=1
    COLON=2
    WORD=3
    PUNCTUATION=4
    NUMBER=5
    WHITESPACE=6
    NEWLINE=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class TextoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(WordsParser.EOF, 0)

        def seccion_mes(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WordsParser.Seccion_mesContext)
            else:
                return self.getTypedRuleContext(WordsParser.Seccion_mesContext,i)


        def otro(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WordsParser.OtroContext)
            else:
                return self.getTypedRuleContext(WordsParser.OtroContext,i)


        def getRuleIndex(self):
            return WordsParser.RULE_texto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTexto" ):
                listener.enterTexto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTexto" ):
                listener.exitTexto(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTexto" ):
                return visitor.visitTexto(self)
            else:
                return visitor.visitChildren(self)




    def texto(self):

        localctx = WordsParser.TextoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_texto)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 6
                    self.seccion_mes()
                    pass
                elif token in [2, 3, 4, 5, 6, 7]:
                    self.state = 7
                    self.otro()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 10 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 254) != 0)):
                    break

            self.state = 12
            self.match(WordsParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Seccion_mesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MONTH(self):
            return self.getToken(WordsParser.MONTH, 0)

        def COLON(self):
            return self.getToken(WordsParser.COLON, 0)

        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(WordsParser.WHITESPACE)
            else:
                return self.getToken(WordsParser.WHITESPACE, i)

        def otro(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WordsParser.OtroContext)
            else:
                return self.getTypedRuleContext(WordsParser.OtroContext,i)


        def getRuleIndex(self):
            return WordsParser.RULE_seccion_mes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSeccion_mes" ):
                listener.enterSeccion_mes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSeccion_mes" ):
                listener.exitSeccion_mes(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSeccion_mes" ):
                return visitor.visitSeccion_mes(self)
            else:
                return visitor.visitChildren(self)




    def seccion_mes(self):

        localctx = WordsParser.Seccion_mesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_seccion_mes)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.match(WordsParser.MONTH)
            self.state = 15
            self.match(WordsParser.COLON)
            self.state = 19
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 16
                    self.match(WordsParser.WHITESPACE) 
                self.state = 21
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 23 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 22
                    self.otro()

                else:
                    raise NoViableAltException(self)
                self.state = 25 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OtroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(WordsParser.WORD)
            else:
                return self.getToken(WordsParser.WORD, i)

        def PUNCTUATION(self, i:int=None):
            if i is None:
                return self.getTokens(WordsParser.PUNCTUATION)
            else:
                return self.getToken(WordsParser.PUNCTUATION, i)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(WordsParser.COLON)
            else:
                return self.getToken(WordsParser.COLON, i)

        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(WordsParser.WHITESPACE)
            else:
                return self.getToken(WordsParser.WHITESPACE, i)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(WordsParser.NEWLINE)
            else:
                return self.getToken(WordsParser.NEWLINE, i)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(WordsParser.NUMBER)
            else:
                return self.getToken(WordsParser.NUMBER, i)

        def getRuleIndex(self):
            return WordsParser.RULE_otro

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOtro" ):
                listener.enterOtro(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOtro" ):
                listener.exitOtro(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOtro" ):
                return visitor.visitOtro(self)
            else:
                return visitor.visitChildren(self)




    def otro(self):

        localctx = WordsParser.OtroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_otro)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 27
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 252) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()

                else:
                    raise NoViableAltException(self)
                self.state = 30 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





