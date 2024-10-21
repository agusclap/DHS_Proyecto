// Generated from /home/agustin/Desktop/dhs/proyecto/src/python/compiladores.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class compiladoresLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		PA=1, PC=2, LLA=3, LLC=4, PYC=5, SUMA=6, RESTA=7, MULT=8, DIV=9, MOD=10, 
		AND=11, OR=12, ORX=13, ASIG=14, IGUAL=15, MAYOR=16, MENOR=17, MENORIG=18, 
		MAYORIG=19, NUMERO=20, INT=21, WHILE=22, FOR=23, IF=24, ID=25, WS=26, 
		OTRO=27;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"LETRA", "DIGITO", "PA", "PC", "LLA", "LLC", "PYC", "SUMA", "RESTA", 
			"MULT", "DIV", "MOD", "AND", "OR", "ORX", "ASIG", "IGUAL", "MAYOR", "MENOR", 
			"MENORIG", "MAYORIG", "NUMERO", "INT", "WHILE", "FOR", "IF", "ID", "WS", 
			"OTRO"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'('", "')'", "'{'", "'}'", "';'", "'+'", "'-'", "'*'", "'/'", 
			"'%'", "'&&'", "'||'", "'^'", "'='", "'=='", "'>'", "'<'", "'<='", "'>='", 
			null, "'int'", "'while'", "'for'", "'if'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "PA", "PC", "LLA", "LLC", "PYC", "SUMA", "RESTA", "MULT", "DIV", 
			"MOD", "AND", "OR", "ORX", "ASIG", "IGUAL", "MAYOR", "MENOR", "MENORIG", 
			"MAYORIG", "NUMERO", "INT", "WHILE", "FOR", "IF", "ID", "WS", "OTRO"
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


	public compiladoresLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "compiladores.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\u001b\u0092\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002"+
		"\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002"+
		"\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002"+
		"\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002"+
		"\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e"+
		"\u0002\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011"+
		"\u0002\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014"+
		"\u0002\u0015\u0007\u0015\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017"+
		"\u0002\u0018\u0007\u0018\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a"+
		"\u0002\u001b\u0007\u001b\u0002\u001c\u0007\u001c\u0001\u0000\u0001\u0000"+
		"\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003"+
		"\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006"+
		"\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\t\u0001\t\u0001\n\u0001"+
		"\n\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001\f\u0001\r\u0001\r\u0001"+
		"\r\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0012\u0001\u0012\u0001\u0013"+
		"\u0001\u0013\u0001\u0013\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0015"+
		"\u0004\u0015l\b\u0015\u000b\u0015\f\u0015m\u0001\u0016\u0001\u0016\u0001"+
		"\u0016\u0001\u0016\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001"+
		"\u0017\u0001\u0017\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001"+
		"\u0019\u0001\u0019\u0001\u0019\u0001\u001a\u0001\u001a\u0003\u001a\u0083"+
		"\b\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0005\u001a\u0088\b\u001a"+
		"\n\u001a\f\u001a\u008b\t\u001a\u0001\u001b\u0001\u001b\u0001\u001b\u0001"+
		"\u001b\u0001\u001c\u0001\u001c\u0000\u0000\u001d\u0001\u0000\u0003\u0000"+
		"\u0005\u0001\u0007\u0002\t\u0003\u000b\u0004\r\u0005\u000f\u0006\u0011"+
		"\u0007\u0013\b\u0015\t\u0017\n\u0019\u000b\u001b\f\u001d\r\u001f\u000e"+
		"!\u000f#\u0010%\u0011\'\u0012)\u0013+\u0014-\u0015/\u00161\u00173\u0018"+
		"5\u00197\u001a9\u001b\u0001\u0000\u0003\u0002\u0000AZaz\u0001\u000009"+
		"\u0003\u0000\t\n\r\r  \u0094\u0000\u0005\u0001\u0000\u0000\u0000\u0000"+
		"\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b"+
		"\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001"+
		"\u0000\u0000\u0000\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001"+
		"\u0000\u0000\u0000\u0000\u0015\u0001\u0000\u0000\u0000\u0000\u0017\u0001"+
		"\u0000\u0000\u0000\u0000\u0019\u0001\u0000\u0000\u0000\u0000\u001b\u0001"+
		"\u0000\u0000\u0000\u0000\u001d\u0001\u0000\u0000\u0000\u0000\u001f\u0001"+
		"\u0000\u0000\u0000\u0000!\u0001\u0000\u0000\u0000\u0000#\u0001\u0000\u0000"+
		"\u0000\u0000%\u0001\u0000\u0000\u0000\u0000\'\u0001\u0000\u0000\u0000"+
		"\u0000)\u0001\u0000\u0000\u0000\u0000+\u0001\u0000\u0000\u0000\u0000-"+
		"\u0001\u0000\u0000\u0000\u0000/\u0001\u0000\u0000\u0000\u00001\u0001\u0000"+
		"\u0000\u0000\u00003\u0001\u0000\u0000\u0000\u00005\u0001\u0000\u0000\u0000"+
		"\u00007\u0001\u0000\u0000\u0000\u00009\u0001\u0000\u0000\u0000\u0001;"+
		"\u0001\u0000\u0000\u0000\u0003=\u0001\u0000\u0000\u0000\u0005?\u0001\u0000"+
		"\u0000\u0000\u0007A\u0001\u0000\u0000\u0000\tC\u0001\u0000\u0000\u0000"+
		"\u000bE\u0001\u0000\u0000\u0000\rG\u0001\u0000\u0000\u0000\u000fI\u0001"+
		"\u0000\u0000\u0000\u0011K\u0001\u0000\u0000\u0000\u0013M\u0001\u0000\u0000"+
		"\u0000\u0015O\u0001\u0000\u0000\u0000\u0017Q\u0001\u0000\u0000\u0000\u0019"+
		"S\u0001\u0000\u0000\u0000\u001bV\u0001\u0000\u0000\u0000\u001dY\u0001"+
		"\u0000\u0000\u0000\u001f[\u0001\u0000\u0000\u0000!]\u0001\u0000\u0000"+
		"\u0000#`\u0001\u0000\u0000\u0000%b\u0001\u0000\u0000\u0000\'d\u0001\u0000"+
		"\u0000\u0000)g\u0001\u0000\u0000\u0000+k\u0001\u0000\u0000\u0000-o\u0001"+
		"\u0000\u0000\u0000/s\u0001\u0000\u0000\u00001y\u0001\u0000\u0000\u0000"+
		"3}\u0001\u0000\u0000\u00005\u0082\u0001\u0000\u0000\u00007\u008c\u0001"+
		"\u0000\u0000\u00009\u0090\u0001\u0000\u0000\u0000;<\u0007\u0000\u0000"+
		"\u0000<\u0002\u0001\u0000\u0000\u0000=>\u0007\u0001\u0000\u0000>\u0004"+
		"\u0001\u0000\u0000\u0000?@\u0005(\u0000\u0000@\u0006\u0001\u0000\u0000"+
		"\u0000AB\u0005)\u0000\u0000B\b\u0001\u0000\u0000\u0000CD\u0005{\u0000"+
		"\u0000D\n\u0001\u0000\u0000\u0000EF\u0005}\u0000\u0000F\f\u0001\u0000"+
		"\u0000\u0000GH\u0005;\u0000\u0000H\u000e\u0001\u0000\u0000\u0000IJ\u0005"+
		"+\u0000\u0000J\u0010\u0001\u0000\u0000\u0000KL\u0005-\u0000\u0000L\u0012"+
		"\u0001\u0000\u0000\u0000MN\u0005*\u0000\u0000N\u0014\u0001\u0000\u0000"+
		"\u0000OP\u0005/\u0000\u0000P\u0016\u0001\u0000\u0000\u0000QR\u0005%\u0000"+
		"\u0000R\u0018\u0001\u0000\u0000\u0000ST\u0005&\u0000\u0000TU\u0005&\u0000"+
		"\u0000U\u001a\u0001\u0000\u0000\u0000VW\u0005|\u0000\u0000WX\u0005|\u0000"+
		"\u0000X\u001c\u0001\u0000\u0000\u0000YZ\u0005^\u0000\u0000Z\u001e\u0001"+
		"\u0000\u0000\u0000[\\\u0005=\u0000\u0000\\ \u0001\u0000\u0000\u0000]^"+
		"\u0005=\u0000\u0000^_\u0005=\u0000\u0000_\"\u0001\u0000\u0000\u0000`a"+
		"\u0005>\u0000\u0000a$\u0001\u0000\u0000\u0000bc\u0005<\u0000\u0000c&\u0001"+
		"\u0000\u0000\u0000de\u0005<\u0000\u0000ef\u0005=\u0000\u0000f(\u0001\u0000"+
		"\u0000\u0000gh\u0005>\u0000\u0000hi\u0005=\u0000\u0000i*\u0001\u0000\u0000"+
		"\u0000jl\u0003\u0003\u0001\u0000kj\u0001\u0000\u0000\u0000lm\u0001\u0000"+
		"\u0000\u0000mk\u0001\u0000\u0000\u0000mn\u0001\u0000\u0000\u0000n,\u0001"+
		"\u0000\u0000\u0000op\u0005i\u0000\u0000pq\u0005n\u0000\u0000qr\u0005t"+
		"\u0000\u0000r.\u0001\u0000\u0000\u0000st\u0005w\u0000\u0000tu\u0005h\u0000"+
		"\u0000uv\u0005i\u0000\u0000vw\u0005l\u0000\u0000wx\u0005e\u0000\u0000"+
		"x0\u0001\u0000\u0000\u0000yz\u0005f\u0000\u0000z{\u0005o\u0000\u0000{"+
		"|\u0005r\u0000\u0000|2\u0001\u0000\u0000\u0000}~\u0005i\u0000\u0000~\u007f"+
		"\u0005f\u0000\u0000\u007f4\u0001\u0000\u0000\u0000\u0080\u0083\u0003\u0001"+
		"\u0000\u0000\u0081\u0083\u0005_\u0000\u0000\u0082\u0080\u0001\u0000\u0000"+
		"\u0000\u0082\u0081\u0001\u0000\u0000\u0000\u0083\u0089\u0001\u0000\u0000"+
		"\u0000\u0084\u0088\u0003\u0001\u0000\u0000\u0085\u0088\u0003\u0003\u0001"+
		"\u0000\u0086\u0088\u0005_\u0000\u0000\u0087\u0084\u0001\u0000\u0000\u0000"+
		"\u0087\u0085\u0001\u0000\u0000\u0000\u0087\u0086\u0001\u0000\u0000\u0000"+
		"\u0088\u008b\u0001\u0000\u0000\u0000\u0089\u0087\u0001\u0000\u0000\u0000"+
		"\u0089\u008a\u0001\u0000\u0000\u0000\u008a6\u0001\u0000\u0000\u0000\u008b"+
		"\u0089\u0001\u0000\u0000\u0000\u008c\u008d\u0007\u0002\u0000\u0000\u008d"+
		"\u008e\u0001\u0000\u0000\u0000\u008e\u008f\u0006\u001b\u0000\u0000\u008f"+
		"8\u0001\u0000\u0000\u0000\u0090\u0091\t\u0000\u0000\u0000\u0091:\u0001"+
		"\u0000\u0000\u0000\u0005\u0000m\u0082\u0087\u0089\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}