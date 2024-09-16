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
        4,0,10,62,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,1,1,
        1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,6,1,7,4,7,42,8,7,11,
        7,12,7,43,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,
        1,11,1,11,1,11,1,11,0,0,12,1,0,3,0,5,1,7,2,9,3,11,4,13,5,15,6,17,
        7,19,8,21,9,23,10,1,0,3,2,0,65,90,97,122,1,0,48,57,3,0,9,10,13,13,
        32,32,60,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,
        0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,
        0,0,0,1,25,1,0,0,0,3,27,1,0,0,0,5,29,1,0,0,0,7,31,1,0,0,0,9,33,1,
        0,0,0,11,35,1,0,0,0,13,37,1,0,0,0,15,41,1,0,0,0,17,45,1,0,0,0,19,
        51,1,0,0,0,21,55,1,0,0,0,23,58,1,0,0,0,25,26,7,0,0,0,26,2,1,0,0,
        0,27,28,7,1,0,0,28,4,1,0,0,0,29,30,5,40,0,0,30,6,1,0,0,0,31,32,5,
        41,0,0,32,8,1,0,0,0,33,34,5,59,0,0,34,10,1,0,0,0,35,36,5,61,0,0,
        36,12,1,0,0,0,37,38,5,61,0,0,38,39,5,61,0,0,39,14,1,0,0,0,40,42,
        3,3,1,0,41,40,1,0,0,0,42,43,1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,0,
        44,16,1,0,0,0,45,46,5,119,0,0,46,47,5,104,0,0,47,48,5,105,0,0,48,
        49,5,108,0,0,49,50,5,101,0,0,50,18,1,0,0,0,51,52,5,102,0,0,52,53,
        5,111,0,0,53,54,5,114,0,0,54,20,1,0,0,0,55,56,5,105,0,0,56,57,5,
        102,0,0,57,22,1,0,0,0,58,59,7,2,0,0,59,60,1,0,0,0,60,61,6,11,0,0,
        61,24,1,0,0,0,2,0,43,1,6,0,0
    ]

class compiladoresLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PA = 1
    PC = 2
    PYC = 3
    ASIG = 4
    IGUAL = 5
    NUMERO = 6
    WHILE = 7
    FOR = 8
    IF = 9
    WS = 10

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "';'", "'='", "'=='", "'while'", "'for'", "'if'" ]

    symbolicNames = [ "<INVALID>",
            "PA", "PC", "PYC", "ASIG", "IGUAL", "NUMERO", "WHILE", "FOR", 
            "IF", "WS" ]

    ruleNames = [ "LETRA", "DIGITO", "PA", "PC", "PYC", "ASIG", "IGUAL", 
                  "NUMERO", "WHILE", "FOR", "IF", "WS" ]

    grammarFileName = "compiladores.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


