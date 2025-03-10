from practicas2.invoice.backend.output.InvoiceParser import InvoiceParser
from practicas2.invoice.backend.output.InvoiceVisitor import InvoiceVisitor
from collections import defaultdict
from practicas2.invoice.utils.func.fruta_funciones import (
    detectarFruta, crearFactura, dict_precios, normalize
)


class MyVisitor(InvoiceVisitor):
    def __init__(self):
        super().__init__()
        self.items = []  # Lista para almacenar los items
        self.client_name = ""  # Nombre del cliente

    def visitInvoice(self, ctx: InvoiceParser.InvoiceContext):
        self.items = []  # Reiniciar la lista de items
        self.client_name = self.visit(ctx.header())  # Capturar el nombre del cliente

        # Procesar cada compra
        for purchase in ctx.purchaseList().purchase():
            item = self.visit(purchase)
            if item:  # Si el item es válido, añadirlo a la lista
                self.items.append(item)

        # Crear la factura usando la función crearFactura
        datos_factura = {}
        for item in self.items:
            fruta = item["descripcion"]
            cantidad = item["cantidad"]
            datos_factura[fruta] = cantidad

        return crearFactura(datos_factura, self.client_name)

    def visitHeader(self, ctx: InvoiceParser.HeaderContext):
        # Capturar el nombre completo del cliente
        nombre_parts = [child.getText() for child in ctx.getChildren()]
        return " ".join(nombre_parts)

    def visitPurchase(self, ctx: InvoiceParser.PurchaseContext):
        # Capturar cantidad
        cantidad = float(str(self.visit(ctx.quantity())))

        # Capturar fruta
        fruta = self.visit(ctx.fruit())
        fruta_normalizada = detectarFruta(fruta)

        if not fruta_normalizada:
            return None  # Si no es una fruta válida, ignorar

        # Determinar unidad y precio
        if ctx.unit():  # Si es por kg
            unidad = "kg"
            precio = dict_precios.get(fruta_normalizada, 0)
        else:  # Si es por pieza
            unidad = "pieza"
            precio = dict_precios.get(fruta_normalizada, 0)

        # Calcular importe
        importe = cantidad * precio

        return {
            "descripcion": fruta_normalizada,
            "cantidad": cantidad,
            "unidad": unidad,
            "precio_unitario": precio,
            "importe": importe
        }

    def visitQuantity(self, ctx: InvoiceParser.QuantityContext):
        if ctx.NUMBER():
            return float(ctx.NUMBER().getText())
        else:
            return self.visit(ctx.fraction())

    def visitFraction(self, ctx: InvoiceParser.FractionContext):
        numerator = float(ctx.NUMBER(0).getText())
        denominator = float(ctx.NUMBER(1).getText())
        return numerator / denominator

    def visitFruit(self, ctx: InvoiceParser.FruitContext):
        fruta = ctx.getText()
        return normalize(fruta.lower())  # Convertir a minúsculas y eliminar acentos


