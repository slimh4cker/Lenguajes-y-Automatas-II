// Generated from c:/Users/monte/OneDrive/Documentos/proyecto/Lenguajes-y-Automatas-II/expr_simplified/Expr.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class ExprParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		ADD=1, SUBTRACT=2, MULTI=3, DIVI=4, LEFT_PARENTH=5, RIGHT_PARENTH=6, ID=7, 
		DIGIT=8, WS=9;
	public static final int
		RULE_expr = 0, RULE_expr_prime = 1, RULE_term = 2, RULE_term_prime = 3, 
		RULE_factor = 4;
	private static String[] makeRuleNames() {
		return new String[] {
			"expr", "expr_prime", "term", "term_prime", "factor"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'+'", "'-'", "'*'", "'/'", "'('", "')'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "ADD", "SUBTRACT", "MULTI", "DIVI", "LEFT_PARENTH", "RIGHT_PARENTH", 
			"ID", "DIGIT", "WS"
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
	public String getGrammarFileName() { return "Expr.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public ExprParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprContext extends ParserRuleContext {
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public Expr_primeContext expr_prime() {
			return getRuleContext(Expr_primeContext.class,0);
		}
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ExprListener ) ((ExprListener)listener).enterExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ExprListener ) ((ExprListener)listener).exitExpr(this);
		}
	}

	public final ExprContext expr() throws RecognitionException {
		ExprContext _localctx = new ExprContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_expr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(10);
			term();
			setState(11);
			expr_prime();
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
	public static class Expr_primeContext extends ParserRuleContext {
		public TerminalNode ADD() { return getToken(ExprParser.ADD, 0); }
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public Expr_primeContext expr_prime() {
			return getRuleContext(Expr_primeContext.class,0);
		}
		public TerminalNode SUBTRACT() { return getToken(ExprParser.SUBTRACT, 0); }
		public Expr_primeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr_prime; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ExprListener ) ((ExprListener)listener).enterExpr_prime(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ExprListener ) ((ExprListener)listener).exitExpr_prime(this);
		}
	}

	public final Expr_primeContext expr_prime() throws RecognitionException {
		Expr_primeContext _localctx = new Expr_primeContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_expr_prime);
		try {
			setState(22);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case RIGHT_PARENTH:
				enterOuterAlt(_localctx, 1);
				{
				}
				break;
			case ADD:
				enterOuterAlt(_localctx, 2);
				{
				setState(14);
				match(ADD);
				setState(15);
				term();
				setState(16);
				expr_prime();
				}
				break;
			case SUBTRACT:
				enterOuterAlt(_localctx, 3);
				{
				setState(18);
				match(SUBTRACT);
				setState(19);
				term();
				setState(20);
				expr_prime();
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
		public Term_primeContext term_prime() {
			return getRuleContext(Term_primeContext.class,0);
		}
		public TermContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ExprListener ) ((ExprListener)listener).enterTerm(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ExprListener ) ((ExprListener)listener).exitTerm(this);
		}
	}

	public final TermContext term() throws RecognitionException {
		TermContext _localctx = new TermContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_term);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(24);
			factor();
			setState(25);
			term_prime();
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
	public static class Term_primeContext extends ParserRuleContext {
		public TerminalNode MULTI() { return getToken(ExprParser.MULTI, 0); }
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public Term_primeContext term_prime() {
			return getRuleContext(Term_primeContext.class,0);
		}
		public TerminalNode DIVI() { return getToken(ExprParser.DIVI, 0); }
		public Term_primeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term_prime; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ExprListener ) ((ExprListener)listener).enterTerm_prime(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ExprListener ) ((ExprListener)listener).exitTerm_prime(this);
		}
	}

	public final Term_primeContext term_prime() throws RecognitionException {
		Term_primeContext _localctx = new Term_primeContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_term_prime);
		try {
			setState(36);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ADD:
			case SUBTRACT:
			case RIGHT_PARENTH:
				enterOuterAlt(_localctx, 1);
				{
				}
				break;
			case MULTI:
				enterOuterAlt(_localctx, 2);
				{
				setState(28);
				match(MULTI);
				setState(29);
				factor();
				setState(30);
				term_prime();
				}
				break;
			case DIVI:
				enterOuterAlt(_localctx, 3);
				{
				setState(32);
				match(DIVI);
				setState(33);
				factor();
				setState(34);
				term_prime();
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
		public TerminalNode ID() { return getToken(ExprParser.ID, 0); }
		public TerminalNode LEFT_PARENTH() { return getToken(ExprParser.LEFT_PARENTH, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RIGHT_PARENTH() { return getToken(ExprParser.RIGHT_PARENTH, 0); }
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ExprListener ) ((ExprListener)listener).enterFactor(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ExprListener ) ((ExprListener)listener).exitFactor(this);
		}
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_factor);
		try {
			setState(43);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(38);
				match(ID);
				}
				break;
			case LEFT_PARENTH:
				enterOuterAlt(_localctx, 2);
				{
				setState(39);
				match(LEFT_PARENTH);
				setState(40);
				expr();
				setState(41);
				match(RIGHT_PARENTH);
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

	public static final String _serializedATN =
		"\u0004\u0001\t.\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003"+
		"\u0001\u0017\b\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0003\u0003%\b\u0003\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0003\u0004,\b\u0004\u0001\u0004\u0000"+
		"\u0000\u0005\u0000\u0002\u0004\u0006\b\u0000\u0000-\u0000\n\u0001\u0000"+
		"\u0000\u0000\u0002\u0016\u0001\u0000\u0000\u0000\u0004\u0018\u0001\u0000"+
		"\u0000\u0000\u0006$\u0001\u0000\u0000\u0000\b+\u0001\u0000\u0000\u0000"+
		"\n\u000b\u0003\u0004\u0002\u0000\u000b\f\u0003\u0002\u0001\u0000\f\u0001"+
		"\u0001\u0000\u0000\u0000\r\u0017\u0001\u0000\u0000\u0000\u000e\u000f\u0005"+
		"\u0001\u0000\u0000\u000f\u0010\u0003\u0004\u0002\u0000\u0010\u0011\u0003"+
		"\u0002\u0001\u0000\u0011\u0017\u0001\u0000\u0000\u0000\u0012\u0013\u0005"+
		"\u0002\u0000\u0000\u0013\u0014\u0003\u0004\u0002\u0000\u0014\u0015\u0003"+
		"\u0002\u0001\u0000\u0015\u0017\u0001\u0000\u0000\u0000\u0016\r\u0001\u0000"+
		"\u0000\u0000\u0016\u000e\u0001\u0000\u0000\u0000\u0016\u0012\u0001\u0000"+
		"\u0000\u0000\u0017\u0003\u0001\u0000\u0000\u0000\u0018\u0019\u0003\b\u0004"+
		"\u0000\u0019\u001a\u0003\u0006\u0003\u0000\u001a\u0005\u0001\u0000\u0000"+
		"\u0000\u001b%\u0001\u0000\u0000\u0000\u001c\u001d\u0005\u0003\u0000\u0000"+
		"\u001d\u001e\u0003\b\u0004\u0000\u001e\u001f\u0003\u0006\u0003\u0000\u001f"+
		"%\u0001\u0000\u0000\u0000 !\u0005\u0004\u0000\u0000!\"\u0003\b\u0004\u0000"+
		"\"#\u0003\u0006\u0003\u0000#%\u0001\u0000\u0000\u0000$\u001b\u0001\u0000"+
		"\u0000\u0000$\u001c\u0001\u0000\u0000\u0000$ \u0001\u0000\u0000\u0000"+
		"%\u0007\u0001\u0000\u0000\u0000&,\u0005\u0007\u0000\u0000\'(\u0005\u0005"+
		"\u0000\u0000()\u0003\u0000\u0000\u0000)*\u0005\u0006\u0000\u0000*,\u0001"+
		"\u0000\u0000\u0000+&\u0001\u0000\u0000\u0000+\'\u0001\u0000\u0000\u0000"+
		",\t\u0001\u0000\u0000\u0000\u0003\u0016$+";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}