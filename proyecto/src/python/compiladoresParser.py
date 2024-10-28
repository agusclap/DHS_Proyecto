# Generated from /home/agustin/Desktop/DHS-Proyecto/proyecto/src/python/compiladores.g4 by ANTLR 4.13.1
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
        4,1,37,329,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,1,0,5,0,70,8,0,10,0,12,0,73,9,0,1,0,5,0,76,8,0,10,0,12,0,79,
        9,0,1,0,1,0,1,1,1,1,3,1,85,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,94,
        8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,109,
        8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,118,8,4,1,5,1,5,1,5,1,5,1,5,
        3,5,125,8,5,1,6,1,6,1,6,1,6,1,6,3,6,132,8,6,1,7,1,7,1,7,1,7,1,7,
        1,8,1,8,1,8,1,8,3,8,143,8,8,1,9,1,9,1,9,1,9,1,9,3,9,150,8,9,1,10,
        1,10,1,10,1,10,3,10,156,8,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,3,11,166,8,11,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,3,13,180,8,13,1,14,1,14,1,14,1,14,1,14,1,15,1,15,
        1,16,1,16,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,3,18,199,8,18,
        1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,3,20,209,8,20,1,21,1,21,
        1,21,1,21,1,21,3,21,216,8,21,1,22,1,22,1,22,1,23,1,23,1,23,1,23,
        1,23,1,23,1,23,1,23,1,23,3,23,230,8,23,1,24,1,24,1,24,1,25,1,25,
        1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,3,25,248,
        8,25,1,26,1,26,1,26,1,26,1,26,1,26,1,26,3,26,257,8,26,1,27,1,27,
        1,27,1,27,1,27,1,27,3,27,265,8,27,1,28,1,28,1,28,1,28,1,29,1,29,
        1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,30,1,30,1,30,1,30,3,30,
        285,8,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,3,30,296,8,
        30,3,30,298,8,30,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,
        31,3,31,310,8,31,1,32,1,32,1,32,1,32,3,32,316,8,32,1,33,1,33,1,33,
        3,33,321,8,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,0,0,34,0,2,4,6,
        8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,
        52,54,56,58,60,62,64,66,0,2,1,0,23,24,2,0,14,14,16,20,333,0,71,1,
        0,0,0,2,84,1,0,0,0,4,86,1,0,0,0,6,108,1,0,0,0,8,110,1,0,0,0,10,124,
        1,0,0,0,12,131,1,0,0,0,14,133,1,0,0,0,16,142,1,0,0,0,18,149,1,0,
        0,0,20,155,1,0,0,0,22,165,1,0,0,0,24,167,1,0,0,0,26,179,1,0,0,0,
        28,181,1,0,0,0,30,186,1,0,0,0,32,188,1,0,0,0,34,190,1,0,0,0,36,198,
        1,0,0,0,38,200,1,0,0,0,40,208,1,0,0,0,42,215,1,0,0,0,44,217,1,0,
        0,0,46,229,1,0,0,0,48,231,1,0,0,0,50,247,1,0,0,0,52,256,1,0,0,0,
        54,258,1,0,0,0,56,266,1,0,0,0,58,270,1,0,0,0,60,297,1,0,0,0,62,299,
        1,0,0,0,64,315,1,0,0,0,66,317,1,0,0,0,68,70,3,26,13,0,69,68,1,0,
        0,0,70,73,1,0,0,0,71,69,1,0,0,0,71,72,1,0,0,0,72,77,1,0,0,0,73,71,
        1,0,0,0,74,76,3,2,1,0,75,74,1,0,0,0,76,79,1,0,0,0,77,75,1,0,0,0,
        77,78,1,0,0,0,78,80,1,0,0,0,79,77,1,0,0,0,80,81,5,0,0,1,81,1,1,0,
        0,0,82,85,3,4,2,0,83,85,3,8,4,0,84,82,1,0,0,0,84,83,1,0,0,0,85,3,
        1,0,0,0,86,87,3,24,12,0,87,88,5,35,0,0,88,89,5,1,0,0,89,90,3,10,
        5,0,90,93,5,2,0,0,91,94,3,6,3,0,92,94,5,5,0,0,93,91,1,0,0,0,93,92,
        1,0,0,0,94,5,1,0,0,0,95,96,5,3,0,0,96,97,3,20,10,0,97,98,5,32,0,
        0,98,99,3,30,15,0,99,100,5,5,0,0,100,101,5,4,0,0,101,109,1,0,0,0,
        102,103,5,3,0,0,103,104,5,32,0,0,104,105,3,30,15,0,105,106,5,5,0,
        0,106,107,5,4,0,0,107,109,1,0,0,0,108,95,1,0,0,0,108,102,1,0,0,0,
        109,7,1,0,0,0,110,111,5,34,0,0,111,112,5,35,0,0,112,113,5,1,0,0,
        113,114,3,10,5,0,114,117,5,2,0,0,115,118,3,56,28,0,116,118,5,5,0,
        0,117,115,1,0,0,0,117,116,1,0,0,0,118,9,1,0,0,0,119,120,3,24,12,
        0,120,121,5,35,0,0,121,122,3,12,6,0,122,125,1,0,0,0,123,125,1,0,
        0,0,124,119,1,0,0,0,124,123,1,0,0,0,125,11,1,0,0,0,126,127,5,21,
        0,0,127,128,3,10,5,0,128,129,3,12,6,0,129,132,1,0,0,0,130,132,1,
        0,0,0,131,126,1,0,0,0,131,130,1,0,0,0,132,13,1,0,0,0,133,134,5,35,
        0,0,134,135,5,1,0,0,135,136,3,16,8,0,136,137,5,2,0,0,137,15,1,0,
        0,0,138,139,3,30,15,0,139,140,3,18,9,0,140,143,1,0,0,0,141,143,1,
        0,0,0,142,138,1,0,0,0,142,141,1,0,0,0,143,17,1,0,0,0,144,145,5,21,
        0,0,145,146,3,16,8,0,146,147,3,18,9,0,147,150,1,0,0,0,148,150,1,
        0,0,0,149,144,1,0,0,0,149,148,1,0,0,0,150,19,1,0,0,0,151,152,3,22,
        11,0,152,153,3,20,10,0,153,156,1,0,0,0,154,156,1,0,0,0,155,151,1,
        0,0,0,155,154,1,0,0,0,156,21,1,0,0,0,157,166,3,26,13,0,158,166,3,
        54,27,0,159,166,3,58,29,0,160,166,3,62,31,0,161,166,3,56,28,0,162,
        166,3,28,14,0,163,166,3,14,7,0,164,166,5,5,0,0,165,157,1,0,0,0,165,
        158,1,0,0,0,165,159,1,0,0,0,165,160,1,0,0,0,165,161,1,0,0,0,165,
        162,1,0,0,0,165,163,1,0,0,0,165,164,1,0,0,0,166,23,1,0,0,0,167,168,
        7,0,0,0,168,25,1,0,0,0,169,170,3,24,12,0,170,171,5,35,0,0,171,172,
        5,5,0,0,172,180,1,0,0,0,173,174,3,24,12,0,174,175,5,35,0,0,175,176,
        5,15,0,0,176,177,3,30,15,0,177,178,5,5,0,0,178,180,1,0,0,0,179,169,
        1,0,0,0,179,173,1,0,0,0,180,27,1,0,0,0,181,182,5,35,0,0,182,183,
        5,15,0,0,183,184,3,30,15,0,184,185,5,5,0,0,185,29,1,0,0,0,186,187,
        3,34,17,0,187,31,1,0,0,0,188,189,7,1,0,0,189,33,1,0,0,0,190,191,
        3,38,19,0,191,192,3,36,18,0,192,35,1,0,0,0,193,194,5,12,0,0,194,
        195,3,38,19,0,195,196,3,36,18,0,196,199,1,0,0,0,197,199,1,0,0,0,
        198,193,1,0,0,0,198,197,1,0,0,0,199,37,1,0,0,0,200,201,3,42,21,0,
        201,202,3,40,20,0,202,39,1,0,0,0,203,204,5,11,0,0,204,205,3,42,21,
        0,205,206,3,40,20,0,206,209,1,0,0,0,207,209,1,0,0,0,208,203,1,0,
        0,0,208,207,1,0,0,0,209,41,1,0,0,0,210,211,3,44,22,0,211,212,3,32,
        16,0,212,213,3,44,22,0,213,216,1,0,0,0,214,216,3,44,22,0,215,210,
        1,0,0,0,215,214,1,0,0,0,216,43,1,0,0,0,217,218,3,48,24,0,218,219,
        3,46,23,0,219,45,1,0,0,0,220,221,5,6,0,0,221,222,3,48,24,0,222,223,
        3,46,23,0,223,230,1,0,0,0,224,225,5,7,0,0,225,226,3,48,24,0,226,
        227,3,46,23,0,227,230,1,0,0,0,228,230,1,0,0,0,229,220,1,0,0,0,229,
        224,1,0,0,0,229,228,1,0,0,0,230,47,1,0,0,0,231,232,3,52,26,0,232,
        233,3,50,25,0,233,49,1,0,0,0,234,235,5,8,0,0,235,236,3,52,26,0,236,
        237,3,50,25,0,237,248,1,0,0,0,238,239,5,9,0,0,239,240,3,52,26,0,
        240,241,3,50,25,0,241,248,1,0,0,0,242,243,5,10,0,0,243,244,3,52,
        26,0,244,245,3,50,25,0,245,248,1,0,0,0,246,248,1,0,0,0,247,234,1,
        0,0,0,247,238,1,0,0,0,247,242,1,0,0,0,247,246,1,0,0,0,248,51,1,0,
        0,0,249,257,5,22,0,0,250,257,5,35,0,0,251,257,3,14,7,0,252,253,5,
        1,0,0,253,254,3,44,22,0,254,255,5,2,0,0,255,257,1,0,0,0,256,249,
        1,0,0,0,256,250,1,0,0,0,256,251,1,0,0,0,256,252,1,0,0,0,257,53,1,
        0,0,0,258,259,5,28,0,0,259,260,5,1,0,0,260,261,3,30,15,0,261,264,
        5,2,0,0,262,265,3,56,28,0,263,265,3,22,11,0,264,262,1,0,0,0,264,
        263,1,0,0,0,265,55,1,0,0,0,266,267,5,3,0,0,267,268,3,20,10,0,268,
        269,5,4,0,0,269,57,1,0,0,0,270,271,5,29,0,0,271,272,5,1,0,0,272,
        273,3,60,30,0,273,274,5,5,0,0,274,275,3,30,15,0,275,276,5,5,0,0,
        276,277,3,30,15,0,277,278,5,2,0,0,278,279,3,22,11,0,279,59,1,0,0,
        0,280,281,5,35,0,0,281,284,5,15,0,0,282,285,3,14,7,0,283,285,3,30,
        15,0,284,282,1,0,0,0,284,283,1,0,0,0,285,298,1,0,0,0,286,298,5,35,
        0,0,287,288,3,24,12,0,288,289,5,35,0,0,289,298,1,0,0,0,290,291,3,
        24,12,0,291,292,5,35,0,0,292,295,5,15,0,0,293,296,3,14,7,0,294,296,
        3,30,15,0,295,293,1,0,0,0,295,294,1,0,0,0,296,298,1,0,0,0,297,280,
        1,0,0,0,297,286,1,0,0,0,297,287,1,0,0,0,297,290,1,0,0,0,298,61,1,
        0,0,0,299,300,5,30,0,0,300,301,5,1,0,0,301,302,3,30,15,0,302,303,
        5,2,0,0,303,304,5,3,0,0,304,305,3,22,11,0,305,306,5,5,0,0,306,309,
        5,4,0,0,307,310,1,0,0,0,308,310,3,64,32,0,309,307,1,0,0,0,309,308,
        1,0,0,0,310,63,1,0,0,0,311,312,5,31,0,0,312,316,3,56,28,0,313,314,
        5,31,0,0,314,316,3,22,11,0,315,311,1,0,0,0,315,313,1,0,0,0,316,65,
        1,0,0,0,317,320,5,33,0,0,318,321,3,56,28,0,319,321,3,22,11,0,320,
        318,1,0,0,0,320,319,1,0,0,0,321,322,1,0,0,0,322,323,5,28,0,0,323,
        324,5,1,0,0,324,325,3,30,15,0,325,326,5,2,0,0,326,327,5,5,0,0,327,
        67,1,0,0,0,26,71,77,84,93,108,117,124,131,142,149,155,165,179,198,
        208,215,229,247,256,264,284,295,297,309,315,320
    ]

