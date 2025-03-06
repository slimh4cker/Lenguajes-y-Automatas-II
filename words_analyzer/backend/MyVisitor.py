from collections import defaultdict
from practicas2.words_analyzer.backend.output.WordsParser import WordsParser
from practicas2.words_analyzer.backend.output.WordsVisitor import WordsVisitor


class MyVisitor(WordsVisitor):
    def __init__(self):
        super().__init__()
        self.unique_fruits = set()
        self.fruits_by_month = defaultdict(set)
        self.fruit_counts = defaultdict(int)

    def visitTexto(self, ctx: WordsParser.TextoContext):
        for seccion in ctx.seccion_mes():
            self.visit(seccion)
        return {
            "unique": self.unique_fruits,
            "monthly": self.fruits_by_month,
            "counts": self.fruit_counts
        }

    def visitSeccion_mes(self, ctx: WordsParser.Seccion_mesContext):
        month = ctx.MONTH().getText()
        for fruta in ctx.fruta():
            fruit_name = self.visit(fruta)
            if fruit_name:
                self.unique_fruits.add(fruit_name)
                self.fruits_by_month[month].add(fruit_name)
                self.fruit_counts[fruit_name] += 1
        return None

    def visitFruta(self, ctx: WordsParser.FrutaContext):
        if ctx.FRUIT_SINGULAR():
            return ctx.FRUIT_SINGULAR().getText()
        elif ctx.FRUIT_PLURAL():
            plural = ctx.FRUIT_PLURAL().getText()
            mapping = {
                "Naranjas": "Naranja",
                "Mandarinas": "Mandarina",
                "Toronjas": "Toronja",
                "Fresas": "Fresa",
                "Guayabas": "Guayaba",
                "Limones": "Limón",
                "Piñas": "Piña",
                "Mangos": "Mango",
                "Papayas": "Papaya",
                "Melones": "Melón",
                "Sandías": "Sandía",
                "Ciruelas": "Ciruela",
                "Duraznos": "Durazno",
                "Higos": "Higo",
                "Peras": "Pera",
                "Tunas": "Tuna",
                "Manzanas": "Manzana",
                "Uvas": "Uva",
                "Granadas": "Granada"
            }
            return mapping.get(plural, plural)
        return None
