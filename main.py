import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from lexico import lexer
import sintaxis
parser = sintaxis.parser
from compilador import Compilador

def ejecutar(codigo):
    print("\n" + "="*50)
    print("COMPILADOR TOLKIN: Élfico/Lengua de Mordor a Python")
    print("="*50 + "\n")

    print("CÓDIGO FUENTE:")
    print("-"*50)
    print(codigo.strip())
    print("-"*50 + "\n")

    arbol = parser.parse(codigo, lexer=lexer)
    print("ÁRBOL DE SINTAXIS ABSTRACTA:")
    print("-"*50)
    imprimir_arbol(arbol)
    print("-"*50 + "\n")
    
    compilador = Compilador()
    if arbol:
        codigo_elfico_mordor, codigo_python = compilador.compilar(arbol)
        
        print("CÓDIGO EN ÉLFICO/LENGUA DE MORDOR:")
        print("-"*50)
        print(codigo_elfico_mordor)
        print("-"*50 + "\n")
        
        print("CÓDIGO PYTHON EQUIVALENTE:")
        print("-"*50)
        print(codigo_python)
        print("-"*50 + "\n")
        
        print("EJECUCIÓN DEL CÓDIGO GENERADO:")
        print("-"*50)
        exec(codigo_python)
        print("-"*50)
    else:
        print("ERROR: No se pudo generar el árbol de sintaxis abstracta.")

def imprimir_arbol(nodo, nivel=0):
    indentacion = "  " * nivel
    if isinstance(nodo, tuple):
        print(f"{indentacion}{nodo[0]}:")
        for elemento in nodo[1:]:
            imprimir_arbol(elemento, nivel + 1)
    elif isinstance(nodo, list):
        for elemento in nodo:
            imprimir_arbol(elemento, nivel)
    else:
        print(f"{indentacion}{nodo}")

def generar_resumen_parser():
    try:
        with open('parser.out', 'r', encoding='utf-8') as f:
            lineas = f.readlines()

        reglas = []
        terminales = []
        no_terminales = []
        estado_actual = None

        for linea in lineas:
            linea = linea.strip()
            if linea.startswith("Grammar"):
                estado_actual = "grammar"
            elif linea.startswith("Terminals"):
                estado_actual = "terminals"
            elif linea.startswith("Nonterminals"):
                estado_actual = "nonterminals"
            elif estado_actual == "grammar" and linea.startswith("Rule"):
                reglas.append(linea)
            elif estado_actual == "terminals" and linea and not linea.startswith("Terminals"):
                terminales.append(linea.split()[0])
            elif estado_actual == "nonterminals" and linea and not linea.startswith("Nonterminals"):
                no_terminales.append(linea.split()[0])

        # Generar el resumen en español
        resumen = "Resumen del Analizador Sintáctico\n"
        resumen += "================================\n\n"

        resumen += "Reglas Gramaticales:\n"
        resumen += "--------------------\n"
        for regla in reglas:
            num, contenido = regla.split(' ', 1)
            explicacion = explicar_regla(contenido)
            resumen += f"{regla}\n"
            resumen += f"Explicación: {explicacion}\n\n"

        resumen += "Símbolos Terminales:\n"
        resumen += "--------------------\n"
        resumen += ", ".join(sorted(set(terminales))) + "\n\n"

        resumen += "Símbolos No Terminales:\n"
        resumen += "------------------------\n"
        resumen += ", ".join(sorted(set([nt for nt in no_terminales if not nt.startswith('state')]))) + "\n\n"

        resumen += "Nota: Este resumen no incluye todos los detalles del archivo parser.out original.\n"
        resumen += "Para ver todos los detalles, por favor consulte el archivo parser.out completo.\n\n"

        # Añadir la comparativa
        resumen += "Comparativa de Léxicos: Tolkin vs Python\n"
        resumen += "======================================\n\n"
        resumen += "| Tolkin (Élfico/Mordor) | Python    | Descripción                |\n"
        resumen += "|------------------------|-----------|----------------------------|\n"
        resumen += "| nauth                  | =         | Asignación de variable     |\n"
        resumen += "| pedo                   | print     | Imprimir en consola        |\n"
        resumen += "| thand                  | if        | Condicional if             |\n"
        resumen += "| ú                      | else      | Condicional else           |\n"
        resumen += "| am                     | while     | Bucle while                |\n"
        resumen += "| +                      | +         | Suma                       |\n"
        resumen += "| -                      | -         | Resta                      |\n"
        resumen += "| *                      | *         | Multiplicación             |\n"
        resumen += "| /                      | /         | División                   |\n"
        resumen += "| <                      | <         | Menor que                  |\n"
        resumen += "| >                      | >         | Mayor que                  |\n"
        resumen += "| ==                     | ==        | Igual a                    |\n"
        resumen += "| !=                     | !=        | Diferente de               |\n"
        resumen += "| ( )                    | ( )       | Paréntesis                 |\n"
        resumen += "| { }                    | :         | Inicio/fin de bloque       |\n"

        # Guardar el resumen en un nuevo archivo
        with open('resumen_parser_es.txt', 'w', encoding='utf-8') as f:
            f.write(resumen)

        print("Se ha generado un resumen en español del archivo parser.out.")
        print("El resumen se encuentra en el archivo 'resumen_parser_es.txt'.")

    except FileNotFoundError:
        print("No se encontró el archivo parser.out. Asegúrese de que el archivo existe en el directorio actual.")
    except Exception as e:
        print(f"Ocurrió un error al generar el resumen: {str(e)}")

