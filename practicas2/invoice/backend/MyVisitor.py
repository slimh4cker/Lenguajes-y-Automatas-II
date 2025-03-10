from backend.output.InvoiceParser import InvoiceParser
from backend.output.InvoiceVisitor import InvoiceVisitor
from lib.fruta_funciones import detectarFruta, crearFactura
from collections import defaultdict

class MyVisitor(InvoiceVisitor):

    def __init__(self):
        super().__init__()        

    def visitInvoice(self, ctx: InvoiceParser.InvoiceContext):
        self.datos = defaultdict(int)
        self.nombre = ""
        children=  self.visitChildren(ctx)


        #transformar a una sola lista para ser enviada

        return crearFactura(self.datos, self.nombre)
    

    def visitHeader(self, ctx: InvoiceParser.HeaderContext):

        #Aqui esta el nombre
        for child in ctx.getChildren():
            print("nombre:", child)
            self.nombre = self.nombre.join(child.getText()).join(" ")
        
        return self.visitChildren(ctx)



    def visitPurchase(self, ctx):
        cantidad = float(str(self.visit(ctx.quantity()))) #cantidad de precio
        fruta = self.visit(ctx.fruit())

        # si lo detectado no es una fruta
        if fruta == 0:
            return 0

        print("compra: ", cantidad, fruta)
        print( self.datos, self.nombre)

        # ----Agregar a diccionario----
        # Ver si ya esta en el diccionario
        if fruta in self.datos:
            self.datos[fruta] += cantidad
        else:
            self.datos[fruta] = cantidad
        
        return self.datos
        
        




    def visitQuantity(self, ctx):
        if ctx.NUMBER():        
            return ctx.NUMBER()
        else:       
            return self.visit(ctx.fraction()) #retorna la fraccion en decimal
        
    def visitFraction(self, ctx):
        denominator = int(str(ctx.NUMBER(0)))
        numerator = int(str(ctx.NUMBER(1)))
        return denominator/numerator #retorna la fraccion en decimal
    
    def visitFruit(self, ctx):
        #Detectar y normalizar el nombre de la fruta
        fruta = detectarFruta(ctx.getText())
        if fruta:
            return fruta
        else:
            return 0 #no es una fruta

    
    


