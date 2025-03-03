from practicas2.csv.backend.output.CSVVisitor import CSVVisitor
from practicas2.csv.backend.output.CSVParser import CSVParser

class MyVisitor(CSVVisitor):
    def __init__(self):
        self.contador = 0 # Contador de campos del CSV
        self.encabezado = [] # Lista con el encabezado
        self.filas = [] # Lista con cada una de las columnas

    def visitFile(self, ctx:CSVParser.FileContext):
        if ctx.header():
            self.encabezado = self.visit(ctx.header())
        for row in ctx.row():
            rows = self.visit(row)
            # Conversión de campos string -> float
            r2, r3, r4, r5, r6, r7, r8, r9 = map(float, (rows[2], rows[3], rows[4], rows[5], rows[6], rows[7], rows[8], rows[9]))
            pa = 0.1 * ((r2 + r5 + r6 + r9) / 4)
            qn = 0.2 * ((r3 + r4) / 2)
            lab = 0.4 * r7
            exa = 0.3 * r8
            cal = pa + qn + lab + exa # Suma de los promedios

            # Estas dos variables son las que irán en el csv
            red = 10 * (round(cal)) if cal >= 7 else 0 # Calficación absoluta
            cal_round = round(cal*10,2) # Calificación relativa

            # Inserción de las calificaciones en la fila correspondiente
            rows[10], rows[11] = str(cal_round), str(red)

            # Lista con las filas que irán dentro del CSV
            self.filas.append(rows)
        return rows
    
    def visitHeader(self, ctx:CSVParser.HeaderContext):
        return self.visit(ctx.non_empty_row())
    
    def visitNon_empty_row(self, ctx: CSVParser.Non_empty_rowContext):
        return [self.visit(field) for field in ctx.field()]

    def visitRow(self, ctx: CSVParser.RowContext):
        if ctx.getChildCount() == 1:  # Fila vacía
            return []
        return [self.visit(field) for field in ctx.field()]

    def visitField(self, ctx: CSVParser.FieldContext):
        if ctx.getChildCount() == 0:
            return None
        elif ctx.TEXT():
            text = ctx.TEXT().getText()
            print(text)
            self.contador += 1
            return text
        elif ctx.STRING():
            string = ctx.STRING().getText()
            self.contador += 1
            return string