# Generated from Words.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .WordsParser import WordsParser
else:
    from WordsParser import WordsParser

# This class defines a complete generic visitor for a parse tree produced by WordsParser.

class WordsVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by WordsParser#texto.
    def visitTexto(self, ctx:WordsParser.TextoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WordsParser#seccion_mes.
    def visitSeccion_mes(self, ctx:WordsParser.Seccion_mesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WordsParser#fruta.
    def visitFruta(self, ctx:WordsParser.FrutaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WordsParser#otro.
    def visitOtro(self, ctx:WordsParser.OtroContext):
        return self.visitChildren(ctx)



del WordsParser