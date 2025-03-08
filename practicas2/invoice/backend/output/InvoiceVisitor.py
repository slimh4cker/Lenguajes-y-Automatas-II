# Generated from Invoice.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .InvoiceParser import InvoiceParser
else:
    from InvoiceParser import InvoiceParser

# This class defines a complete generic visitor for a parse tree produced by InvoiceParser.

class InvoiceVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by InvoiceParser#invoice.
    def visitInvoice(self, ctx:InvoiceParser.InvoiceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InvoiceParser#header.
    def visitHeader(self, ctx:InvoiceParser.HeaderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InvoiceParser#verb.
    def visitVerb(self, ctx:InvoiceParser.VerbContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InvoiceParser#purchaseList.
    def visitPurchaseList(self, ctx:InvoiceParser.PurchaseListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InvoiceParser#separator.
    def visitSeparator(self, ctx:InvoiceParser.SeparatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InvoiceParser#purchase.
    def visitPurchase(self, ctx:InvoiceParser.PurchaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InvoiceParser#quantity.
    def visitQuantity(self, ctx:InvoiceParser.QuantityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InvoiceParser#fraction.
    def visitFraction(self, ctx:InvoiceParser.FractionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InvoiceParser#unit.
    def visitUnit(self, ctx:InvoiceParser.UnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InvoiceParser#pieceUnit.
    def visitPieceUnit(self, ctx:InvoiceParser.PieceUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InvoiceParser#fruit.
    def visitFruit(self, ctx:InvoiceParser.FruitContext):
        return self.visitChildren(ctx)



del InvoiceParser