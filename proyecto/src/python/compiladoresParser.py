# Generated from compiladores.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,36,328,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,1,0,1,0,1,0,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,
        1,4,1,4,1,4,3,4,101,8,4,1,5,1,5,1,5,1,5,1,5,1,5,3,5,109,8,5,1,6,
        1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,3,7,120,8,7,1,8,1,8,1,8,1,8,1,8,
        3,8,127,8,8,1,9,1,9,1,9,1,9,3,9,133,8,9,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,3,10,157,8,10,1,11,1,11,1,11,1,12,1,12,1,13,
        1,13,1,13,1,14,1,14,1,14,1,14,3,14,171,8,14,1,15,1,15,1,15,1,15,
        1,15,3,15,178,8,15,1,16,1,16,1,16,1,16,1,17,1,17,1,17,3,17,187,8,
        17,1,18,1,18,1,18,1,18,1,19,1,19,1,20,1,20,1,21,1,21,1,21,1,22,1,
        22,1,22,1,22,1,22,3,22,205,8,22,1,23,1,23,1,23,1,24,1,24,1,24,1,
        24,1,24,3,24,215,8,24,1,25,1,25,1,25,1,25,1,25,3,25,222,8,25,1,26,
        1,26,1,26,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,3,27,236,
        8,27,1,28,1,28,1,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,
        1,29,1,29,1,29,1,29,3,29,254,8,29,1,30,1,30,1,30,1,30,1,30,1,30,
        1,30,3,30,263,8,30,1,31,1,31,1,31,1,31,1,31,1,31,1,32,1,32,1,32,
        1,32,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,34,1,34,
        3,34,287,8,34,1,35,1,35,3,35,291,8,35,1,36,1,36,1,36,1,36,1,36,1,
        36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,3,36,310,
        8,36,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,
        1,37,1,37,3,37,326,8,37,1,37,0,0,38,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,
        66,68,70,72,74,0,3,3,0,23,24,26,26,33,33,2,0,23,24,26,26,2,0,14,
        14,16,20,328,0,76,1,0,0,0,2,79,1,0,0,0,4,86,1,0,0,0,6,88,1,0,0,0,
        8,100,1,0,0,0,10,108,1,0,0,0,12,110,1,0,0,0,14,119,1,0,0,0,16,126,
        1,0,0,0,18,132,1,0,0,0,20,156,1,0,0,0,22,158,1,0,0,0,24,161,1,0,
        0,0,26,163,1,0,0,0,28,170,1,0,0,0,30,177,1,0,0,0,32,179,1,0,0,0,
        34,186,1,0,0,0,36,188,1,0,0,0,38,192,1,0,0,0,40,194,1,0,0,0,42,196,
        1,0,0,0,44,204,1,0,0,0,46,206,1,0,0,0,48,214,1,0,0,0,50,221,1,0,
        0,0,52,223,1,0,0,0,54,235,1,0,0,0,56,237,1,0,0,0,58,253,1,0,0,0,
        60,262,1,0,0,0,62,264,1,0,0,0,64,270,1,0,0,0,66,274,1,0,0,0,68,286,
        1,0,0,0,70,290,1,0,0,0,72,309,1,0,0,0,74,325,1,0,0,0,76,77,3,18,
        9,0,77,78,5,0,0,1,78,1,1,0,0,0,79,80,3,4,2,0,80,81,5,34,0,0,81,82,
        5,1,0,0,82,83,3,8,4,0,83,84,5,2,0,0,84,85,5,5,0,0,85,3,1,0,0,0,86,
        87,7,0,0,0,87,5,1,0,0,0,88,89,3,4,2,0,89,90,5,34,0,0,90,91,5,1,0,
        0,91,92,3,8,4,0,92,93,5,2,0,0,93,94,3,64,32,0,94,7,1,0,0,0,95,96,
        3,24,12,0,96,97,5,34,0,0,97,98,3,10,5,0,98,101,1,0,0,0,99,101,1,
        0,0,0,100,95,1,0,0,0,100,99,1,0,0,0,101,9,1,0,0,0,102,103,5,21,0,
        0,103,104,3,24,12,0,104,105,5,34,0,0,105,106,3,10,5,0,106,109,1,
        0,0,0,107,109,1,0,0,0,108,102,1,0,0,0,108,107,1,0,0,0,109,11,1,0,
        0,0,110,111,5,34,0,0,111,112,5,1,0,0,112,113,3,14,7,0,113,114,5,
        2,0,0,114,13,1,0,0,0,115,116,3,38,19,0,116,117,3,16,8,0,117,120,
        1,0,0,0,118,120,1,0,0,0,119,115,1,0,0,0,119,118,1,0,0,0,120,15,1,
        0,0,0,121,122,5,21,0,0,122,123,3,38,19,0,123,124,3,16,8,0,124,127,
        1,0,0,0,125,127,1,0,0,0,126,121,1,0,0,0,126,125,1,0,0,0,127,17,1,
        0,0,0,128,129,3,20,10,0,129,130,3,18,9,0,130,133,1,0,0,0,131,133,
        1,0,0,0,132,128,1,0,0,0,132,131,1,0,0,0,133,19,1,0,0,0,134,135,3,
        26,13,0,135,136,5,5,0,0,136,157,1,0,0,0,137,157,3,62,31,0,138,157,
        3,66,33,0,139,157,3,74,37,0,140,157,3,64,32,0,141,142,3,36,18,0,
        142,143,5,5,0,0,143,157,1,0,0,0,144,145,3,12,6,0,145,146,5,5,0,0,
        146,157,1,0,0,0,147,148,3,22,11,0,148,149,5,5,0,0,149,157,1,0,0,
        0,150,151,3,38,19,0,151,152,5,5,0,0,152,157,1,0,0,0,153,157,5,5,
        0,0,154,157,3,6,3,0,155,157,3,2,1,0,156,134,1,0,0,0,156,137,1,0,
        0,0,156,138,1,0,0,0,156,139,1,0,0,0,156,140,1,0,0,0,156,141,1,0,
        0,0,156,144,1,0,0,0,156,147,1,0,0,0,156,150,1,0,0,0,156,153,1,0,
        0,0,156,154,1,0,0,0,156,155,1,0,0,0,157,21,1,0,0,0,158,159,5,32,
        0,0,159,160,3,38,19,0,160,23,1,0,0,0,161,162,7,1,0,0,162,25,1,0,
        0,0,163,164,3,32,16,0,164,165,3,28,14,0,165,27,1,0,0,0,166,167,5,
        21,0,0,167,168,5,34,0,0,168,171,3,30,15,0,169,171,1,0,0,0,170,166,
        1,0,0,0,170,169,1,0,0,0,171,29,1,0,0,0,172,173,5,15,0,0,173,174,
        3,38,19,0,174,175,3,28,14,0,175,178,1,0,0,0,176,178,3,28,14,0,177,
        172,1,0,0,0,177,176,1,0,0,0,178,31,1,0,0,0,179,180,3,24,12,0,180,
        181,5,34,0,0,181,182,3,34,17,0,182,33,1,0,0,0,183,184,5,15,0,0,184,
        187,3,38,19,0,185,187,1,0,0,0,186,183,1,0,0,0,186,185,1,0,0,0,187,
        35,1,0,0,0,188,189,5,34,0,0,189,190,5,15,0,0,190,191,3,38,19,0,191,
        37,1,0,0,0,192,193,3,42,21,0,193,39,1,0,0,0,194,195,7,2,0,0,195,
        41,1,0,0,0,196,197,3,46,23,0,197,198,3,44,22,0,198,43,1,0,0,0,199,
        200,5,12,0,0,200,201,3,46,23,0,201,202,3,44,22,0,202,205,1,0,0,0,
        203,205,1,0,0,0,204,199,1,0,0,0,204,203,1,0,0,0,205,45,1,0,0,0,206,
        207,3,50,25,0,207,208,3,48,24,0,208,47,1,0,0,0,209,210,5,11,0,0,
        210,211,3,50,25,0,211,212,3,48,24,0,212,215,1,0,0,0,213,215,1,0,
        0,0,214,209,1,0,0,0,214,213,1,0,0,0,215,49,1,0,0,0,216,217,3,52,
        26,0,217,218,3,40,20,0,218,219,3,52,26,0,219,222,1,0,0,0,220,222,
        3,52,26,0,221,216,1,0,0,0,221,220,1,0,0,0,222,51,1,0,0,0,223,224,
        3,56,28,0,224,225,3,54,27,0,225,53,1,0,0,0,226,227,5,6,0,0,227,228,
        3,56,28,0,228,229,3,54,27,0,229,236,1,0,0,0,230,231,5,7,0,0,231,
        232,3,56,28,0,232,233,3,54,27,0,233,236,1,0,0,0,234,236,1,0,0,0,
        235,226,1,0,0,0,235,230,1,0,0,0,235,234,1,0,0,0,236,55,1,0,0,0,237,
        238,3,60,30,0,238,239,3,58,29,0,239,57,1,0,0,0,240,241,5,8,0,0,241,
        242,3,60,30,0,242,243,3,58,29,0,243,254,1,0,0,0,244,245,5,9,0,0,
        245,246,3,60,30,0,246,247,3,58,29,0,247,254,1,0,0,0,248,249,5,10,
        0,0,249,250,3,60,30,0,250,251,3,58,29,0,251,254,1,0,0,0,252,254,
        1,0,0,0,253,240,1,0,0,0,253,244,1,0,0,0,253,248,1,0,0,0,253,252,
        1,0,0,0,254,59,1,0,0,0,255,263,5,22,0,0,256,263,5,34,0,0,257,263,
        3,12,6,0,258,259,5,1,0,0,259,260,3,52,26,0,260,261,5,2,0,0,261,263,
        1,0,0,0,262,255,1,0,0,0,262,256,1,0,0,0,262,257,1,0,0,0,262,258,
        1,0,0,0,263,61,1,0,0,0,264,265,5,28,0,0,265,266,5,1,0,0,266,267,
        3,38,19,0,267,268,5,2,0,0,268,269,3,20,10,0,269,63,1,0,0,0,270,271,
        5,3,0,0,271,272,3,18,9,0,272,273,5,4,0,0,273,65,1,0,0,0,274,275,
        5,29,0,0,275,276,5,1,0,0,276,277,3,68,34,0,277,278,5,5,0,0,278,279,
        3,70,35,0,279,280,5,5,0,0,280,281,3,72,36,0,281,282,5,2,0,0,282,
        283,3,20,10,0,283,67,1,0,0,0,284,287,3,36,18,0,285,287,1,0,0,0,286,
        284,1,0,0,0,286,285,1,0,0,0,287,69,1,0,0,0,288,291,3,38,19,0,289,
        291,1,0,0,0,290,288,1,0,0,0,290,289,1,0,0,0,291,71,1,0,0,0,292,310,
        3,38,19,0,293,294,5,34,0,0,294,295,5,6,0,0,295,310,5,6,0,0,296,297,
        5,6,0,0,297,298,5,6,0,0,298,310,5,34,0,0,299,300,5,34,0,0,300,301,
        5,7,0,0,301,310,5,7,0,0,302,303,5,7,0,0,303,304,5,7,0,0,304,310,
        5,34,0,0,305,306,5,34,0,0,306,307,5,15,0,0,307,310,3,38,19,0,308,
        310,1,0,0,0,309,292,1,0,0,0,309,293,1,0,0,0,309,296,1,0,0,0,309,
        299,1,0,0,0,309,302,1,0,0,0,309,305,1,0,0,0,309,308,1,0,0,0,310,
        73,1,0,0,0,311,312,5,30,0,0,312,313,5,1,0,0,313,314,3,38,19,0,314,
        315,5,2,0,0,315,316,3,20,10,0,316,326,1,0,0,0,317,318,5,30,0,0,318,
        319,5,1,0,0,319,320,3,38,19,0,320,321,5,2,0,0,321,322,3,20,10,0,
        322,323,5,31,0,0,323,324,3,20,10,0,324,326,1,0,0,0,325,311,1,0,0,
        0,325,317,1,0,0,0,326,75,1,0,0,0,19,100,108,119,126,132,156,170,
        177,186,204,214,221,235,253,262,286,290,309,325
    ]

