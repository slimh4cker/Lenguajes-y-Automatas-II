// Generated from d:/Mis trabajos/6to semestre/Lenguajes y automatas II/Lenguajes-y-Automatas-II/practicas2/words_analyzer/backend/Invoice.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class InvoiceParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, NOMBRE=2, KG=3, PIEZA=4, PIEZAS=5, COLON=6, WORD=7, PUNCTUATION=8, 
		NUMBER=9, WHITESPACE=10, NEWLINE=11;
	public static final int
		RULE_texto = 0, RULE_compra = 1, RULE_cantidad = 2, RULE_unidad = 3, RULE_otro = 4;
	private static String[] makeRuleNames() {
		return new String[] {
			"texto", "compra", "cantidad", "unidad", "otro"
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

	@Override
	public String getGrammarFileName() { return "Invoice.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public InvoiceParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TextoContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(InvoiceParser.EOF, 0); }
		public List<TerminalNode> NOMBRE() { return getTokens(InvoiceParser.NOMBRE); }
		public TerminalNode NOMBRE(int i) {
			return getToken(InvoiceParser.NOMBRE, i);
		}
		public List<CompraContext> compra() {
			return getRuleContexts(CompraContext.class);
		}
		public CompraContext compra(int i) {
			return getRuleContext(CompraContext.class,i);
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
			setState(11); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(10);
				match(NOMBRE);
				}
				}
				setState(13); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==NOMBRE );
			setState(16); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(15);
				compra();
				}
				}
				setState(18); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==NUMBER );
			setState(20);
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
	public static class CompraContext extends ParserRuleContext {
		public CantidadContext cantidad() {
			return getRuleContext(CantidadContext.class,0);
		}
		public UnidadContext unidad() {
			return getRuleContext(UnidadContext.class,0);
		}
		public TerminalNode WORD() { return getToken(InvoiceParser.WORD, 0); }
		public OtroContext otro() {
			return getRuleContext(OtroContext.class,0);
		}
		public CompraContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_compra; }
	}

	public final CompraContext compra() throws RecognitionException {
		CompraContext _localctx = new CompraContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_compra);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(22);
			cantidad();
			setState(23);
			unidad();
			setState(24);
			match(WORD);
			setState(26);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 3392L) != 0)) {
				{
				setState(25);
				otro();
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
	public static class CantidadContext extends ParserRuleContext {
		public List<TerminalNode> NUMBER() { return getTokens(InvoiceParser.NUMBER); }
		public TerminalNode NUMBER(int i) {
			return getToken(InvoiceParser.NUMBER, i);
		}
		public CantidadContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cantidad; }
	}

	public final CantidadContext cantidad() throws RecognitionException {
		CantidadContext _localctx = new CantidadContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_cantidad);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(28);
			match(NUMBER);
			setState(31);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__0) {
				{
				setState(29);
				match(T__0);
				setState(30);
				match(NUMBER);
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
	public static class UnidadContext extends ParserRuleContext {
		public TerminalNode KG() { return getToken(InvoiceParser.KG, 0); }
		public TerminalNode PIEZA() { return getToken(InvoiceParser.PIEZA, 0); }
		public TerminalNode PIEZAS() { return getToken(InvoiceParser.PIEZAS, 0); }
		public UnidadContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unidad; }
	}

	public final UnidadContext unidad() throws RecognitionException {
		UnidadContext _localctx = new UnidadContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_unidad);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(33);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 56L) != 0)) ) {
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
		public List<TerminalNode> PUNCTUATION() { return getTokens(InvoiceParser.PUNCTUATION); }
		public TerminalNode PUNCTUATION(int i) {
			return getToken(InvoiceParser.PUNCTUATION, i);
		}
		public List<TerminalNode> COLON() { return getTokens(InvoiceParser.COLON); }
		public TerminalNode COLON(int i) {
			return getToken(InvoiceParser.COLON, i);
		}
		public List<TerminalNode> WHITESPACE() { return getTokens(InvoiceParser.WHITESPACE); }
		public TerminalNode WHITESPACE(int i) {
			return getToken(InvoiceParser.WHITESPACE, i);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(InvoiceParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(InvoiceParser.NEWLINE, i);
		}
		public OtroContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_otro; }
	}

	public final OtroContext otro() throws RecognitionException {
		OtroContext _localctx = new OtroContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_otro);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(36); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(35);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 3392L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				}
				setState(38); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 3392L) != 0) );
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
		"\u0004\u0001\u000b)\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0001"+
		"\u0000\u0004\u0000\f\b\u0000\u000b\u0000\f\u0000\r\u0001\u0000\u0004\u0000"+
		"\u0011\b\u0000\u000b\u0000\f\u0000\u0012\u0001\u0000\u0001\u0000\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001\u001b\b\u0001\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0003\u0002 \b\u0002\u0001\u0003\u0001"+
		"\u0003\u0001\u0004\u0004\u0004%\b\u0004\u000b\u0004\f\u0004&\u0001\u0004"+
		"\u0000\u0000\u0005\u0000\u0002\u0004\u0006\b\u0000\u0002\u0001\u0000\u0003"+
		"\u0005\u0003\u0000\u0006\u0006\b\b\n\u000b(\u0000\u000b\u0001\u0000\u0000"+
		"\u0000\u0002\u0016\u0001\u0000\u0000\u0000\u0004\u001c\u0001\u0000\u0000"+
		"\u0000\u0006!\u0001\u0000\u0000\u0000\b$\u0001\u0000\u0000\u0000\n\f\u0005"+
		"\u0002\u0000\u0000\u000b\n\u0001\u0000\u0000\u0000\f\r\u0001\u0000\u0000"+
		"\u0000\r\u000b\u0001\u0000\u0000\u0000\r\u000e\u0001\u0000\u0000\u0000"+
		"\u000e\u0010\u0001\u0000\u0000\u0000\u000f\u0011\u0003\u0002\u0001\u0000"+
		"\u0010\u000f\u0001\u0000\u0000\u0000\u0011\u0012\u0001\u0000\u0000\u0000"+
		"\u0012\u0010\u0001\u0000\u0000\u0000\u0012\u0013\u0001\u0000\u0000\u0000"+
		"\u0013\u0014\u0001\u0000\u0000\u0000\u0014\u0015\u0005\u0000\u0000\u0001"+
		"\u0015\u0001\u0001\u0000\u0000\u0000\u0016\u0017\u0003\u0004\u0002\u0000"+
		"\u0017\u0018\u0003\u0006\u0003\u0000\u0018\u001a\u0005\u0007\u0000\u0000"+
		"\u0019\u001b\u0003\b\u0004\u0000\u001a\u0019\u0001\u0000\u0000\u0000\u001a"+
		"\u001b\u0001\u0000\u0000\u0000\u001b\u0003\u0001\u0000\u0000\u0000\u001c"+
		"\u001f\u0005\t\u0000\u0000\u001d\u001e\u0005\u0001\u0000\u0000\u001e "+
		"\u0005\t\u0000\u0000\u001f\u001d\u0001\u0000\u0000\u0000\u001f \u0001"+
		"\u0000\u0000\u0000 \u0005\u0001\u0000\u0000\u0000!\"\u0007\u0000\u0000"+
		"\u0000\"\u0007\u0001\u0000\u0000\u0000#%\u0007\u0001\u0000\u0000$#\u0001"+
		"\u0000\u0000\u0000%&\u0001\u0000\u0000\u0000&$\u0001\u0000\u0000\u0000"+
		"&\'\u0001\u0000\u0000\u0000\'\t\u0001\u0000\u0000\u0000\u0005\r\u0012"+
		"\u001a\u001f&";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}