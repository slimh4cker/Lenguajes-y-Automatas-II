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
public class WordsLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		MONTH=1, COLON=2, WORD=3, PUNCTUATION=4, NUMBER=5, WHITESPACE=6, NEWLINE=7;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"MONTH", "COLON", "WORD", "PUNCTUATION", "NUMBER", "WHITESPACE", "NEWLINE"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, "':'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "MONTH", "COLON", "WORD", "PUNCTUATION", "NUMBER", "WHITESPACE", 
			"NEWLINE"
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


	public WordsLexer(CharStream input) {
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
		"\u0004\u0000\u0007x\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0003\u0000]\b\u0000"+
		"\u0001\u0001\u0001\u0001\u0001\u0002\u0004\u0002b\b\u0002\u000b\u0002"+
		"\f\u0002c\u0001\u0003\u0001\u0003\u0001\u0004\u0004\u0004i\b\u0004\u000b"+
		"\u0004\f\u0004j\u0001\u0005\u0004\u0005n\b\u0005\u000b\u0005\f\u0005o"+
		"\u0001\u0006\u0003\u0006s\b\u0006\u0001\u0006\u0001\u0006\u0003\u0006"+
		"w\b\u0006\u0000\u0000\u0007\u0001\u0001\u0003\u0002\u0005\u0003\u0007"+
		"\u0004\t\u0005\u000b\u0006\r\u0007\u0001\u0000\u0004\u000e\u0000AZaz\u00c1"+
		"\u00c1\u00c9\u00c9\u00cd\u00cd\u00d1\u00d1\u00d3\u00d3\u00da\u00da\u00e1"+
		"\u00e1\u00e9\u00e9\u00ed\u00ed\u00f1\u00f1\u00f3\u00f3\u00fa\u00fa\u0007"+
		"\u0000!!,.;;??\u00a1\u00a1\u00bf\u00bf\u2014\u2014\u0001\u000009\u0002"+
		"\u0000\t\t  \u0087\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001"+
		"\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001"+
		"\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000"+
		"\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0001\\\u0001\u0000\u0000"+
		"\u0000\u0003^\u0001\u0000\u0000\u0000\u0005a\u0001\u0000\u0000\u0000\u0007"+
		"e\u0001\u0000\u0000\u0000\th\u0001\u0000\u0000\u0000\u000bm\u0001\u0000"+
		"\u0000\u0000\rv\u0001\u0000\u0000\u0000\u000f\u0010\u0005E\u0000\u0000"+
		"\u0010\u0011\u0005n\u0000\u0000\u0011\u0012\u0005e\u0000\u0000\u0012\u0013"+
		"\u0005r\u0000\u0000\u0013]\u0005o\u0000\u0000\u0014\u0015\u0005F\u0000"+
		"\u0000\u0015\u0016\u0005e\u0000\u0000\u0016\u0017\u0005b\u0000\u0000\u0017"+
		"\u0018\u0005r\u0000\u0000\u0018\u0019\u0005e\u0000\u0000\u0019\u001a\u0005"+
		"r\u0000\u0000\u001a]\u0005o\u0000\u0000\u001b\u001c\u0005M\u0000\u0000"+
		"\u001c\u001d\u0005a\u0000\u0000\u001d\u001e\u0005r\u0000\u0000\u001e\u001f"+
		"\u0005z\u0000\u0000\u001f]\u0005o\u0000\u0000 !\u0005A\u0000\u0000!\""+
		"\u0005b\u0000\u0000\"#\u0005r\u0000\u0000#$\u0005i\u0000\u0000$]\u0005"+
		"l\u0000\u0000%&\u0005M\u0000\u0000&\'\u0005a\u0000\u0000\'(\u0005y\u0000"+
		"\u0000(]\u0005o\u0000\u0000)*\u0005J\u0000\u0000*+\u0005u\u0000\u0000"+
		"+,\u0005n\u0000\u0000,-\u0005i\u0000\u0000-]\u0005o\u0000\u0000./\u0005"+
		"J\u0000\u0000/0\u0005u\u0000\u000001\u0005l\u0000\u000012\u0005i\u0000"+
		"\u00002]\u0005o\u0000\u000034\u0005A\u0000\u000045\u0005g\u0000\u0000"+
		"56\u0005o\u0000\u000067\u0005s\u0000\u000078\u0005t\u0000\u00008]\u0005"+
		"o\u0000\u00009:\u0005S\u0000\u0000:;\u0005e\u0000\u0000;<\u0005p\u0000"+
		"\u0000<=\u0005t\u0000\u0000=>\u0005i\u0000\u0000>?\u0005e\u0000\u0000"+
		"?@\u0005m\u0000\u0000@A\u0005b\u0000\u0000AB\u0005r\u0000\u0000B]\u0005"+
		"e\u0000\u0000CD\u0005O\u0000\u0000DE\u0005c\u0000\u0000EF\u0005t\u0000"+
		"\u0000FG\u0005u\u0000\u0000GH\u0005b\u0000\u0000HI\u0005r\u0000\u0000"+
		"I]\u0005e\u0000\u0000JK\u0005N\u0000\u0000KL\u0005o\u0000\u0000LM\u0005"+
		"v\u0000\u0000MN\u0005i\u0000\u0000NO\u0005e\u0000\u0000OP\u0005m\u0000"+
		"\u0000PQ\u0005b\u0000\u0000QR\u0005r\u0000\u0000R]\u0005e\u0000\u0000"+
		"ST\u0005D\u0000\u0000TU\u0005i\u0000\u0000UV\u0005c\u0000\u0000VW\u0005"+
		"i\u0000\u0000WX\u0005e\u0000\u0000XY\u0005m\u0000\u0000YZ\u0005b\u0000"+
		"\u0000Z[\u0005r\u0000\u0000[]\u0005e\u0000\u0000\\\u000f\u0001\u0000\u0000"+
		"\u0000\\\u0014\u0001\u0000\u0000\u0000\\\u001b\u0001\u0000\u0000\u0000"+
		"\\ \u0001\u0000\u0000\u0000\\%\u0001\u0000\u0000\u0000\\)\u0001\u0000"+
		"\u0000\u0000\\.\u0001\u0000\u0000\u0000\\3\u0001\u0000\u0000\u0000\\9"+
		"\u0001\u0000\u0000\u0000\\C\u0001\u0000\u0000\u0000\\J\u0001\u0000\u0000"+
		"\u0000\\S\u0001\u0000\u0000\u0000]\u0002\u0001\u0000\u0000\u0000^_\u0005"+
		":\u0000\u0000_\u0004\u0001\u0000\u0000\u0000`b\u0007\u0000\u0000\u0000"+
		"a`\u0001\u0000\u0000\u0000bc\u0001\u0000\u0000\u0000ca\u0001\u0000\u0000"+
		"\u0000cd\u0001\u0000\u0000\u0000d\u0006\u0001\u0000\u0000\u0000ef\u0007"+
		"\u0001\u0000\u0000f\b\u0001\u0000\u0000\u0000gi\u0007\u0002\u0000\u0000"+
		"hg\u0001\u0000\u0000\u0000ij\u0001\u0000\u0000\u0000jh\u0001\u0000\u0000"+
		"\u0000jk\u0001\u0000\u0000\u0000k\n\u0001\u0000\u0000\u0000ln\u0007\u0003"+
		"\u0000\u0000ml\u0001\u0000\u0000\u0000no\u0001\u0000\u0000\u0000om\u0001"+
		"\u0000\u0000\u0000op\u0001\u0000\u0000\u0000p\f\u0001\u0000\u0000\u0000"+
		"qs\u0005\r\u0000\u0000rq\u0001\u0000\u0000\u0000rs\u0001\u0000\u0000\u0000"+
		"st\u0001\u0000\u0000\u0000tw\u0005\n\u0000\u0000uw\u0005\r\u0000\u0000"+
		"vr\u0001\u0000\u0000\u0000vu\u0001\u0000\u0000\u0000w\u000e\u0001\u0000"+
		"\u0000\u0000\u0007\u0000\\cjorv\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}