import ply.yacc as yacc
from lexico import tokens

# Definición de las reglas de gramática
def p_programa(p):
    '''programa : declaraciones'''
    p[0] = p[1]

def p_declaraciones(p):
    '''declaraciones : declaracion
                     | declaraciones declaracion'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_declaracion(p):
    '''declaracion : asignacion
                   | impresion
                   | condicional
                   | ciclo_while'''
    p[0] = p[1]

def p_asignacion(p):
    'asignacion : VARIABLE ID IGUAL expresion'
    p[0] = ('asignacion', p[2], p[4])

def p_impresion(p):
    'impresion : IMPRIMIR PARENTESIS_IZQ expresion PARENTESIS_DER'
    p[0] = ('imprimir', p[3])

def p_condicional(p):
    '''condicional : SI PARENTESIS_IZQ expresion PARENTESIS_DER LLAVE_IZQ declaraciones LLAVE_DER
                   | SI PARENTESIS_IZQ expresion PARENTESIS_DER LLAVE_IZQ declaraciones LLAVE_DER SINO LLAVE_IZQ declaraciones LLAVE_DER'''
    if len(p) == 8:
        p[0] = ('si_sino', p[3], p[6], None)
    else:
        p[0] = ('si_sino', p[3], p[6], p[10])

def p_ciclo_while(p):
    'ciclo_while : MIENTRAS PARENTESIS_IZQ expresion PARENTESIS_DER LLAVE_IZQ declaraciones LLAVE_DER'
    p[0] = ('mientras', p[3], p[6])

def p_expresion(p):
    '''expresion : ID
                 | NUMERO
                 | CADENA
                 | expresion SUMA expresion
                 | expresion RESTA expresion
                 | expresion MULTIPLICACION expresion
                 | expresion DIVISION expresion
                 | expresion MENOR expresion
                 | expresion MAYOR expresion'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[2], p[1], p[3])

# Manejo de errores de sintaxis
def p_error(p):
    if p:
        print(f"Error de sintaxis en token '{p.value}'")
    else:
        print("Error de sintaxis en EOF")

# Construir el parser
parser = yacc.yacc(debug=True, write_tables=False, outputdir='.')
