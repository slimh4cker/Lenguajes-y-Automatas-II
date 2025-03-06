// Generated from d:/Mis trabajos/6to semestre/Lenguajes y automatas II/Lenguajes-y-Automatas-II/words_analyzer/backend/Words.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class WordsParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		MONTH=1, COLON=2, FRUIT_SINGULAR=3, FRUIT_PLURAL=4, WORD=5, NUMBER=6, 
		PUNCTUATION=7, WHITESPACE=8, NEWLINE=9;
	public static final int
		RULE_texto = 0, RULE_seccion_mes = 1, RULE_fruta = 2, RULE_otro = 3;
	private static String[] makeRuleNames() {
		return new String[] {
			"texto", "seccion_mes", "fruta", "otro"
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
			"PUNCTUATION", "WHITESPACE", "NEWLINE"
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
	public String getGrammarFileName() { return "Words.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public WordsParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TextoContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(WordsParser.EOF, 0); }
		public List<Seccion_mesContext> seccion_mes() {
			return getRuleContexts(Seccion_mesContext.class);
		}
		public Seccion_mesContext seccion_mes(int i) {
			return getRuleContext(Seccion_mesContext.class,i);
		}
		public List<OtroContext> otro() {
			return getRuleContexts(OtroContext.class);
		}
		public OtroContext otro(int i) {
			return getRuleContext(OtroContext.class,i);
		}
		public TextoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_texto; }
	}

	public final TextoContext texto() throws RecognitionException {
		TextoContext _localctx = new TextoContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_texto);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(10); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				setState(10);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case MONTH:
					{
					setState(8);
					seccion_mes();
					}
					break;
				case WORD:
				case PUNCTUATION:
				case WHITESPACE:
				case NEWLINE:
					{
					setState(9);
					otro();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(12); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 930L) != 0) );
			setState(14);
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
	public static class Seccion_mesContext extends ParserRuleContext {
		public TerminalNode MONTH() { return getToken(WordsParser.MONTH, 0); }
		public TerminalNode COLON() { return getToken(WordsParser.COLON, 0); }
		public List<TerminalNode> WHITESPACE() { return getTokens(WordsParser.WHITESPACE); }
		public TerminalNode WHITESPACE(int i) {
			return getToken(WordsParser.WHITESPACE, i);
		}
		public List<FrutaContext> fruta() {
			return getRuleContexts(FrutaContext.class);
		}
		public FrutaContext fruta(int i) {
			return getRuleContext(FrutaContext.class,i);
		}
		public List<OtroContext> otro() {
			return getRuleContexts(OtroContext.class);
		}
		public OtroContext otro(int i) {
			return getRuleContext(OtroContext.class,i);
		}
		public Seccion_mesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_seccion_mes; }
	}

	public final Seccion_mesContext seccion_mes() throws RecognitionException {
		Seccion_mesContext _localctx = new Seccion_mesContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_seccion_mes);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(16);
			match(MONTH);
			setState(17);
			match(COLON);
			setState(21);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(18);
					match(WHITESPACE);
					}
					} 
				}
				setState(23);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			}
			setState(26); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					setState(26);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case FRUIT_SINGULAR:
					case FRUIT_PLURAL:
						{
						setState(24);
						fruta();
						}
						break;
					case WORD:
					case PUNCTUATION:
					case WHITESPACE:
					case NEWLINE:
						{
						setState(25);
						otro();
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(28); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
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
	public static class FrutaContext extends ParserRuleContext {
		public TerminalNode FRUIT_SINGULAR() { return getToken(WordsParser.FRUIT_SINGULAR, 0); }
		public TerminalNode FRUIT_PLURAL() { return getToken(WordsParser.FRUIT_PLURAL, 0); }
		public FrutaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fruta; }
	}

	public final FrutaContext fruta() throws RecognitionException {
		FrutaContext _localctx = new FrutaContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_fruta);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(30);
			_la = _input.LA(1);
			if ( !(_la==FRUIT_SINGULAR || _la==FRUIT_PLURAL) ) {
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
	public static class OtroContext extends ParserRuleContext {
		public List<TerminalNode> WORD() { return getTokens(WordsParser.WORD); }
		public TerminalNode WORD(int i) {
			return getToken(WordsParser.WORD, i);
		}
		public List<TerminalNode> PUNCTUATION() { return getTokens(WordsParser.PUNCTUATION); }
		public TerminalNode PUNCTUATION(int i) {
			return getToken(WordsParser.PUNCTUATION, i);
		}
		public List<TerminalNode> WHITESPACE() { return getTokens(WordsParser.WHITESPACE); }
		public TerminalNode WHITESPACE(int i) {
			return getToken(WordsParser.WHITESPACE, i);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(WordsParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(WordsParser.NEWLINE, i);
		}
		public OtroContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_otro; }
	}

	public final OtroContext otro() throws RecognitionException {
		OtroContext _localctx = new OtroContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_otro);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(33); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(32);
					_la = _input.LA(1);
					if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 928L) != 0)) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(35); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
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
		"\u0004\u0001\t&\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0001\u0000\u0001\u0000\u0004"+
		"\u0000\u000b\b\u0000\u000b\u0000\f\u0000\f\u0001\u0000\u0001\u0000\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0005\u0001\u0014\b\u0001\n\u0001\f\u0001"+
		"\u0017\t\u0001\u0001\u0001\u0001\u0001\u0004\u0001\u001b\b\u0001\u000b"+
		"\u0001\f\u0001\u001c\u0001\u0002\u0001\u0002\u0001\u0003\u0004\u0003\""+
		"\b\u0003\u000b\u0003\f\u0003#\u0001\u0003\u0000\u0000\u0004\u0000\u0002"+
		"\u0004\u0006\u0000\u0002\u0001\u0000\u0003\u0004\u0002\u0000\u0005\u0005"+
		"\u0007\t\'\u0000\n\u0001\u0000\u0000\u0000\u0002\u0010\u0001\u0000\u0000"+
		"\u0000\u0004\u001e\u0001\u0000\u0000\u0000\u0006!\u0001\u0000\u0000\u0000"+
		"\b\u000b\u0003\u0002\u0001\u0000\t\u000b\u0003\u0006\u0003\u0000\n\b\u0001"+
		"\u0000\u0000\u0000\n\t\u0001\u0000\u0000\u0000\u000b\f\u0001\u0000\u0000"+
		"\u0000\f\n\u0001\u0000\u0000\u0000\f\r\u0001\u0000\u0000\u0000\r\u000e"+
		"\u0001\u0000\u0000\u0000\u000e\u000f\u0005\u0000\u0000\u0001\u000f\u0001"+
		"\u0001\u0000\u0000\u0000\u0010\u0011\u0005\u0001\u0000\u0000\u0011\u0015"+
		"\u0005\u0002\u0000\u0000\u0012\u0014\u0005\b\u0000\u0000\u0013\u0012\u0001"+
		"\u0000\u0000\u0000\u0014\u0017\u0001\u0000\u0000\u0000\u0015\u0013\u0001"+
		"\u0000\u0000\u0000\u0015\u0016\u0001\u0000\u0000\u0000\u0016\u001a\u0001"+
		"\u0000\u0000\u0000\u0017\u0015\u0001\u0000\u0000\u0000\u0018\u001b\u0003"+
		"\u0004\u0002\u0000\u0019\u001b\u0003\u0006\u0003\u0000\u001a\u0018\u0001"+
		"\u0000\u0000\u0000\u001a\u0019\u0001\u0000\u0000\u0000\u001b\u001c\u0001"+
		"\u0000\u0000\u0000\u001c\u001a\u0001\u0000\u0000\u0000\u001c\u001d\u0001"+
		"\u0000\u0000\u0000\u001d\u0003\u0001\u0000\u0000\u0000\u001e\u001f\u0007"+
		"\u0000\u0000\u0000\u001f\u0005\u0001\u0000\u0000\u0000 \"\u0007\u0001"+
		"\u0000\u0000! \u0001\u0000\u0000\u0000\"#\u0001\u0000\u0000\u0000#!\u0001"+
		"\u0000\u0000\u0000#$\u0001\u0000\u0000\u0000$\u0007\u0001\u0000\u0000"+
		"\u0000\u0006\n\f\u0015\u001a\u001c#";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}