import os
import copy
from antlr4 import ErrorNode, TerminalNode
from compiladoresListener import compiladoresListener
from compiladoresParser import compiladoresParser
from Estructuras.TablaSimbolos import TablaSimbolos
from Estructuras.Id import Funcion, Variable

# Ruta del archivo de errores
ERRORS_PATH = os.path.join(os.path.dirname(__file__), "output", "errores.txt")


class Escucha(compiladoresListener):
    """
    Listener semántico:
    - Manejo básico de tabla de símbolos por contexto.
    - Declaraciones con inicializador.
    - Advertencias de uso de variables no inicializadas.
    - Reporte de errores/warnings con número de línea.
    """

    def __init__(self):
        self.tablaSimbolos = TablaSimbolos()
        self.declaration_type = None
        self.listaParametros = []
        self.flagFuncion = False
        self.flagUsoFuncion = False
        self.listaVariables = []  # acumulador para RHS
        self.tieneErroresSemanticos = False
        self.tieneErroresSintacticos = False
        # reset archivo de errores
        open(ERRORS_PATH, "w", encoding="utf-8").close()

    # Utilidades ---------------------------------------------------------
    def _write_error(self, mensaje: str, linea: int | None = None):
        if "Error Semantico" in mensaje:
            self.tieneErroresSemanticos = True
        if "Error Sintactico" in mensaje or "ERROR [Sintactico]" in mensaje:
            self.tieneErroresSintacticos = True
        if linea is not None:
            mensaje = mensaje.rstrip("\n")
            mensaje = f"{mensaje} (linea {linea})"
        if not mensaje.endswith("\n"):
            mensaje += "\n"
        try:
            with open(ERRORS_PATH, "a", encoding="utf-8") as f:
                f.write(mensaje)
        except OSError:
            pass

    def _line(self, ctx):
        tok = getattr(ctx, "start", None)
        return tok.line if tok else None

    # Programa -----------------------------------------------------------
    def enterPrograma(self, ctx: compiladoresParser.ProgramaContext):
        print("Comienzo de la compilacion")

    def exitPrograma(self, ctx: compiladoresParser.ProgramaContext):
        print("Fin de la compilacion")
        # Marca main como accedido si existe
        main = self.tablaSimbolos.buscarID("main")
        if main is not None:
            main.setAccedido()
            self.tablaSimbolos.actualizarId(main)

        # Warnings del último contexto global
        last_context = self.tablaSimbolos.borrarContexto()
        for sim in last_context.getSimbolos().values():
            if isinstance(sim, Variable):
                if not sim.getAccedido():
                    print(f"WARNING [Semantico]: La variable {sim.getNombre()} no ha sido accedida.\n")
                    self._write_error(
                        f"WARNING [Semantico]: La variable {sim.getNombre()} no ha sido accedida.", sim.getLinea()
                    )
                elif not sim.getInicializado():
                    print(f"WARNING [Semantico]: La variable {sim.getNombre()} no ha sido inicializada.\n")
                    self._write_error(
                        f"WARNING [Semantico]: La variable {sim.getNombre()} no ha sido inicializada.", sim.getLinea()
                    )
            else:
                if not sim.getAccedido():
                    print(f"WARNING [Semantico]: La funcion {sim.getNombre()} no ha sido accedida.\n")
                    self._write_error(
                        f"WARNING [Semantico]: La funcion {sim.getNombre()} no ha sido accedida.", sim.getLinea()
                    )

    # Contextos ----------------------------------------------------------
    def enterBloque(self, ctx: compiladoresParser.BloqueContext):
        self.tablaSimbolos.agregarContexto()
        if self.flagFuncion:
            # agregar parámetros como variables inicializadas
            for param in self.listaParametros:
                v = Variable(param["nombre"], param["tipo"], inicializado=True, linea=param.get("linea"))
                self.tablaSimbolos.agregar(v)
            self.listaParametros = []
            self.flagFuncion = False

    def exitBloque(self, ctx: compiladoresParser.BloqueContext):
        contexto = self.tablaSimbolos.borrarContexto()
        for sim in contexto.getSimbolos().values():
            if isinstance(sim, Variable):
                if not sim.getInicializado():
                    print(f"WARNING [Semantico]: La variable {sim.getNombre()} no ha sido inicializada.\n")
                    self._write_error(
                        f"WARNING [Semantico]: La variable {sim.getNombre()} no ha sido inicializada.", sim.getLinea()
                    )
                elif not sim.getAccedido():
                    print(f"WARNING [Semantico]: La variable {sim.getNombre()} no ha sido accedida.\n")
                    self._write_error(
                        f"WARNING [Semantico]: La variable {sim.getNombre()} no ha sido accedida.", sim.getLinea()
                    )
            else:
                if not sim.getAccedido():
                    print(f"WARNING [Semantico]: La funcion {sim.getNombre()} no ha sido accedida.\n")
                    self._write_error(
                        f"WARNING [Semantico]: La funcion {sim.getNombre()} no ha sido accedida.", sim.getLinea()
                    )

    # Declaraciones ------------------------------------------------------
    def exitDeclaracion(self, ctx: compiladoresParser.DeclaracionContext):
        tipo = ctx.tdato().getText()
        nombre = ctx.ID().getText()
        linea = self._line(ctx)
        if self.tablaSimbolos.buscarLocalID(nombre) is not None:
            print(f"Error Semantico: Variable {nombre} ya declarada")
            self._write_error(f"Error Semantico: Variable {nombre} ya declarada", linea)
            return
        nueva = Variable(nombre, tipo, inicializado=False, linea=linea)
        # inicializador opcional en declaracionp
        declp = ctx.declaracionp()
        if declp is not None and declp.getChildCount() > 0:
            temp_tipo = self._line(declp)
            # marcamos como inicializada, el walker se encarga del código
            nueva.setInicializado()
        self.tablaSimbolos.agregar(nueva)

    def exitDeclaraciones(self, ctx: compiladoresParser.DeclaracionesContext):
        if ctx.getChildCount() == 0:
            return
        nombre = ctx.ID().getText()
        linea = self._line(ctx)
        if self.tablaSimbolos.buscarLocalID(nombre) is not None:
            print(f"Error Semantico: Variable {nombre} ya declarada")
            self._write_error(f"Error Semantico: Variable {nombre} ya declarada", linea)
        else:
            v = Variable(nombre, self.declaration_type, inicializado=False, linea=linea)
            declp2 = ctx.declaracionesp2()
            if declp2 is not None and declp2.getChildCount() > 0 and declp2.getChild(0).getText() == "=":
                v.setInicializado()
            self.tablaSimbolos.agregar(v)

    def exitDeclaracionesp(self, ctx: compiladoresParser.DeclaracionespContext):
        self.declaration_type = None

    # Asignaciones -------------------------------------------------------
    def enterAsignacion(self, ctx: compiladoresParser.AsignacionContext):
        self.listaVariables = []

    def exitAsignacion(self, ctx: compiladoresParser.AsignacionContext):
        nombre = ctx.ID().getText()
        linea = self._line(ctx)
        var = self.tablaSimbolos.buscarID(nombre)
        if var is None:
            print(f"Error Semantico: Variable {nombre} no esta declarada, no se puede asignar")
            self._write_error(f"Error Semantico: Variable {nombre} no esta declarada, no se puede asignar", linea)
            return
        var.setInicializado()
        self.tablaSimbolos.actualizarId(var)
        # chequeo simple de RHS para advertir no inicializadas
        for helper in self.listaVariables:
            ref = self.tablaSimbolos.buscarID(helper["nombre"])
            if ref and not ref.getInicializado():
                print(f"WARNING [Semantico]: La variable {ref.getNombre()} puede no haber sido inicializada.")
                self._write_error(
                    f"WARNING [Semantico]: La variable {ref.getNombre()} puede no haber sido inicializada.",
                    ref.getLinea() or linea,
                )
        self.listaVariables = []

    # Factores / usos de identificadores --------------------------------
    def exitFactor(self, ctx: compiladoresParser.FactorContext):
        # factor: NUMERO | ID | usofuncion | '(' exp ')'
        if ctx.NUMERO():
            return
        if ctx.ID():
            nombre = ctx.ID().getText()
            linea = self._line(ctx)
            var = self.tablaSimbolos.buscarID(nombre)
            if var is None:
                print(f"WARNING [Semantico]: La variable {nombre} no esta declarada.")
                self._write_error(f"WARNING [Semantico]: La variable {nombre} no esta declarada.", linea)
                return
            if not var.getInicializado():
                print(f"WARNING [Semantico]: La variable {nombre} puede no haber sido inicializada.")
                self._write_error(
                    f"WARNING [Semantico]: La variable {nombre} puede no haber sido inicializada.", linea
                )
            var.setAccedido()
            self.tablaSimbolos.actualizarId(var)
            self.listaVariables.append({"nombre": nombre, "tipo": var.getTipo()})
            return
        if ctx.usofuncion():
            return
        # paréntesis -> exp ya procesado

    # Parámetros ---------------------------------------------------------
    def exitParametro(self, ctx: compiladoresParser.ParametroContext):
        if ctx.getChildCount() == 0:
            return
        tipo = ctx.getChild(0).getText()
        nombre = ctx.getChild(1).getText()
        self.listaParametros.append({"nombre": nombre, "tipo": tipo, "linea": self._line(ctx)})

    def exitParametros(self, ctx: compiladoresParser.ParametrosContext):
        if ctx.getChildCount() == 0:
            return
        tipo = ctx.getChild(1).getText()
        nombre = ctx.getChild(2).getText()
        self.listaParametros.append({"nombre": nombre, "tipo": tipo, "linea": self._line(ctx)})

    # Funciones ----------------------------------------------------------
    def exitPrototipo(self, ctx: compiladoresParser.PrototipoContext):
        nombre = ctx.ID().getText()
        linea = self._line(ctx)
        if self.tablaSimbolos.buscarID(nombre):
            print(f"WARNING [Semantico]: Funcion {nombre} ya declarada")
            self._write_error(f"WARNING [Semantico]: Funcion {nombre} ya declarada", linea)
            return
        f = Funcion(nombre, ctx.tfuncion().getText(), copy.deepcopy(self.listaParametros), linea=linea)
        self.tablaSimbolos.agregar(f)
        self.listaParametros = []

    def enterFuncion(self, ctx: compiladoresParser.FuncionContext):
        self.flagFuncion = True

    def exitFuncion(self, ctx: compiladoresParser.FuncionContext):
        nombre = ctx.ID().getText()
        linea = self._line(ctx)
        f_decl = self.tablaSimbolos.buscarID(nombre)
        if f_decl is None:
            f_decl = Funcion(nombre, ctx.tfuncion().getText(), copy.deepcopy(self.listaParametros), linea=linea)
            f_decl.setInicializado()
            self.tablaSimbolos.agregar(f_decl)
        else:
            # actualización de prototipo
            f_decl.setInicializado()
            self.tablaSimbolos.actualizarId(f_decl)
        self.listaParametros = []

    # Uso de función -----------------------------------------------------
    def enterUsofuncion(self, ctx: compiladoresParser.UsofuncionContext):
        self.flagUsoFuncion = True

    def exitUsofuncion(self, ctx: compiladoresParser.UsofuncionContext):
        self.flagUsoFuncion = False
        nombre = ctx.ID().getText()
        linea = self._line(ctx)
        func = self.tablaSimbolos.buscarID(nombre)
        if func is None:
            print(f"WARNING [Semantico]: Funcion {nombre} no declarada")
            self._write_error(f"WARNING [Semantico]: Funcion {nombre} no declarada", linea)
            return
        func.setAccedido()
        self.tablaSimbolos.actualizarId(func)

    # Otros --------------------------------------------------------------
    def visitErrorNode(self, node: ErrorNode):
        linea = getattr(node.symbol, "line", None)
        self.tieneErroresSintacticos = True
        self._write_error(f"Error Sintactico: {node.getText()}", linea)

    def visitTerminal(self, node: TerminalNode):
        pass
