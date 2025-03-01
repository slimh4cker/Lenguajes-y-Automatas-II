# Generated from Expr.g4 by ANTLR 4.13.2
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
        4,1,9,46,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,23,8,1,1,2,1,2,1,2,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,37,8,3,1,4,1,4,1,4,1,4,1,4,3,4,44,
        8,4,1,4,0,0,5,0,2,4,6,8,0,0,45,0,10,1,0,0,0,2,22,1,0,0,0,4,24,1,
        0,0,0,6,36,1,0,0,0,8,43,1,0,0,0,10,11,3,4,2,0,11,12,3,2,1,0,12,1,
        1,0,0,0,13,23,1,0,0,0,14,15,5,1,0,0,15,16,3,4,2,0,16,17,3,2,1,0,
        17,23,1,0,0,0,18,19,5,2,0,0,19,20,3,4,2,0,20,21,3,2,1,0,21,23,1,
        0,0,0,22,13,1,0,0,0,22,14,1,0,0,0,22,18,1,0,0,0,23,3,1,0,0,0,24,
        25,3,8,4,0,25,26,3,6,3,0,26,5,1,0,0,0,27,37,1,0,0,0,28,29,5,3,0,
        0,29,30,3,8,4,0,30,31,3,6,3,0,31,37,1,0,0,0,32,33,5,4,0,0,33,34,
        3,8,4,0,34,35,3,6,3,0,35,37,1,0,0,0,36,27,1,0,0,0,36,28,1,0,0,0,
        36,32,1,0,0,0,37,7,1,0,0,0,38,44,5,7,0,0,39,40,5,5,0,0,40,41,3,0,
        0,0,41,42,5,6,0,0,42,44,1,0,0,0,43,38,1,0,0,0,43,39,1,0,0,0,44,9,
        1,0,0,0,3,22,36,43
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "ADD", "SUBTRACT", "MULTI", "DIVI", "LEFT_PARENTH", 
                      "RIGHT_PARENTH", "ID", "DIGIT", "WS" ]

    RULE_expr = 0
    RULE_expr_prime = 1
    RULE_term = 2
    RULE_term_prime = 3
    RULE_factor = 4

    ruleNames =  [ "expr", "expr_prime", "term", "term_prime", "factor" ]

    EOF = Token.EOF
    ADD=1
    SUBTRACT=2
    MULTI=3
    DIVI=4
    LEFT_PARENTH=5
    RIGHT_PARENTH=6
    ID=7
    DIGIT=8
    WS=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(ExprParser.TermContext,0)


        def expr_prime(self):
            return self.getTypedRuleContext(ExprParser.Expr_primeContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = ExprParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.term()
            self.state = 11
            self.expr_prime()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(ExprParser.ADD, 0)

        def term(self):
            return self.getTypedRuleContext(ExprParser.TermContext,0)


        def expr_prime(self):
            return self.getTypedRuleContext(ExprParser.Expr_primeContext,0)


        def SUBTRACT(self):
            return self.getToken(ExprParser.SUBTRACT, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_expr_prime

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_prime" ):
                listener.enterExpr_prime(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_prime" ):
                listener.exitExpr_prime(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_prime" ):
                return visitor.visitExpr_prime(self)
            else:
                return visitor.visitChildren(self)




    def expr_prime(self):

        localctx = ExprParser.Expr_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr_prime)
        try:
            self.state = 22
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 14
                self.match(ExprParser.ADD)
                self.state = 15
                self.term()
                self.state = 16
                self.expr_prime()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 18
                self.match(ExprParser.SUBTRACT)
                self.state = 19
                self.term()
                self.state = 20
                self.expr_prime()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(ExprParser.FactorContext,0)


        def term_prime(self):
            return self.getTypedRuleContext(ExprParser.Term_primeContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = ExprParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_term)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.factor()
            self.state = 25
            self.term_prime()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Term_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MULTI(self):
            return self.getToken(ExprParser.MULTI, 0)

        def factor(self):
            return self.getTypedRuleContext(ExprParser.FactorContext,0)


        def term_prime(self):
            return self.getTypedRuleContext(ExprParser.Term_primeContext,0)


        def DIVI(self):
            return self.getToken(ExprParser.DIVI, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_term_prime

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm_prime" ):
                listener.enterTerm_prime(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm_prime" ):
                listener.exitTerm_prime(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm_prime" ):
                return visitor.visitTerm_prime(self)
            else:
                return visitor.visitChildren(self)




    def term_prime(self):

        localctx = ExprParser.Term_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_term_prime)
        try:
            self.state = 36
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 6]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.match(ExprParser.MULTI)
                self.state = 29
                self.factor()
                self.state = 30
                self.term_prime()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 32
                self.match(ExprParser.DIVI)
                self.state = 33
                self.factor()
                self.state = 34
                self.term_prime()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def LEFT_PARENTH(self):
            return self.getToken(ExprParser.LEFT_PARENTH, 0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def RIGHT_PARENTH(self):
            return self.getToken(ExprParser.RIGHT_PARENTH, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = ExprParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_factor)
        try:
            self.state = 43
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                self.match(ExprParser.ID)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.match(ExprParser.LEFT_PARENTH)
                self.state = 40
                self.expr()
                self.state = 41
                self.match(ExprParser.RIGHT_PARENTH)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





