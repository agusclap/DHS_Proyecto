from antlr4.error.ErrorListener import ErrorListener

class CustomErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # Formatear el mensaje de advertencia
        warning_message = f"WARNING: Error de sintaxis en la línea {line}, columna {column}: {msg}\n"
        print(warning_message)
