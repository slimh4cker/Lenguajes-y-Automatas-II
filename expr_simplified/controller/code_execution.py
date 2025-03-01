from antlr4 import InputStream, CommonTokenStream
from practicas2.expr_simplified.controller.MyVisitor import MyVisitor
from practicas2.expr_simplified.controller.output.ExprLexer import ExprLexer
from practicas2.expr_simplified.controller.output.ExprParser import ExprParser
from practicas2.expr_simplified.utils.classes.TreeGenerator import TreeGenerator


def generate_trees(input_expr):
    trees = []
    for line in input_expr.split('\n'):
        if line.strip():
            try:
                line_stream = InputStream(line.strip())
                lexer = ExprLexer(line_stream)
                tokens = CommonTokenStream(lexer)
                parser = ExprParser(tokens)
                tree = parser.expr()
                image_buffer = TreeGenerator.generate_tree_image(tree, parser)
                if image_buffer:
                    trees.append(image_buffer)
            except:
                continue
    return trees


def execute_code(input_expr):
    try:
        input_stream = InputStream(input_expr)
        lexer = ExprLexer(input_stream)
        tokens = CommonTokenStream(lexer)
        parser = ExprParser(tokens)
        tree = parser.expr()
        visitor = MyVisitor()
        result = visitor.visit(tree)
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"
