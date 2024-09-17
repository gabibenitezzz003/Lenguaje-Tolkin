import ply.lex as lex

# Palabras reservadas
reserved = {
    'thand': 'SI',           # 'si' en élfico
    'ú': 'SINO',             # 'sino' en élfico
    'am': 'MIENTRAS',        # 'mientras' en élfico
    'pedo': 'IMPRIMIR',      # 'imprimir' en élfico
    'nauth': 'VARIABLE',     # 'variable' en élfico
}

# Lista de tokens
tokens = [
    'ID', 'NUMERO', 'CADENA',
    'SUMA', 'RESTA', 'MULTIPLICACION', 'DIVISION',
    'MENOR', 'MAYOR', 'IGUAL',
    'PARENTESIS_IZQ', 'PARENTESIS_DER',
    'LLAVE_IZQ', 'LLAVE_DER'
] + list(reserved.values())

# Reglas para tokens simples
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_MENOR = r'<'
t_MAYOR = r'>'
t_IGUAL = r'='
t_PARENTESIS_IZQ = r'\('
t_PARENTESIS_DER = r'\)'
t_LLAVE_IZQ = r'\{'
t_LLAVE_DER = r'\}'

# Reglas para tokens complejos
def t_ID(t):
    r'[a-zA-ZñÑáéíóúÁÉÍÓÚ_][a-zA-ZñÑáéíóúÁÉÍÓÚ_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_CADENA(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]
    return t

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Regla para saltos de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejo de errores
def t_error(t):
    print(f"Caracter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()
