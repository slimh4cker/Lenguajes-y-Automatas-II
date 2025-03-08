// Generated from d:/Mis trabajos/6to semestre/Lenguajes y automatas II/Lenguajes-y-Automatas-II/practicas2/words_analyzer/backend/Words.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class InvoiceLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, NOMBRE=2, KG=3, PIEZA=4, PIEZAS=5, COLON=6, WORD=7, PUNCTUATION=8, 
		NUMBER=9, WHITESPACE=10, NEWLINE=11;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "NOMBRE", "KG", "PIEZA", "PIEZAS", "COLON", "WORD", "PUNCTUATION", 
			"NUMBER", "WHITESPACE", "NEWLINE"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'/'", null, "'kg'", "'pieza'", "'piezas'", "':'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, "NOMBRE", "KG", "PIEZA", "PIEZAS", "COLON", "WORD", "PUNCTUATION", 
			"NUMBER", "WHITESPACE", "NEWLINE"
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


	public InvoiceLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Words.g4"; }

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
		"\u0004\u0000\u000bI\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0001\u0000"+
		"\u0001\u0000\u0001\u0001\u0001\u0001\u0004\u0001\u001c\b\u0001\u000b\u0001"+
		"\f\u0001\u001d\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005"+
		"\u0001\u0005\u0001\u0006\u0004\u00063\b\u0006\u000b\u0006\f\u00064\u0001"+
		"\u0007\u0001\u0007\u0001\b\u0004\b:\b\b\u000b\b\f\b;\u0001\t\u0004\t?"+
		"\b\t\u000b\t\f\t@\u0001\n\u0003\nD\b\n\u0001\n\u0001\n\u0003\nH\b\n\u0000"+
		"\u0000\u000b\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b"+
		"\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b\u0001\u0000\u0006\u0006"+
		"\u0000AZ\u00c1\u00c1\u00c9\u00c9\u00cd\u00cd\u00d3\u00d3\u00da\u00da\u0006"+
		"\u0000az\u00e1\u00e1\u00e9\u00e9\u00ed\u00ed\u00f3\u00f3\u00fa\u00fa\r"+
		"\u000009AZaz\u00c1\u00c1\u00c9\u00c9\u00cd\u00cd\u00d3\u00d3\u00da\u00da"+
		"\u00e1\u00e1\u00e9\u00e9\u00ed\u00ed\u00f3\u00f3\u00fa\u00fa\u0007\u0000"+
		"!!,.;;??\u00a1\u00a1\u00bf\u00bf\u2014\u2014\u0001\u000009\u0002\u0000"+
		"\t\t  N\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000"+
		"\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000"+
		"\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000"+
		"\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000"+
		"\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000\u0000"+
		"\u0015\u0001\u0000\u0000\u0000\u0001\u0017\u0001\u0000\u0000\u0000\u0003"+
		"\u0019\u0001\u0000\u0000\u0000\u0005\u001f\u0001\u0000\u0000\u0000\u0007"+
		"\"\u0001\u0000\u0000\u0000\t(\u0001\u0000\u0000\u0000\u000b/\u0001\u0000"+
		"\u0000\u0000\r2\u0001\u0000\u0000\u0000\u000f6\u0001\u0000\u0000\u0000"+
		"\u00119\u0001\u0000\u0000\u0000\u0013>\u0001\u0000\u0000\u0000\u0015G"+
		"\u0001\u0000\u0000\u0000\u0017\u0018\u0005/\u0000\u0000\u0018\u0002\u0001"+
		"\u0000\u0000\u0000\u0019\u001b\u0007\u0000\u0000\u0000\u001a\u001c\u0007"+
		"\u0001\u0000\u0000\u001b\u001a\u0001\u0000\u0000\u0000\u001c\u001d\u0001"+
		"\u0000\u0000\u0000\u001d\u001b\u0001\u0000\u0000\u0000\u001d\u001e\u0001"+
		"\u0000\u0000\u0000\u001e\u0004\u0001\u0000\u0000\u0000\u001f \u0005k\u0000"+
		"\u0000 !\u0005g\u0000\u0000!\u0006\u0001\u0000\u0000\u0000\"#\u0005p\u0000"+
		"\u0000#$\u0005i\u0000\u0000$%\u0005e\u0000\u0000%&\u0005z\u0000\u0000"+
		"&\'\u0005a\u0000\u0000\'\b\u0001\u0000\u0000\u0000()\u0005p\u0000\u0000"+
		")*\u0005i\u0000\u0000*+\u0005e\u0000\u0000+,\u0005z\u0000\u0000,-\u0005"+
		"a\u0000\u0000-.\u0005s\u0000\u0000.\n\u0001\u0000\u0000\u0000/0\u0005"+
		":\u0000\u00000\f\u0001\u0000\u0000\u000013\u0007\u0002\u0000\u000021\u0001"+
		"\u0000\u0000\u000034\u0001\u0000\u0000\u000042\u0001\u0000\u0000\u0000"+
		"45\u0001\u0000\u0000\u00005\u000e\u0001\u0000\u0000\u000067\u0007\u0003"+
		"\u0000\u00007\u0010\u0001\u0000\u0000\u00008:\u0007\u0004\u0000\u0000"+
		"98\u0001\u0000\u0000\u0000:;\u0001\u0000\u0000\u0000;9\u0001\u0000\u0000"+
		"\u0000;<\u0001\u0000\u0000\u0000<\u0012\u0001\u0000\u0000\u0000=?\u0007"+
		"\u0005\u0000\u0000>=\u0001\u0000\u0000\u0000?@\u0001\u0000\u0000\u0000"+
		"@>\u0001\u0000\u0000\u0000@A\u0001\u0000\u0000\u0000A\u0014\u0001\u0000"+
		"\u0000\u0000BD\u0005\r\u0000\u0000CB\u0001\u0000\u0000\u0000CD\u0001\u0000"+
		"\u0000\u0000DE\u0001\u0000\u0000\u0000EH\u0005\n\u0000\u0000FH\u0005\r"+
		"\u0000\u0000GC\u0001\u0000\u0000\u0000GF\u0001\u0000\u0000\u0000H\u0016"+
		"\u0001\u0000\u0000\u0000\u0007\u0000\u001d4;@CG\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}