# Generated from Expr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#expr.
    def visitExpr(self, ctx:ExprParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#expr_prime.
    def visitExpr_prime(self, ctx:ExprParser.Expr_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#term.
    def visitTerm(self, ctx:ExprParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#term_prime.
    def visitTerm_prime(self, ctx:ExprParser.Term_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#factor.
    def visitFactor(self, ctx:ExprParser.FactorContext):
        return self.visitChildren(ctx)



del ExprParser