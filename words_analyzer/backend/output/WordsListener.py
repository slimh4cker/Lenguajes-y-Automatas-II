# Generated from Words.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .WordsParser import WordsParser
else:
    from WordsParser import WordsParser

# This class defines a complete listener for a parse tree produced by WordsParser.
class WordsListener(ParseTreeListener):

    # Enter a parse tree produced by WordsParser#texto.
    def enterTexto(self, ctx:WordsParser.TextoContext):
        pass

    # Exit a parse tree produced by WordsParser#texto.
    def exitTexto(self, ctx:WordsParser.TextoContext):
        pass


    # Enter a parse tree produced by WordsParser#seccion_mes.
    def enterSeccion_mes(self, ctx:WordsParser.Seccion_mesContext):
        pass

    # Exit a parse tree produced by WordsParser#seccion_mes.
    def exitSeccion_mes(self, ctx:WordsParser.Seccion_mesContext):
        pass


    # Enter a parse tree produced by WordsParser#fruta.
    def enterFruta(self, ctx:WordsParser.FrutaContext):
        pass

    # Exit a parse tree produced by WordsParser#fruta.
    def exitFruta(self, ctx:WordsParser.FrutaContext):
        pass


    # Enter a parse tree produced by WordsParser#otro.
    def enterOtro(self, ctx:WordsParser.OtroContext):
        pass

    # Exit a parse tree produced by WordsParser#otro.
    def exitOtro(self, ctx:WordsParser.OtroContext):
        pass



del WordsParser