# Generated from CSV.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CSVParser import CSVParser
else:
    from CSVParser import CSVParser

# This class defines a complete generic visitor for a parse tree produced by CSVParser.

class CSVVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CSVParser#file.
    def visitFile(self, ctx:CSVParser.FileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSVParser#header.
    def visitHeader(self, ctx:CSVParser.HeaderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSVParser#non_empty_row.
    def visitNon_empty_row(self, ctx:CSVParser.Non_empty_rowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSVParser#row.
    def visitRow(self, ctx:CSVParser.RowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSVParser#field.
    def visitField(self, ctx:CSVParser.FieldContext):
        return self.visitChildren(ctx)



del CSVParser