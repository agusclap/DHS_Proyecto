import os
from compiladoresVisitor import compiladoresVisitor
from compiladoresParser import compiladoresParser

INTERMEDIATE_PATH = os.path.join(os.path.dirname(__file__), "output", "CodigoIntermedio.txt")


class Walker(compiladoresVisitor):
    def __init__(self):
        # temporales y etiquetas
        self.tempCount = 0
        self.labelCount = 0
        os.makedirs(os.path.dirname(INTERMEDIATE_PATH), exist_ok=True)
        self.f = open(INTERMEDIATE_PATH, "w", encoding="utf-8")
        self.currentRetAddr = None
   
    # Helpers

    def visitChildren(self, node):
        """
        Los contextos generados por ANTLR no llaman a visit<Regla>,
        solo a visitChildren, así que despachamos manualmente al método específico.
        """
        method_name = "visit" + type(node).__name__.replace("Context", "")
        visitor = Walker.__dict__.get(method_name)
        if visitor:
            return visitor(self, node)
        return super().visitChildren(node)

    def ensure_temp(self, value: str):
        """
        Garantiza que la condición/salida esté en un temporal tN.
        Si ya es un temporal (t\d+), lo devuelve tal cual.
        Si es literal o identificador, genera tX = value y devuelve tX.
        """
        if isinstance(value, str) and value.startswith("t") and value[1:].isdigit():
            return value
        t = self.newTemp()
        self.emit(f"{t} = {value}")
        return t
    

    def newTemp(self):
        t = f"t{self.tempCount}"
        self.tempCount += 1
        return t
    
    def newLabel(self):
        l = f"l{self.labelCount}"
        self.labelCount += 1
        return l
    
    def emit(self, text):
        """Escribe una línea de código intermedio"""
        self.f.write(text + "\n")
        print(text)

    
    # Entrada principal
    

    def visitPrograma(self, ctx: compiladoresParser.ProgramaContext):
        print("******Generando codigo intermedio*******")
        if ctx.instrucciones():
            self.visit(ctx.instrucciones())
        print("*******Codigo intermedio generado*******")
        self.f.close()
        return None
    

    

    def visitInstrucciones(self, ctx: compiladoresParser.InstruccionesContext):
        # Caso base: rama vacía de la gramática
        instr = ctx.instruccion()
        if instr is not None:
            self.visit(instr)

        resto = ctx.instrucciones()
        if resto is not None:
            self.visit(resto)
        return None



    
    # Asignaciones
    

    def visitAsignacion(self, ctx: compiladoresParser.AsignacionContext):
        var = ctx.ID().getText()
        exprTemp = self.visit(ctx.opal())
        if exprTemp is None:
            return None
        exprTemp = self.ensure_temp(exprTemp)
        # Ejemplo que sale:  t0 = y * 2 ; z = t0
        self.emit(f"{var} = {exprTemp}")
        return None

    # Declaraciones con inicializador
    def visitDeclaracion(self, ctx: compiladoresParser.DeclaracionContext):
        # declaracion : tdato ID declaracionp
        declp = ctx.declaracionp()
        if declp and declp.getChildCount() > 0 and declp.getChild(0).getText() == "=":
            target = ctx.ID().getText()
            temp = self.ensure_temp(self.visit(declp.opal()))
            self.emit(f"{target} = {temp}")
        return None

    def visitDeclaraciones(self, ctx: compiladoresParser.DeclaracionesContext):
        # declaraciones : COMA ID declaracionesp2 | ;
        if ctx.getChildCount() == 0:
            return None
        target = ctx.ID().getText()
        declp2 = ctx.declaracionesp2()
        if declp2 and declp2.getChildCount() > 0 and declp2.getChild(0).getText() == "=":
            temp = self.ensure_temp(self.visit(declp2.opal()))
            self.emit(f"{target} = {temp}")
        # procesar posibles más ids en la cola
        if declp2 and declp2.declaraciones():
            self.visit(declp2.declaraciones())
        return None

    def visitDeclaracionesp(self, ctx: compiladoresParser.DeclaracionespContext):
        # declaracionesp : declaracion declaraciones
        self.visit(ctx.declaracion())
        if ctx.declaraciones():
            self.visit(ctx.declaraciones())
        return None

    def visitDeclaracionesp2(self, ctx: compiladoresParser.Declaracionesp2Context):
        # declaracionesp2 : ASIG opal declaraciones | declaraciones
        if ctx.getChildCount() == 0:
            return None
        if ctx.getChild(0).getText() == "=":
            # la asignación se maneja en visitDeclaraciones, aquí solo seguimos la cola
            if ctx.declaraciones():
                self.visit(ctx.declaraciones())
        else:
            self.visit(ctx.declaraciones())
        return None

    
    # IF / IF-ELSE
    

    def visitIif(self, ctx: compiladoresParser.IifContext):
        # iif: 'if' '(' opal ')' instruccion ('else' instruccion)?
        condTemp = self.ensure_temp(self.visit(ctx.opal()))
        thenInstr = ctx.instruccion(0)

        if len(ctx.instruccion()) == 2:
            # if (...) ... else ...
            elseInstr = ctx.instruccion(1)
            labelElse = self.newLabel()
            labelEnd  = self.newLabel()

            # si la condición NO es verdadera, salto al else
            self.emit(f"ifntjmp {condTemp} , {labelElse}")
            self.visit(thenInstr)
            self.emit(f"jump {labelEnd}")
            self.emit(f"label {labelElse}")
            self.visit(elseInstr)
            self.emit(f"label {labelEnd}")
        else:
            # if simple sin else
            labelEnd = self.newLabel()
            self.emit(f"ifntjmp {condTemp} , {labelEnd}")
            self.visit(thenInstr)
            self.emit(f"label {labelEnd}")
        return None

    
    # WHILE
   

    def visitIwhile(self, ctx: compiladoresParser.IwhileContext): # while
        # iwhile: 'while' '(' opal ')' instruccion
        labelStart = self.newLabel()
        labelEnd   = self.newLabel()

        self.emit(f"label {labelStart}")
        condTemp = self.ensure_temp(self.visit(ctx.opal()))
        self.emit(f"ifntjmp {condTemp} , {labelEnd}")
        self.visit(ctx.instruccion())
        self.emit(f"jump {labelStart}")
        self.emit(f"label {labelEnd}")
        return None # end
   
   
    # FOR
   

    def visitIfor(self, ctx: compiladoresParser.IforContext):
        # init: puede estar vacio o ser una asignacion
        if ctx.init() and ctx.init().getChildCount() > 0:
            # solo hay asignacion en la gramática
            self.visit(ctx.init().asignacion())

        start_label = self.newLabel()
        end_label = self.newLabel()

        self.emit(f"label {start_label}")

        # condicion opcional
        cond_ctx = ctx.cond()
        if cond_ctx is not None and cond_ctx.getChildCount() > 0:
            cond_temp = self.ensure_temp(self.visit(cond_ctx.opal()))
            self.emit(f"ifntjmp {cond_temp} , {end_label}")

        # cuerpo
        self.visit(ctx.instruccion())

        # iteracion
        iter_ctx = ctx.iter_()
        if iter_ctx is not None and iter_ctx.getChildCount() > 0:
            self.visitIter(iter_ctx)

        self.emit(f"jump {start_label}")
        self.emit(f"label {end_label}")
        return None

   
   
    # Llamada a función (usofuncion)
    

    
    def visitIter(self, ctx: compiladoresParser.IterContext):
        # iter : opal | ID ++ | ++ ID | ID -- | -- ID | ID = opal | ;
        if ctx.getChildCount() == 0:
            return None
        texto = ctx.getText()
        # Forma ID++ o ID--
        if texto.endswith('++') and ctx.ID():
            var = ctx.ID().getText()
            tmp = self.newTemp()
            self.emit(f"{tmp} = {var} + 1")
            self.emit(f"{var} = {tmp}")
            return None
        if texto.endswith('--') and ctx.ID():
            var = ctx.ID().getText()
            tmp = self.newTemp()
            self.emit(f"{tmp} = {var} - 1")
            self.emit(f"{var} = {tmp}")
            return None
        # Forma ++ID o --ID
        if texto.startswith('++') and ctx.ID():
            var = ctx.ID().getText()
            tmp = self.newTemp()
            self.emit(f"{tmp} = {var} + 1")
            self.emit(f"{var} = {tmp}")
            return None
        if texto.startswith('--') and ctx.ID():
            var = ctx.ID().getText()
            tmp = self.newTemp()
            self.emit(f"{tmp} = {var} - 1")
            self.emit(f"{var} = {tmp}")
            return None
        # Asignacion ID = opal
        if ctx.ASIG():
            var = ctx.ID().getText()
            val = self.visit(ctx.opal())
            if val is None:
                return None
            val = self.ensure_temp(val)
            self.emit(f"{var} = {val}")
            return None
        # caso general: una expresion opal
        if ctx.opal():
            self.visit(ctx.opal())
        return None

    def visitUsofuncion(self, ctx: compiladoresParser.UsofuncionContext):
        fname = ctx.ID().getText()

        # 1) Evaluar argumentos y pushearlos
        args_temps = []
        arg_ctx = ctx.argumentos()
        if arg_ctx is not None:
            # primer opal
            first_opal = arg_ctx.opal()
            if first_opal is not None:
                t = self.visit(first_opal)
                args_temps.append(t)

            # resto
            argsp = arg_ctx.argumentosp()
            while argsp is not None:
                opal_node = argsp.opal()
                if opal_node is not None:
                    t = self.visit(opal_node)
                    args_temps.append(t)
                argsp = argsp.argumentosp()

        # pushear argumentos en orden
        for a in args_temps:
            self.emit(f"push {a}")

        # 2) Crear etiqueta de retorno y pushearla
        ret_label = self.newLabel()
        self.emit(f"push {ret_label}")

        # 3) Saltar al inicio de la función
        self.emit(f"jump {fname}")

        # 4) Etiqueta de retorno
        self.emit(f"label {ret_label}")

        # 5) Pop del resultado de la función a un temporal
        ret_temp = self.newTemp()
        self.emit(f"pop {ret_temp}")

        return ret_temp


    def visitFuncion(self, ctx: compiladoresParser.FuncionContext):
        fname = ctx.ID().getText()

        if fname == "main":
            self.emit(f"label {fname}")
            # main no tiene dirección de retorno
            self.currentRetAddr = None
            self.visit(ctx.bloque())
            return None

        # --- Funciones normales ---
        self.emit(f"label {fname}")

        ret_temp = self.newTemp()
        self.emit(f"pop {ret_temp}")
        self.currentRetAddr = ret_temp

        # parámetros
        params = []
        pctx = ctx.parametro()
        if pctx is not None:
            id_tok = pctx.ID()
            if id_tok is not None:
                params.append(id_tok.getText())
            p2 = pctx.parametros()
            while p2 is not None:
                id2 = p2.ID()
                if id2 is not None:
                    params.append(id2.getText())
                p2 = p2.parametros()

        for p in reversed(params):
            self.emit(f"pop {p}")

        self.visit(ctx.bloque())
        return None



    

    def visitOpal(self, ctx: compiladoresParser.OpalContext):
        return self.visit(ctx.lor())
    
    def visitLor(self, ctx: compiladoresParser.LorContext):
        left = self.visit(ctx.land())
        lorp_ctx = ctx.lorp()
        while lorp_ctx is not None and lorp_ctx.getChildCount() > 0:
            right = self.visit(lorp_ctx.land())
            if right is None:
                return left
            t = self.newTemp()
            self.emit(f"{t} = {left} || {right}")
            left = t
            lorp_ctx = lorp_ctx.lorp()
        return left
        
    def visitLand(self, ctx: compiladoresParser.LandContext):
        left = self.visit(ctx.comp())
        landp_ctx = ctx.landp()
        while landp_ctx is not None and landp_ctx.getChildCount() > 0:
            right = self.visit(landp_ctx.comp())
            if right is None:
                return left
            t = self.newTemp()
            self.emit(f"{t} = {left} && {right}")
            left = t
            landp_ctx = landp_ctx.landp()
        return left

    def visitComp(self, ctx: compiladoresParser.CompContext):
        if ctx.getChildCount() == 1:
            exp0 = ctx.exp(0)
            if exp0 is None:
                return None
            return self.visit(exp0)
        left_node = ctx.exp(0)
        right_node = ctx.exp(1)
        if left_node is None or right_node is None:
            return None
        left = self.visit(left_node)
        right = self.visit(right_node)
        if left is None or right is None:
            return None
        op = ctx.comparadores().getText()
        t = self.newTemp()
        self.emit(f"{t} = {left} {op} {right}")
        return t

    def visitExp(self, ctx: compiladoresParser.ExpContext):
        # exp: term e ;
        term0 = ctx.term()
        if term0 is None:
            return None
        left = self.visit(term0)          #  sin índice
        if left is None:
            return None

        ectx = ctx.e()
        while ectx is not None and ectx.getChildCount() > 0:
            op = ectx.getChild(0).getText()
            right_node = ectx.term()
            if right_node is None:
                return left
            right = self.visit(right_node)   #  también sin índice
            if right is None:
                return left

            t = self.newTemp()
            self.emit(f"{t} = {left} {op} {right}")
            left = t
            ectx = ectx.e()

        return left


    
    def visitTerm(self, ctx: compiladoresParser.TermContext):
        # term: factor t ;
        factor0 = ctx.factor()
        if factor0 is None:
            return None
        left = self.visit(factor0)     
        if left is None:
            return None

        tctx = ctx.t()
        while tctx is not None and tctx.getChildCount() > 0:
            op = tctx.getChild(0).getText()
            right_node = tctx.factor()
            if right_node is None:
                return left
            right = self.visit(right_node)
            if right is None:
                return left

            tmp = self.newTemp()
            self.emit(f"{tmp} = {left} {op} {right}")
            left = tmp
            tctx = tctx.t()

        return left

    def visitFactor(self, ctx: compiladoresParser.FactorContext):
        if ctx.NUMERO():
            return ctx.NUMERO().getText()
        if ctx.ID():
            return ctx.ID().getText()
        if ctx.usofuncion():
            return self.visit(ctx.usofuncion())
        # caso de paréntesis: factor -> '(' exp ')'
        exp_node = ctx.exp()
        if exp_node is None:
            return None
        return self.visit(exp_node)

    
    # RETURN

    def visitReturn(self, ctx: compiladoresParser.ReturnContext):
        retTemp = self.visit(ctx.opal())
        if retTemp is None:
            return None

        if self.currentRetAddr is None:
            # caso main (o return fuera de función)
            self.emit(f"return {retTemp}")
        else:
            # funciones normales: protocolo con pila
            self.emit(f"push {retTemp}")
            self.emit(f"jump {self.currentRetAddr}")

        return retTemp

