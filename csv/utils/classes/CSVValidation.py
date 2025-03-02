from practicas2.csv.backend.output.CSVParser import CSVParser
from practicas2.csv.backend.output.CSVListener import CSVListener


class CSVValidationListener(CSVListener):
    def __init__(self):
        self.errors = []
        self.header_fields = []
        self.expected_fields = 0
        self.num_fields_current_row = 0
        self.total_fields = 0

    def enterNon_empty_row(self, ctx: CSVParser.Non_empty_rowContext):
        if ctx.parentCtx and isinstance(ctx.parentCtx, CSVParser.HeaderContext):
            self.header_fields = [field.TEXT().getText() if field.TEXT() else "" for field in ctx.field()]
            self.expected_fields = len(self.header_fields)
            self.num_fields_current_row = len(ctx.field())
            self.total_fields += self.num_fields_current_row
            for field in ctx.field():
                text = field.TEXT().getText() if field.TEXT() else ""
                if not text:
                    self.errors.append("Error: Header field cannot be empty")
                elif any(c.isspace() for c in text):
                    self.errors.append(f"Invalid header '{text}': Contains whitespace")

            self.header_fields = [f.TEXT().getText() if f.TEXT() else "" for f in ctx.field()]
            self.expected_fields = len(self.header_fields)

            if len(self.header_fields) != len(set(self.header_fields)):
                self.errors.append("Error: Duplicate header fields")

    def enterRow(self, ctx: CSVParser.RowContext):
        num_fields = len(ctx.field())
        self.total_fields += num_fields
        if not isinstance(ctx.parentCtx, CSVParser.HeaderContext):
            actual_fields = len(ctx.field())
            if actual_fields != self.expected_fields:
                self.errors.append(f"Row has {actual_fields} fields, expected {self.expected_fields}")