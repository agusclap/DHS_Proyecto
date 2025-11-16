// Generated from c:/Users/Agustin/Desktop/DHS/proyecto/src/python/compiladores.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class compiladoresParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		PA=1, PC=2, LLA=3, LLC=4, PYC=5, SUMA=6, RESTA=7, MULT=8, DIV=9, MOD=10, 
		AND=11, OR=12, ORX=13, DIF=14, ASIG=15, IGUAL=16, MAYOR=17, MENOR=18, 
		MENORIG=19, MAYORIG=20, COMA=21, NUMERO=22, INT=23, DOUBLE=24, LONG=25, 
		CHAR=26, STRING=27, WHILE=28, FOR=29, IF=30, ELSE=31, RETURN=32, VOID=33, 
		ID=34, WS=35, OTRO=36;
	public static final int
		RULE_programa = 0, RULE_prototipo = 1, RULE_tfuncion = 2, RULE_funcion = 3, 
		RULE_parametro = 4, RULE_parametros = 5, RULE_usofuncion = 6, RULE_argumentos = 7, 
		RULE_argumentosp = 8, RULE_instrucciones = 9, RULE_instruccion = 10, RULE_return = 11, 
		RULE_tdato = 12, RULE_declaracionesp = 13, RULE_declaraciones = 14, RULE_declaracion = 15, 
		RULE_asignacion = 16, RULE_opal = 17, RULE_comparadores = 18, RULE_lor = 19, 
		RULE_lorp = 20, RULE_land = 21, RULE_landp = 22, RULE_comp = 23, RULE_exp = 24, 
		RULE_e = 25, RULE_term = 26, RULE_t = 27, RULE_factor = 28, RULE_iwhile = 29, 
		RULE_bloque = 30, RULE_ifor = 31, RULE_init = 32, RULE_cond = 33, RULE_iter = 34, 
		RULE_iif = 35;
	private static String[] makeRuleNames() {
		return new String[] {
			"programa", "prototipo", "tfuncion", "funcion", "parametro", "parametros", 
			"usofuncion", "argumentos", "argumentosp", "instrucciones", "instruccion", 
			"return", "tdato", "declaracionesp", "declaraciones", "declaracion", 
			"asignacion", "opal", "comparadores", "lor", "lorp", "land", "landp", 
			"comp", "exp", "e", "term", "t", "factor", "iwhile", "bloque", "ifor", 
			"init", "cond", "iter", "iif"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'('", "')'", "'{'", "'}'", "';'", "'+'", "'-'", "'*'", "'/'", 
			"'%'", "'&&'", "'||'", "'^'", "'=!'", "'='", "'=='", "'>'", "'<'", "'<='", 
			"'>='", "','", null, "'int'", "'double'", "'long'", "'char'", "'string'", 
			"'while'", "'for'", "'if'", "'else'", "'return'", "'void'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "PA", "PC", "LLA", "LLC", "PYC", "SUMA", "RESTA", "MULT", "DIV", 
			"MOD", "AND", "OR", "ORX", "DIF", "ASIG", "IGUAL", "MAYOR", "MENOR", 
			"MENORIG", "MAYORIG", "COMA", "NUMERO", "INT", "DOUBLE", "LONG", "CHAR", 
			"STRING", "WHILE", "FOR", "IF", "ELSE", "RETURN", "VOID", "ID", "WS", 
			"OTRO"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "compiladores.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public compiladoresParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramaContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(compiladoresParser.EOF, 0); }
		public List<DeclaracionesContext> declaraciones() {
			return getRuleContexts(DeclaracionesContext.class);
		}
		public DeclaracionesContext declaraciones(int i) {
			return getRuleContext(DeclaracionesContext.class,i);
		}
		public List<TerminalNode> PYC() { return getTokens(compiladoresParser.PYC); }
		public TerminalNode PYC(int i) {
			return getToken(compiladoresParser.PYC, i);
		}
		public List<FuncionContext> funcion() {
			return getRuleContexts(FuncionContext.class);
		}
		public FuncionContext funcion(int i) {
			return getRuleContext(FuncionContext.class,i);
		}
		public List<PrototipoContext> prototipo() {
			return getRuleContexts(PrototipoContext.class);
		}
		public PrototipoContext prototipo(int i) {
			return getRuleContext(PrototipoContext.class,i);
		}
		public ProgramaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_programa; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterPrograma(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitPrograma(this);
		}
	}

	public final ProgramaContext programa() throws RecognitionException {
		ProgramaContext _localctx = new ProgramaContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_programa);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(77);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==PYC || _la==COMA) {
				{
				{
				setState(72);
				declaraciones();
				setState(73);
				match(PYC);
				}
				}
				setState(79);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(83);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,1,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(80);
					funcion();
					}
					} 
				}
				setState(85);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,1,_ctx);
			}
			setState(89);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 8682209280L) != 0)) {
				{
				{
				setState(86);
				prototipo();
				}
				}
				setState(91);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(92);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PrototipoContext extends ParserRuleContext {
		public TfuncionContext tfuncion() {
			return getRuleContext(TfuncionContext.class,0);
		}
		public TerminalNode ID() { return getToken(compiladoresParser.ID, 0); }
		public TerminalNode PA() { return getToken(compiladoresParser.PA, 0); }
		public ParametroContext parametro() {
			return getRuleContext(ParametroContext.class,0);
		}
		public TerminalNode PC() { return getToken(compiladoresParser.PC, 0); }
		public TerminalNode PYC() { return getToken(compiladoresParser.PYC, 0); }
		public PrototipoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prototipo; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterPrototipo(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitPrototipo(this);
		}
	}

	public final PrototipoContext prototipo() throws RecognitionException {
		PrototipoContext _localctx = new PrototipoContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_prototipo);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(94);
			tfuncion();
			setState(95);
			match(ID);
			setState(96);
			match(PA);
			setState(97);
			parametro();
			setState(98);
			match(PC);
			setState(99);
			match(PYC);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TfuncionContext extends ParserRuleContext {
		public TerminalNode VOID() { return getToken(compiladoresParser.VOID, 0); }
		public TerminalNode INT() { return getToken(compiladoresParser.INT, 0); }
		public TerminalNode DOUBLE() { return getToken(compiladoresParser.DOUBLE, 0); }
		public TerminalNode CHAR() { return getToken(compiladoresParser.CHAR, 0); }
		public TfuncionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tfuncion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterTfuncion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitTfuncion(this);
		}
	}

	public final TfuncionContext tfuncion() throws RecognitionException {
		TfuncionContext _localctx = new TfuncionContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_tfuncion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(101);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 8682209280L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FuncionContext extends ParserRuleContext {
		public TfuncionContext tfuncion() {
			return getRuleContext(TfuncionContext.class,0);
		}
		public TerminalNode ID() { return getToken(compiladoresParser.ID, 0); }
		public TerminalNode PA() { return getToken(compiladoresParser.PA, 0); }
		public ParametroContext parametro() {
			return getRuleContext(ParametroContext.class,0);
		}
		public TerminalNode PC() { return getToken(compiladoresParser.PC, 0); }
		public BloqueContext bloque() {
			return getRuleContext(BloqueContext.class,0);
		}
		public FuncionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funcion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterFuncion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitFuncion(this);
		}
	}

	public final FuncionContext funcion() throws RecognitionException {
		FuncionContext _localctx = new FuncionContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_funcion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(103);
			tfuncion();
			setState(104);
			match(ID);
			setState(105);
			match(PA);
			setState(106);
			parametro();
			setState(107);
			match(PC);
			setState(108);
			bloque();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParametroContext extends ParserRuleContext {
		public TdatoContext tdato() {
			return getRuleContext(TdatoContext.class,0);
		}
		public TerminalNode ID() { return getToken(compiladoresParser.ID, 0); }
		public ParametrosContext parametros() {
			return getRuleContext(ParametrosContext.class,0);
		}
		public ParametroContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parametro; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterParametro(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitParametro(this);
		}
	}

	public final ParametroContext parametro() throws RecognitionException {
		ParametroContext _localctx = new ParametroContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_parametro);
		try {
			setState(115);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
			case DOUBLE:
			case CHAR:
				enterOuterAlt(_localctx, 1);
				{
				setState(110);
				tdato();
				setState(111);
				match(ID);
				setState(112);
				parametros();
				}
				break;
			case PC:
			case COMA:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParametrosContext extends ParserRuleContext {
		public TerminalNode COMA() { return getToken(compiladoresParser.COMA, 0); }
		public ParametroContext parametro() {
			return getRuleContext(ParametroContext.class,0);
		}
		public ParametrosContext parametros() {
			return getRuleContext(ParametrosContext.class,0);
		}
		public ParametrosContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parametros; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterParametros(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitParametros(this);
		}
	}

	public final ParametrosContext parametros() throws RecognitionException {
		ParametrosContext _localctx = new ParametrosContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_parametros);
		try {
			setState(122);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(117);
				match(COMA);
				setState(118);
				parametro();
				setState(119);
				parametros();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class UsofuncionContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(compiladoresParser.ID, 0); }
		public TerminalNode PA() { return getToken(compiladoresParser.PA, 0); }
		public ArgumentosContext argumentos() {
			return getRuleContext(ArgumentosContext.class,0);
		}
		public TerminalNode PC() { return getToken(compiladoresParser.PC, 0); }
		public UsofuncionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_usofuncion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterUsofuncion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitUsofuncion(this);
		}
	}

	public final UsofuncionContext usofuncion() throws RecognitionException {
		UsofuncionContext _localctx = new UsofuncionContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_usofuncion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(124);
			match(ID);
			setState(125);
			match(PA);
			setState(126);
			argumentos();
			setState(127);
			match(PC);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ArgumentosContext extends ParserRuleContext {
		public OpalContext opal() {
			return getRuleContext(OpalContext.class,0);
		}
		public ArgumentospContext argumentosp() {
			return getRuleContext(ArgumentospContext.class,0);
		}
		public ArgumentosContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_argumentos; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterArgumentos(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitArgumentos(this);
		}
	}

	public final ArgumentosContext argumentos() throws RecognitionException {
		ArgumentosContext _localctx = new ArgumentosContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_argumentos);
		try {
			setState(133);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PA:
			case NUMERO:
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(129);
				opal();
				setState(130);
				argumentosp();
				}
				break;
			case PC:
			case COMA:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ArgumentospContext extends ParserRuleContext {
		public TerminalNode COMA() { return getToken(compiladoresParser.COMA, 0); }
		public ArgumentosContext argumentos() {
			return getRuleContext(ArgumentosContext.class,0);
		}
		public ArgumentospContext argumentosp() {
			return getRuleContext(ArgumentospContext.class,0);
		}
		public ArgumentospContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_argumentosp; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterArgumentosp(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitArgumentosp(this);
		}
	}

	public final ArgumentospContext argumentosp() throws RecognitionException {
		ArgumentospContext _localctx = new ArgumentospContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_argumentosp);
		try {
			setState(140);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(135);
				match(COMA);
				setState(136);
				argumentos();
				setState(137);
				argumentosp();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class InstruccionesContext extends ParserRuleContext {
		public InstruccionContext instruccion() {
			return getRuleContext(InstruccionContext.class,0);
		}
		public InstruccionesContext instrucciones() {
			return getRuleContext(InstruccionesContext.class,0);
		}
		public InstruccionesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_instrucciones; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterInstrucciones(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitInstrucciones(this);
		}
	}

	public final InstruccionesContext instrucciones() throws RecognitionException {
		InstruccionesContext _localctx = new InstruccionesContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_instrucciones);
		try {
			setState(146);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PA:
			case LLA:
			case PYC:
			case NUMERO:
			case INT:
			case DOUBLE:
			case CHAR:
			case WHILE:
			case FOR:
			case IF:
			case RETURN:
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(142);
				instruccion();
				setState(143);
				instrucciones();
				}
				break;
			case LLC:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class InstruccionContext extends ParserRuleContext {
		public DeclaracionespContext declaracionesp() {
			return getRuleContext(DeclaracionespContext.class,0);
		}
		public TerminalNode PYC() { return getToken(compiladoresParser.PYC, 0); }
		public IwhileContext iwhile() {
			return getRuleContext(IwhileContext.class,0);
		}
		public IforContext ifor() {
			return getRuleContext(IforContext.class,0);
		}
		public IifContext iif() {
			return getRuleContext(IifContext.class,0);
		}
		public BloqueContext bloque() {
			return getRuleContext(BloqueContext.class,0);
		}
		public AsignacionContext asignacion() {
			return getRuleContext(AsignacionContext.class,0);
		}
		public UsofuncionContext usofuncion() {
			return getRuleContext(UsofuncionContext.class,0);
		}
		public ReturnContext return_() {
			return getRuleContext(ReturnContext.class,0);
		}
		public OpalContext opal() {
			return getRuleContext(OpalContext.class,0);
		}
		public InstruccionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_instruccion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterInstruccion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitInstruccion(this);
		}
	}

	public final InstruccionContext instruccion() throws RecognitionException {
		InstruccionContext _localctx = new InstruccionContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_instruccion);
		try {
			setState(168);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(148);
				declaracionesp();
				setState(149);
				match(PYC);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(151);
				iwhile();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(152);
				ifor();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(153);
				iif();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(154);
				bloque();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(155);
				asignacion();
				setState(156);
				match(PYC);
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(158);
				usofuncion();
				setState(159);
				match(PYC);
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(161);
				return_();
				setState(162);
				match(PYC);
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(164);
				opal();
				setState(165);
				match(PYC);
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(167);
				match(PYC);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ReturnContext extends ParserRuleContext {
		public TerminalNode RETURN() { return getToken(compiladoresParser.RETURN, 0); }
		public OpalContext opal() {
			return getRuleContext(OpalContext.class,0);
		}
		public ReturnContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_return; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterReturn(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitReturn(this);
		}
	}

	public final ReturnContext return_() throws RecognitionException {
		ReturnContext _localctx = new ReturnContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_return);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(170);
			match(RETURN);
			setState(171);
			opal();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TdatoContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(compiladoresParser.INT, 0); }
		public TerminalNode DOUBLE() { return getToken(compiladoresParser.DOUBLE, 0); }
		public TerminalNode CHAR() { return getToken(compiladoresParser.CHAR, 0); }
		public TdatoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tdato; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterTdato(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitTdato(this);
		}
	}

	public final TdatoContext tdato() throws RecognitionException {
		TdatoContext _localctx = new TdatoContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_tdato);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(173);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 92274688L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclaracionespContext extends ParserRuleContext {
		public DeclaracionContext declaracion() {
			return getRuleContext(DeclaracionContext.class,0);
		}
		public DeclaracionesContext declaraciones() {
			return getRuleContext(DeclaracionesContext.class,0);
		}
		public DeclaracionespContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaracionesp; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterDeclaracionesp(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitDeclaracionesp(this);
		}
	}

	public final DeclaracionespContext declaracionesp() throws RecognitionException {
		DeclaracionespContext _localctx = new DeclaracionespContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_declaracionesp);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(175);
			declaracion();
			setState(176);
			declaraciones();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclaracionesContext extends ParserRuleContext {
		public TerminalNode COMA() { return getToken(compiladoresParser.COMA, 0); }
		public TerminalNode ID() { return getToken(compiladoresParser.ID, 0); }
		public DeclaracionesContext declaraciones() {
			return getRuleContext(DeclaracionesContext.class,0);
		}
		public TerminalNode ASIG() { return getToken(compiladoresParser.ASIG, 0); }
		public OpalContext opal() {
			return getRuleContext(OpalContext.class,0);
		}
		public DeclaracionesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaraciones; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterDeclaraciones(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitDeclaraciones(this);
		}
	}

	public final DeclaracionesContext declaraciones() throws RecognitionException {
		DeclaracionesContext _localctx = new DeclaracionesContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_declaraciones);
		int _la;
		try {
			setState(186);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case COMA:
				enterOuterAlt(_localctx, 1);
				{
				setState(178);
				match(COMA);
				setState(179);
				match(ID);
				setState(182);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ASIG) {
					{
					setState(180);
					match(ASIG);
					setState(181);
					opal();
					}
				}

				setState(184);
				declaraciones();
				}
				break;
			case PYC:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclaracionContext extends ParserRuleContext {
		public TdatoContext tdato() {
			return getRuleContext(TdatoContext.class,0);
		}
		public TerminalNode ID() { return getToken(compiladoresParser.ID, 0); }
		public TerminalNode ASIG() { return getToken(compiladoresParser.ASIG, 0); }
		public OpalContext opal() {
			return getRuleContext(OpalContext.class,0);
		}
		public DeclaracionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaracion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterDeclaracion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitDeclaracion(this);
		}
	}

	public final DeclaracionContext declaracion() throws RecognitionException {
		DeclaracionContext _localctx = new DeclaracionContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_declaracion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(188);
			tdato();
			setState(189);
			match(ID);
			setState(192);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ASIG) {
				{
				setState(190);
				match(ASIG);
				setState(191);
				opal();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AsignacionContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(compiladoresParser.ID, 0); }
		public TerminalNode ASIG() { return getToken(compiladoresParser.ASIG, 0); }
		public OpalContext opal() {
			return getRuleContext(OpalContext.class,0);
		}
		public AsignacionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_asignacion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterAsignacion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitAsignacion(this);
		}
	}

	public final AsignacionContext asignacion() throws RecognitionException {
		AsignacionContext _localctx = new AsignacionContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_asignacion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(194);
			match(ID);
			setState(195);
			match(ASIG);
			setState(196);
			opal();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OpalContext extends ParserRuleContext {
		public LorContext lor() {
			return getRuleContext(LorContext.class,0);
		}
		public OpalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_opal; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterOpal(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitOpal(this);
		}
	}

	public final OpalContext opal() throws RecognitionException {
		OpalContext _localctx = new OpalContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_opal);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(198);
			lor();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ComparadoresContext extends ParserRuleContext {
		public TerminalNode MAYOR() { return getToken(compiladoresParser.MAYOR, 0); }
		public TerminalNode MENOR() { return getToken(compiladoresParser.MENOR, 0); }
		public TerminalNode IGUAL() { return getToken(compiladoresParser.IGUAL, 0); }
		public TerminalNode MENORIG() { return getToken(compiladoresParser.MENORIG, 0); }
		public TerminalNode MAYORIG() { return getToken(compiladoresParser.MAYORIG, 0); }
		public TerminalNode DIF() { return getToken(compiladoresParser.DIF, 0); }
		public ComparadoresContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comparadores; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterComparadores(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitComparadores(this);
		}
	}

	public final ComparadoresContext comparadores() throws RecognitionException {
		ComparadoresContext _localctx = new ComparadoresContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_comparadores);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(200);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 2048000L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LorContext extends ParserRuleContext {
		public LandContext land() {
			return getRuleContext(LandContext.class,0);
		}
		public LorpContext lorp() {
			return getRuleContext(LorpContext.class,0);
		}
		public LorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lor; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterLor(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitLor(this);
		}
	}

	public final LorContext lor() throws RecognitionException {
		LorContext _localctx = new LorContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_lor);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(202);
			land();
			setState(203);
			lorp();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LorpContext extends ParserRuleContext {
		public TerminalNode OR() { return getToken(compiladoresParser.OR, 0); }
		public LandContext land() {
			return getRuleContext(LandContext.class,0);
		}
		public LorpContext lorp() {
			return getRuleContext(LorpContext.class,0);
		}
		public LorpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lorp; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterLorp(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitLorp(this);
		}
	}

	public final LorpContext lorp() throws RecognitionException {
		LorpContext _localctx = new LorpContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_lorp);
		try {
			setState(210);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case OR:
				enterOuterAlt(_localctx, 1);
				{
				setState(205);
				match(OR);
				setState(206);
				land();
				setState(207);
				lorp();
				}
				break;
			case PC:
			case PYC:
			case COMA:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LandContext extends ParserRuleContext {
		public CompContext comp() {
			return getRuleContext(CompContext.class,0);
		}
		public LandpContext landp() {
			return getRuleContext(LandpContext.class,0);
		}
		public LandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_land; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterLand(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitLand(this);
		}
	}

	public final LandContext land() throws RecognitionException {
		LandContext _localctx = new LandContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_land);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(212);
			comp();
			setState(213);
			landp();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LandpContext extends ParserRuleContext {
		public TerminalNode AND() { return getToken(compiladoresParser.AND, 0); }
		public CompContext comp() {
			return getRuleContext(CompContext.class,0);
		}
		public LandpContext landp() {
			return getRuleContext(LandpContext.class,0);
		}
		public LandpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_landp; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterLandp(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitLandp(this);
		}
	}

	public final LandpContext landp() throws RecognitionException {
		LandpContext _localctx = new LandpContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_landp);
		try {
			setState(220);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case AND:
				enterOuterAlt(_localctx, 1);
				{
				setState(215);
				match(AND);
				setState(216);
				comp();
				setState(217);
				landp();
				}
				break;
			case PC:
			case PYC:
			case OR:
			case COMA:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CompContext extends ParserRuleContext {
		public List<ExpContext> exp() {
			return getRuleContexts(ExpContext.class);
		}
		public ExpContext exp(int i) {
			return getRuleContext(ExpContext.class,i);
		}
		public ComparadoresContext comparadores() {
			return getRuleContext(ComparadoresContext.class,0);
		}
		public CompContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comp; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterComp(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitComp(this);
		}
	}

	public final CompContext comp() throws RecognitionException {
		CompContext _localctx = new CompContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_comp);
		try {
			setState(227);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(222);
				exp();
				setState(223);
				comparadores();
				setState(224);
				exp();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(226);
				exp();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpContext extends ParserRuleContext {
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public EContext e() {
			return getRuleContext(EContext.class,0);
		}
		public ExpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterExp(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitExp(this);
		}
	}

	public final ExpContext exp() throws RecognitionException {
		ExpContext _localctx = new ExpContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_exp);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(229);
			term();
			setState(230);
			e();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EContext extends ParserRuleContext {
		public TerminalNode SUMA() { return getToken(compiladoresParser.SUMA, 0); }
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public EContext e() {
			return getRuleContext(EContext.class,0);
		}
		public TerminalNode RESTA() { return getToken(compiladoresParser.RESTA, 0); }
		public EContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_e; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterE(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitE(this);
		}
	}

	public final EContext e() throws RecognitionException {
		EContext _localctx = new EContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_e);
		try {
			setState(241);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case SUMA:
				enterOuterAlt(_localctx, 1);
				{
				setState(232);
				match(SUMA);
				setState(233);
				term();
				setState(234);
				e();
				}
				break;
			case RESTA:
				enterOuterAlt(_localctx, 2);
				{
				setState(236);
				match(RESTA);
				setState(237);
				term();
				setState(238);
				e();
				}
				break;
			case PC:
			case PYC:
			case AND:
			case OR:
			case DIF:
			case IGUAL:
			case MAYOR:
			case MENOR:
			case MENORIG:
			case MAYORIG:
			case COMA:
				enterOuterAlt(_localctx, 3);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TermContext extends ParserRuleContext {
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public TContext t() {
			return getRuleContext(TContext.class,0);
		}
		public TermContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterTerm(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitTerm(this);
		}
	}

	public final TermContext term() throws RecognitionException {
		TermContext _localctx = new TermContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_term);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(243);
			factor();
			setState(244);
			t();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TContext extends ParserRuleContext {
		public TerminalNode MULT() { return getToken(compiladoresParser.MULT, 0); }
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public TContext t() {
			return getRuleContext(TContext.class,0);
		}
		public TerminalNode DIV() { return getToken(compiladoresParser.DIV, 0); }
		public TerminalNode MOD() { return getToken(compiladoresParser.MOD, 0); }
		public TContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_t; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterT(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitT(this);
		}
	}

	public final TContext t() throws RecognitionException {
		TContext _localctx = new TContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_t);
		try {
			setState(259);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case MULT:
				enterOuterAlt(_localctx, 1);
				{
				setState(246);
				match(MULT);
				setState(247);
				factor();
				setState(248);
				t();
				}
				break;
			case DIV:
				enterOuterAlt(_localctx, 2);
				{
				setState(250);
				match(DIV);
				setState(251);
				factor();
				setState(252);
				t();
				}
				break;
			case MOD:
				enterOuterAlt(_localctx, 3);
				{
				setState(254);
				match(MOD);
				setState(255);
				factor();
				setState(256);
				t();
				}
				break;
			case PC:
			case PYC:
			case SUMA:
			case RESTA:
			case AND:
			case OR:
			case DIF:
			case IGUAL:
			case MAYOR:
			case MENOR:
			case MENORIG:
			case MAYORIG:
			case COMA:
				enterOuterAlt(_localctx, 4);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FactorContext extends ParserRuleContext {
		public TerminalNode NUMERO() { return getToken(compiladoresParser.NUMERO, 0); }
		public TerminalNode ID() { return getToken(compiladoresParser.ID, 0); }
		public UsofuncionContext usofuncion() {
			return getRuleContext(UsofuncionContext.class,0);
		}
		public TerminalNode PA() { return getToken(compiladoresParser.PA, 0); }
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public TerminalNode PC() { return getToken(compiladoresParser.PC, 0); }
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterFactor(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitFactor(this);
		}
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_factor);
		try {
			setState(268);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(261);
				match(NUMERO);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(262);
				match(ID);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(263);
				usofuncion();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(264);
				match(PA);
				setState(265);
				exp();
				setState(266);
				match(PC);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IwhileContext extends ParserRuleContext {
		public TerminalNode WHILE() { return getToken(compiladoresParser.WHILE, 0); }
		public TerminalNode PA() { return getToken(compiladoresParser.PA, 0); }
		public OpalContext opal() {
			return getRuleContext(OpalContext.class,0);
		}
		public TerminalNode PC() { return getToken(compiladoresParser.PC, 0); }
		public InstruccionContext instruccion() {
			return getRuleContext(InstruccionContext.class,0);
		}
		public IwhileContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_iwhile; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterIwhile(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitIwhile(this);
		}
	}

	public final IwhileContext iwhile() throws RecognitionException {
		IwhileContext _localctx = new IwhileContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_iwhile);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(270);
			match(WHILE);
			setState(271);
			match(PA);
			setState(272);
			opal();
			setState(273);
			match(PC);
			setState(274);
			instruccion();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BloqueContext extends ParserRuleContext {
		public TerminalNode LLA() { return getToken(compiladoresParser.LLA, 0); }
		public InstruccionesContext instrucciones() {
			return getRuleContext(InstruccionesContext.class,0);
		}
		public TerminalNode LLC() { return getToken(compiladoresParser.LLC, 0); }
		public BloqueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bloque; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterBloque(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitBloque(this);
		}
	}

	public final BloqueContext bloque() throws RecognitionException {
		BloqueContext _localctx = new BloqueContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_bloque);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(276);
			match(LLA);
			setState(277);
			instrucciones();
			setState(278);
			match(LLC);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IforContext extends ParserRuleContext {
		public TerminalNode FOR() { return getToken(compiladoresParser.FOR, 0); }
		public TerminalNode PA() { return getToken(compiladoresParser.PA, 0); }
		public InitContext init() {
			return getRuleContext(InitContext.class,0);
		}
		public List<TerminalNode> PYC() { return getTokens(compiladoresParser.PYC); }
		public TerminalNode PYC(int i) {
			return getToken(compiladoresParser.PYC, i);
		}
		public CondContext cond() {
			return getRuleContext(CondContext.class,0);
		}
		public IterContext iter() {
			return getRuleContext(IterContext.class,0);
		}
		public TerminalNode PC() { return getToken(compiladoresParser.PC, 0); }
		public InstruccionContext instruccion() {
			return getRuleContext(InstruccionContext.class,0);
		}
		public IforContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifor; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterIfor(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitIfor(this);
		}
	}

	public final IforContext ifor() throws RecognitionException {
		IforContext _localctx = new IforContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_ifor);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(280);
			match(FOR);
			setState(281);
			match(PA);
			setState(282);
			init();
			setState(283);
			match(PYC);
			setState(284);
			cond();
			setState(285);
			match(PYC);
			setState(286);
			iter();
			setState(287);
			match(PC);
			setState(288);
			instruccion();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class InitContext extends ParserRuleContext {
		public AsignacionContext asignacion() {
			return getRuleContext(AsignacionContext.class,0);
		}
		public InitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_init; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterInit(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitInit(this);
		}
	}

	public final InitContext init() throws RecognitionException {
		InitContext _localctx = new InitContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_init);
		try {
			setState(292);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(290);
				asignacion();
				}
				break;
			case PYC:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CondContext extends ParserRuleContext {
		public OpalContext opal() {
			return getRuleContext(OpalContext.class,0);
		}
		public CondContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cond; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterCond(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitCond(this);
		}
	}

	public final CondContext cond() throws RecognitionException {
		CondContext _localctx = new CondContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_cond);
		try {
			setState(296);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PA:
			case NUMERO:
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(294);
				opal();
				}
				break;
			case PYC:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IterContext extends ParserRuleContext {
		public OpalContext opal() {
			return getRuleContext(OpalContext.class,0);
		}
		public TerminalNode ID() { return getToken(compiladoresParser.ID, 0); }
		public List<TerminalNode> SUMA() { return getTokens(compiladoresParser.SUMA); }
		public TerminalNode SUMA(int i) {
			return getToken(compiladoresParser.SUMA, i);
		}
		public List<TerminalNode> RESTA() { return getTokens(compiladoresParser.RESTA); }
		public TerminalNode RESTA(int i) {
			return getToken(compiladoresParser.RESTA, i);
		}
		public TerminalNode ASIG() { return getToken(compiladoresParser.ASIG, 0); }
		public IterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_iter; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterIter(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitIter(this);
		}
	}

	public final IterContext iter() throws RecognitionException {
		IterContext _localctx = new IterContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_iter);
		try {
			setState(315);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,20,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(298);
				opal();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(299);
				match(ID);
				setState(300);
				match(SUMA);
				setState(301);
				match(SUMA);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(302);
				match(SUMA);
				setState(303);
				match(SUMA);
				setState(304);
				match(ID);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(305);
				match(ID);
				setState(306);
				match(RESTA);
				setState(307);
				match(RESTA);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(308);
				match(RESTA);
				setState(309);
				match(RESTA);
				setState(310);
				match(ID);
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(311);
				match(ID);
				setState(312);
				match(ASIG);
				setState(313);
				opal();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IifContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(compiladoresParser.IF, 0); }
		public TerminalNode PA() { return getToken(compiladoresParser.PA, 0); }
		public OpalContext opal() {
			return getRuleContext(OpalContext.class,0);
		}
		public TerminalNode PC() { return getToken(compiladoresParser.PC, 0); }
		public List<InstruccionContext> instruccion() {
			return getRuleContexts(InstruccionContext.class);
		}
		public InstruccionContext instruccion(int i) {
			return getRuleContext(InstruccionContext.class,i);
		}
		public TerminalNode ELSE() { return getToken(compiladoresParser.ELSE, 0); }
		public IifContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_iif; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterIif(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitIif(this);
		}
	}

	public final IifContext iif() throws RecognitionException {
		IifContext _localctx = new IifContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_iif);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(317);
			match(IF);
			setState(318);
			match(PA);
			setState(319);
			opal();
			setState(320);
			match(PC);
			setState(321);
			instruccion();
			setState(325);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,21,_ctx) ) {
			case 1:
				{
				setState(322);
				match(ELSE);
				setState(323);
				instruccion();
				}
				break;
			case 2:
				{
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001$\u0148\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007\u0018"+
		"\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002\u001b\u0007\u001b"+
		"\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002\u001e\u0007\u001e"+
		"\u0002\u001f\u0007\u001f\u0002 \u0007 \u0002!\u0007!\u0002\"\u0007\"\u0002"+
		"#\u0007#\u0001\u0000\u0001\u0000\u0001\u0000\u0005\u0000L\b\u0000\n\u0000"+
		"\f\u0000O\t\u0000\u0001\u0000\u0005\u0000R\b\u0000\n\u0000\f\u0000U\t"+
		"\u0000\u0001\u0000\u0005\u0000X\b\u0000\n\u0000\f\u0000[\t\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0003\u0004t\b"+
		"\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0003"+
		"\u0005{\b\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0003\u0007\u0086"+
		"\b\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0003\b\u008d\b\b\u0001"+
		"\t\u0001\t\u0001\t\u0001\t\u0003\t\u0093\b\t\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0003\n\u00a9"+
		"\b\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001\r\u0001"+
		"\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0003\u000e"+
		"\u00b7\b\u000e\u0001\u000e\u0001\u000e\u0003\u000e\u00bb\b\u000e\u0001"+
		"\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0003\u000f\u00c1\b\u000f\u0001"+
		"\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0001"+
		"\u0012\u0001\u0012\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0014\u0001"+
		"\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0003\u0014\u00d3\b\u0014\u0001"+
		"\u0015\u0001\u0015\u0001\u0015\u0001\u0016\u0001\u0016\u0001\u0016\u0001"+
		"\u0016\u0001\u0016\u0003\u0016\u00dd\b\u0016\u0001\u0017\u0001\u0017\u0001"+
		"\u0017\u0001\u0017\u0001\u0017\u0003\u0017\u00e4\b\u0017\u0001\u0018\u0001"+
		"\u0018\u0001\u0018\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001"+
		"\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0003\u0019\u00f2"+
		"\b\u0019\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001b\u0001\u001b\u0001"+
		"\u001b\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001b\u0001"+
		"\u001b\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001b\u0003\u001b\u0104"+
		"\b\u001b\u0001\u001c\u0001\u001c\u0001\u001c\u0001\u001c\u0001\u001c\u0001"+
		"\u001c\u0001\u001c\u0003\u001c\u010d\b\u001c\u0001\u001d\u0001\u001d\u0001"+
		"\u001d\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001e\u0001\u001e\u0001"+
		"\u001e\u0001\u001e\u0001\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0001"+
		"\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0001"+
		" \u0001 \u0003 \u0125\b \u0001!\u0001!\u0003!\u0129\b!\u0001\"\u0001\""+
		"\u0001\"\u0001\"\u0001\"\u0001\"\u0001\"\u0001\"\u0001\"\u0001\"\u0001"+
		"\"\u0001\"\u0001\"\u0001\"\u0001\"\u0001\"\u0001\"\u0003\"\u013c\b\"\u0001"+
		"#\u0001#\u0001#\u0001#\u0001#\u0001#\u0001#\u0001#\u0003#\u0146\b#\u0001"+
		"#\u0000\u0000$\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016"+
		"\u0018\u001a\u001c\u001e \"$&(*,.02468:<>@BDF\u0000\u0003\u0003\u0000"+
		"\u0017\u0018\u001a\u001a!!\u0002\u0000\u0017\u0018\u001a\u001a\u0002\u0000"+
		"\u000e\u000e\u0010\u0014\u014b\u0000M\u0001\u0000\u0000\u0000\u0002^\u0001"+
		"\u0000\u0000\u0000\u0004e\u0001\u0000\u0000\u0000\u0006g\u0001\u0000\u0000"+
		"\u0000\bs\u0001\u0000\u0000\u0000\nz\u0001\u0000\u0000\u0000\f|\u0001"+
		"\u0000\u0000\u0000\u000e\u0085\u0001\u0000\u0000\u0000\u0010\u008c\u0001"+
		"\u0000\u0000\u0000\u0012\u0092\u0001\u0000\u0000\u0000\u0014\u00a8\u0001"+
		"\u0000\u0000\u0000\u0016\u00aa\u0001\u0000\u0000\u0000\u0018\u00ad\u0001"+
		"\u0000\u0000\u0000\u001a\u00af\u0001\u0000\u0000\u0000\u001c\u00ba\u0001"+
		"\u0000\u0000\u0000\u001e\u00bc\u0001\u0000\u0000\u0000 \u00c2\u0001\u0000"+
		"\u0000\u0000\"\u00c6\u0001\u0000\u0000\u0000$\u00c8\u0001\u0000\u0000"+
		"\u0000&\u00ca\u0001\u0000\u0000\u0000(\u00d2\u0001\u0000\u0000\u0000*"+
		"\u00d4\u0001\u0000\u0000\u0000,\u00dc\u0001\u0000\u0000\u0000.\u00e3\u0001"+
		"\u0000\u0000\u00000\u00e5\u0001\u0000\u0000\u00002\u00f1\u0001\u0000\u0000"+
		"\u00004\u00f3\u0001\u0000\u0000\u00006\u0103\u0001\u0000\u0000\u00008"+
		"\u010c\u0001\u0000\u0000\u0000:\u010e\u0001\u0000\u0000\u0000<\u0114\u0001"+
		"\u0000\u0000\u0000>\u0118\u0001\u0000\u0000\u0000@\u0124\u0001\u0000\u0000"+
		"\u0000B\u0128\u0001\u0000\u0000\u0000D\u013b\u0001\u0000\u0000\u0000F"+
		"\u013d\u0001\u0000\u0000\u0000HI\u0003\u001c\u000e\u0000IJ\u0005\u0005"+
		"\u0000\u0000JL\u0001\u0000\u0000\u0000KH\u0001\u0000\u0000\u0000LO\u0001"+
		"\u0000\u0000\u0000MK\u0001\u0000\u0000\u0000MN\u0001\u0000\u0000\u0000"+
		"NS\u0001\u0000\u0000\u0000OM\u0001\u0000\u0000\u0000PR\u0003\u0006\u0003"+
		"\u0000QP\u0001\u0000\u0000\u0000RU\u0001\u0000\u0000\u0000SQ\u0001\u0000"+
		"\u0000\u0000ST\u0001\u0000\u0000\u0000TY\u0001\u0000\u0000\u0000US\u0001"+
		"\u0000\u0000\u0000VX\u0003\u0002\u0001\u0000WV\u0001\u0000\u0000\u0000"+
		"X[\u0001\u0000\u0000\u0000YW\u0001\u0000\u0000\u0000YZ\u0001\u0000\u0000"+
		"\u0000Z\\\u0001\u0000\u0000\u0000[Y\u0001\u0000\u0000\u0000\\]\u0005\u0000"+
		"\u0000\u0001]\u0001\u0001\u0000\u0000\u0000^_\u0003\u0004\u0002\u0000"+
		"_`\u0005\"\u0000\u0000`a\u0005\u0001\u0000\u0000ab\u0003\b\u0004\u0000"+
		"bc\u0005\u0002\u0000\u0000cd\u0005\u0005\u0000\u0000d\u0003\u0001\u0000"+
		"\u0000\u0000ef\u0007\u0000\u0000\u0000f\u0005\u0001\u0000\u0000\u0000"+
		"gh\u0003\u0004\u0002\u0000hi\u0005\"\u0000\u0000ij\u0005\u0001\u0000\u0000"+
		"jk\u0003\b\u0004\u0000kl\u0005\u0002\u0000\u0000lm\u0003<\u001e\u0000"+
		"m\u0007\u0001\u0000\u0000\u0000no\u0003\u0018\f\u0000op\u0005\"\u0000"+
		"\u0000pq\u0003\n\u0005\u0000qt\u0001\u0000\u0000\u0000rt\u0001\u0000\u0000"+
		"\u0000sn\u0001\u0000\u0000\u0000sr\u0001\u0000\u0000\u0000t\t\u0001\u0000"+
		"\u0000\u0000uv\u0005\u0015\u0000\u0000vw\u0003\b\u0004\u0000wx\u0003\n"+
		"\u0005\u0000x{\u0001\u0000\u0000\u0000y{\u0001\u0000\u0000\u0000zu\u0001"+
		"\u0000\u0000\u0000zy\u0001\u0000\u0000\u0000{\u000b\u0001\u0000\u0000"+
		"\u0000|}\u0005\"\u0000\u0000}~\u0005\u0001\u0000\u0000~\u007f\u0003\u000e"+
		"\u0007\u0000\u007f\u0080\u0005\u0002\u0000\u0000\u0080\r\u0001\u0000\u0000"+
		"\u0000\u0081\u0082\u0003\"\u0011\u0000\u0082\u0083\u0003\u0010\b\u0000"+
		"\u0083\u0086\u0001\u0000\u0000\u0000\u0084\u0086\u0001\u0000\u0000\u0000"+
		"\u0085\u0081\u0001\u0000\u0000\u0000\u0085\u0084\u0001\u0000\u0000\u0000"+
		"\u0086\u000f\u0001\u0000\u0000\u0000\u0087\u0088\u0005\u0015\u0000\u0000"+
		"\u0088\u0089\u0003\u000e\u0007\u0000\u0089\u008a\u0003\u0010\b\u0000\u008a"+
		"\u008d\u0001\u0000\u0000\u0000\u008b\u008d\u0001\u0000\u0000\u0000\u008c"+
		"\u0087\u0001\u0000\u0000\u0000\u008c\u008b\u0001\u0000\u0000\u0000\u008d"+
		"\u0011\u0001\u0000\u0000\u0000\u008e\u008f\u0003\u0014\n\u0000\u008f\u0090"+
		"\u0003\u0012\t\u0000\u0090\u0093\u0001\u0000\u0000\u0000\u0091\u0093\u0001"+
		"\u0000\u0000\u0000\u0092\u008e\u0001\u0000\u0000\u0000\u0092\u0091\u0001"+
		"\u0000\u0000\u0000\u0093\u0013\u0001\u0000\u0000\u0000\u0094\u0095\u0003"+
		"\u001a\r\u0000\u0095\u0096\u0005\u0005\u0000\u0000\u0096\u00a9\u0001\u0000"+
		"\u0000\u0000\u0097\u00a9\u0003:\u001d\u0000\u0098\u00a9\u0003>\u001f\u0000"+
		"\u0099\u00a9\u0003F#\u0000\u009a\u00a9\u0003<\u001e\u0000\u009b\u009c"+
		"\u0003 \u0010\u0000\u009c\u009d\u0005\u0005\u0000\u0000\u009d\u00a9\u0001"+
		"\u0000\u0000\u0000\u009e\u009f\u0003\f\u0006\u0000\u009f\u00a0\u0005\u0005"+
		"\u0000\u0000\u00a0\u00a9\u0001\u0000\u0000\u0000\u00a1\u00a2\u0003\u0016"+
		"\u000b\u0000\u00a2\u00a3\u0005\u0005\u0000\u0000\u00a3\u00a9\u0001\u0000"+
		"\u0000\u0000\u00a4\u00a5\u0003\"\u0011\u0000\u00a5\u00a6\u0005\u0005\u0000"+
		"\u0000\u00a6\u00a9\u0001\u0000\u0000\u0000\u00a7\u00a9\u0005\u0005\u0000"+
		"\u0000\u00a8\u0094\u0001\u0000\u0000\u0000\u00a8\u0097\u0001\u0000\u0000"+
		"\u0000\u00a8\u0098\u0001\u0000\u0000\u0000\u00a8\u0099\u0001\u0000\u0000"+
		"\u0000\u00a8\u009a\u0001\u0000\u0000\u0000\u00a8\u009b\u0001\u0000\u0000"+
		"\u0000\u00a8\u009e\u0001\u0000\u0000\u0000\u00a8\u00a1\u0001\u0000\u0000"+
		"\u0000\u00a8\u00a4\u0001\u0000\u0000\u0000\u00a8\u00a7\u0001\u0000\u0000"+
		"\u0000\u00a9\u0015\u0001\u0000\u0000\u0000\u00aa\u00ab\u0005 \u0000\u0000"+
		"\u00ab\u00ac\u0003\"\u0011\u0000\u00ac\u0017\u0001\u0000\u0000\u0000\u00ad"+
		"\u00ae\u0007\u0001\u0000\u0000\u00ae\u0019\u0001\u0000\u0000\u0000\u00af"+
		"\u00b0\u0003\u001e\u000f\u0000\u00b0\u00b1\u0003\u001c\u000e\u0000\u00b1"+
		"\u001b\u0001\u0000\u0000\u0000\u00b2\u00b3\u0005\u0015\u0000\u0000\u00b3"+
		"\u00b6\u0005\"\u0000\u0000\u00b4\u00b5\u0005\u000f\u0000\u0000\u00b5\u00b7"+
		"\u0003\"\u0011\u0000\u00b6\u00b4\u0001\u0000\u0000\u0000\u00b6\u00b7\u0001"+
		"\u0000\u0000\u0000\u00b7\u00b8\u0001\u0000\u0000\u0000\u00b8\u00bb\u0003"+
		"\u001c\u000e\u0000\u00b9\u00bb\u0001\u0000\u0000\u0000\u00ba\u00b2\u0001"+
		"\u0000\u0000\u0000\u00ba\u00b9\u0001\u0000\u0000\u0000\u00bb\u001d\u0001"+
		"\u0000\u0000\u0000\u00bc\u00bd\u0003\u0018\f\u0000\u00bd\u00c0\u0005\""+
		"\u0000\u0000\u00be\u00bf\u0005\u000f\u0000\u0000\u00bf\u00c1\u0003\"\u0011"+
		"\u0000\u00c0\u00be\u0001\u0000\u0000\u0000\u00c0\u00c1\u0001\u0000\u0000"+
		"\u0000\u00c1\u001f\u0001\u0000\u0000\u0000\u00c2\u00c3\u0005\"\u0000\u0000"+
		"\u00c3\u00c4\u0005\u000f\u0000\u0000\u00c4\u00c5\u0003\"\u0011\u0000\u00c5"+
		"!\u0001\u0000\u0000\u0000\u00c6\u00c7\u0003&\u0013\u0000\u00c7#\u0001"+
		"\u0000\u0000\u0000\u00c8\u00c9\u0007\u0002\u0000\u0000\u00c9%\u0001\u0000"+
		"\u0000\u0000\u00ca\u00cb\u0003*\u0015\u0000\u00cb\u00cc\u0003(\u0014\u0000"+
		"\u00cc\'\u0001\u0000\u0000\u0000\u00cd\u00ce\u0005\f\u0000\u0000\u00ce"+
		"\u00cf\u0003*\u0015\u0000\u00cf\u00d0\u0003(\u0014\u0000\u00d0\u00d3\u0001"+
		"\u0000\u0000\u0000\u00d1\u00d3\u0001\u0000\u0000\u0000\u00d2\u00cd\u0001"+
		"\u0000\u0000\u0000\u00d2\u00d1\u0001\u0000\u0000\u0000\u00d3)\u0001\u0000"+
		"\u0000\u0000\u00d4\u00d5\u0003.\u0017\u0000\u00d5\u00d6\u0003,\u0016\u0000"+
		"\u00d6+\u0001\u0000\u0000\u0000\u00d7\u00d8\u0005\u000b\u0000\u0000\u00d8"+
		"\u00d9\u0003.\u0017\u0000\u00d9\u00da\u0003,\u0016\u0000\u00da\u00dd\u0001"+
		"\u0000\u0000\u0000\u00db\u00dd\u0001\u0000\u0000\u0000\u00dc\u00d7\u0001"+
		"\u0000\u0000\u0000\u00dc\u00db\u0001\u0000\u0000\u0000\u00dd-\u0001\u0000"+
		"\u0000\u0000\u00de\u00df\u00030\u0018\u0000\u00df\u00e0\u0003$\u0012\u0000"+
		"\u00e0\u00e1\u00030\u0018\u0000\u00e1\u00e4\u0001\u0000\u0000\u0000\u00e2"+
		"\u00e4\u00030\u0018\u0000\u00e3\u00de\u0001\u0000\u0000\u0000\u00e3\u00e2"+
		"\u0001\u0000\u0000\u0000\u00e4/\u0001\u0000\u0000\u0000\u00e5\u00e6\u0003"+
		"4\u001a\u0000\u00e6\u00e7\u00032\u0019\u0000\u00e71\u0001\u0000\u0000"+
		"\u0000\u00e8\u00e9\u0005\u0006\u0000\u0000\u00e9\u00ea\u00034\u001a\u0000"+
		"\u00ea\u00eb\u00032\u0019\u0000\u00eb\u00f2\u0001\u0000\u0000\u0000\u00ec"+
		"\u00ed\u0005\u0007\u0000\u0000\u00ed\u00ee\u00034\u001a\u0000\u00ee\u00ef"+
		"\u00032\u0019\u0000\u00ef\u00f2\u0001\u0000\u0000\u0000\u00f0\u00f2\u0001"+
		"\u0000\u0000\u0000\u00f1\u00e8\u0001\u0000\u0000\u0000\u00f1\u00ec\u0001"+
		"\u0000\u0000\u0000\u00f1\u00f0\u0001\u0000\u0000\u0000\u00f23\u0001\u0000"+
		"\u0000\u0000\u00f3\u00f4\u00038\u001c\u0000\u00f4\u00f5\u00036\u001b\u0000"+
		"\u00f55\u0001\u0000\u0000\u0000\u00f6\u00f7\u0005\b\u0000\u0000\u00f7"+
		"\u00f8\u00038\u001c\u0000\u00f8\u00f9\u00036\u001b\u0000\u00f9\u0104\u0001"+
		"\u0000\u0000\u0000\u00fa\u00fb\u0005\t\u0000\u0000\u00fb\u00fc\u00038"+
		"\u001c\u0000\u00fc\u00fd\u00036\u001b\u0000\u00fd\u0104\u0001\u0000\u0000"+
		"\u0000\u00fe\u00ff\u0005\n\u0000\u0000\u00ff\u0100\u00038\u001c\u0000"+
		"\u0100\u0101\u00036\u001b\u0000\u0101\u0104\u0001\u0000\u0000\u0000\u0102"+
		"\u0104\u0001\u0000\u0000\u0000\u0103\u00f6\u0001\u0000\u0000\u0000\u0103"+
		"\u00fa\u0001\u0000\u0000\u0000\u0103\u00fe\u0001\u0000\u0000\u0000\u0103"+
		"\u0102\u0001\u0000\u0000\u0000\u01047\u0001\u0000\u0000\u0000\u0105\u010d"+
		"\u0005\u0016\u0000\u0000\u0106\u010d\u0005\"\u0000\u0000\u0107\u010d\u0003"+
		"\f\u0006\u0000\u0108\u0109\u0005\u0001\u0000\u0000\u0109\u010a\u00030"+
		"\u0018\u0000\u010a\u010b\u0005\u0002\u0000\u0000\u010b\u010d\u0001\u0000"+
		"\u0000\u0000\u010c\u0105\u0001\u0000\u0000\u0000\u010c\u0106\u0001\u0000"+
		"\u0000\u0000\u010c\u0107\u0001\u0000\u0000\u0000\u010c\u0108\u0001\u0000"+
		"\u0000\u0000\u010d9\u0001\u0000\u0000\u0000\u010e\u010f\u0005\u001c\u0000"+
		"\u0000\u010f\u0110\u0005\u0001\u0000\u0000\u0110\u0111\u0003\"\u0011\u0000"+
		"\u0111\u0112\u0005\u0002\u0000\u0000\u0112\u0113\u0003\u0014\n\u0000\u0113"+
		";\u0001\u0000\u0000\u0000\u0114\u0115\u0005\u0003\u0000\u0000\u0115\u0116"+
		"\u0003\u0012\t\u0000\u0116\u0117\u0005\u0004\u0000\u0000\u0117=\u0001"+
		"\u0000\u0000\u0000\u0118\u0119\u0005\u001d\u0000\u0000\u0119\u011a\u0005"+
		"\u0001\u0000\u0000\u011a\u011b\u0003@ \u0000\u011b\u011c\u0005\u0005\u0000"+
		"\u0000\u011c\u011d\u0003B!\u0000\u011d\u011e\u0005\u0005\u0000\u0000\u011e"+
		"\u011f\u0003D\"\u0000\u011f\u0120\u0005\u0002\u0000\u0000\u0120\u0121"+
		"\u0003\u0014\n\u0000\u0121?\u0001\u0000\u0000\u0000\u0122\u0125\u0003"+
		" \u0010\u0000\u0123\u0125\u0001\u0000\u0000\u0000\u0124\u0122\u0001\u0000"+
		"\u0000\u0000\u0124\u0123\u0001\u0000\u0000\u0000\u0125A\u0001\u0000\u0000"+
		"\u0000\u0126\u0129\u0003\"\u0011\u0000\u0127\u0129\u0001\u0000\u0000\u0000"+
		"\u0128\u0126\u0001\u0000\u0000\u0000\u0128\u0127\u0001\u0000\u0000\u0000"+
		"\u0129C\u0001\u0000\u0000\u0000\u012a\u013c\u0003\"\u0011\u0000\u012b"+
		"\u012c\u0005\"\u0000\u0000\u012c\u012d\u0005\u0006\u0000\u0000\u012d\u013c"+
		"\u0005\u0006\u0000\u0000\u012e\u012f\u0005\u0006\u0000\u0000\u012f\u0130"+
		"\u0005\u0006\u0000\u0000\u0130\u013c\u0005\"\u0000\u0000\u0131\u0132\u0005"+
		"\"\u0000\u0000\u0132\u0133\u0005\u0007\u0000\u0000\u0133\u013c\u0005\u0007"+
		"\u0000\u0000\u0134\u0135\u0005\u0007\u0000\u0000\u0135\u0136\u0005\u0007"+
		"\u0000\u0000\u0136\u013c\u0005\"\u0000\u0000\u0137\u0138\u0005\"\u0000"+
		"\u0000\u0138\u0139\u0005\u000f\u0000\u0000\u0139\u013c\u0003\"\u0011\u0000"+
		"\u013a\u013c\u0001\u0000\u0000\u0000\u013b\u012a\u0001\u0000\u0000\u0000"+
		"\u013b\u012b\u0001\u0000\u0000\u0000\u013b\u012e\u0001\u0000\u0000\u0000"+
		"\u013b\u0131\u0001\u0000\u0000\u0000\u013b\u0134\u0001\u0000\u0000\u0000"+
		"\u013b\u0137\u0001\u0000\u0000\u0000\u013b\u013a\u0001\u0000\u0000\u0000"+
		"\u013cE\u0001\u0000\u0000\u0000\u013d\u013e\u0005\u001e\u0000\u0000\u013e"+
		"\u013f\u0005\u0001\u0000\u0000\u013f\u0140\u0003\"\u0011\u0000\u0140\u0141"+
		"\u0005\u0002\u0000\u0000\u0141\u0145\u0003\u0014\n\u0000\u0142\u0143\u0005"+
		"\u001f\u0000\u0000\u0143\u0146\u0003\u0014\n\u0000\u0144\u0146\u0001\u0000"+
		"\u0000\u0000\u0145\u0142\u0001\u0000\u0000\u0000\u0145\u0144\u0001\u0000"+
		"\u0000\u0000\u0146G\u0001\u0000\u0000\u0000\u0016MSYsz\u0085\u008c\u0092"+
		"\u00a8\u00b6\u00ba\u00c0\u00d2\u00dc\u00e3\u00f1\u0103\u010c\u0124\u0128"+
		"\u013b\u0145";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}