import ply.yacc as yacc

from lex_rust import tokens

# Define the grammar for Rust constructs
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'INCREMENT', 'DECREMENT'),
)

def p_for_loop(p):
    '''
    for_loop : FOR IDENTIFIER IN expression DOTDOT expression LBRACE statements RBRACE statements
             | FOR IDENTIFIER IN IDENTIFIER LBRACE statements RBRACE statements
    '''
    p[0] = 'Valid Rust Syntax'

def p_if_else(p):
    '''
    if_else : IF condition LBRACE statements RBRACE else_part statements
    '''
    p[0] = 'Valid Rust Syntax'

def p_else_part(p):
    '''
    else_part : ELSE LBRACE statements RBRACE statements
              | ELSE if_else statements
              | empty statements
    '''


def p_struct_def(p):
    '''
    struct_def : STRUCT IDENTIFIER LBRACE struct_body RBRACE statements
    '''
    p[0] = 'Valid Rust Syntax'

def p_struct_body(p):
    '''
    struct_body : IDENTIFIER COLON TYPE COMMA struct_body
                | IDENTIFIER COLON TYPE
                | empty
    '''
    p[0] = 'Valid Rust Syntax'

def p_var(p):
    '''
    var : LET name SEMICOLON statements
        | CONST name EQUALS value SEMICOLON statements
        | LET name EQUALS value SEMICOLON statements
        | CONST name EQUALS value SEMICOLON var statements
        | LET name EQUALS value SEMICOLON var statements
        | CONST name SEMICOLON statements
        | CONST name SEMICOLON var statements
        | LET name SEMICOLON var statements
        | empty 
    '''
    p[0] = 'Valid Rust Syntax'


def p_name(p):
    '''
    name : IDENTIFIER 
         | IDENTIFIER COLON TYPE
    '''

def p_value(p):
    '''
    value : BOOL
          | STRING
          | NUMBER
          | expression
    '''

def p_function_def(p):
    '''
    function_def : FN IDENTIFIER LPAREN parameters RPAREN LBRACE statements RETURN statement RBRACE statements
    '''
    p[0] = 'Valid Rust Syntax'

def p_parameters(p):
    '''
    parameters : IDENTIFIER COLON TYPE COMMA parameters
               | IDENTIFIER COLON TYPE
               | empty
    '''

def p_statements(p):
    '''
    statements : statement
               | statements statement
               | empty
    '''

def p_statement(p):
    '''
    statement : for_loop
              | if_else
              | struct_def
              | var
              | function_def
              | expression SEMICOLON
              | empty
    '''
    p[0] = 'Valid Rust Syntax'

def p_condition(p):
    '''
    condition : expression
              | expression GREATER expression
              | expression LESS expression
              | expression GREATER EQUALS expression
              | expression LESS EQUALS expression
              | expression EQUALS EQUALS expression
    '''
    p[0] = 'Valid Rust Syntax'

def p_expression(p):
    '''
    expression : expression PLUS expression
               | expression EQUALS expression
               | expression MINUS expression
               | expression TIMES expression
               | expression DIVIDE expression
               | expression INCREMENT
               | expression DECREMENT
               | INCREMENT expression 
               | DECREMENT expression 
               | NUMBER
               | IDENTIFIER
    '''
    p[0] = 'Valid Rust Syntax'

def p_empty(p):
    'empty :'
    pass

# Error handling
def p_error(p):
    if p:
        print(f"Syntax error at line {p.lineno}, position {p.lexpos}: Unexpected token '{p.value}'")
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc(debug=False, write_tables=False)

# Example Rust code
file_path = 'exampleInput.txt'
with open(file_path, 'r') as file:
    rust_code = file.read()

# Parse the Rust code
result = parser.parse(rust_code)
print(result)