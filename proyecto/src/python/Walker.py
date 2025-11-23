from compiladoresVisitor import compiladoresVisitor
from compiladoresParser import compiladoresParser


class Walker(compiladoresVisitor):
    def __init__(self):
        # temporales y etiquetas
        self.tempCount = 0
        self.labelCount = 0
        self.f = open("./output/CodigoIntermedio.txt", "w")
        self.currentRetAddr = None
   
    # Helpers
    

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
        # Ejemplo que sale:  t0 = y * 2 ; z = t0
        self.emit(f"{var} = {exprTemp}")
        return None

    
    # IF / IF-ELSE
    

    def visitIif(self, ctx: compiladoresParser.IifContext):
        # iif: 'if' '(' opal ')' instruccion ('else' instruccion)?
        condTemp = self.visit(ctx.opal())
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
   

    def visitIwhile(self, ctx: compiladoresParser.IwhileContext):
        # iwhile: 'while' '(' opal ')' instruccion
        labelStart = self.newLabel()
        labelEnd   = self.newLabel()

        self.emit(f"label {labelStart}")
        condTemp = self.visit(ctx.opal())
        self.emit(f"ifntjmp {condTemp} , {labelEnd}")
        self.visit(ctx.instruccion())
        self.emit(f"jump {labelStart}")
        self.emit(f"label {labelEnd}")
        return None
   
   
    # Llamada a función (usofuncion)
    

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
        # Si no hay OR, bajo a AND
        if ctx.lorp().getChildCount() == 0:
            return self.visit(ctx.land())
        else:
            left = self.visit(ctx.land())
            # suponemos un solo OR
            right = self.visit(ctx.lorp())
            t = self.newTemp()
            self.emit(f"{t} = {left} || {right}")
            return t
        
    def visitLand(self, ctx: compiladoresParser.LandContext):
        # Si no hay AND, bajo a comparación
        
        if ctx.landp().getChildCount() == 0:
            return self.visit(ctx.comp())
        else:
            left = self.visit(ctx.comp())
            right = self.visit(ctx.landp())
            t = self.newTemp()
            self.emit(f"{t} = {left} && {right}")
            return t
        
    def visitComp(self, ctx: compiladoresParser.CompContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp(0))
        else:
            left = self.visit(ctx.exp(0))
            op = ctx.comparadores().getText()
            right = self.visit(ctx.exp(1))
            t = self.newTemp()
            self.emit(f"{t} = {left} {op} {right}")
            return t
    
    def visitExp(self, ctx: compiladoresParser.ExpContext):
    # exp: term e ;
        left = self.visit(ctx.term())          #  sin índice

        ectx = ctx.e()
        if ectx is not None and ectx.getChildCount() > 0:
            # e: (SUMA | RESTA) term e | /* vacío */ ;
            op_token = ectx.SUMA() or ectx.RESTA()
            op = op_token.getText()
            right = self.visit(ectx.term())   #  también sin índice

            t = self.newTemp()
            self.emit(f"{t} = {left} {op} {right}")
            return t

        return left

    
    def visitTerm(self, ctx: compiladoresParser.TermContext):
    # term: factor t ;
        left = self.visit(ctx.factor())       # ✅ sin [0]

        tctx = ctx.t()
        if tctx is not None and tctx.getChildCount() > 0:
            # t: (('*' | '/' | '%') factor t) | /* vacío */ ;
            op = tctx.getChild(0).getText()
            right = self.visit(tctx.factor())

            tmp = self.newTemp()
            self.emit(f"{tmp} = {left} {op} {right}")
            return tmp

        return left

    
    def visitFactor(self, ctx: compiladoresParser.FactorContext):
        if ctx.NUMERO():
            return ctx.NUMERO().getText()
        if ctx.ID():
            return ctx.ID().getText()
        if ctx.usofuncion():
            return self.visit(ctx.usofuncion())
        # caso de paréntesis: factor -> '(' exp ')'
        return self.visit(ctx.exp())

    
    # RETURN

    def visitReturn(self, ctx: compiladoresParser.ReturnContext):
        retTemp = self.visit(ctx.opal())

        if self.currentRetAddr is None:
            # caso main (o return fuera de función)
            self.emit(f"return {retTemp}")
        else:
            # funciones normales: protocolo con pila
            self.emit(f"push {retTemp}")
            self.emit(f"jump {self.currentRetAddr}")

        return retTemp



