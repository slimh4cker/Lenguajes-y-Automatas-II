from antlr4 import InputStream, CommonTokenStream
from practicas2.csv.backend.output.CSVParser import CSVParser
from practicas2.csv.backend.output.CSVLexer import CSVLexer
from practicas2.csv.utils.classes.CSVErrorHandler import CSVErrorHandler


def csv_processing(input_data: str) -> tuple[CSVParser, CSVLexer, CommonTokenStream, CSVErrorHandler]:
    input_stream = InputStream(input_data)
    lexer = CSVLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = CSVParser(tokens)
    error_handler = CSVErrorHandler()
    lexer.removeErrorListeners()
    parser.removeErrorListeners()
    lexer.addErrorListener(error_handler)
    parser.addErrorListener(error_handler)

    return parser, lexer, tokens, error_handler
