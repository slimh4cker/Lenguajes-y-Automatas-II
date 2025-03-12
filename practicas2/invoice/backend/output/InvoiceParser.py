# Generated from Invoice.g4 by ANTLR 4.13.2
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
        4,1,12,115,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,4,0,25,8,0,11,0,12,0,
        26,1,0,1,0,1,0,1,1,4,1,33,8,1,11,1,12,1,34,3,1,37,8,1,1,1,1,1,4,
        1,41,8,1,11,1,12,1,42,3,1,45,8,1,1,1,5,1,48,8,1,10,1,12,1,51,9,1,
        1,2,1,2,3,2,55,8,2,1,3,1,3,1,3,4,3,60,8,3,11,3,12,3,61,1,3,4,3,65,
        8,3,11,3,12,3,66,3,3,69,8,3,1,3,1,3,5,3,73,8,3,10,3,12,3,76,9,3,
        1,4,1,4,5,4,80,8,4,10,4,12,4,83,9,4,1,5,1,5,1,5,3,5,88,8,5,1,5,1,
        5,1,5,1,5,1,5,3,5,95,8,5,1,5,1,5,3,5,99,8,5,1,6,1,6,3,6,103,8,6,
        1,7,1,7,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,10,0,0,11,0,2,4,6,8,
        10,12,14,16,18,20,0,3,2,0,2,3,7,7,2,0,2,3,11,11,1,0,5,6,120,0,22,
        1,0,0,0,2,36,1,0,0,0,4,52,1,0,0,0,6,56,1,0,0,0,8,77,1,0,0,0,10,98,
        1,0,0,0,12,102,1,0,0,0,14,104,1,0,0,0,16,108,1,0,0,0,18,110,1,0,
        0,0,20,112,1,0,0,0,22,24,3,2,1,0,23,25,3,4,2,0,24,23,1,0,0,0,25,
        26,1,0,0,0,26,24,1,0,0,0,26,27,1,0,0,0,27,28,1,0,0,0,28,29,3,6,3,
        0,29,30,5,0,0,1,30,1,1,0,0,0,31,33,5,10,0,0,32,31,1,0,0,0,33,34,
        1,0,0,0,34,32,1,0,0,0,34,35,1,0,0,0,35,37,1,0,0,0,36,32,1,0,0,0,
        36,37,1,0,0,0,37,38,1,0,0,0,38,44,5,9,0,0,39,41,5,10,0,0,40,39,1,
        0,0,0,41,42,1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,0,43,45,1,0,0,0,44,
        40,1,0,0,0,44,45,1,0,0,0,45,49,1,0,0,0,46,48,5,9,0,0,47,46,1,0,0,
        0,48,51,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,3,1,0,0,0,51,49,1,
        0,0,0,52,54,5,10,0,0,53,55,7,0,0,0,54,53,1,0,0,0,54,55,1,0,0,0,55,
        5,1,0,0,0,56,74,3,10,5,0,57,68,3,8,4,0,58,60,5,10,0,0,59,58,1,0,
        0,0,60,61,1,0,0,0,61,59,1,0,0,0,61,62,1,0,0,0,62,69,1,0,0,0,63,65,
        5,11,0,0,64,63,1,0,0,0,65,66,1,0,0,0,66,64,1,0,0,0,66,67,1,0,0,0,
        67,69,1,0,0,0,68,59,1,0,0,0,68,64,1,0,0,0,68,69,1,0,0,0,69,70,1,
        0,0,0,70,71,3,10,5,0,71,73,1,0,0,0,72,57,1,0,0,0,73,76,1,0,0,0,74,
        72,1,0,0,0,74,75,1,0,0,0,75,7,1,0,0,0,76,74,1,0,0,0,77,81,7,1,0,
        0,78,80,5,12,0,0,79,78,1,0,0,0,80,83,1,0,0,0,81,79,1,0,0,0,81,82,
        1,0,0,0,82,9,1,0,0,0,83,81,1,0,0,0,84,85,3,12,6,0,85,87,3,16,8,0,
        86,88,5,7,0,0,87,86,1,0,0,0,87,88,1,0,0,0,88,89,1,0,0,0,89,90,3,
        20,10,0,90,99,1,0,0,0,91,92,3,12,6,0,92,94,3,18,9,0,93,95,5,7,0,
        0,94,93,1,0,0,0,94,95,1,0,0,0,95,96,1,0,0,0,96,97,3,20,10,0,97,99,
        1,0,0,0,98,84,1,0,0,0,98,91,1,0,0,0,99,11,1,0,0,0,100,103,3,14,7,
        0,101,103,5,8,0,0,102,100,1,0,0,0,102,101,1,0,0,0,103,13,1,0,0,0,
        104,105,5,8,0,0,105,106,5,1,0,0,106,107,5,8,0,0,107,15,1,0,0,0,108,
        109,5,4,0,0,109,17,1,0,0,0,110,111,7,2,0,0,111,19,1,0,0,0,112,113,
        5,10,0,0,113,21,1,0,0,0,16,26,34,36,42,44,49,54,61,66,68,74,81,87,
        94,98,102
    ]

