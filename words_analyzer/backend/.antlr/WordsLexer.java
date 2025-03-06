// Generated from c:/Users/monte/OneDrive/Documentos/proyecto/Lenguajes-y-Automatas-II/words_analyzer/backend/Words.g4 by ANTLR 4.13.1
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
		MONTH=1, COLON=2, FRUIT_SINGULAR=3, FRUIT_PLURAL=4, WORD=5, NUMBER=6, 
		PUNCTUATION=7, WHITESPACE=8, NEWLINE=9, WS=10;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"MONTH", "COLON", "FRUIT_SINGULAR", "FRUIT_PLURAL", "WORD", "NUMBER", 
			"PUNCTUATION", "WHITESPACE", "NEWLINE", "WS"
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
			null, "MONTH", "COLON", "FRUIT_SINGULAR", "FRUIT_PLURAL", "WORD", "NUMBER", 
			"PUNCTUATION", "WHITESPACE", "NEWLINE", "WS"
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
		"\u0004\u0000\n\u0178\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0003\u0000c\b\u0000\u0001\u0001\u0001"+
		"\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0003\u0002\u00d4\b\u0002\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0003\u0003\u0158\b\u0003\u0001\u0004\u0004\u0004\u015b"+
		"\b\u0004\u000b\u0004\f\u0004\u015c\u0001\u0005\u0004\u0005\u0160\b\u0005"+
		"\u000b\u0005\f\u0005\u0161\u0001\u0006\u0001\u0006\u0001\u0007\u0004\u0007"+
		"\u0167\b\u0007\u000b\u0007\f\u0007\u0168\u0001\b\u0003\b\u016c\b\b\u0001"+
		"\b\u0001\b\u0003\b\u0170\b\b\u0001\t\u0004\t\u0173\b\t\u000b\t\f\t\u0174"+
		"\u0001\t\u0001\t\u0000\u0000\n\u0001\u0001\u0003\u0002\u0005\u0003\u0007"+
		"\u0004\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0001\u0000"+
		"\u0005\u000e\u0000AZaz\u00c1\u00c1\u00c9\u00c9\u00cd\u00cd\u00d1\u00d1"+
		"\u00d3\u00d3\u00da\u00da\u00e1\u00e1\u00e9\u00e9\u00ed\u00ed\u00f1\u00f1"+
		"\u00f3\u00f3\u00fa\u00fa\u0001\u000009\u0007\u0000!!,,..;;??\u00a1\u00a1"+
		"\u00bf\u00bf\u0002\u0000\t\t  \u0003\u0000\t\n\r\r  \u01ac\u0000\u0001"+
		"\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005"+
		"\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001"+
		"\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000"+
		"\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000"+
		"\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000\u0001b\u0001\u0000\u0000"+
		"\u0000\u0003d\u0001\u0000\u0000\u0000\u0005\u00d3\u0001\u0000\u0000\u0000"+
		"\u0007\u0157\u0001\u0000\u0000\u0000\t\u015a\u0001\u0000\u0000\u0000\u000b"+
		"\u015f\u0001\u0000\u0000\u0000\r\u0163\u0001\u0000\u0000\u0000\u000f\u0166"+
		"\u0001\u0000\u0000\u0000\u0011\u016f\u0001\u0000\u0000\u0000\u0013\u0172"+
		"\u0001\u0000\u0000\u0000\u0015\u0016\u0005E\u0000\u0000\u0016\u0017\u0005"+
		"n\u0000\u0000\u0017\u0018\u0005e\u0000\u0000\u0018\u0019\u0005r\u0000"+
		"\u0000\u0019c\u0005o\u0000\u0000\u001a\u001b\u0005F\u0000\u0000\u001b"+
		"\u001c\u0005e\u0000\u0000\u001c\u001d\u0005b\u0000\u0000\u001d\u001e\u0005"+
		"r\u0000\u0000\u001e\u001f\u0005e\u0000\u0000\u001f \u0005r\u0000\u0000"+
		" c\u0005o\u0000\u0000!\"\u0005M\u0000\u0000\"#\u0005a\u0000\u0000#$\u0005"+
		"r\u0000\u0000$%\u0005z\u0000\u0000%c\u0005o\u0000\u0000&\'\u0005A\u0000"+
		"\u0000\'(\u0005b\u0000\u0000()\u0005r\u0000\u0000)*\u0005i\u0000\u0000"+
		"*c\u0005l\u0000\u0000+,\u0005M\u0000\u0000,-\u0005a\u0000\u0000-.\u0005"+
		"y\u0000\u0000.c\u0005o\u0000\u0000/0\u0005J\u0000\u000001\u0005u\u0000"+
		"\u000012\u0005n\u0000\u000023\u0005i\u0000\u00003c\u0005o\u0000\u0000"+
		"45\u0005J\u0000\u000056\u0005u\u0000\u000067\u0005l\u0000\u000078\u0005"+
		"i\u0000\u00008c\u0005o\u0000\u00009:\u0005A\u0000\u0000:;\u0005g\u0000"+
		"\u0000;<\u0005o\u0000\u0000<=\u0005s\u0000\u0000=>\u0005t\u0000\u0000"+
		">c\u0005o\u0000\u0000?@\u0005S\u0000\u0000@A\u0005e\u0000\u0000AB\u0005"+
		"p\u0000\u0000BC\u0005t\u0000\u0000CD\u0005i\u0000\u0000DE\u0005e\u0000"+
		"\u0000EF\u0005m\u0000\u0000FG\u0005b\u0000\u0000GH\u0005r\u0000\u0000"+
		"Hc\u0005e\u0000\u0000IJ\u0005O\u0000\u0000JK\u0005c\u0000\u0000KL\u0005"+
		"t\u0000\u0000LM\u0005u\u0000\u0000MN\u0005b\u0000\u0000NO\u0005r\u0000"+
		"\u0000Oc\u0005e\u0000\u0000PQ\u0005N\u0000\u0000QR\u0005o\u0000\u0000"+
		"RS\u0005v\u0000\u0000ST\u0005i\u0000\u0000TU\u0005e\u0000\u0000UV\u0005"+
		"m\u0000\u0000VW\u0005b\u0000\u0000WX\u0005r\u0000\u0000Xc\u0005e\u0000"+
		"\u0000YZ\u0005D\u0000\u0000Z[\u0005i\u0000\u0000[\\\u0005c\u0000\u0000"+
		"\\]\u0005i\u0000\u0000]^\u0005e\u0000\u0000^_\u0005m\u0000\u0000_`\u0005"+
		"b\u0000\u0000`a\u0005r\u0000\u0000ac\u0005e\u0000\u0000b\u0015\u0001\u0000"+
		"\u0000\u0000b\u001a\u0001\u0000\u0000\u0000b!\u0001\u0000\u0000\u0000"+
		"b&\u0001\u0000\u0000\u0000b+\u0001\u0000\u0000\u0000b/\u0001\u0000\u0000"+
		"\u0000b4\u0001\u0000\u0000\u0000b9\u0001\u0000\u0000\u0000b?\u0001\u0000"+
		"\u0000\u0000bI\u0001\u0000\u0000\u0000bP\u0001\u0000\u0000\u0000bY\u0001"+
		"\u0000\u0000\u0000c\u0002\u0001\u0000\u0000\u0000de\u0005:\u0000\u0000"+
		"e\u0004\u0001\u0000\u0000\u0000fg\u0005N\u0000\u0000gh\u0005a\u0000\u0000"+
		"hi\u0005r\u0000\u0000ij\u0005a\u0000\u0000jk\u0005n\u0000\u0000kl\u0005"+
		"j\u0000\u0000l\u00d4\u0005a\u0000\u0000mn\u0005M\u0000\u0000no\u0005a"+
		"\u0000\u0000op\u0005n\u0000\u0000pq\u0005d\u0000\u0000qr\u0005a\u0000"+
		"\u0000rs\u0005r\u0000\u0000st\u0005i\u0000\u0000tu\u0005n\u0000\u0000"+
		"u\u00d4\u0005a\u0000\u0000vw\u0005T\u0000\u0000wx\u0005o\u0000\u0000x"+
		"y\u0005r\u0000\u0000yz\u0005o\u0000\u0000z{\u0005n\u0000\u0000{|\u0005"+
		"j\u0000\u0000|\u00d4\u0005a\u0000\u0000}~\u0005F\u0000\u0000~\u007f\u0005"+
		"r\u0000\u0000\u007f\u0080\u0005e\u0000\u0000\u0080\u0081\u0005s\u0000"+
		"\u0000\u0081\u00d4\u0005a\u0000\u0000\u0082\u0083\u0005G\u0000\u0000\u0083"+
		"\u0084\u0005u\u0000\u0000\u0084\u0085\u0005a\u0000\u0000\u0085\u0086\u0005"+
		"y\u0000\u0000\u0086\u0087\u0005a\u0000\u0000\u0087\u0088\u0005b\u0000"+
		"\u0000\u0088\u00d4\u0005a\u0000\u0000\u0089\u008a\u0005L\u0000\u0000\u008a"+
		"\u008b\u0005i\u0000\u0000\u008b\u008c\u0005m\u0000\u0000\u008c\u008d\u0005"+
		"\u00f3\u0000\u0000\u008d\u00d4\u0005n\u0000\u0000\u008e\u008f\u0005P\u0000"+
		"\u0000\u008f\u0090\u0005i\u0000\u0000\u0090\u0091\u0005\u00f1\u0000\u0000"+
		"\u0091\u00d4\u0005a\u0000\u0000\u0092\u0093\u0005M\u0000\u0000\u0093\u0094"+
		"\u0005a\u0000\u0000\u0094\u0095\u0005n\u0000\u0000\u0095\u0096\u0005g"+
		"\u0000\u0000\u0096\u00d4\u0005o\u0000\u0000\u0097\u0098\u0005P\u0000\u0000"+
		"\u0098\u0099\u0005a\u0000\u0000\u0099\u009a\u0005p\u0000\u0000\u009a\u009b"+
		"\u0005a\u0000\u0000\u009b\u009c\u0005y\u0000\u0000\u009c\u00d4\u0005a"+
		"\u0000\u0000\u009d\u009e\u0005M\u0000\u0000\u009e\u009f\u0005e\u0000\u0000"+
		"\u009f\u00a0\u0005l\u0000\u0000\u00a0\u00a1\u0005\u00f3\u0000\u0000\u00a1"+
		"\u00d4\u0005n\u0000\u0000\u00a2\u00a3\u0005S\u0000\u0000\u00a3\u00a4\u0005"+
		"a\u0000\u0000\u00a4\u00a5\u0005n\u0000\u0000\u00a5\u00a6\u0005d\u0000"+
		"\u0000\u00a6\u00a7\u0005\u00ed\u0000\u0000\u00a7\u00d4\u0005a\u0000\u0000"+
		"\u00a8\u00a9\u0005C\u0000\u0000\u00a9\u00aa\u0005i\u0000\u0000\u00aa\u00ab"+
		"\u0005r\u0000\u0000\u00ab\u00ac\u0005u\u0000\u0000\u00ac\u00ad\u0005e"+
		"\u0000\u0000\u00ad\u00ae\u0005l\u0000\u0000\u00ae\u00d4\u0005a\u0000\u0000"+
		"\u00af\u00b0\u0005D\u0000\u0000\u00b0\u00b1\u0005u\u0000\u0000\u00b1\u00b2"+
		"\u0005r\u0000\u0000\u00b2\u00b3\u0005a\u0000\u0000\u00b3\u00b4\u0005z"+
		"\u0000\u0000\u00b4\u00b5\u0005n\u0000\u0000\u00b5\u00d4\u0005o\u0000\u0000"+
		"\u00b6\u00b7\u0005H\u0000\u0000\u00b7\u00b8\u0005i\u0000\u0000\u00b8\u00b9"+
		"\u0005g\u0000\u0000\u00b9\u00d4\u0005o\u0000\u0000\u00ba\u00bb\u0005P"+
		"\u0000\u0000\u00bb\u00bc\u0005e\u0000\u0000\u00bc\u00bd\u0005r\u0000\u0000"+
		"\u00bd\u00d4\u0005a\u0000\u0000\u00be\u00bf\u0005T\u0000\u0000\u00bf\u00c0"+
		"\u0005u\u0000\u0000\u00c0\u00c1\u0005n\u0000\u0000\u00c1\u00d4\u0005a"+
		"\u0000\u0000\u00c2\u00c3\u0005M\u0000\u0000\u00c3\u00c4\u0005a\u0000\u0000"+
		"\u00c4\u00c5\u0005n\u0000\u0000\u00c5\u00c6\u0005z\u0000\u0000\u00c6\u00c7"+
		"\u0005a\u0000\u0000\u00c7\u00c8\u0005n\u0000\u0000\u00c8\u00d4\u0005a"+
		"\u0000\u0000\u00c9\u00ca\u0005U\u0000\u0000\u00ca\u00cb\u0005v\u0000\u0000"+
		"\u00cb\u00d4\u0005a\u0000\u0000\u00cc\u00cd\u0005G\u0000\u0000\u00cd\u00ce"+
		"\u0005r\u0000\u0000\u00ce\u00cf\u0005a\u0000\u0000\u00cf\u00d0\u0005n"+
		"\u0000\u0000\u00d0\u00d1\u0005a\u0000\u0000\u00d1\u00d2\u0005d\u0000\u0000"+
		"\u00d2\u00d4\u0005a\u0000\u0000\u00d3f\u0001\u0000\u0000\u0000\u00d3m"+
		"\u0001\u0000\u0000\u0000\u00d3v\u0001\u0000\u0000\u0000\u00d3}\u0001\u0000"+
		"\u0000\u0000\u00d3\u0082\u0001\u0000\u0000\u0000\u00d3\u0089\u0001\u0000"+
		"\u0000\u0000\u00d3\u008e\u0001\u0000\u0000\u0000\u00d3\u0092\u0001\u0000"+
		"\u0000\u0000\u00d3\u0097\u0001\u0000\u0000\u0000\u00d3\u009d\u0001\u0000"+
		"\u0000\u0000\u00d3\u00a2\u0001\u0000\u0000\u0000\u00d3\u00a8\u0001\u0000"+
		"\u0000\u0000\u00d3\u00af\u0001\u0000\u0000\u0000\u00d3\u00b6\u0001\u0000"+
		"\u0000\u0000\u00d3\u00ba\u0001\u0000\u0000\u0000\u00d3\u00be\u0001\u0000"+
		"\u0000\u0000\u00d3\u00c2\u0001\u0000\u0000\u0000\u00d3\u00c9\u0001\u0000"+
		"\u0000\u0000\u00d3\u00cc\u0001\u0000\u0000\u0000\u00d4\u0006\u0001\u0000"+
		"\u0000\u0000\u00d5\u00d6\u0005N\u0000\u0000\u00d6\u00d7\u0005a\u0000\u0000"+
		"\u00d7\u00d8\u0005r\u0000\u0000\u00d8\u00d9\u0005a\u0000\u0000\u00d9\u00da"+
		"\u0005n\u0000\u0000\u00da\u00db\u0005j\u0000\u0000\u00db\u00dc\u0005a"+
		"\u0000\u0000\u00dc\u0158\u0005s\u0000\u0000\u00dd\u00de\u0005M\u0000\u0000"+
		"\u00de\u00df\u0005a\u0000\u0000\u00df\u00e0\u0005n\u0000\u0000\u00e0\u00e1"+
		"\u0005d\u0000\u0000\u00e1\u00e2\u0005a\u0000\u0000\u00e2\u00e3\u0005r"+
		"\u0000\u0000\u00e3\u00e4\u0005i\u0000\u0000\u00e4\u00e5\u0005n\u0000\u0000"+
		"\u00e5\u00e6\u0005a\u0000\u0000\u00e6\u0158\u0005s\u0000\u0000\u00e7\u00e8"+
		"\u0005T\u0000\u0000\u00e8\u00e9\u0005o\u0000\u0000\u00e9\u00ea\u0005r"+
		"\u0000\u0000\u00ea\u00eb\u0005o\u0000\u0000\u00eb\u00ec\u0005n\u0000\u0000"+
		"\u00ec\u00ed\u0005j\u0000\u0000\u00ed\u00ee\u0005a\u0000\u0000\u00ee\u0158"+
		"\u0005s\u0000\u0000\u00ef\u00f0\u0005F\u0000\u0000\u00f0\u00f1\u0005r"+
		"\u0000\u0000\u00f1\u00f2\u0005e\u0000\u0000\u00f2\u00f3\u0005s\u0000\u0000"+
		"\u00f3\u00f4\u0005a\u0000\u0000\u00f4\u0158\u0005s\u0000\u0000\u00f5\u00f6"+
		"\u0005G\u0000\u0000\u00f6\u00f7\u0005u\u0000\u0000\u00f7\u00f8\u0005a"+
		"\u0000\u0000\u00f8\u00f9\u0005y\u0000\u0000\u00f9\u00fa\u0005a\u0000\u0000"+
		"\u00fa\u00fb\u0005b\u0000\u0000\u00fb\u00fc\u0005a\u0000\u0000\u00fc\u0158"+
		"\u0005s\u0000\u0000\u00fd\u00fe\u0005L\u0000\u0000\u00fe\u00ff\u0005i"+
		"\u0000\u0000\u00ff\u0100\u0005m\u0000\u0000\u0100\u0101\u0005o\u0000\u0000"+
		"\u0101\u0102\u0005n\u0000\u0000\u0102\u0103\u0005e\u0000\u0000\u0103\u0158"+
		"\u0005s\u0000\u0000\u0104\u0105\u0005P\u0000\u0000\u0105\u0106\u0005i"+
		"\u0000\u0000\u0106\u0107\u0005\u00f1\u0000\u0000\u0107\u0108\u0005a\u0000"+
		"\u0000\u0108\u0158\u0005s\u0000\u0000\u0109\u010a\u0005M\u0000\u0000\u010a"+
		"\u010b\u0005a\u0000\u0000\u010b\u010c\u0005n\u0000\u0000\u010c\u010d\u0005"+
		"g\u0000\u0000\u010d\u010e\u0005o\u0000\u0000\u010e\u0158\u0005s\u0000"+
		"\u0000\u010f\u0110\u0005P\u0000\u0000\u0110\u0111\u0005a\u0000\u0000\u0111"+
		"\u0112\u0005p\u0000\u0000\u0112\u0113\u0005a\u0000\u0000\u0113\u0114\u0005"+
		"y\u0000\u0000\u0114\u0115\u0005a\u0000\u0000\u0115\u0158\u0005s\u0000"+
		"\u0000\u0116\u0117\u0005M\u0000\u0000\u0117\u0118\u0005e\u0000\u0000\u0118"+
		"\u0119\u0005l\u0000\u0000\u0119\u011a\u0005o\u0000\u0000\u011a\u011b\u0005"+
		"n\u0000\u0000\u011b\u011c\u0005e\u0000\u0000\u011c\u0158\u0005s\u0000"+
		"\u0000\u011d\u011e\u0005S\u0000\u0000\u011e\u011f\u0005a\u0000\u0000\u011f"+
		"\u0120\u0005n\u0000\u0000\u0120\u0121\u0005d\u0000\u0000\u0121\u0122\u0005"+
		"\u00ed\u0000\u0000\u0122\u0123\u0005a\u0000\u0000\u0123\u0158\u0005s\u0000"+
		"\u0000\u0124\u0125\u0005C\u0000\u0000\u0125\u0126\u0005i\u0000\u0000\u0126"+
		"\u0127\u0005r\u0000\u0000\u0127\u0128\u0005u\u0000\u0000\u0128\u0129\u0005"+
		"e\u0000\u0000\u0129\u012a\u0005l\u0000\u0000\u012a\u012b\u0005a\u0000"+
		"\u0000\u012b\u0158\u0005s\u0000\u0000\u012c\u012d\u0005D\u0000\u0000\u012d"+
		"\u012e\u0005u\u0000\u0000\u012e\u012f\u0005r\u0000\u0000\u012f\u0130\u0005"+
		"a\u0000\u0000\u0130\u0131\u0005z\u0000\u0000\u0131\u0132\u0005n\u0000"+
		"\u0000\u0132\u0133\u0005o\u0000\u0000\u0133\u0158\u0005s\u0000\u0000\u0134"+
		"\u0135\u0005H\u0000\u0000\u0135\u0136\u0005i\u0000\u0000\u0136\u0137\u0005"+
		"g\u0000\u0000\u0137\u0138\u0005o\u0000\u0000\u0138\u0158\u0005s\u0000"+
		"\u0000\u0139\u013a\u0005P\u0000\u0000\u013a\u013b\u0005e\u0000\u0000\u013b"+
		"\u013c\u0005r\u0000\u0000\u013c\u013d\u0005a\u0000\u0000\u013d\u0158\u0005"+
		"s\u0000\u0000\u013e\u013f\u0005T\u0000\u0000\u013f\u0140\u0005u\u0000"+
		"\u0000\u0140\u0141\u0005n\u0000\u0000\u0141\u0142\u0005a\u0000\u0000\u0142"+
		"\u0158\u0005s\u0000\u0000\u0143\u0144\u0005M\u0000\u0000\u0144\u0145\u0005"+
		"a\u0000\u0000\u0145\u0146\u0005n\u0000\u0000\u0146\u0147\u0005z\u0000"+
		"\u0000\u0147\u0148\u0005a\u0000\u0000\u0148\u0149\u0005n\u0000\u0000\u0149"+
		"\u014a\u0005a\u0000\u0000\u014a\u0158\u0005s\u0000\u0000\u014b\u014c\u0005"+
		"U\u0000\u0000\u014c\u014d\u0005v\u0000\u0000\u014d\u014e\u0005a\u0000"+
		"\u0000\u014e\u0158\u0005s\u0000\u0000\u014f\u0150\u0005G\u0000\u0000\u0150"+
		"\u0151\u0005r\u0000\u0000\u0151\u0152\u0005a\u0000\u0000\u0152\u0153\u0005"+
		"n\u0000\u0000\u0153\u0154\u0005a\u0000\u0000\u0154\u0155\u0005d\u0000"+
		"\u0000\u0155\u0156\u0005a\u0000\u0000\u0156\u0158\u0005s\u0000\u0000\u0157"+
		"\u00d5\u0001\u0000\u0000\u0000\u0157\u00dd\u0001\u0000\u0000\u0000\u0157"+
		"\u00e7\u0001\u0000\u0000\u0000\u0157\u00ef\u0001\u0000\u0000\u0000\u0157"+
		"\u00f5\u0001\u0000\u0000\u0000\u0157\u00fd\u0001\u0000\u0000\u0000\u0157"+
		"\u0104\u0001\u0000\u0000\u0000\u0157\u0109\u0001\u0000\u0000\u0000\u0157"+
		"\u010f\u0001\u0000\u0000\u0000\u0157\u0116\u0001\u0000\u0000\u0000\u0157"+
		"\u011d\u0001\u0000\u0000\u0000\u0157\u0124\u0001\u0000\u0000\u0000\u0157"+
		"\u012c\u0001\u0000\u0000\u0000\u0157\u0134\u0001\u0000\u0000\u0000\u0157"+
		"\u0139\u0001\u0000\u0000\u0000\u0157\u013e\u0001\u0000\u0000\u0000\u0157"+
		"\u0143\u0001\u0000\u0000\u0000\u0157\u014b\u0001\u0000\u0000\u0000\u0157"+
		"\u014f\u0001\u0000\u0000\u0000\u0158\b\u0001\u0000\u0000\u0000\u0159\u015b"+
		"\u0007\u0000\u0000\u0000\u015a\u0159\u0001\u0000\u0000\u0000\u015b\u015c"+
		"\u0001\u0000\u0000\u0000\u015c\u015a\u0001\u0000\u0000\u0000\u015c\u015d"+
		"\u0001\u0000\u0000\u0000\u015d\n\u0001\u0000\u0000\u0000\u015e\u0160\u0007"+
		"\u0001\u0000\u0000\u015f\u015e\u0001\u0000\u0000\u0000\u0160\u0161\u0001"+
		"\u0000\u0000\u0000\u0161\u015f\u0001\u0000\u0000\u0000\u0161\u0162\u0001"+
		"\u0000\u0000\u0000\u0162\f\u0001\u0000\u0000\u0000\u0163\u0164\u0007\u0002"+
		"\u0000\u0000\u0164\u000e\u0001\u0000\u0000\u0000\u0165\u0167\u0007\u0003"+
		"\u0000\u0000\u0166\u0165\u0001\u0000\u0000\u0000\u0167\u0168\u0001\u0000"+
		"\u0000\u0000\u0168\u0166\u0001\u0000\u0000\u0000\u0168\u0169\u0001\u0000"+
		"\u0000\u0000\u0169\u0010\u0001\u0000\u0000\u0000\u016a\u016c\u0005\r\u0000"+
		"\u0000\u016b\u016a\u0001\u0000\u0000\u0000\u016b\u016c\u0001\u0000\u0000"+
		"\u0000\u016c\u016d\u0001\u0000\u0000\u0000\u016d\u0170\u0005\n\u0000\u0000"+
		"\u016e\u0170\u0005\r\u0000\u0000\u016f\u016b\u0001\u0000\u0000\u0000\u016f"+
		"\u016e\u0001\u0000\u0000\u0000\u0170\u0012\u0001\u0000\u0000\u0000\u0171"+
		"\u0173\u0007\u0004\u0000\u0000\u0172\u0171\u0001\u0000\u0000\u0000\u0173"+
		"\u0174\u0001\u0000\u0000\u0000\u0174\u0172\u0001\u0000\u0000\u0000\u0174"+
		"\u0175\u0001\u0000\u0000\u0000\u0175\u0176\u0001\u0000\u0000\u0000\u0176"+
		"\u0177\u0006\t\u0000\u0000\u0177\u0014\u0001\u0000\u0000\u0000\n\u0000"+
		"b\u00d3\u0157\u015c\u0161\u0168\u016b\u016f\u0174\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}