class compiladoresParser ( Parser ):

    grammarFileName = "compiladores.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'{'", "'}'", "';'", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'&&'", "'||'", "'^'", 
                     "'=!'", "'='", "'=='", "'>'", "'<'", "'<='", "'>='", 
                     "','", "<INVALID>", "'int'", "'double'", "'long'", 
                     "'char'", "'string'", "'while'", "'for'", "'if'", "'else'", 
                     "'return'", "'do'", "'void'" ]

    symbolicNames = [ "<INVALID>", "PA", "PC", "LLA", "LLC", "PYC", "SUMA", 
                      "RESTA", "MULT", "DIV", "MOD", "AND", "OR", "ORX", 
                      "DIF", "ASIG", "IGUAL", "MAYOR", "MENOR", "MENORIG", 
                      "MAYORIG", "COMA", "NUMERO", "INT", "DOUBLE", "LONG", 
                      "CHAR", "STRING", "WHILE", "FOR", "IF", "ELSE", "RETURN", 
                      "DO", "VOID", "ID", "WS", "OTRO" ]

    RULE_programa = 0
    RULE_funcion = 1
    RULE_funcionreturn = 2
    RULE_returnblock = 3
    RULE_voidfuncion = 4
    RULE_parametro = 5
    RULE_parametros = 6
    RULE_usofuncion = 7
    RULE_argumentos = 8
    RULE_argumentosp = 9
    RULE_instrucciones = 10
    RULE_instruccion = 11
    RULE_tdato = 12
    RULE_declaracion = 13
    RULE_asignacion = 14
    RULE_opal = 15
    RULE_comparadores = 16
    RULE_lor = 17
    RULE_lorp = 18
    RULE_land = 19
    RULE_landp = 20
    RULE_comp = 21
    RULE_exp = 22
    RULE_e = 23
    RULE_term = 24
    RULE_t = 25
    RULE_factor = 26
    RULE_iwhile = 27
    RULE_bloque = 28
    RULE_ifor = 29
    RULE_init = 30
    RULE_iif = 31
    RULE_ielse = 32
    RULE_ido = 33

    ruleNames =  [ "programa", "funcion", "funcionreturn", "returnblock", 
                   "voidfuncion", "parametro", "parametros", "usofuncion", 
                   "argumentos", "argumentosp", "instrucciones", "instruccion", 
                   "tdato", "declaracion", "asignacion", "opal", "comparadores", 
                   "lor", "lorp", "land", "landp", "comp", "exp", "e", "term", 
                   "t", "factor", "iwhile", "bloque", "ifor", "init", "iif", 
                   "ielse", "ido" ]

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
    DO=33
    VOID=34
    ID=35
    WS=36
    OTRO=37

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(compiladoresParser.EOF, 0)

        def declaracion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(compiladoresParser.DeclaracionContext)
            else:
                return self.getTypedRuleContext(compiladoresParser.DeclaracionContext,i)


        def funcion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(compiladoresParser.FuncionContext)
            else:
                return self.getTypedRuleContext(compiladoresParser.FuncionContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 68
                    self.declaracion() 
                self.state = 73
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 17205035008) != 0):
                self.state = 74
                self.funcion()
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 80
            self.match(compiladoresParser.EOF)
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

        def funcionreturn(self):
            return self.getTypedRuleContext(compiladoresParser.FuncionreturnContext,0)


        def voidfuncion(self):
            return self.getTypedRuleContext(compiladoresParser.VoidfuncionContext,0)


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
        self.enterRule(localctx, 2, self.RULE_funcion)
        try:
            self.state = 84
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23, 24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                self.funcionreturn()
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 83
                self.voidfuncion()
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


    class FuncionreturnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tdato(self):
            return self.getTypedRuleContext(compiladoresParser.TdatoContext,0)


        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def parametro(self):
            return self.getTypedRuleContext(compiladoresParser.ParametroContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def returnblock(self):
            return self.getTypedRuleContext(compiladoresParser.ReturnblockContext,0)


        def PYC(self):
            return self.getToken(compiladoresParser.PYC, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_funcionreturn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncionreturn" ):
                listener.enterFuncionreturn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncionreturn" ):
                listener.exitFuncionreturn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncionreturn" ):
                return visitor.visitFuncionreturn(self)
            else:
                return visitor.visitChildren(self)




    def funcionreturn(self):

        localctx = compiladoresParser.FuncionreturnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_funcionreturn)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.tdato()
            self.state = 87
            self.match(compiladoresParser.ID)
            self.state = 88
            self.match(compiladoresParser.PA)
            self.state = 89
            self.parametro()
            self.state = 90
            self.match(compiladoresParser.PC)
            self.state = 93
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.state = 91
                self.returnblock()
                pass
            elif token in [5]:
                self.state = 92
                self.match(compiladoresParser.PYC)
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


    class ReturnblockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LLA(self):
            return self.getToken(compiladoresParser.LLA, 0)

        def instrucciones(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionesContext,0)


        def RETURN(self):
            return self.getToken(compiladoresParser.RETURN, 0)

        def opal(self):
            return self.getTypedRuleContext(compiladoresParser.OpalContext,0)


        def PYC(self):
            return self.getToken(compiladoresParser.PYC, 0)

        def LLC(self):
            return self.getToken(compiladoresParser.LLC, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_returnblock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnblock" ):
                listener.enterReturnblock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnblock" ):
                listener.exitReturnblock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnblock" ):
                return visitor.visitReturnblock(self)
            else:
                return visitor.visitChildren(self)




    def returnblock(self):

        localctx = compiladoresParser.ReturnblockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_returnblock)
        try:
            self.state = 108
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.match(compiladoresParser.LLA)
                self.state = 96
                self.instrucciones()
                self.state = 97
                self.match(compiladoresParser.RETURN)
                self.state = 98
                self.opal()
                self.state = 99
                self.match(compiladoresParser.PYC)
                self.state = 100
                self.match(compiladoresParser.LLC)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.match(compiladoresParser.LLA)
                self.state = 103
                self.match(compiladoresParser.RETURN)
                self.state = 104
                self.opal()
                self.state = 105
                self.match(compiladoresParser.PYC)
                self.state = 106
                self.match(compiladoresParser.LLC)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VoidfuncionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VOID(self):
            return self.getToken(compiladoresParser.VOID, 0)

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


        def PYC(self):
            return self.getToken(compiladoresParser.PYC, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_voidfuncion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVoidfuncion" ):
                listener.enterVoidfuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVoidfuncion" ):
                listener.exitVoidfuncion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVoidfuncion" ):
                return visitor.visitVoidfuncion(self)
            else:
                return visitor.visitChildren(self)




    def voidfuncion(self):

        localctx = compiladoresParser.VoidfuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_voidfuncion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(compiladoresParser.VOID)
            self.state = 111
            self.match(compiladoresParser.ID)
            self.state = 112
            self.match(compiladoresParser.PA)
            self.state = 113
            self.parametro()
            self.state = 114
            self.match(compiladoresParser.PC)
            self.state = 117
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.state = 115
                self.bloque()
                pass
            elif token in [5]:
                self.state = 116
                self.match(compiladoresParser.PYC)
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
        self.enterRule(localctx, 10, self.RULE_parametro)
        try:
            self.state = 124
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23, 24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 119
                self.tdato()
                self.state = 120
                self.match(compiladoresParser.ID)
                self.state = 121
                self.parametros()
                pass
            elif token in [2, 21]:
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

        def parametro(self):
            return self.getTypedRuleContext(compiladoresParser.ParametroContext,0)


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
        self.enterRule(localctx, 12, self.RULE_parametros)
        try:
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                self.match(compiladoresParser.COMA)
                self.state = 127
                self.parametro()
                self.state = 128
                self.parametros()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


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

        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def argumentos(self):
            return self.getTypedRuleContext(compiladoresParser.ArgumentosContext,0)


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
        self.enterRule(localctx, 14, self.RULE_usofuncion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(compiladoresParser.ID)
            self.state = 134
            self.match(compiladoresParser.PA)

            self.state = 135
            self.argumentos()
            self.state = 136
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
        self.enterRule(localctx, 16, self.RULE_argumentos)
        try:
            self.state = 142
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 22, 35]:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.opal()
                self.state = 139
                self.argumentosp()
                pass
            elif token in [2, 21]:
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

        def argumentos(self):
            return self.getTypedRuleContext(compiladoresParser.ArgumentosContext,0)


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
        self.enterRule(localctx, 18, self.RULE_argumentosp)
        try:
            self.state = 149
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 144
                self.match(compiladoresParser.COMA)
                self.state = 145
                self.argumentos()
                self.state = 146
                self.argumentosp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


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
        self.enterRule(localctx, 20, self.RULE_instrucciones)
        try:
            self.state = 155
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 5, 23, 24, 28, 29, 30, 35]:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.instruccion()
                self.state = 152
                self.instrucciones()
                pass
            elif token in [4, 32]:
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

        def declaracion(self):
            return self.getTypedRuleContext(compiladoresParser.DeclaracionContext,0)


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


        def PYC(self):
            return self.getToken(compiladoresParser.PYC, 0)

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
        self.enterRule(localctx, 22, self.RULE_instruccion)
        try:
            self.state = 165
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 157
                self.declaracion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 158
                self.iwhile()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 159
                self.ifor()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 160
                self.iif()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 161
                self.bloque()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 162
                self.asignacion()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 163
                self.usofuncion()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 164
                self.match(compiladoresParser.PYC)
                pass


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
            self.state = 167
            _la = self._input.LA(1)
            if not(_la==23 or _la==24):
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


    class DeclaracionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tdato(self):
            return self.getTypedRuleContext(compiladoresParser.TdatoContext,0)


        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def PYC(self):
            return self.getToken(compiladoresParser.PYC, 0)

        def ASIG(self):
            return self.getToken(compiladoresParser.ASIG, 0)

        def opal(self):
            return self.getTypedRuleContext(compiladoresParser.OpalContext,0)


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
        self.enterRule(localctx, 26, self.RULE_declaracion)
        try:
            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.tdato()
                self.state = 170
                self.match(compiladoresParser.ID)
                self.state = 171
                self.match(compiladoresParser.PYC)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
                self.tdato()
                self.state = 174
                self.match(compiladoresParser.ID)
                self.state = 175
                self.match(compiladoresParser.ASIG)
                self.state = 176
                self.opal()
                self.state = 177
                self.match(compiladoresParser.PYC)
                pass


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


        def PYC(self):
            return self.getToken(compiladoresParser.PYC, 0)

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
        self.enterRule(localctx, 28, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(compiladoresParser.ID)
            self.state = 182
            self.match(compiladoresParser.ASIG)
            self.state = 183
            self.opal()
            self.state = 184
            self.match(compiladoresParser.PYC)
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
        self.enterRule(localctx, 30, self.RULE_opal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
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
        self.enterRule(localctx, 32, self.RULE_comparadores)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
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
        self.enterRule(localctx, 34, self.RULE_lor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.land()
            self.state = 191
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
        self.enterRule(localctx, 36, self.RULE_lorp)
        try:
            self.state = 198
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self.match(compiladoresParser.OR)
                self.state = 194
                self.land()
                self.state = 195
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
        self.enterRule(localctx, 38, self.RULE_land)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.comp()
            self.state = 201
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
        self.enterRule(localctx, 40, self.RULE_landp)
        try:
            self.state = 208
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 203
                self.match(compiladoresParser.AND)
                self.state = 204
                self.comp()
                self.state = 205
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
        self.enterRule(localctx, 42, self.RULE_comp)
        try:
            self.state = 215
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 210
                self.exp()
                self.state = 211
                self.comparadores()
                self.state = 212
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 214
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
        self.enterRule(localctx, 44, self.RULE_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.term()
            self.state = 218
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
        self.enterRule(localctx, 46, self.RULE_e)
        try:
            self.state = 229
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.match(compiladoresParser.SUMA)
                self.state = 221
                self.term()
                self.state = 222
                self.e()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 224
                self.match(compiladoresParser.RESTA)
                self.state = 225
                self.term()
                self.state = 226
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
        self.enterRule(localctx, 48, self.RULE_term)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.factor()
            self.state = 232
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
        self.enterRule(localctx, 50, self.RULE_t)
        try:
            self.state = 247
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 234
                self.match(compiladoresParser.MULT)
                self.state = 235
                self.factor()
                self.state = 236
                self.t()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 238
                self.match(compiladoresParser.DIV)
                self.state = 239
                self.factor()
                self.state = 240
                self.t()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 242
                self.match(compiladoresParser.MOD)
                self.state = 243
                self.factor()
                self.state = 244
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
        self.enterRule(localctx, 52, self.RULE_factor)
        try:
            self.state = 256
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 249
                self.match(compiladoresParser.NUMERO)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
                self.match(compiladoresParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 251
                self.usofuncion()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 252
                self.match(compiladoresParser.PA)
                self.state = 253
                self.exp()
                self.state = 254
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

        def bloque(self):
            return self.getTypedRuleContext(compiladoresParser.BloqueContext,0)


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
        self.enterRule(localctx, 54, self.RULE_iwhile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(compiladoresParser.WHILE)
            self.state = 259
            self.match(compiladoresParser.PA)
            self.state = 260
            self.opal()
            self.state = 261
            self.match(compiladoresParser.PC)
            self.state = 264
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 262
                self.bloque()
                pass

            elif la_ == 2:
                self.state = 263
                self.instruccion()
                pass


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
        self.enterRule(localctx, 56, self.RULE_bloque)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.match(compiladoresParser.LLA)
            self.state = 267
            self.instrucciones()
            self.state = 268
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

        def opal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(compiladoresParser.OpalContext)
            else:
                return self.getTypedRuleContext(compiladoresParser.OpalContext,i)


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
        self.enterRule(localctx, 58, self.RULE_ifor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.match(compiladoresParser.FOR)
            self.state = 271
            self.match(compiladoresParser.PA)
            self.state = 272
            self.init()
            self.state = 273
            self.match(compiladoresParser.PYC)
            self.state = 274
            self.opal()
            self.state = 275
            self.match(compiladoresParser.PYC)
            self.state = 276
            self.opal()
            self.state = 277
            self.match(compiladoresParser.PC)
            self.state = 278
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

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def ASIG(self):
            return self.getToken(compiladoresParser.ASIG, 0)

        def usofuncion(self):
            return self.getTypedRuleContext(compiladoresParser.UsofuncionContext,0)


        def opal(self):
            return self.getTypedRuleContext(compiladoresParser.OpalContext,0)


        def tdato(self):
            return self.getTypedRuleContext(compiladoresParser.TdatoContext,0)


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
        self.enterRule(localctx, 60, self.RULE_init)
        try:
            self.state = 297
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 280
                self.match(compiladoresParser.ID)
                self.state = 281
                self.match(compiladoresParser.ASIG)
                self.state = 284
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                if la_ == 1:
                    self.state = 282
                    self.usofuncion()
                    pass

                elif la_ == 2:
                    self.state = 283
                    self.opal()
                    pass


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 286
                self.match(compiladoresParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 287
                self.tdato()
                self.state = 288
                self.match(compiladoresParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 290
                self.tdato()
                self.state = 291
                self.match(compiladoresParser.ID)
                self.state = 292
                self.match(compiladoresParser.ASIG)
                self.state = 295
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                if la_ == 1:
                    self.state = 293
                    self.usofuncion()
                    pass

                elif la_ == 2:
                    self.state = 294
                    self.opal()
                    pass


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

        def LLA(self):
            return self.getToken(compiladoresParser.LLA, 0)

        def instruccion(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionContext,0)


        def PYC(self):
            return self.getToken(compiladoresParser.PYC, 0)

        def LLC(self):
            return self.getToken(compiladoresParser.LLC, 0)

        def ielse(self):
            return self.getTypedRuleContext(compiladoresParser.IelseContext,0)


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
        self.enterRule(localctx, 62, self.RULE_iif)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.match(compiladoresParser.IF)
            self.state = 300
            self.match(compiladoresParser.PA)
            self.state = 301
            self.opal()
            self.state = 302
            self.match(compiladoresParser.PC)
            self.state = 303
            self.match(compiladoresParser.LLA)
            self.state = 304
            self.instruccion()
            self.state = 305
            self.match(compiladoresParser.PYC)
            self.state = 306
            self.match(compiladoresParser.LLC)
            self.state = 309
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 5, 23, 24, 28, 29, 30, 32, 35]:
                pass
            elif token in [31]:
                self.state = 308
                self.ielse()
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


    class IelseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(compiladoresParser.ELSE, 0)

        def bloque(self):
            return self.getTypedRuleContext(compiladoresParser.BloqueContext,0)


        def instruccion(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_ielse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIelse" ):
                listener.enterIelse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIelse" ):
                listener.exitIelse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIelse" ):
                return visitor.visitIelse(self)
            else:
                return visitor.visitChildren(self)




    def ielse(self):

        localctx = compiladoresParser.IelseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_ielse)
        try:
            self.state = 315
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 311
                self.match(compiladoresParser.ELSE)
                self.state = 312
                self.bloque()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 313
                self.match(compiladoresParser.ELSE)
                self.state = 314
                self.instruccion()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(compiladoresParser.DO, 0)

        def WHILE(self):
            return self.getToken(compiladoresParser.WHILE, 0)

        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def opal(self):
            return self.getTypedRuleContext(compiladoresParser.OpalContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def PYC(self):
            return self.getToken(compiladoresParser.PYC, 0)

        def bloque(self):
            return self.getTypedRuleContext(compiladoresParser.BloqueContext,0)


        def instruccion(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_ido

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdo" ):
                listener.enterIdo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdo" ):
                listener.exitIdo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdo" ):
                return visitor.visitIdo(self)
            else:
                return visitor.visitChildren(self)




    def ido(self):

        localctx = compiladoresParser.IdoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_ido)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.match(compiladoresParser.DO)
            self.state = 320
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 318
                self.bloque()
                pass

            elif la_ == 2:
                self.state = 319
                self.instruccion()
                pass


            self.state = 322
            self.match(compiladoresParser.WHILE)
            self.state = 323
            self.match(compiladoresParser.PA)
            self.state = 324
            self.opal()
            self.state = 325
            self.match(compiladoresParser.PC)
            self.state = 326
            self.match(compiladoresParser.PYC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





