# Generated from Invoice.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .InvoiceParser import InvoiceParser
else:
    from InvoiceParser import InvoiceParser

# This class defines a complete listener for a parse tree produced by InvoiceParser.
class InvoiceListener(ParseTreeListener):

    # Enter a parse tree produced by InvoiceParser#invoice.
    def enterInvoice(self, ctx:InvoiceParser.InvoiceContext):
        pass

    # Exit a parse tree produced by InvoiceParser#invoice.
    def exitInvoice(self, ctx:InvoiceParser.InvoiceContext):
        pass


    # Enter a parse tree produced by InvoiceParser#header.
    def enterHeader(self, ctx:InvoiceParser.HeaderContext):
        pass

    # Exit a parse tree produced by InvoiceParser#header.
    def exitHeader(self, ctx:InvoiceParser.HeaderContext):
        pass


    # Enter a parse tree produced by InvoiceParser#verb.
    def enterVerb(self, ctx:InvoiceParser.VerbContext):
        pass

    # Exit a parse tree produced by InvoiceParser#verb.
    def exitVerb(self, ctx:InvoiceParser.VerbContext):
        pass


    # Enter a parse tree produced by InvoiceParser#purchaseList.
    def enterPurchaseList(self, ctx:InvoiceParser.PurchaseListContext):
        pass

    # Exit a parse tree produced by InvoiceParser#purchaseList.
    def exitPurchaseList(self, ctx:InvoiceParser.PurchaseListContext):
        pass


    # Enter a parse tree produced by InvoiceParser#separator.
    def enterSeparator(self, ctx:InvoiceParser.SeparatorContext):
        pass

    # Exit a parse tree produced by InvoiceParser#separator.
    def exitSeparator(self, ctx:InvoiceParser.SeparatorContext):
        pass


    # Enter a parse tree produced by InvoiceParser#purchase.
    def enterPurchase(self, ctx:InvoiceParser.PurchaseContext):
        pass

    # Exit a parse tree produced by InvoiceParser#purchase.
    def exitPurchase(self, ctx:InvoiceParser.PurchaseContext):
        pass


    # Enter a parse tree produced by InvoiceParser#quantity.
    def enterQuantity(self, ctx:InvoiceParser.QuantityContext):
        pass

    # Exit a parse tree produced by InvoiceParser#quantity.
    def exitQuantity(self, ctx:InvoiceParser.QuantityContext):
        pass


    # Enter a parse tree produced by InvoiceParser#fraction.
    def enterFraction(self, ctx:InvoiceParser.FractionContext):
        pass

    # Exit a parse tree produced by InvoiceParser#fraction.
    def exitFraction(self, ctx:InvoiceParser.FractionContext):
        pass


    # Enter a parse tree produced by InvoiceParser#unit.
    def enterUnit(self, ctx:InvoiceParser.UnitContext):
        pass

    # Exit a parse tree produced by InvoiceParser#unit.
    def exitUnit(self, ctx:InvoiceParser.UnitContext):
        pass


    # Enter a parse tree produced by InvoiceParser#pieceUnit.
    def enterPieceUnit(self, ctx:InvoiceParser.PieceUnitContext):
        pass

    # Exit a parse tree produced by InvoiceParser#pieceUnit.
    def exitPieceUnit(self, ctx:InvoiceParser.PieceUnitContext):
        pass


    # Enter a parse tree produced by InvoiceParser#fruit.
    def enterFruit(self, ctx:InvoiceParser.FruitContext):
        pass

    # Exit a parse tree produced by InvoiceParser#fruit.
    def exitFruit(self, ctx:InvoiceParser.FruitContext):
        pass



del InvoiceParser