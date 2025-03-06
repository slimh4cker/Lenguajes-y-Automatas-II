from backend.output.WordsParser import WordsParser
from backend.output.WordsVisitor import WordsVisitor

class MyVisitor(WordsVisitor):
    def __init__(self):
        super().__init__()
        self.unique_fruits = set()  # Set no permite valores repetidos

    def visitTexto(self, ctx: WordsParser.TextoContext):
        for seccion in ctx.seccion_mes():
            self.visit(seccion)
        for otro in ctx.otro():
            self.visit(otro)
        print(self.unique_fruits) # Para validar las frutas
        return len(self.unique_fruits)

    def visitSeccion_mes(self, ctx: WordsParser.Seccion_mesContext):
        for f in ctx.fruta():
            self.visit(f)
        for otro in ctx.otro():
            self.visit(otro)
        return None

    def visitFruta(self, ctx: WordsParser.FrutaContext):
        fruit = None
        if ctx.FRUIT_SINGULAR() is not None:
            fruit = ctx.FRUIT_SINGULAR().getText()
        # si es plural se convierte a singular
        elif ctx.FRUIT_PLURAL() is not None:
            plural_fruit = ctx.FRUIT_PLURAL().getText()
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
            fruit = mapping.get(plural_fruit, plural_fruit)
        if fruit:
            self.unique_fruits.add(fruit)
        return None
