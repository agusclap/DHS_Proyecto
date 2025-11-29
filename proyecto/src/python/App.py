import os
import sys
from antlr4 import *
from compiladoresLexer  import compiladoresLexer
from compiladoresParser import compiladoresParser
from Escucha import Escucha
from Walker import Walker
from CustomErrorListener import CustomErrorListener
from Optimizador import Optimizador
from antlr4 import ParseTreeWalker

def main(argv):
    archivo = "input/matematica.txt"
    if len(argv) > 1:
        archivo = argv[1]

    if not os.path.exists(archivo):
        print(f"Error: El archivo {archivo} no existe.")
        return

    input_stream = FileStream(archivo)

    lexer = compiladoresLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(CustomErrorListener())

    stream = CommonTokenStream(lexer)
    parser = compiladoresParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(CustomErrorListener())

    escucha = Escucha()
    tree = parser.programa()
    # Recorrido semantico primero
    listener_walker = ParseTreeWalker()
    listener_walker.walk(escucha, tree)

    if (
        escucha.tieneErroresSemanticos
        or escucha.tieneErroresSintacticos
        or parser.getNumberOfSyntaxErrors() > 0
    ):
        print("Se encontraron errores (sintacticos o semanticos). No se genera codigo intermedio.")
        return

    # Generacion de codigo intermedio
    caminante = Walker()
    caminante.visit(tree)

    optimizador = Optimizador()
    optimizador.optimizar()

if __name__ == '__main__':
    main(sys.argv)