class compiladoresParser ( Parser ):

    grammarFileName = "compiladores.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'{'", "'}'", "';'", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'&&'", "'||'", "'^'", 
                     "'!='", "'='", "'=='", "'>'", "'<'", "'<='", "'>='", 
                     "','", "<INVALID>", "'int'", "'double'", "'long'", 
                     "'char'", "'string'", "'while'", "'for'", "'if'", "'else'", 
                     "'return'", "'void'" ]

    symbolicNames = [ "<INVALID>", "PA", "PC", "LLA", "LLC", "PYC", "SUMA", 
                      "RESTA", "MULT", "DIV", "MOD", "AND", "OR", "ORX", 
                      "DIF", "ASIG", "IGUAL", "MAYOR", "MENOR", "MENORIG", 
                      "MAYORIG", "COMA", "NUMERO", "INT", "DOUBLE", "LONG", 
                      "CHAR", "STRING", "WHILE", "FOR", "IF", "ELSE", "RETURN", 
                      "VOID", "ID", "WS", "OTRO" ]

    RULE_programa = 0
    RULE_prototipo = 1
    RULE_tfuncion = 2
    RULE_funcion = 3
    RULE_parametro = 4
    RULE_parametros = 5
    RULE_usofuncion = 6
    RULE_argumentos = 7
    RULE_argumentosp = 8
    RULE_instrucciones = 9
    RULE_instruccion = 10
    RULE_return = 11
    RULE_tdato = 12
    RULE_declaracionesp = 13
    RULE_declaraciones = 14
    RULE_declaracionesp2 = 15
    RULE_declaracion = 16
    RULE_declaracionp = 17
    RULE_asignacion = 18
    RULE_opal = 19
    RULE_comparadores = 20
    RULE_lor = 21
    RULE_lorp = 22
    RULE_land = 23
    RULE_landp = 24
    RULE_comp = 25
    RULE_exp = 26
    RULE_e = 27
    RULE_term = 28
    RULE_t = 29
    RULE_factor = 30
    RULE_iwhile = 31
    RULE_bloque = 32
    RULE_ifor = 33
    RULE_init = 34
    RULE_cond = 35
    RULE_iter = 36
    RULE_iif = 37

    ruleNames =  [ "programa", "prototipo", "tfuncion", "funcion", "parametro", 
                   "parametros", "usofuncion", "argumentos", "argumentosp", 
                   "instrucciones", "instruccion", "return", "tdato", "declaracionesp", 
                   "declaraciones", "declaracionesp2", "declaracion", "declaracionp", 
                   "asignacion", "opal", "comparadores", "lor", "lorp", 
                   "land", "landp", "comp", "exp", "e", "term", "t", "factor", 
                   "iwhile", "bloque", "ifor", "init", "cond", "iter", "iif" ]

    EOF = Token.EOF
    PA=1
    PC=2
    LLA=3
    LLC=4
    PYC=5
    SUMA=6
    RESTA=7
    MULT=8
    DIV=9
    MOD=10
    AND=11
    OR=12
    ORX=13
    DIF=14
    ASIG=15
    IGUAL=16
    MAYOR=17
    MENOR=18
    MENORIG=19
    MAYORIG=20
    COMA=21
    NUMERO=22
    INT=23
    DOUBLE=24
    LONG=25
    CHAR=26
    STRING=27
    WHILE=28
    FOR=29
    IF=30
    ELSE=31
    RETURN=32
    VOID=33
    ID=34
    WS=35
    OTRO=36

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instrucciones(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionesContext,0)


        def EOF(self):
            return self.getToken(compiladoresParser.EOF, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = compiladoresParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.instrucciones()
            self.state = 77
            self.match(compiladoresParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrototipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tfuncion(self):
            return self.getTypedRuleContext(compiladoresParser.TfuncionContext,0)


        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def parametro(self):
            return self.getTypedRuleContext(compiladoresParser.ParametroContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def PYC(self):
            return self.getToken(compiladoresParser.PYC, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_prototipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrototipo" ):
                listener.enterPrototipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrototipo" ):
                listener.exitPrototipo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrototipo" ):
                return visitor.visitPrototipo(self)
            else:
                return visitor.visitChildren(self)




    def prototipo(self):

        localctx = compiladoresParser.PrototipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_prototipo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.tfuncion()
            self.state = 80
            self.match(compiladoresParser.ID)
            self.state = 81
            self.match(compiladoresParser.PA)
            self.state = 82
            self.parametro()
            self.state = 83
            self.match(compiladoresParser.PC)
            self.state = 84
            self.match(compiladoresParser.PYC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TfuncionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VOID(self):
            return self.getToken(compiladoresParser.VOID, 0)

        def INT(self):
            return self.getToken(compiladoresParser.INT, 0)

        def DOUBLE(self):
            return self.getToken(compiladoresParser.DOUBLE, 0)

        def CHAR(self):
            return self.getToken(compiladoresParser.CHAR, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_tfuncion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTfuncion" ):
                listener.enterTfuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTfuncion" ):
                listener.exitTfuncion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTfuncion" ):
                return visitor.visitTfuncion(self)
            else:
                return visitor.visitChildren(self)




    def tfuncion(self):

        localctx = compiladoresParser.TfuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_tfuncion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8682209280) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tfuncion(self):
            return self.getTypedRuleContext(compiladoresParser.TfuncionContext,0)


        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def parametro(self):
            return self.getTypedRuleContext(compiladoresParser.ParametroContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def bloque(self):
            return self.getTypedRuleContext(compiladoresParser.BloqueContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_funcion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncion" ):
                listener.enterFuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncion" ):
                listener.exitFuncion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncion" ):
                return visitor.visitFuncion(self)
            else:
                return visitor.visitChildren(self)




    def funcion(self):

        localctx = compiladoresParser.FuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_funcion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.tfuncion()
            self.state = 89
            self.match(compiladoresParser.ID)
            self.state = 90
            self.match(compiladoresParser.PA)
            self.state = 91
            self.parametro()
            self.state = 92
            self.match(compiladoresParser.PC)
            self.state = 93
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tdato(self):
            return self.getTypedRuleContext(compiladoresParser.TdatoContext,0)


        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def parametros(self):
            return self.getTypedRuleContext(compiladoresParser.ParametrosContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_parametro

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametro" ):
                listener.enterParametro(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametro" ):
                listener.exitParametro(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametro" ):
                return visitor.visitParametro(self)
            else:
                return visitor.visitChildren(self)




    def parametro(self):

        localctx = compiladoresParser.ParametroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_parametro)
        try:
            self.state = 100
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23, 24, 26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.tdato()
                self.state = 96
                self.match(compiladoresParser.ID)
                self.state = 97
                self.parametros()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametrosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(compiladoresParser.COMA, 0)

        def tdato(self):
            return self.getTypedRuleContext(compiladoresParser.TdatoContext,0)


        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def parametros(self):
            return self.getTypedRuleContext(compiladoresParser.ParametrosContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_parametros

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametros" ):
                listener.enterParametros(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametros" ):
                listener.exitParametros(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametros" ):
                return visitor.visitParametros(self)
            else:
                return visitor.visitChildren(self)




    def parametros(self):

        localctx = compiladoresParser.ParametrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_parametros)
        try:
            self.state = 108
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.match(compiladoresParser.COMA)
                self.state = 103
                self.tdato()
                self.state = 104
                self.match(compiladoresParser.ID)
                self.state = 105
                self.parametros()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UsofuncionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def argumentos(self):
            return self.getTypedRuleContext(compiladoresParser.ArgumentosContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_usofuncion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUsofuncion" ):
                listener.enterUsofuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUsofuncion" ):
                listener.exitUsofuncion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUsofuncion" ):
                return visitor.visitUsofuncion(self)
            else:
                return visitor.visitChildren(self)




    def usofuncion(self):

        localctx = compiladoresParser.UsofuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_usofuncion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(compiladoresParser.ID)
            self.state = 111
            self.match(compiladoresParser.PA)
            self.state = 112
            self.argumentos()
            self.state = 113
            self.match(compiladoresParser.PC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opal(self):
            return self.getTypedRuleContext(compiladoresParser.OpalContext,0)


        def argumentosp(self):
            return self.getTypedRuleContext(compiladoresParser.ArgumentospContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_argumentos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentos" ):
                listener.enterArgumentos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentos" ):
                listener.exitArgumentos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentos" ):
                return visitor.visitArgumentos(self)
            else:
                return visitor.visitChildren(self)




    def argumentos(self):

        localctx = compiladoresParser.ArgumentosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_argumentos)
        try:
            self.state = 119
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 22, 34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 115
                self.opal()
                self.state = 116
                self.argumentosp()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentospContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(compiladoresParser.COMA, 0)

        def opal(self):
            return self.getTypedRuleContext(compiladoresParser.OpalContext,0)


        def argumentosp(self):
            return self.getTypedRuleContext(compiladoresParser.ArgumentospContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_argumentosp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentosp" ):
                listener.enterArgumentosp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentosp" ):
                listener.exitArgumentosp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentosp" ):
                return visitor.visitArgumentosp(self)
            else:
                return visitor.visitChildren(self)




    def argumentosp(self):

        localctx = compiladoresParser.ArgumentospContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_argumentosp)
        try:
            self.state = 126
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 121
                self.match(compiladoresParser.COMA)
                self.state = 122
                self.opal()
                self.state = 123
                self.argumentosp()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruccion(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionContext,0)


        def instrucciones(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionesContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_instrucciones

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrucciones" ):
                listener.enterInstrucciones(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrucciones" ):
                listener.exitInstrucciones(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstrucciones" ):
                return visitor.visitInstrucciones(self)
            else:
                return visitor.visitChildren(self)




    def instrucciones(self):

        localctx = compiladoresParser.InstruccionesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_instrucciones)
        try:
            self.state = 132
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 3, 5, 22, 23, 24, 26, 28, 29, 30, 32, 33, 34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 128
                self.instruccion()
                self.state = 129
                self.instrucciones()
                pass
            elif token in [-1, 4]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracionesp(self):
            return self.getTypedRuleContext(compiladoresParser.DeclaracionespContext,0)


        def PYC(self):
            return self.getToken(compiladoresParser.PYC, 0)

        def iwhile(self):
            return self.getTypedRuleContext(compiladoresParser.IwhileContext,0)


        def ifor(self):
            return self.getTypedRuleContext(compiladoresParser.IforContext,0)


        def iif(self):
            return self.getTypedRuleContext(compiladoresParser.IifContext,0)


        def bloque(self):
            return self.getTypedRuleContext(compiladoresParser.BloqueContext,0)


        def asignacion(self):
            return self.getTypedRuleContext(compiladoresParser.AsignacionContext,0)


        def usofuncion(self):
            return self.getTypedRuleContext(compiladoresParser.UsofuncionContext,0)


        def return_(self):
            return self.getTypedRuleContext(compiladoresParser.ReturnContext,0)


        def opal(self):
            return self.getTypedRuleContext(compiladoresParser.OpalContext,0)


        def funcion(self):
            return self.getTypedRuleContext(compiladoresParser.FuncionContext,0)


        def prototipo(self):
            return self.getTypedRuleContext(compiladoresParser.PrototipoContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_instruccion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruccion" ):
                listener.enterInstruccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruccion" ):
                listener.exitInstruccion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccion" ):
                return visitor.visitInstruccion(self)
            else:
                return visitor.visitChildren(self)




    def instruccion(self):

        localctx = compiladoresParser.InstruccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_instruccion)
        try:
            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 134
                self.declaracionesp()
                self.state = 135
                self.match(compiladoresParser.PYC)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
                self.iwhile()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 138
                self.ifor()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 139
                self.iif()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 140
                self.bloque()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 141
                self.asignacion()
                self.state = 142
                self.match(compiladoresParser.PYC)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 144
                self.usofuncion()
                self.state = 145
                self.match(compiladoresParser.PYC)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 147
                self.return_()
                self.state = 148
                self.match(compiladoresParser.PYC)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 150
                self.opal()
                self.state = 151
                self.match(compiladoresParser.PYC)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 153
                self.match(compiladoresParser.PYC)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 154
                self.funcion()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 155
                self.prototipo()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(compiladoresParser.RETURN, 0)

        def opal(self):
            return self.getTypedRuleContext(compiladoresParser.OpalContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_return

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn" ):
                listener.enterReturn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn" ):
                listener.exitReturn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn" ):
                return visitor.visitReturn(self)
            else:
                return visitor.visitChildren(self)




    def return_(self):

        localctx = compiladoresParser.ReturnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_return)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(compiladoresParser.RETURN)
            self.state = 159
            self.opal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TdatoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(compiladoresParser.INT, 0)

        def DOUBLE(self):
            return self.getToken(compiladoresParser.DOUBLE, 0)

        def CHAR(self):
            return self.getToken(compiladoresParser.CHAR, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_tdato

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTdato" ):
                listener.enterTdato(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTdato" ):
                listener.exitTdato(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTdato" ):
                return visitor.visitTdato(self)
            else:
                return visitor.visitChildren(self)




    def tdato(self):

        localctx = compiladoresParser.TdatoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_tdato)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 92274688) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionespContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracion(self):
            return self.getTypedRuleContext(compiladoresParser.DeclaracionContext,0)


        def declaraciones(self):
            return self.getTypedRuleContext(compiladoresParser.DeclaracionesContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_declaracionesp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracionesp" ):
                listener.enterDeclaracionesp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracionesp" ):
                listener.exitDeclaracionesp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracionesp" ):
                return visitor.visitDeclaracionesp(self)
            else:
                return visitor.visitChildren(self)




    def declaracionesp(self):

        localctx = compiladoresParser.DeclaracionespContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_declaracionesp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.declaracion()
            self.state = 164
            self.declaraciones()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(compiladoresParser.COMA, 0)

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def declaracionesp2(self):
            return self.getTypedRuleContext(compiladoresParser.Declaracionesp2Context,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_declaraciones

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaraciones" ):
                listener.enterDeclaraciones(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaraciones" ):
                listener.exitDeclaraciones(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaraciones" ):
                return visitor.visitDeclaraciones(self)
            else:
                return visitor.visitChildren(self)




    def declaraciones(self):

        localctx = compiladoresParser.DeclaracionesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_declaraciones)
        try:
            self.state = 170
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.match(compiladoresParser.COMA)
                self.state = 167
                self.match(compiladoresParser.ID)
                self.state = 168
                self.declaracionesp2()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaracionesp2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASIG(self):
            return self.getToken(compiladoresParser.ASIG, 0)

        def opal(self):
            return self.getTypedRuleContext(compiladoresParser.OpalContext,0)


        def declaraciones(self):
            return self.getTypedRuleContext(compiladoresParser.DeclaracionesContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_declaracionesp2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracionesp2" ):
                listener.enterDeclaracionesp2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracionesp2" ):
                listener.exitDeclaracionesp2(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracionesp2" ):
                return visitor.visitDeclaracionesp2(self)
            else:
                return visitor.visitChildren(self)




    def declaracionesp2(self):

        localctx = compiladoresParser.Declaracionesp2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_declaracionesp2)
        try:
            self.state = 177
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 172
                self.match(compiladoresParser.ASIG)
                self.state = 173
                self.opal()
                self.state = 174
                self.declaraciones()
                pass
            elif token in [5, 21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 176
                self.declaraciones()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tdato(self):
            return self.getTypedRuleContext(compiladoresParser.TdatoContext,0)


        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def declaracionp(self):
            return self.getTypedRuleContext(compiladoresParser.DeclaracionpContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_declaracion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion" ):
                listener.enterDeclaracion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion" ):
                listener.exitDeclaracion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracion" ):
                return visitor.visitDeclaracion(self)
            else:
                return visitor.visitChildren(self)




    def declaracion(self):

        localctx = compiladoresParser.DeclaracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_declaracion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.tdato()
            self.state = 180
            self.match(compiladoresParser.ID)
            self.state = 181
            self.declaracionp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASIG(self):
            return self.getToken(compiladoresParser.ASIG, 0)

        def opal(self):
            return self.getTypedRuleContext(compiladoresParser.OpalContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_declaracionp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracionp" ):
                listener.enterDeclaracionp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracionp" ):
                listener.exitDeclaracionp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracionp" ):
                return visitor.visitDeclaracionp(self)
            else:
                return visitor.visitChildren(self)




    def declaracionp(self):

        localctx = compiladoresParser.DeclaracionpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_declaracionp)
        try:
            self.state = 186
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.match(compiladoresParser.ASIG)
                self.state = 184
                self.opal()
                pass
            elif token in [5, 21]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def ASIG(self):
            return self.getToken(compiladoresParser.ASIG, 0)

        def opal(self):
            return self.getTypedRuleContext(compiladoresParser.OpalContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)




    def asignacion(self):

        localctx = compiladoresParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.match(compiladoresParser.ID)
            self.state = 189
            self.match(compiladoresParser.ASIG)
            self.state = 190
            self.opal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lor(self):
            return self.getTypedRuleContext(compiladoresParser.LorContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_opal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpal" ):
                listener.enterOpal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpal" ):
                listener.exitOpal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpal" ):
                return visitor.visitOpal(self)
            else:
                return visitor.visitChildren(self)




    def opal(self):

        localctx = compiladoresParser.OpalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_opal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.lor()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparadoresContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAYOR(self):
            return self.getToken(compiladoresParser.MAYOR, 0)

        def MENOR(self):
            return self.getToken(compiladoresParser.MENOR, 0)

        def IGUAL(self):
            return self.getToken(compiladoresParser.IGUAL, 0)

        def MENORIG(self):
            return self.getToken(compiladoresParser.MENORIG, 0)

        def MAYORIG(self):
            return self.getToken(compiladoresParser.MAYORIG, 0)

        def DIF(self):
            return self.getToken(compiladoresParser.DIF, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_comparadores

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparadores" ):
                listener.enterComparadores(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparadores" ):
                listener.exitComparadores(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparadores" ):
                return visitor.visitComparadores(self)
            else:
                return visitor.visitChildren(self)




    def comparadores(self):

        localctx = compiladoresParser.ComparadoresContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_comparadores)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2048000) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def land(self):
            return self.getTypedRuleContext(compiladoresParser.LandContext,0)


        def lorp(self):
            return self.getTypedRuleContext(compiladoresParser.LorpContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_lor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLor" ):
                listener.enterLor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLor" ):
                listener.exitLor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLor" ):
                return visitor.visitLor(self)
            else:
                return visitor.visitChildren(self)




    def lor(self):

        localctx = compiladoresParser.LorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_lor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.land()
            self.state = 197
            self.lorp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LorpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OR(self):
            return self.getToken(compiladoresParser.OR, 0)

        def land(self):
            return self.getTypedRuleContext(compiladoresParser.LandContext,0)


        def lorp(self):
            return self.getTypedRuleContext(compiladoresParser.LorpContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_lorp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLorp" ):
                listener.enterLorp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLorp" ):
                listener.exitLorp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLorp" ):
                return visitor.visitLorp(self)
            else:
                return visitor.visitChildren(self)




    def lorp(self):

        localctx = compiladoresParser.LorpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_lorp)
        try:
            self.state = 204
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 199
                self.match(compiladoresParser.OR)
                self.state = 200
                self.land()
                self.state = 201
                self.lorp()
                pass
            elif token in [2, 5, 21]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comp(self):
            return self.getTypedRuleContext(compiladoresParser.CompContext,0)


        def landp(self):
            return self.getTypedRuleContext(compiladoresParser.LandpContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_land

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLand" ):
                listener.enterLand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLand" ):
                listener.exitLand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLand" ):
                return visitor.visitLand(self)
            else:
                return visitor.visitChildren(self)




    def land(self):

        localctx = compiladoresParser.LandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_land)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.comp()
            self.state = 207
            self.landp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LandpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(compiladoresParser.AND, 0)

        def comp(self):
            return self.getTypedRuleContext(compiladoresParser.CompContext,0)


        def landp(self):
            return self.getTypedRuleContext(compiladoresParser.LandpContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_landp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLandp" ):
                listener.enterLandp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLandp" ):
                listener.exitLandp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLandp" ):
                return visitor.visitLandp(self)
            else:
                return visitor.visitChildren(self)




    def landp(self):

        localctx = compiladoresParser.LandpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_landp)
        try:
            self.state = 214
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 209
                self.match(compiladoresParser.AND)
                self.state = 210
                self.comp()
                self.state = 211
                self.landp()
                pass
            elif token in [2, 5, 12, 21]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(compiladoresParser.ExpContext)
            else:
                return self.getTypedRuleContext(compiladoresParser.ExpContext,i)


        def comparadores(self):
            return self.getTypedRuleContext(compiladoresParser.ComparadoresContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_comp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComp" ):
                listener.enterComp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComp" ):
                listener.exitComp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComp" ):
                return visitor.visitComp(self)
            else:
                return visitor.visitChildren(self)




    def comp(self):

        localctx = compiladoresParser.CompContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_comp)
        try:
            self.state = 221
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 216
                self.exp()
                self.state = 217
                self.comparadores()
                self.state = 218
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
                self.exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(compiladoresParser.TermContext,0)


        def e(self):
            return self.getTypedRuleContext(compiladoresParser.EContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = compiladoresParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.term()
            self.state = 224
            self.e()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUMA(self):
            return self.getToken(compiladoresParser.SUMA, 0)

        def term(self):
            return self.getTypedRuleContext(compiladoresParser.TermContext,0)


        def e(self):
            return self.getTypedRuleContext(compiladoresParser.EContext,0)


        def RESTA(self):
            return self.getToken(compiladoresParser.RESTA, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_e

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterE" ):
                listener.enterE(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitE" ):
                listener.exitE(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitE" ):
                return visitor.visitE(self)
            else:
                return visitor.visitChildren(self)




    def e(self):

        localctx = compiladoresParser.EContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_e)
        try:
            self.state = 235
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                self.match(compiladoresParser.SUMA)
                self.state = 227
                self.term()
                self.state = 228
                self.e()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 230
                self.match(compiladoresParser.RESTA)
                self.state = 231
                self.term()
                self.state = 232
                self.e()
                pass
            elif token in [2, 5, 11, 12, 14, 16, 17, 18, 19, 20, 21]:
                self.enterOuterAlt(localctx, 3)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(compiladoresParser.FactorContext,0)


        def t(self):
            return self.getTypedRuleContext(compiladoresParser.TContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = compiladoresParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_term)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.factor()
            self.state = 238
            self.t()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MULT(self):
            return self.getToken(compiladoresParser.MULT, 0)

        def factor(self):
            return self.getTypedRuleContext(compiladoresParser.FactorContext,0)


        def t(self):
            return self.getTypedRuleContext(compiladoresParser.TContext,0)


        def DIV(self):
            return self.getToken(compiladoresParser.DIV, 0)

        def MOD(self):
            return self.getToken(compiladoresParser.MOD, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_t

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT" ):
                listener.enterT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT" ):
                listener.exitT(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT" ):
                return visitor.visitT(self)
            else:
                return visitor.visitChildren(self)




    def t(self):

        localctx = compiladoresParser.TContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_t)
        try:
            self.state = 253
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.match(compiladoresParser.MULT)
                self.state = 241
                self.factor()
                self.state = 242
                self.t()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 244
                self.match(compiladoresParser.DIV)
                self.state = 245
                self.factor()
                self.state = 246
                self.t()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 248
                self.match(compiladoresParser.MOD)
                self.state = 249
                self.factor()
                self.state = 250
                self.t()
                pass
            elif token in [2, 5, 6, 7, 11, 12, 14, 16, 17, 18, 19, 20, 21]:
                self.enterOuterAlt(localctx, 4)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMERO(self):
            return self.getToken(compiladoresParser.NUMERO, 0)

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def usofuncion(self):
            return self.getTypedRuleContext(compiladoresParser.UsofuncionContext,0)


        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def exp(self):
            return self.getTypedRuleContext(compiladoresParser.ExpContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = compiladoresParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_factor)
        try:
            self.state = 262
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 255
                self.match(compiladoresParser.NUMERO)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 256
                self.match(compiladoresParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 257
                self.usofuncion()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 258
                self.match(compiladoresParser.PA)
                self.state = 259
                self.exp()
                self.state = 260
                self.match(compiladoresParser.PC)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IwhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(compiladoresParser.WHILE, 0)

        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def opal(self):
            return self.getTypedRuleContext(compiladoresParser.OpalContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def instruccion(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_iwhile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIwhile" ):
                listener.enterIwhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIwhile" ):
                listener.exitIwhile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIwhile" ):
                return visitor.visitIwhile(self)
            else:
                return visitor.visitChildren(self)




    def iwhile(self):

        localctx = compiladoresParser.IwhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_iwhile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.match(compiladoresParser.WHILE)
            self.state = 265
            self.match(compiladoresParser.PA)
            self.state = 266
            self.opal()
            self.state = 267
            self.match(compiladoresParser.PC)
            self.state = 268
            self.instruccion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BloqueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LLA(self):
            return self.getToken(compiladoresParser.LLA, 0)

        def instrucciones(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionesContext,0)


        def LLC(self):
            return self.getToken(compiladoresParser.LLC, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_bloque

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloque" ):
                listener.enterBloque(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloque" ):
                listener.exitBloque(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloque" ):
                return visitor.visitBloque(self)
            else:
                return visitor.visitChildren(self)




    def bloque(self):

        localctx = compiladoresParser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_bloque)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.match(compiladoresParser.LLA)
            self.state = 271
            self.instrucciones()
            self.state = 272
            self.match(compiladoresParser.LLC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IforContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(compiladoresParser.FOR, 0)

        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def init(self):
            return self.getTypedRuleContext(compiladoresParser.InitContext,0)


        def PYC(self, i:int=None):
            if i is None:
                return self.getTokens(compiladoresParser.PYC)
            else:
                return self.getToken(compiladoresParser.PYC, i)

        def cond(self):
            return self.getTypedRuleContext(compiladoresParser.CondContext,0)


        def iter_(self):
            return self.getTypedRuleContext(compiladoresParser.IterContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def instruccion(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_ifor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfor" ):
                listener.enterIfor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfor" ):
                listener.exitIfor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfor" ):
                return visitor.visitIfor(self)
            else:
                return visitor.visitChildren(self)




    def ifor(self):

        localctx = compiladoresParser.IforContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_ifor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.match(compiladoresParser.FOR)
            self.state = 275
            self.match(compiladoresParser.PA)
            self.state = 276
            self.init()
            self.state = 277
            self.match(compiladoresParser.PYC)
            self.state = 278
            self.cond()
            self.state = 279
            self.match(compiladoresParser.PYC)
            self.state = 280
            self.iter_()
            self.state = 281
            self.match(compiladoresParser.PC)
            self.state = 282
            self.instruccion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asignacion(self):
            return self.getTypedRuleContext(compiladoresParser.AsignacionContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_init

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInit" ):
                listener.enterInit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInit" ):
                listener.exitInit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit" ):
                return visitor.visitInit(self)
            else:
                return visitor.visitChildren(self)




    def init(self):

        localctx = compiladoresParser.InitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_init)
        try:
            self.state = 286
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 284
                self.asignacion()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opal(self):
            return self.getTypedRuleContext(compiladoresParser.OpalContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_cond

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCond" ):
                listener.enterCond(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCond" ):
                listener.exitCond(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCond" ):
                return visitor.visitCond(self)
            else:
                return visitor.visitChildren(self)




    def cond(self):

        localctx = compiladoresParser.CondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_cond)
        try:
            self.state = 290
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 22, 34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 288
                self.opal()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opal(self):
            return self.getTypedRuleContext(compiladoresParser.OpalContext,0)


        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def SUMA(self, i:int=None):
            if i is None:
                return self.getTokens(compiladoresParser.SUMA)
            else:
                return self.getToken(compiladoresParser.SUMA, i)

        def RESTA(self, i:int=None):
            if i is None:
                return self.getTokens(compiladoresParser.RESTA)
            else:
                return self.getToken(compiladoresParser.RESTA, i)

        def ASIG(self):
            return self.getToken(compiladoresParser.ASIG, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_iter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIter" ):
                listener.enterIter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIter" ):
                listener.exitIter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIter" ):
                return visitor.visitIter(self)
            else:
                return visitor.visitChildren(self)




    def iter_(self):

        localctx = compiladoresParser.IterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_iter)
        try:
            self.state = 309
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                self.opal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 293
                self.match(compiladoresParser.ID)
                self.state = 294
                self.match(compiladoresParser.SUMA)
                self.state = 295
                self.match(compiladoresParser.SUMA)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 296
                self.match(compiladoresParser.SUMA)
                self.state = 297
                self.match(compiladoresParser.SUMA)
                self.state = 298
                self.match(compiladoresParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 299
                self.match(compiladoresParser.ID)
                self.state = 300
                self.match(compiladoresParser.RESTA)
                self.state = 301
                self.match(compiladoresParser.RESTA)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 302
                self.match(compiladoresParser.RESTA)
                self.state = 303
                self.match(compiladoresParser.RESTA)
                self.state = 304
                self.match(compiladoresParser.ID)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 305
                self.match(compiladoresParser.ID)
                self.state = 306
                self.match(compiladoresParser.ASIG)
                self.state = 307
                self.opal()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(compiladoresParser.IF, 0)

        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def opal(self):
            return self.getTypedRuleContext(compiladoresParser.OpalContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def instruccion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(compiladoresParser.InstruccionContext)
            else:
                return self.getTypedRuleContext(compiladoresParser.InstruccionContext,i)


        def ELSE(self):
            return self.getToken(compiladoresParser.ELSE, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_iif

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIif" ):
                listener.enterIif(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIif" ):
                listener.exitIif(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIif" ):
                return visitor.visitIif(self)
            else:
                return visitor.visitChildren(self)




    def iif(self):

        localctx = compiladoresParser.IifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_iif)
        try:
            self.state = 325
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 311
                self.match(compiladoresParser.IF)
                self.state = 312
                self.match(compiladoresParser.PA)
                self.state = 313
                self.opal()
                self.state = 314
                self.match(compiladoresParser.PC)
                self.state = 315
                self.instruccion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 317
                self.match(compiladoresParser.IF)
                self.state = 318
                self.match(compiladoresParser.PA)
                self.state = 319
                self.opal()
                self.state = 320
                self.match(compiladoresParser.PC)
                self.state = 321
                self.instruccion()
                self.state = 322
                self.match(compiladoresParser.ELSE)
                self.state = 323
                self.instruccion()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