class InvoiceParser ( Parser ):

    grammarFileName = "Invoice.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'/'", "'y'", "','", "'kg'", "'pieza'", 
                     "'piezas'", "'de'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "Y_CONJ", "COMMA", "KG", 
                      "PIEZA", "PIEZAS", "DE", "NUMBER", "NOMBRE", "WORD", 
                      "DOT", "WS" ]

    RULE_invoice = 0
    RULE_header = 1
    RULE_verb = 2
    RULE_purchaseList = 3
    RULE_separator = 4
    RULE_purchase = 5
    RULE_quantity = 6
    RULE_fraction = 7
    RULE_unit = 8
    RULE_pieceUnit = 9
    RULE_fruit = 10

    ruleNames =  [ "invoice", "header", "verb", "purchaseList", "separator", 
                   "purchase", "quantity", "fraction", "unit", "pieceUnit", 
                   "fruit" ]

    EOF = Token.EOF
    T__0=1
    Y_CONJ=2
    COMMA=3
    KG=4
    PIEZA=5
    PIEZAS=6
    DE=7
    NUMBER=8
    NOMBRE=9
    WORD=10
    DOT=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class InvoiceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def header(self):
            return self.getTypedRuleContext(InvoiceParser.HeaderContext,0)


        def purchaseList(self):
            return self.getTypedRuleContext(InvoiceParser.PurchaseListContext,0)


        def EOF(self):
            return self.getToken(InvoiceParser.EOF, 0)

        def verb(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(InvoiceParser.VerbContext)
            else:
                return self.getTypedRuleContext(InvoiceParser.VerbContext,i)


        def getRuleIndex(self):
            return InvoiceParser.RULE_invoice

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInvoice" ):
                listener.enterInvoice(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInvoice" ):
                listener.exitInvoice(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInvoice" ):
                return visitor.visitInvoice(self)
            else:
                return visitor.visitChildren(self)




    def invoice(self):

        localctx = InvoiceParser.InvoiceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_invoice)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.header()
            self.state = 24 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 23
                self.verb()
                self.state = 26 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==10):
                    break

            self.state = 28
            self.purchaseList()
            self.state = 29
            self.match(InvoiceParser.EOF)
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

        def NOMBRE(self, i:int=None):
            if i is None:
                return self.getTokens(InvoiceParser.NOMBRE)
            else:
                return self.getToken(InvoiceParser.NOMBRE, i)

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(InvoiceParser.WORD)
            else:
                return self.getToken(InvoiceParser.WORD, i)

        def getRuleIndex(self):
            return InvoiceParser.RULE_header

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

        localctx = InvoiceParser.HeaderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_header)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 32 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 31
                    self.match(InvoiceParser.WORD)
                    self.state = 34 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==10):
                        break



            self.state = 38
            self.match(InvoiceParser.NOMBRE)
            self.state = 44
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 40 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 39
                        self.match(InvoiceParser.WORD)

                    else:
                        raise NoViableAltException(self)
                    self.state = 42 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,3,self._ctx)



            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 46
                self.match(InvoiceParser.NOMBRE)
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VerbContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(InvoiceParser.WORD, 0)

        def COMMA(self):
            return self.getToken(InvoiceParser.COMMA, 0)

        def Y_CONJ(self):
            return self.getToken(InvoiceParser.Y_CONJ, 0)

        def DE(self):
            return self.getToken(InvoiceParser.DE, 0)

        def getRuleIndex(self):
            return InvoiceParser.RULE_verb

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVerb" ):
                listener.enterVerb(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVerb" ):
                listener.exitVerb(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVerb" ):
                return visitor.visitVerb(self)
            else:
                return visitor.visitChildren(self)




    def verb(self):

        localctx = InvoiceParser.VerbContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_verb)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(InvoiceParser.WORD)
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 140) != 0):
                self.state = 53
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 140) != 0)):
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


    class PurchaseListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def purchase(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(InvoiceParser.PurchaseContext)
            else:
                return self.getTypedRuleContext(InvoiceParser.PurchaseContext,i)


        def separator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(InvoiceParser.SeparatorContext)
            else:
                return self.getTypedRuleContext(InvoiceParser.SeparatorContext,i)


        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(InvoiceParser.WORD)
            else:
                return self.getToken(InvoiceParser.WORD, i)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(InvoiceParser.DOT)
            else:
                return self.getToken(InvoiceParser.DOT, i)

        def getRuleIndex(self):
            return InvoiceParser.RULE_purchaseList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPurchaseList" ):
                listener.enterPurchaseList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPurchaseList" ):
                listener.exitPurchaseList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPurchaseList" ):
                return visitor.visitPurchaseList(self)
            else:
                return visitor.visitChildren(self)




    def purchaseList(self):

        localctx = InvoiceParser.PurchaseListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_purchaseList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.purchase()
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2060) != 0):
                self.state = 57
                self.separator()
                self.state = 68
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [10]:
                    self.state = 59 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 58
                        self.match(InvoiceParser.WORD)
                        self.state = 61 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==10):
                            break

                    pass
                elif token in [11]:
                    self.state = 64 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 63
                        self.match(InvoiceParser.DOT)
                        self.state = 66 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==11):
                            break

                    pass
                elif token in [8]:
                    pass
                else:
                    pass
                self.state = 70
                self.purchase()
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SeparatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(InvoiceParser.COMMA, 0)

        def Y_CONJ(self):
            return self.getToken(InvoiceParser.Y_CONJ, 0)

        def DOT(self):
            return self.getToken(InvoiceParser.DOT, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(InvoiceParser.WS)
            else:
                return self.getToken(InvoiceParser.WS, i)

        def getRuleIndex(self):
            return InvoiceParser.RULE_separator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSeparator" ):
                listener.enterSeparator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSeparator" ):
                listener.exitSeparator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSeparator" ):
                return visitor.visitSeparator(self)
            else:
                return visitor.visitChildren(self)




    def separator(self):

        localctx = InvoiceParser.SeparatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_separator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2060) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 78
                self.match(InvoiceParser.WS)
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PurchaseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def quantity(self):
            return self.getTypedRuleContext(InvoiceParser.QuantityContext,0)


        def unit(self):
            return self.getTypedRuleContext(InvoiceParser.UnitContext,0)


        def fruit(self):
            return self.getTypedRuleContext(InvoiceParser.FruitContext,0)


        def DE(self):
            return self.getToken(InvoiceParser.DE, 0)

        def pieceUnit(self):
            return self.getTypedRuleContext(InvoiceParser.PieceUnitContext,0)


        def getRuleIndex(self):
            return InvoiceParser.RULE_purchase

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPurchase" ):
                listener.enterPurchase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPurchase" ):
                listener.exitPurchase(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPurchase" ):
                return visitor.visitPurchase(self)
            else:
                return visitor.visitChildren(self)




    def purchase(self):

        localctx = InvoiceParser.PurchaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_purchase)
        self._la = 0 # Token type
        try:
            self.state = 98
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                self.quantity()

                self.state = 85
                self.unit()
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==7:
                    self.state = 86
                    self.match(InvoiceParser.DE)


                self.state = 89
                self.fruit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 91
                self.quantity()

                self.state = 92
                self.pieceUnit()
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==7:
                    self.state = 93
                    self.match(InvoiceParser.DE)


                self.state = 96
                self.fruit()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuantityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fraction(self):
            return self.getTypedRuleContext(InvoiceParser.FractionContext,0)


        def NUMBER(self):
            return self.getToken(InvoiceParser.NUMBER, 0)

        def getRuleIndex(self):
            return InvoiceParser.RULE_quantity

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuantity" ):
                listener.enterQuantity(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuantity" ):
                listener.exitQuantity(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuantity" ):
                return visitor.visitQuantity(self)
            else:
                return visitor.visitChildren(self)




    def quantity(self):

        localctx = InvoiceParser.QuantityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_quantity)
        try:
            self.state = 102
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 100
                self.fraction()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 101
                self.match(InvoiceParser.NUMBER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FractionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(InvoiceParser.NUMBER)
            else:
                return self.getToken(InvoiceParser.NUMBER, i)

        def getRuleIndex(self):
            return InvoiceParser.RULE_fraction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFraction" ):
                listener.enterFraction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFraction" ):
                listener.exitFraction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFraction" ):
                return visitor.visitFraction(self)
            else:
                return visitor.visitChildren(self)




    def fraction(self):

        localctx = InvoiceParser.FractionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_fraction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(InvoiceParser.NUMBER)
            self.state = 105
            self.match(InvoiceParser.T__0)
            self.state = 106
            self.match(InvoiceParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KG(self):
            return self.getToken(InvoiceParser.KG, 0)

        def getRuleIndex(self):
            return InvoiceParser.RULE_unit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnit" ):
                listener.enterUnit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnit" ):
                listener.exitUnit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnit" ):
                return visitor.visitUnit(self)
            else:
                return visitor.visitChildren(self)




    def unit(self):

        localctx = InvoiceParser.UnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_unit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(InvoiceParser.KG)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PieceUnitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PIEZA(self):
            return self.getToken(InvoiceParser.PIEZA, 0)

        def PIEZAS(self):
            return self.getToken(InvoiceParser.PIEZAS, 0)

        def getRuleIndex(self):
            return InvoiceParser.RULE_pieceUnit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPieceUnit" ):
                listener.enterPieceUnit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPieceUnit" ):
                listener.exitPieceUnit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPieceUnit" ):
                return visitor.visitPieceUnit(self)
            else:
                return visitor.visitChildren(self)




    def pieceUnit(self):

        localctx = InvoiceParser.PieceUnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_pieceUnit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            _la = self._input.LA(1)
            if not(_la==5 or _la==6):
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


    class FruitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(InvoiceParser.WORD, 0)

        def getRuleIndex(self):
            return InvoiceParser.RULE_fruit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFruit" ):
                listener.enterFruit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFruit" ):
                listener.exitFruit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFruit" ):
                return visitor.visitFruit(self)
            else:
                return visitor.visitChildren(self)




    def fruit(self):

        localctx = InvoiceParser.FruitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_fruit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(InvoiceParser.WORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





