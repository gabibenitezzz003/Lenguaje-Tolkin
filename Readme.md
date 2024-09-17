# Proyecto Tolkin: Compilador de Lenguaje Élfico/Mordor a Python

## Descripción
El Proyecto Tolkin es un compilador que traduce un lenguaje de programación inspirado en el élfico (Sindarin) y la lengua de Mordor a Python. Este proyecto permite escribir código utilizando palabras clave de los lenguajes de la Tierra Media y lo convierte en código Python ejecutable.

## Características
- Léxico y sintaxis inspirados en el élfico y la lengua de Mordor
- Generación de código Python equivalente
- Ejecución del código Python generado
- Visualización del árbol de sintaxis abstracta

## Palabras clave del lenguaje
- `nauth`: Declaración de variable (élfico)
- `thand`: Condicional if (élfico)
- `ú`: Condicional else (élfico)
- `am`: Bucle while (élfico)
- `pedo`: Imprimir (élfico)
- `dûr`: Bucle for (élfico)
- `ash`: En (lengua de Mordor)
- `ghâsh`: Función (lengua de Mordor)
- `lûk`: Retornar (lengua de Mordor)

## Estructura del proyecto
- `lexico.py`: Analizador léxico
- `sintaxis.py`: Analizador sintáctico
- `compilador.py`: Generador de código
- `main.py`: Archivo principal para ejecutar el compilador

## Cómo usar
1. Asegúrate de tener Python y PLY (Python Lex-Yacc) instalados.
2. Clona el repositorio: `git clone https://github.com/tu-usuario/proyecto-tolkin.git`
3. Navega al directorio del proyecto: `cd proyecto-tolkin`
4. Ejecuta el compilador: `python main.py`

## Ejemplo de código