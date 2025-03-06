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
        4,1,9,38,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,4,0,11,8,0,11,0,
        12,0,12,1,0,1,0,1,1,1,1,1,1,5,1,20,8,1,10,1,12,1,23,9,1,1,1,1,1,
        4,1,27,8,1,11,1,12,1,28,1,2,1,2,1,3,4,3,34,8,3,11,3,12,3,35,1,3,
        0,0,4,0,2,4,6,0,2,1,0,3,4,2,0,5,5,7,9,39,0,10,1,0,0,0,2,16,1,0,0,
        0,4,30,1,0,0,0,6,33,1,0,0,0,8,11,3,2,1,0,9,11,3,6,3,0,10,8,1,0,0,
        0,10,9,1,0,0,0,11,12,1,0,0,0,12,10,1,0,0,0,12,13,1,0,0,0,13,14,1,
        0,0,0,14,15,5,0,0,1,15,1,1,0,0,0,16,17,5,1,0,0,17,21,5,2,0,0,18,
        20,5,8,0,0,19,18,1,0,0,0,20,23,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,
        0,22,26,1,0,0,0,23,21,1,0,0,0,24,27,3,4,2,0,25,27,3,6,3,0,26,24,
        1,0,0,0,26,25,1,0,0,0,27,28,1,0,0,0,28,26,1,0,0,0,28,29,1,0,0,0,
        29,3,1,0,0,0,30,31,7,0,0,0,31,5,1,0,0,0,32,34,7,1,0,0,33,32,1,0,
        0,0,34,35,1,0,0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,7,1,0,0,0,6,10,
        12,21,26,28,35
    ]

class WordsParser ( Parser ):

    grammarFileName = "Words.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "':'" ]

    symbolicNames = [ "<INVALID>", "MONTH", "COLON", "FRUIT_SINGULAR", "FRUIT_PLURAL", 
                      "WORD", "NUMBER", "PUNCTUATION", "WHITESPACE", "NEWLINE" ]

    RULE_texto = 0
    RULE_seccion_mes = 1
    RULE_fruta = 2
    RULE_otro = 3

    ruleNames =  [ "texto", "seccion_mes", "fruta", "otro" ]

    EOF = Token.EOF
    MONTH=1
    COLON=2
    FRUIT_SINGULAR=3
    FRUIT_PLURAL=4
    WORD=5
    NUMBER=6
    PUNCTUATION=7
    WHITESPACE=8
    NEWLINE=9

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
            self.state = 10 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 8
                    self.seccion_mes()
                    pass
                elif token in [5, 7, 8, 9]:
                    self.state = 9
                    self.otro()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 12 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 930) != 0)):
                    break

            self.state = 14
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

        def fruta(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WordsParser.FrutaContext)
            else:
                return self.getTypedRuleContext(WordsParser.FrutaContext,i)


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
            self.state = 16
            self.match(WordsParser.MONTH)
            self.state = 17
            self.match(WordsParser.COLON)
            self.state = 21
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 18
                    self.match(WordsParser.WHITESPACE) 
                self.state = 23
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 26 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 26
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [3, 4]:
                        self.state = 24
                        self.fruta()
                        pass
                    elif token in [5, 7, 8, 9]:
                        self.state = 25
                        self.otro()
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 28 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FrutaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FRUIT_SINGULAR(self):
            return self.getToken(WordsParser.FRUIT_SINGULAR, 0)

        def FRUIT_PLURAL(self):
            return self.getToken(WordsParser.FRUIT_PLURAL, 0)

        def getRuleIndex(self):
            return WordsParser.RULE_fruta

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFruta" ):
                listener.enterFruta(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFruta" ):
                listener.exitFruta(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFruta" ):
                return visitor.visitFruta(self)
            else:
                return visitor.visitChildren(self)




    def fruta(self):

        localctx = WordsParser.FrutaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_fruta)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            _la = self._input.LA(1)
            if not(_la==3 or _la==4):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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
        self.enterRule(localctx, 6, self.RULE_otro)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 32
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 928) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()

                else:
                    raise NoViableAltException(self)
                self.state = 35 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





