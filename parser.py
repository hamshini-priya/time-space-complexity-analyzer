import ast

def get_ast(code):
    try:
        return ast.parse(code)
    except SyntaxError as e:
        print("Syntax Error:", e)
        return None
