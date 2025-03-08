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
        4,1,12,92,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,4,0,25,8,0,11,0,12,0,
        26,1,0,1,0,3,0,31,8,0,1,0,1,0,1,1,1,1,5,1,37,8,1,10,1,12,1,40,9,
        1,1,2,1,2,3,2,44,8,2,1,3,1,3,1,3,1,3,5,3,50,8,3,10,3,12,3,53,9,3,
        1,4,1,4,5,4,57,8,4,10,4,12,4,60,9,4,1,5,1,5,1,5,3,5,65,8,5,1,5,1,
        5,1,5,1,5,1,5,3,5,72,8,5,1,5,1,5,3,5,76,8,5,1,6,1,6,3,6,80,8,6,1,
        7,1,7,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,10,0,0,11,0,2,4,6,8,10,
        12,14,16,18,20,0,3,2,0,2,3,7,7,1,0,2,3,1,0,5,6,90,0,22,1,0,0,0,2,
        34,1,0,0,0,4,41,1,0,0,0,6,45,1,0,0,0,8,54,1,0,0,0,10,75,1,0,0,0,
        12,79,1,0,0,0,14,81,1,0,0,0,16,85,1,0,0,0,18,87,1,0,0,0,20,89,1,
        0,0,0,22,24,3,2,1,0,23,25,3,4,2,0,24,23,1,0,0,0,25,26,1,0,0,0,26,
        24,1,0,0,0,26,27,1,0,0,0,27,28,1,0,0,0,28,30,3,6,3,0,29,31,5,11,
        0,0,30,29,1,0,0,0,30,31,1,0,0,0,31,32,1,0,0,0,32,33,5,0,0,1,33,1,
        1,0,0,0,34,38,5,9,0,0,35,37,5,9,0,0,36,35,1,0,0,0,37,40,1,0,0,0,
        38,36,1,0,0,0,38,39,1,0,0,0,39,3,1,0,0,0,40,38,1,0,0,0,41,43,5,10,
        0,0,42,44,7,0,0,0,43,42,1,0,0,0,43,44,1,0,0,0,44,5,1,0,0,0,45,51,
        3,10,5,0,46,47,3,8,4,0,47,48,3,10,5,0,48,50,1,0,0,0,49,46,1,0,0,
        0,50,53,1,0,0,0,51,49,1,0,0,0,51,52,1,0,0,0,52,7,1,0,0,0,53,51,1,
        0,0,0,54,58,7,1,0,0,55,57,5,12,0,0,56,55,1,0,0,0,57,60,1,0,0,0,58,
        56,1,0,0,0,58,59,1,0,0,0,59,9,1,0,0,0,60,58,1,0,0,0,61,62,3,12,6,
        0,62,64,3,16,8,0,63,65,5,7,0,0,64,63,1,0,0,0,64,65,1,0,0,0,65,66,
        1,0,0,0,66,67,3,20,10,0,67,76,1,0,0,0,68,69,3,12,6,0,69,71,3,18,
        9,0,70,72,5,7,0,0,71,70,1,0,0,0,71,72,1,0,0,0,72,73,1,0,0,0,73,74,
        3,20,10,0,74,76,1,0,0,0,75,61,1,0,0,0,75,68,1,0,0,0,76,11,1,0,0,
        0,77,80,3,14,7,0,78,80,5,8,0,0,79,77,1,0,0,0,79,78,1,0,0,0,80,13,
        1,0,0,0,81,82,5,8,0,0,82,83,5,1,0,0,83,84,5,8,0,0,84,15,1,0,0,0,
        85,86,5,4,0,0,86,17,1,0,0,0,87,88,7,2,0,0,88,19,1,0,0,0,89,90,5,
        10,0,0,90,21,1,0,0,0,10,26,30,38,43,51,58,64,71,75,79
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


        def DOT(self):
            return self.getToken(InvoiceParser.DOT, 0)

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
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 29
                self.match(InvoiceParser.DOT)


            self.state = 32
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
            self.state = 34
            self.match(InvoiceParser.NOMBRE)
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 35
                self.match(InvoiceParser.NOMBRE)
                self.state = 40
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
            self.state = 41
            self.match(InvoiceParser.WORD)
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 140) != 0):
                self.state = 42
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
            self.state = 45
            self.purchase()
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2 or _la==3:
                self.state = 46
                self.separator()
                self.state = 47
                self.purchase()
                self.state = 53
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
            self.state = 54
            _la = self._input.LA(1)
            if not(_la==2 or _la==3):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 55
                self.match(InvoiceParser.WS)
                self.state = 60
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
            self.state = 75
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.quantity()

                self.state = 62
                self.unit()
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==7:
                    self.state = 63
                    self.match(InvoiceParser.DE)


                self.state = 66
                self.fruit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 68
                self.quantity()

                self.state = 69
                self.pieceUnit()
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==7:
                    self.state = 70
                    self.match(InvoiceParser.DE)


                self.state = 73
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
            self.state = 79
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.fraction()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 78
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
            self.state = 81
            self.match(InvoiceParser.NUMBER)
            self.state = 82
            self.match(InvoiceParser.T__0)
            self.state = 83
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
            self.state = 85
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
            self.state = 87
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
            self.state = 89
            self.match(InvoiceParser.WORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





