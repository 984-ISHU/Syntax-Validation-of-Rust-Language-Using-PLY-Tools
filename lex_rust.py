import ply.lex as lex

# List of token names
tokens = (
    'FOR',
    'LET',
    'CONST',
    'FN',
    'IN',
    'RETURN',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'SEMICOLON',
    'IF',
    'ELSE',
    'STRUCT',
    'TYPE',
    'COMMA',
    'EQUALS',
    'DOTDOT',
    'GREATER',
    'LESS',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'NUMBER',
    'BOOL',  
    'STRING',  
    'COLON', 
    'INCREMENT',
    'DECREMENT',
    'IDENTIFIER'
)

# Regular expressions for tokens
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r';'
t_COLON = r':'
t_COMMA = r','
t_EQUALS = r'='
t_DOTDOT = r'\.\.'
t_GREATER = r'\>'
t_LESS = r'\<'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_INCREMENT = r'\+\+'
t_DECREMENT = r'\+\+'

def t_FOR(t):
    r'for'
    return t

def t_IN(t):
    r'in'
    return t

def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_STRUCT(t):
    r'struct'
    return t

def t_RETURN(t):
    r'return'
    return t

def t_TYPE(t):
    r'i32|i64|u32|u64|f32|f64|char|bool'
    return t

def t_FN(t):
    r'fn'
    return t

def t_LET(t):
    r'let'
    return t

def t_CONST(t):
    r'const'
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_BOOL(t):
    r'true|false'
    return t

def t_STRING(t):
    r'"([^"\\]|\\.)*"'
    return t




t_ignore = ' \t\n'

# Define a function to capture errors
def t_error(t):
    print(f"Illegal character: '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()



# Example Rust code
file_path = 'exampleInput.txt'
with open(file_path, 'r') as file:
    rust_code = file.read()
# Give the lexer some input
lexer.input(rust_code)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)


