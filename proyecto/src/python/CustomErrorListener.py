import os
from antlr4.error.ErrorListener import ErrorListener

# Ruta absoluta al archivo de errores para registrar tambien los errores sintacticos
ERRORS_PATH = os.path.join(os.path.dirname(__file__), "output", "errores.txt")


class CustomErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        mensaje = f"ERROR [Sintactico]: linea {line}, columna {column}: {msg}\n"
        print(mensaje)
        try:
            with open(ERRORS_PATH, "a", encoding="utf-8") as errores:
                errores.write(mensaje)
        except OSError:
            # Si no se puede escribir, al menos mostrar por consola
            pass
