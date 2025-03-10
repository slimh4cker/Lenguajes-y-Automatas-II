from collections import defaultdict
from practicas2.words_analyzer.backend.output.WordsParser import WordsParser
from practicas2.words_analyzer.backend.output.WordsVisitor import WordsVisitor


class MyVisitor(WordsVisitor):
    def __init__(self):
        super().__init__()
        self.unique_fruits = set()
        self.fruits_by_month = defaultdict(int)
        self.fruit_counts = defaultdict(int)
        self.num = 1
        self.singular = None # NO BORRAR
        self.total_fruits = 0 # Total de frutas
        self.fruits = [
                        "naranja", "naranjas", "mandarina", "mandarinas", "toronja", "toronjas",
                        "fresa", "fresas", "guayaba", "guayabas", "limon", "limones",
                        "piña", "piñas", "mango", "mangos", "papaya", "papayas", "melon", "melones",
                        "sandia", "sandias", "ciruela", "ciruelas", "durazno", "duraznos", "higo", "higos",
                        "pera", "peras", "tuna", "tunas", "manzana", "manzanas", "uva", "uvas", "granada", "granadas"
                     ]
        self.fruits_plural = [
                    "naranjas", "mandarinas", "toronjas", "fresas", "guayabas", "limones",
                    "piñas", "mangos", "papayas", "melones", "sandias", "ciruelas",
                    "duraznos", "higos", "peras", "tunas", "manzanas", "uvas", "granadas"
                            ]
        
        self.fruits_singular = [
                    "naranja", "mandarina", "toronja", "fresa", "guayaba", "limone",
                    "piña", "mango", "papaya", "melon", "sandia", "ciruela",
                    "durazno", "higo", "pera", "tuna", "manzana", "uva", "granada"
                            ]

        self.mapping = {
            "naranjas": "Naranja",
            "mandarinas": "Mandarina",
            "toronjas": "Toronja",
            "fresas": "Fresa",
            "guayabas": "Guayaba",
            "limones": "Limon",
            "piñas": "Piña",
            "mangos": "Mango",
            "papayas": "Papaya",
            "melones": "Melon",
            "sandias": "Sandia",
            "ciruelas": "Ciruela",
            "duraznos": "Durazno",
            "higos": "Higo",
            "peras": "Pera",
            "tunas": "Tuna",
            "manzanas": "Manzana",
            "uvas": "Uva",
            "granadas": "Granada"
        }

    def visitTexto(self, ctx: WordsParser.TextoContext):
        for seccion in ctx.seccion_mes():
            self.visit(seccion)
        for otro in ctx.otro():
            self.visit(otro)
        
        return {
            "unique": self.unique_fruits,
            "monthly": self.fruits_by_month,
            "counts": self.fruit_counts,
            "total": self.total_fruits
            }
    
    def visitSeccion_mes(self, ctx: WordsParser.Seccion_mesContext):
        month = ctx.MONTH().getText()
        for otro in ctx.otro():
            fruit_names = self.visit(otro)
            if fruit_names:
                self.unique_fruits.update(fruit_names)
                self.fruits_by_month[month] += len(fruit_names)
                for fruit in fruit_names:
                    self.fruit_counts[fruit] += 1
                    
        return None



    def visitOtro(self, ctx: WordsParser.OtroContext):
        fruits_found = []  # Para almacenar todas las frutas encontradas
        
        for word in ctx.WORD():
            # Conversión de todo texto a Lower
            fruit = word.getText().lower()
            
            if fruit in self.fruits_singular:
                print(f"Singular: {fruit}")
                fruits_found.append(fruit.capitalize())
                self.total_fruits += 1
            
            elif fruit in self.fruits_plural:
                fruit_mapping = self.mapping.get(fruit, fruit)
                print(f"Plural: {fruit}")
                self.total_fruits += 1
                fruits_found.append(fruit_mapping)
        
        return fruits_found if fruits_found else None # Con esta gramatica no se puede retornar dentro de cada if

                