from practicas2.invoice.backend.output.InvoiceParser import InvoiceParser
from practicas2.invoice.backend.output.InvoiceVisitor import InvoiceVisitor

class MyVisitor(InvoiceVisitor):
    def __init__(self):
        super().__init__()


    def visitInvoice(self, ctx: InvoiceParser.InvoiceContext):
        return 
    

    # Así con las demas producciones
    



