import os
import sys
from antlr4 import *
from compiladoresLexer  import compiladoresLexer
from compiladoresParser import compiladoresParser
from Escucha import Escucha
from Walker import Walker
from CustomErrorListener import CustomErrorListener

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
    parser.addParseListener(escucha)

    tree = parser.programa()
    #print(tree.toStringTree(recog=parser))

    
    caminante = Walker()
    caminante.visit(tree)   

if __name__ == '__main__':
    main(sys.argv)
