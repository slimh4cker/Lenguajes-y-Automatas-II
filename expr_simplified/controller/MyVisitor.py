from practicas2.expr_simplified.controller.output.ExprParser import ExprParser
from practicas2.expr_simplified.controller.output.ExprVisitor import ExprVisitor


class MyVisitor(ExprVisitor):
    def __init__(self):
        self.output = []

    def visitExpr(self, ctx: ExprParser.ExprContext):
        result = self.visit(ctx.term()) + self.visit(ctx.expr_prime())
        self.output.append(result)
        return result

    def visitExpr_prime(self, ctx: ExprParser.Expr_primeContext):
        if ctx.getChildCount() == 0:
            return 0
        elif ctx.ADD():
            return self.visit(ctx.term()) + self.visit(ctx.expr_prime())
        elif ctx.SUBTRACT():
            return -self.visit(ctx.term()) + self.visit(ctx.expr_prime())

    def visitTerm(self, ctx: ExprParser.TermContext):
        return self.visit(ctx.factor()) * self.visit(ctx.term_prime())

    def visitTerm_prime(self, ctx: ExprParser.Term_primeContext):
        if ctx.getChildCount() == 0:
            return 1
        elif ctx.MULTI():
            return self.visit(ctx.factor()) * self.visit(ctx.term_prime())
        elif ctx.DIVI():
            return 1 / self.visit(ctx.factor()) * self.visit(ctx.term_prime())

    def visitFactor(self, ctx: ExprParser.FactorContext):
        if ctx.ID():
            return int(ctx.ID().getText())
        elif ctx.LEFT_PARENTH():
            return self.visit(ctx.expr())
