import re

class Optimizador:
    """
    Optimizador de código intermedio en 3 direcciones.

    Fases:
      1) Cargar y normalizar el archivo de código intermedio.
      2) Construir bloques básicos.
      3) Propagación de constantes dentro de cada bloque.
      4) Eliminación de expresiones comunes dentro de cada bloque.
      5) Eliminación de código muerto (temporales nunca usados).
      6) Guardar resultado en CodigoIntermedioOptimizado.txt
    """

    def __init__(self,
                 src_path: str = "./output/CodigoIntermedio.txt",
                 dst_path: str = "./output/CodigoIntermedioOptimizado.txt"):
        self.src_path = src_path
        self.dst_path = dst_path
        self.lines: list[str] = []      # líneas originales (normalizadas)
        self.blocks: list[tuple[int,int]] = []  # [(inicio, fin), ...] índices de líneas

   

    def optimizar(self):
        print("***** INICIANDO OPTIMIZACIÓN *****")

        self._cargar_y_normalizar()
        self._construir_bloques()
        self._propagacion_constantes()
        self._cse()
        self._eliminar_codigo_muerto()
        self._guardar()

        print("***** OPTIMIZACIÓN TERMINADA *****")

    
    # 1) Cargar y normalizar
    

    def _cargar_y_normalizar(self):
        """Carga CodigoIntermedio.txt en memoria y limpia espacios/lineas vacías."""
        with open(self.src_path, "r") as f:
            raw_lines = f.readlines()

        self.lines = []
        for line in raw_lines:
            line = line.strip()
            if not line:
                continue  # ignoro líneas vacías
            # Normalización simple (no toco demasiado):
            #   - colapso espacios múltiples
            #   - dejo comas tal cual porque las usás en ifntjmp t0 , l1
            parts = line.split()
            self.lines.append(" ".join(parts))

   
    # 2) Bloques básicos
    

    def _construir_bloques(self):
        """
        Construye bloques básicos usando un algoritmo clásico:
          - Es líder:
              * la primera instrucción
              * el destino de un salto (label)
              * la instrucción siguiente a un jump / ifntjmp
        """
        n = len(self.lines)
        if n == 0:
            self.blocks = []
            return

        leaders = set()
        leaders.add(0)  # primera línea

        # 1º pasada: detectar leaders
        for i, line in enumerate(self.lines):
            tokens = line.split()
            if not tokens:
                continue

            op = tokens[0]

            if op == "jump" or op == "ifntjmp":
                # la siguiente es líder (si existe)
                if i + 1 < n:
                    leaders.add(i + 1)
            if op == "label":
                # un label es posible destino de salto → líder
                leaders.add(i)

        # 2º: ordenar leaders y formar (inicio, fin) de cada bloque
        sorted_leaders = sorted(leaders)
        blocks = []
        for idx, start in enumerate(sorted_leaders):
            if idx == len(sorted_leaders) - 1:
                end = n - 1
            else:
                end = sorted_leaders[idx + 1] - 1
            blocks.append((start, end))

        self.blocks = blocks
        # print("Bloques básicos:", self.blocks)

    # ---------------------------------------------------------
    # 3) Propagación de constantes
    # ---------------------------------------------------------

    def _es_num(self, s: str) -> bool:
        """True si s representa un entero (positivo o negativo)."""
        return re.fullmatch(r'-?\d+', s) is not None

    def _propagacion_constantes(self):
        """
        Propaga constantes dentro de cada bloque:
          - t1 = 5
          - t2 = t1         → t2 = 5
          - t3 = t1 + 3     → t3 = 5 + 3  → t3 = 8
        """
        ops_arit = {"+", "-", "*", "/", "%"}
        ops_rel  = {">", "<", ">=", "<=", "==", "!="}
        ops_log  = {"&&", "||"}

        for (start, end) in self.blocks:
            env_const = {}   # var -> valor constante (int o bool)

            for i in range(start, end + 1):
                line = self.lines[i]
                tokens = line.split()
                if len(tokens) < 3 or tokens[1] != "=":
                    # no es asignación → no toco
                    continue

                lhs = tokens[0]
                rhs_tokens = tokens[2:]

                # Reemplazo variables conocidas por sus constantes
                for j, tok in enumerate(rhs_tokens):
                    if tok in env_const:
                        rhs_tokens[j] = str(env_const[tok])

                # Reconstruyo línea provisional con reemplazos
                tokens = [lhs, "="] + rhs_tokens
                # Caso 1: x = 5
                if len(rhs_tokens) == 1 and self._es_num(rhs_tokens[0]):
                    val = int(rhs_tokens[0])
                    env_const[lhs] = val
                    new_line = f"{lhs} = {val}"

                # Caso 2: x = y y y es constante
                elif len(rhs_tokens) == 1 and rhs_tokens[0] in env_const:
                    val = env_const[rhs_tokens[0]]
                    env_const[lhs] = val
                    new_line = f"{lhs} = {val}"

                # Caso 3: x = a op b (ambos numéricos)
                elif len(rhs_tokens) == 3 and \
                     self._es_num(rhs_tokens[0]) and \
                     self._es_num(rhs_tokens[2]) and \
                     rhs_tokens[1] in ops_arit.union(ops_rel).union(ops_log):

                    a = int(rhs_tokens[0])
                    b = int(rhs_tokens[2])
                    op = rhs_tokens[1]

                    expr = f"{a} {op} {b}"
                    # me apoyo en eval para simplificar
                    try:
                        val = eval(expr.replace("&&", " and ").replace("||", " or "))
                    except Exception:
                        # si algo falla, no la trato como constante
                        if lhs in env_const:
                            del env_const[lhs]
                        continue

                    env_const[lhs] = val
                    new_line = f"{lhs} = {int(val) if isinstance(val, bool) else val}"

                else:
                    # no puedo mantener lhs como constante
                    if lhs in env_const:
                        del env_const[lhs]
                    new_line = " ".join(tokens)

                # guardo la línea actualizada
                self.lines[i] = new_line

    
    # 4) Common Subexpression Elimination (CSE)
    

    def _vars_en_rhs(self, rhs_tokens: list[str]) -> set[str]:
        """Devuelve conjunto de 'variables' usadas en RHS (ignora números y operadores)."""
        ops = {"+", "-", "*", "/", "%", ">", "<", ">=", "<=", "==", "!=", "&&", "||"}
        vars_used = set()
        for tok in rhs_tokens:
            if tok in ops:
                continue
            if self._es_num(tok):
                continue
            # cualquier otro identificador lo considero variable (incluye t0, n, etc.)
            vars_used.add(tok)
        return vars_used

    def _cse(self):
        """
        Common Subexpression Elimination por bloque:
        Si en el mismo bloque tengo:
          t1 = a + b
          ...
          t2 = a + b   (sin que a ni b cambien)
        -> se reemplaza la segunda por:
          t2 = t1
        """
        ops_binarios = {"+", "-", "*", "/", "%", ">", "<", ">=", "<=", "==", "!=", "&&", "||"}

        for (start, end) in self.blocks:
            expr_table = {}   # exprKey -> (var, index)
            last_assign = {}  # var -> último índice donde se asignó

            i = start
            while i <= end:
                line = self.lines[i]
                tokens = line.split()
                if len(tokens) < 3 or tokens[1] != "=":
                    # no es asignación
                    # igual, si es algo tipo "return r" actualizo uso, pero no afecto CSE
                    i += 1
                    continue

                lhs = tokens[0]
                rhs = tokens[2:]

                # Si es una expresión binaria de tres tokens: a op b
                if len(rhs) == 3 and rhs[1] in ops_binarios:
                    a, op, b = rhs

                    # key canónica (para +,* &&,||,==,!= las considero conmutativas)
                    commutativas = {"+", "*", "&&", "||", "==", "!="}
                    if op in commutativas:
                        key_operandos = tuple(sorted([a, b]))
                    else:
                        key_operandos = (a, b)

                    exprKey = (op, key_operandos)

                    # Antes de usar exprKey, veo vars usadas y sus last_assign
                    vars_rhs = self._vars_en_rhs(rhs)

                    if exprKey in expr_table:
                        prev_var, prev_idx = expr_table[exprKey]
                        # Verifico que ninguna var usada se haya reasignado
                        valido = True
                        for v in vars_rhs:
                            if v in last_assign and last_assign[v] > prev_idx:
                                valido = False
                                break

                        if valido:
                            # Podemos reutilizar el resultado de prev_var
                            self.lines[i] = f"{lhs} = {prev_var}"
                            # registro que lhs ahora tiene el mismo valor
                            last_assign[lhs] = i
                            i += 1
                            continue

                    # Si no se pudo reutilizar, registro la nueva expresión
                    expr_table[exprKey] = (lhs, i)

                # actualizar last_assign del lhs
                last_assign[lhs] = i
                i += 1

    
    # 5) Eliminación de código muerto (Dead Code Elimination)
    

    def _eliminar_codigo_muerto(self):
        """
        Elimina asignaciones a temporales tN que nunca se usan.
        No toca labels, jumps, pushes, pops, returns, ni asignaciones a variables
        de usuario (n, r, b, etc.), solo a t0, t1, ... que estén realmente muertos.
        """
        used = set()               # variables usadas en cualquier lado
        defs_indices = {}          # index -> lhs  (solo temporales tN)

        # 1º pasada: recolecto usos
        for i, line in enumerate(self.lines):
            tokens = line.split()
            if not tokens:
                continue

            op = tokens[0]

            # Asignaciones: lhs = ...
            if len(tokens) >= 3 and tokens[1] == "=":
                lhs = tokens[0]
                rhs = tokens[2:]

                # Registro definición si es temporal
                if re.fullmatch(r"t\d+", lhs):
                    defs_indices[i] = lhs

                # Variables usadas en RHS
                rhs_vars = self._vars_en_rhs(rhs)
                used.update(rhs_vars)

            elif op in {"ifntjmp"}:
                # ifntjmp t0 , l1
                if len(tokens) >= 2:
                    used.add(tokens[1])

            elif op in {"push", "pop", "return"}:
                # push r / pop t0 / return x
                # podría haber más de un token, pero el principal es el 1
                if len(tokens) >= 2:
                    used.add(tokens[1])

            # jumps y labels no definen ni usan temporales relevantes en RHS

        # 2º pasada: elimino definiciones de temporales nunca usados
        nuevas_lineas = []
        for i, line in enumerate(self.lines):
            if i in defs_indices:
                lhs = defs_indices[i]
                if lhs not in used:
                    # definición de temporal muerto -> elimino línea
                    continue
            nuevas_lineas.append(line)

        self.lines = nuevas_lineas

    
    # 6) Guardar resultado
    

    def _guardar(self):
        with open(self.dst_path, "w") as f:
            for line in self.lines:
                f.write(line + "\n")
