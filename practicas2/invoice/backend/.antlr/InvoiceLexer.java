// Generated from d:/Mis trabajos/6to semestre/Lenguajes y automatas II/salva/Lenguajes-y-Automatas-II/practicas2/invoice/backend/Invoice.g4 by ANTLR 4.13.1
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
		T__0=1, Y_CONJ=2, COMMA=3, KG=4, PIEZA=5, PIEZAS=6, DE=7, NUMBER=8, NOMBRE=9, 
		WORD=10, DOT=11, WS=12;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "Y_CONJ", "COMMA", "KG", "PIEZA", "PIEZAS", "DE", "NUMBER", "NOMBRE", 
			"WORD", "DOT", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'/'", "'y'", "','", "'kg'", "'pieza'", "'piezas'", "'de'", null, 
			null, null, "'.'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, "Y_CONJ", "COMMA", "KG", "PIEZA", "PIEZAS", "DE", "NUMBER", 
			"NOMBRE", "WORD", "DOT", "WS"
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
	public String getGrammarFileName() { return "Invoice.g4"; }

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
		"\u0004\u0000\fK\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0002"+
		"\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0007\u0004\u00074\b\u0007\u000b\u0007"+
		"\f\u00075\u0001\b\u0001\b\u0004\b:\b\b\u000b\b\f\b;\u0001\t\u0004\t?\b"+
		"\t\u000b\t\f\t@\u0001\n\u0001\n\u0001\u000b\u0004\u000bF\b\u000b\u000b"+
		"\u000b\f\u000bG\u0001\u000b\u0001\u000b\u0000\u0000\f\u0001\u0001\u0003"+
		"\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011"+
		"\t\u0013\n\u0015\u000b\u0017\f\u0001\u0000\u0005\u0001\u000009\u0006\u0000"+
		"AZ\u00c1\u00c1\u00c9\u00c9\u00cd\u00cd\u00d3\u00d3\u00da\u00da\b\u0000"+
		"az\u00d1\u00d1\u00e1\u00e1\u00e9\u00e9\u00ed\u00ed\u00f1\u00f1\u00f3\u00f3"+
		"\u00fa\u00fa\u000e\u0000AZaz\u00c1\u00c1\u00c9\u00c9\u00cd\u00cd\u00d1"+
		"\u00d1\u00d3\u00d3\u00da\u00da\u00e1\u00e1\u00e9\u00e9\u00ed\u00ed\u00f1"+
		"\u00f1\u00f3\u00f3\u00fa\u00fa\u0003\u0000\t\n\r\r  N\u0000\u0001\u0001"+
		"\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001"+
		"\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000"+
		"\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000"+
		"\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000\u0000"+
		"\u0000\u0000\u0013\u0001\u0000\u0000\u0000\u0000\u0015\u0001\u0000\u0000"+
		"\u0000\u0000\u0017\u0001\u0000\u0000\u0000\u0001\u0019\u0001\u0000\u0000"+
		"\u0000\u0003\u001b\u0001\u0000\u0000\u0000\u0005\u001d\u0001\u0000\u0000"+
		"\u0000\u0007\u001f\u0001\u0000\u0000\u0000\t\"\u0001\u0000\u0000\u0000"+
		"\u000b(\u0001\u0000\u0000\u0000\r/\u0001\u0000\u0000\u0000\u000f3\u0001"+
		"\u0000\u0000\u0000\u00117\u0001\u0000\u0000\u0000\u0013>\u0001\u0000\u0000"+
		"\u0000\u0015B\u0001\u0000\u0000\u0000\u0017E\u0001\u0000\u0000\u0000\u0019"+
		"\u001a\u0005/\u0000\u0000\u001a\u0002\u0001\u0000\u0000\u0000\u001b\u001c"+
		"\u0005y\u0000\u0000\u001c\u0004\u0001\u0000\u0000\u0000\u001d\u001e\u0005"+
		",\u0000\u0000\u001e\u0006\u0001\u0000\u0000\u0000\u001f \u0005k\u0000"+
		"\u0000 !\u0005g\u0000\u0000!\b\u0001\u0000\u0000\u0000\"#\u0005p\u0000"+
		"\u0000#$\u0005i\u0000\u0000$%\u0005e\u0000\u0000%&\u0005z\u0000\u0000"+
		"&\'\u0005a\u0000\u0000\'\n\u0001\u0000\u0000\u0000()\u0005p\u0000\u0000"+
		")*\u0005i\u0000\u0000*+\u0005e\u0000\u0000+,\u0005z\u0000\u0000,-\u0005"+
		"a\u0000\u0000-.\u0005s\u0000\u0000.\f\u0001\u0000\u0000\u0000/0\u0005"+
		"d\u0000\u000001\u0005e\u0000\u00001\u000e\u0001\u0000\u0000\u000024\u0007"+
		"\u0000\u0000\u000032\u0001\u0000\u0000\u000045\u0001\u0000\u0000\u0000"+
		"53\u0001\u0000\u0000\u000056\u0001\u0000\u0000\u00006\u0010\u0001\u0000"+
		"\u0000\u000079\u0007\u0001\u0000\u00008:\u0007\u0002\u0000\u000098\u0001"+
		"\u0000\u0000\u0000:;\u0001\u0000\u0000\u0000;9\u0001\u0000\u0000\u0000"+
		";<\u0001\u0000\u0000\u0000<\u0012\u0001\u0000\u0000\u0000=?\u0007\u0003"+
		"\u0000\u0000>=\u0001\u0000\u0000\u0000?@\u0001\u0000\u0000\u0000@>\u0001"+
		"\u0000\u0000\u0000@A\u0001\u0000\u0000\u0000A\u0014\u0001\u0000\u0000"+
		"\u0000BC\u0005.\u0000\u0000C\u0016\u0001\u0000\u0000\u0000DF\u0007\u0004"+
		"\u0000\u0000ED\u0001\u0000\u0000\u0000FG\u0001\u0000\u0000\u0000GE\u0001"+
		"\u0000\u0000\u0000GH\u0001\u0000\u0000\u0000HI\u0001\u0000\u0000\u0000"+
		"IJ\u0006\u000b\u0000\u0000J\u0018\u0001\u0000\u0000\u0000\u0005\u0000"+
		"5;@G\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}