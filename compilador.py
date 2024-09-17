class Compilador:
    def __init__(self):
        self.codigo_elfico_mordor = []
        self.codigo_python = []
        self.indentacion = 0
        self.variables = set()

    def compilar(self, arbol):
        self.codigo_elfico_mordor = []  # Reinicializar para cada compilación
        self.codigo_python = []  # Reinicializar para cada compilación
        if arbol:  # Verifica si el árbol no está vacío
            for nodo in arbol:
                self.generar_codigo(nodo)
        return "\n".join(self.codigo_elfico_mordor), "\n".join(self.codigo_python)

    def generar_codigo(self, nodo):
        if isinstance(nodo, tuple):
            if nodo[0] == 'asignacion':
                self.generar_asignacion(nodo)
            elif nodo[0] == 'imprimir':
                self.generar_imprimir(nodo)
            elif nodo[0] == 'si_sino':
                self.generar_si_sino(nodo)
            elif nodo[0] == 'mientras':
                self.generar_mientras(nodo)
            elif nodo[0] in ['+', '-', '*', '/', '<', '>']:
                return self.generar_operacion(nodo)
        elif isinstance(nodo, str):
            if nodo in self.variables:
                return nodo
            else:
                return repr(nodo)
        elif isinstance(nodo, int):
            return str(nodo)

    def generar_asignacion(self, nodo):
        _, variable, valor = nodo
        self.variables.add(variable)
        valor_codigo = self.generar_codigo(valor)
        self.codigo_elfico_mordor.append(f"{' ' * self.indentacion}nauth {variable} = {valor_codigo}")
        self.codigo_python.append(f"{' ' * self.indentacion}{variable} = {valor_codigo}")

    def generar_imprimir(self, nodo):
        _, valor = nodo
        valor_codigo = self.generar_codigo(valor)
        self.codigo_elfico_mordor.append(f"{' ' * self.indentacion}pedo({valor_codigo})")
        self.codigo_python.append(f"{' ' * self.indentacion}print({valor_codigo})")

    def generar_si_sino(self, nodo):
        _, condicion, bloque_si, bloque_sino = nodo
        condicion_codigo = self.generar_codigo(condicion)
        self.codigo_elfico_mordor.append(f"{' ' * self.indentacion}thand ({condicion_codigo}) {{")
        self.codigo_python.append(f"{' ' * self.indentacion}if {condicion_codigo}:")
        self.indentacion += 4
        for instruccion in bloque_si:
            self.generar_codigo(instruccion)
        self.indentacion -= 4
        self.codigo_elfico_mordor.append(f"{' ' * self.indentacion}}}")
        if bloque_sino:
            self.codigo_elfico_mordor.append(f"{' ' * self.indentacion}ú {{")
            self.codigo_python.append(f"{' ' * self.indentacion}else:")
            self.indentacion += 4
            for instruccion in bloque_sino:
                self.generar_codigo(instruccion)
            self.indentacion -= 4
            self.codigo_elfico_mordor.append(f"{' ' * self.indentacion}}}")

    def generar_mientras(self, nodo):
        _, condicion, bloque = nodo
        condicion_codigo = self.generar_codigo(condicion)
        self.codigo_elfico_mordor.append(f"{' ' * self.indentacion}am ({condicion_codigo}) {{")
        self.codigo_python.append(f"{' ' * self.indentacion}while {condicion_codigo}:")
        self.indentacion += 4
        for instruccion in bloque:
            self.generar_codigo(instruccion)
        self.indentacion -= 4
        self.codigo_elfico_mordor.append(f"{' ' * self.indentacion}}}")

    def generar_operacion(self, nodo):
        operador, izq, der = nodo
        izq_codigo = self.generar_codigo(izq)
        der_codigo = self.generar_codigo(der)
        return f"({izq_codigo} {operador} {der_codigo})"