def explicar_regla(regla):
    if "S' -> programa" in regla:
        return "Regla inicial: Un programa completo."
    elif "programa -> declaraciones" in regla:
        return "Un programa consiste en una serie de declaraciones."
    elif "declaraciones -> declaracion" in regla:
        return "Las declaraciones pueden ser una sola declaración."
    elif "declaraciones -> declaraciones declaracion" in regla:
        return "Las declaraciones pueden ser múltiples declaraciones en secuencia."
    elif "declaracion -> asignacion" in regla:
        return "Una declaración puede ser una asignación de variable."
    elif "declaracion -> impresion" in regla:
        return "Una declaración puede ser una instrucción de impresión."
    elif "declaracion -> condicional" in regla:
        return "Una declaración puede ser una estructura condicional (if-else)."
    elif "declaracion -> ciclo_while" in regla:
        return "Una declaración puede ser un bucle while."
    elif "asignacion -> VARIABLE ID IGUAL expresion" in regla:
        return "Una asignación consiste en la palabra clave 'nauth', un identificador, el signo igual y una expresión."
    elif "impresion -> IMPRIMIR PARENTESIS_IZQ expresion PARENTESIS_DER" in regla:
        return "Una impresión consiste en la palabra clave 'pedo' seguida de una expresión entre paréntesis."
    elif "condicional -> SI PARENTESIS_IZQ expresion PARENTESIS_DER LLAVE_IZQ declaraciones LLAVE_DER" in regla:
        return "Un condicional 'if' con su condición y bloque de código."
    elif "condicional -> SI PARENTESIS_IZQ expresion PARENTESIS_DER LLAVE_IZQ declaraciones LLAVE_DER SINO LLAVE_IZQ declaraciones LLAVE_DER" in regla:
        return "Un condicional 'if-else' completo con ambos bloques de código."
    elif "ciclo_while -> MIENTRAS PARENTESIS_IZQ expresion PARENTESIS_DER LLAVE_IZQ declaraciones LLAVE_DER" in regla:
        return "Un bucle 'while' con su condición y bloque de código."
    elif "expresion -> ID" in regla:
        return "Una expresión puede ser un identificador de variable."
    elif "expresion -> NUMERO" in regla:
        return "Una expresión puede ser un número."
    elif "expresion -> CADENA" in regla:
        return "Una expresión puede ser una cadena de texto."
    elif "expresion -> expresion SUMA expresion" in regla:
        return "Una expresión puede ser la suma de dos expresiones."
    elif "expresion -> expresion RESTA expresion" in regla:
        return "Una expresión puede ser la resta de dos expresiones."
    elif "expresion -> expresion MULTIPLICACION expresion" in regla:
        return "Una expresión puede ser la multiplicación de dos expresiones."
    elif "expresion -> expresion DIVISION expresion" in regla:
        return "Una expresión puede ser la división de dos expresiones."
    elif "expresion -> expresion MENOR expresion" in regla:
        return "Una expresión puede ser una comparación 'menor que' entre dos expresiones."
    elif "expresion -> expresion MAYOR expresion" in regla:
        return "Una expresión puede ser una comparación 'mayor que' entre dos expresiones."
    else:
        return "Regla no reconocida."

# Código de ejemplo
codigo_ejemplo = '''
nauth x = 10
nauth y = 20
thand (x < y) {
    pedo("x es menor que y")
} ú {
    pedo("x no es menor que y")
}
am (x < y) {
    pedo(x)
    nauth x = x + 1
}
'''

if __name__ == "__main__":
    ejecutar(codigo_ejemplo)
    generar_resumen_parser()

