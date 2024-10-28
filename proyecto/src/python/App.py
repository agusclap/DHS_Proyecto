import os
import sys
from antlr4 import *
from compiladoresLexer  import compiladoresLexer
from compiladoresParser import compiladoresParser
from Escucha import Escucha
from Walker import Walker

def main(argv):
    #print("Directorio actual de trabajo:", os.getcwd())
    #archivo = "input/entrada.txt"
    archivo = "input/matematica.txt"
    if not os.path.exists(archivo):
        print(f"Error: El archivo {archivo} no existe.")
        return
    if len(argv) > 1 :
        archivo = argv[1]
    input = FileStream(archivo)
    lexer = compiladoresLexer(input)
    stream = CommonTokenStream(lexer)
    parser = compiladoresParser(stream) #Analizador sintactico
    escucha = Escucha()
    parser.addParseListener(escucha)
    tree = parser.programa() #arranca con programa txt
    print(tree.toStringTree(recog=parser))
    #caminante = Walker()
    #caminante.visitPrograma(tree)

if __name__ == '__main__':
    main(sys.argv)
