# Generated from /home/agustin/Desktop/DHS-Proyecto/proyecto/src/python/compiladores.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,20,114,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,
        5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,11,1,11,1,12,1,
        12,1,13,1,13,1,13,1,14,4,14,76,8,14,11,14,12,14,77,1,15,1,15,1,15,
        1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,18,1,18,
        1,18,1,19,1,19,3,19,99,8,19,1,19,1,19,1,19,5,19,104,8,19,10,19,12,
        19,107,9,19,1,20,1,20,1,20,1,20,1,21,1,21,0,0,22,1,0,3,0,5,1,7,2,
        9,3,11,4,13,5,15,6,17,7,19,8,21,9,23,10,25,11,27,12,29,13,31,14,
        33,15,35,16,37,17,39,18,41,19,43,20,1,0,3,2,0,65,90,97,122,1,0,48,
        57,3,0,9,10,13,13,32,32,116,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,
        0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,
        0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,
        0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,
        0,41,1,0,0,0,0,43,1,0,0,0,1,45,1,0,0,0,3,47,1,0,0,0,5,49,1,0,0,0,
        7,51,1,0,0,0,9,53,1,0,0,0,11,55,1,0,0,0,13,57,1,0,0,0,15,59,1,0,
        0,0,17,61,1,0,0,0,19,63,1,0,0,0,21,65,1,0,0,0,23,67,1,0,0,0,25,69,
        1,0,0,0,27,71,1,0,0,0,29,75,1,0,0,0,31,79,1,0,0,0,33,83,1,0,0,0,
        35,89,1,0,0,0,37,93,1,0,0,0,39,98,1,0,0,0,41,108,1,0,0,0,43,112,
        1,0,0,0,45,46,7,0,0,0,46,2,1,0,0,0,47,48,7,1,0,0,48,4,1,0,0,0,49,
        50,5,40,0,0,50,6,1,0,0,0,51,52,5,41,0,0,52,8,1,0,0,0,53,54,5,123,
        0,0,54,10,1,0,0,0,55,56,5,125,0,0,56,12,1,0,0,0,57,58,5,59,0,0,58,
        14,1,0,0,0,59,60,5,43,0,0,60,16,1,0,0,0,61,62,5,45,0,0,62,18,1,0,
        0,0,63,64,5,42,0,0,64,20,1,0,0,0,65,66,5,47,0,0,66,22,1,0,0,0,67,
        68,5,37,0,0,68,24,1,0,0,0,69,70,5,61,0,0,70,26,1,0,0,0,71,72,5,61,
        0,0,72,73,5,61,0,0,73,28,1,0,0,0,74,76,3,3,1,0,75,74,1,0,0,0,76,
        77,1,0,0,0,77,75,1,0,0,0,77,78,1,0,0,0,78,30,1,0,0,0,79,80,5,105,
        0,0,80,81,5,110,0,0,81,82,5,116,0,0,82,32,1,0,0,0,83,84,5,119,0,
        0,84,85,5,104,0,0,85,86,5,105,0,0,86,87,5,108,0,0,87,88,5,101,0,
        0,88,34,1,0,0,0,89,90,5,102,0,0,90,91,5,111,0,0,91,92,5,114,0,0,
        92,36,1,0,0,0,93,94,5,105,0,0,94,95,5,102,0,0,95,38,1,0,0,0,96,99,
        3,1,0,0,97,99,5,95,0,0,98,96,1,0,0,0,98,97,1,0,0,0,99,105,1,0,0,
        0,100,104,3,1,0,0,101,104,3,3,1,0,102,104,5,95,0,0,103,100,1,0,0,
        0,103,101,1,0,0,0,103,102,1,0,0,0,104,107,1,0,0,0,105,103,1,0,0,
        0,105,106,1,0,0,0,106,40,1,0,0,0,107,105,1,0,0,0,108,109,7,2,0,0,
        109,110,1,0,0,0,110,111,6,20,0,0,111,42,1,0,0,0,112,113,9,0,0,0,
        113,44,1,0,0,0,5,0,77,98,103,105,1,6,0,0
    ]

class compiladoresLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PA = 1
    PC = 2
    LLA = 3
    LLC = 4
    PYC = 5
    SUMA = 6
    RESTA = 7
    MULT = 8
    DIV = 9
    MOD = 10
    ASIG = 11
    IGUAL = 12
    NUMERO = 13
    INT = 14
    WHILE = 15
    FOR = 16
    IF = 17
    ID = 18
    WS = 19
    OTRO = 20

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'{'", "'}'", "';'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'='", "'=='", "'int'", "'while'", "'for'", "'if'" ]

    symbolicNames = [ "<INVALID>",
            "PA", "PC", "LLA", "LLC", "PYC", "SUMA", "RESTA", "MULT", "DIV", 
            "MOD", "ASIG", "IGUAL", "NUMERO", "INT", "WHILE", "FOR", "IF", 
            "ID", "WS", "OTRO" ]

    ruleNames = [ "LETRA", "DIGITO", "PA", "PC", "LLA", "LLC", "PYC", "SUMA", 
                  "RESTA", "MULT", "DIV", "MOD", "ASIG", "IGUAL", "NUMERO", 
                  "INT", "WHILE", "FOR", "IF", "ID", "WS", "OTRO" ]

    grammarFileName = "compiladores.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


