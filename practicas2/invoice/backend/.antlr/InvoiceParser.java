// Generated from d:/Mis trabajos/6to semestre/Lenguajes y automatas II/Lenguajes-y-Automatas-II/practicas2/invoice/backend/Invoice.g4 by ANTLR 4.13.1
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
		T__0=1, Y_CONJ=2, COMMA=3, KG=4, PIEZA=5, PIEZAS=6, DE=7, NUMBER=8, NOMBRE=9, 
		WORD=10, DOT=11, WS=12;
	public static final int
		RULE_invoice = 0, RULE_header = 1, RULE_verb = 2, RULE_purchaseList = 3, 
		RULE_separator = 4, RULE_purchase = 5, RULE_quantity = 6, RULE_fraction = 7, 
		RULE_unit = 8, RULE_pieceUnit = 9, RULE_fruit = 10;
	private static String[] makeRuleNames() {
		return new String[] {
			"invoice", "header", "verb", "purchaseList", "separator", "purchase", 
			"quantity", "fraction", "unit", "pieceUnit", "fruit"
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
	public static class InvoiceContext extends ParserRuleContext {
		public HeaderContext header() {
			return getRuleContext(HeaderContext.class,0);
		}
		public PurchaseListContext purchaseList() {
			return getRuleContext(PurchaseListContext.class,0);
		}
		public TerminalNode EOF() { return getToken(InvoiceParser.EOF, 0); }
		public List<VerbContext> verb() {
			return getRuleContexts(VerbContext.class);
		}
		public VerbContext verb(int i) {
			return getRuleContext(VerbContext.class,i);
		}
		public TerminalNode DOT() { return getToken(InvoiceParser.DOT, 0); }
		public InvoiceContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_invoice; }
	}

	public final InvoiceContext invoice() throws RecognitionException {
		InvoiceContext _localctx = new InvoiceContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_invoice);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(22);
			header();
			setState(24); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(23);
				verb();
				}
				}
				setState(26); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==WORD );
			setState(28);
			purchaseList();
			setState(30);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==DOT) {
				{
				setState(29);
				match(DOT);
				}
			}

			setState(32);
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
	public static class HeaderContext extends ParserRuleContext {
		public List<TerminalNode> NOMBRE() { return getTokens(InvoiceParser.NOMBRE); }
		public TerminalNode NOMBRE(int i) {
			return getToken(InvoiceParser.NOMBRE, i);
		}
		public HeaderContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_header; }
	}

	public final HeaderContext header() throws RecognitionException {
		HeaderContext _localctx = new HeaderContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_header);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(34);
			match(NOMBRE);
			setState(38);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==NOMBRE) {
				{
				{
				setState(35);
				match(NOMBRE);
				}
				}
				setState(40);
				_errHandler.sync(this);
				_la = _input.LA(1);
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
	public static class VerbContext extends ParserRuleContext {
		public TerminalNode WORD() { return getToken(InvoiceParser.WORD, 0); }
		public TerminalNode COMMA() { return getToken(InvoiceParser.COMMA, 0); }
		public TerminalNode Y_CONJ() { return getToken(InvoiceParser.Y_CONJ, 0); }
		public TerminalNode DE() { return getToken(InvoiceParser.DE, 0); }
		public VerbContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_verb; }
	}

	public final VerbContext verb() throws RecognitionException {
		VerbContext _localctx = new VerbContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_verb);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(41);
			match(WORD);
			setState(43);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 140L) != 0)) {
				{
				setState(42);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 140L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
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
	public static class PurchaseListContext extends ParserRuleContext {
		public List<PurchaseContext> purchase() {
			return getRuleContexts(PurchaseContext.class);
		}
		public PurchaseContext purchase(int i) {
			return getRuleContext(PurchaseContext.class,i);
		}
		public List<SeparatorContext> separator() {
			return getRuleContexts(SeparatorContext.class);
		}
		public SeparatorContext separator(int i) {
			return getRuleContext(SeparatorContext.class,i);
		}
		public PurchaseListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_purchaseList; }
	}

	public final PurchaseListContext purchaseList() throws RecognitionException {
		PurchaseListContext _localctx = new PurchaseListContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_purchaseList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(45);
			purchase();
			setState(51);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==Y_CONJ || _la==COMMA) {
				{
				{
				setState(46);
				separator();
				setState(47);
				purchase();
				}
				}
				setState(53);
				_errHandler.sync(this);
				_la = _input.LA(1);
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
	public static class SeparatorContext extends ParserRuleContext {
		public TerminalNode COMMA() { return getToken(InvoiceParser.COMMA, 0); }
		public TerminalNode Y_CONJ() { return getToken(InvoiceParser.Y_CONJ, 0); }
		public List<TerminalNode> WS() { return getTokens(InvoiceParser.WS); }
		public TerminalNode WS(int i) {
			return getToken(InvoiceParser.WS, i);
		}
		public SeparatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_separator; }
	}

	public final SeparatorContext separator() throws RecognitionException {
		SeparatorContext _localctx = new SeparatorContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_separator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(54);
			_la = _input.LA(1);
			if ( !(_la==Y_CONJ || _la==COMMA) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(58);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==WS) {
				{
				{
				setState(55);
				match(WS);
				}
				}
				setState(60);
				_errHandler.sync(this);
				_la = _input.LA(1);
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
	public static class PurchaseContext extends ParserRuleContext {
		public QuantityContext quantity() {
			return getRuleContext(QuantityContext.class,0);
		}
		public UnitContext unit() {
			return getRuleContext(UnitContext.class,0);
		}
		public FruitContext fruit() {
			return getRuleContext(FruitContext.class,0);
		}
		public TerminalNode DE() { return getToken(InvoiceParser.DE, 0); }
		public PieceUnitContext pieceUnit() {
			return getRuleContext(PieceUnitContext.class,0);
		}
		public PurchaseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_purchase; }
	}

	public final PurchaseContext purchase() throws RecognitionException {
		PurchaseContext _localctx = new PurchaseContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_purchase);
		int _la;
		try {
			setState(75);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(61);
				quantity();
				{
				setState(62);
				unit();
				setState(64);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==DE) {
					{
					setState(63);
					match(DE);
					}
				}

				setState(66);
				fruit();
				}
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(68);
				quantity();
				{
				setState(69);
				pieceUnit();
				setState(71);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==DE) {
					{
					setState(70);
					match(DE);
					}
				}

				setState(73);
				fruit();
				}
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
	public static class QuantityContext extends ParserRuleContext {
		public FractionContext fraction() {
			return getRuleContext(FractionContext.class,0);
		}
		public TerminalNode NUMBER() { return getToken(InvoiceParser.NUMBER, 0); }
		public QuantityContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_quantity; }
	}

	public final QuantityContext quantity() throws RecognitionException {
		QuantityContext _localctx = new QuantityContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_quantity);
		try {
			setState(79);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(77);
				fraction();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(78);
				match(NUMBER);
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
	public static class FractionContext extends ParserRuleContext {
		public List<TerminalNode> NUMBER() { return getTokens(InvoiceParser.NUMBER); }
		public TerminalNode NUMBER(int i) {
			return getToken(InvoiceParser.NUMBER, i);
		}
		public FractionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fraction; }
	}

	public final FractionContext fraction() throws RecognitionException {
		FractionContext _localctx = new FractionContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_fraction);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(81);
			match(NUMBER);
			setState(82);
			match(T__0);
			setState(83);
			match(NUMBER);
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
	public static class UnitContext extends ParserRuleContext {
		public TerminalNode KG() { return getToken(InvoiceParser.KG, 0); }
		public UnitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unit; }
	}

	public final UnitContext unit() throws RecognitionException {
		UnitContext _localctx = new UnitContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_unit);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(85);
			match(KG);
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
	public static class PieceUnitContext extends ParserRuleContext {
		public TerminalNode PIEZA() { return getToken(InvoiceParser.PIEZA, 0); }
		public TerminalNode PIEZAS() { return getToken(InvoiceParser.PIEZAS, 0); }
		public PieceUnitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_pieceUnit; }
	}

	public final PieceUnitContext pieceUnit() throws RecognitionException {
		PieceUnitContext _localctx = new PieceUnitContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_pieceUnit);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(87);
			_la = _input.LA(1);
			if ( !(_la==PIEZA || _la==PIEZAS) ) {
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
	public static class FruitContext extends ParserRuleContext {
		public TerminalNode WORD() { return getToken(InvoiceParser.WORD, 0); }
		public FruitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fruit; }
	}

	public final FruitContext fruit() throws RecognitionException {
		FruitContext _localctx = new FruitContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_fruit);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(89);
			match(WORD);
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
		"\u0004\u0001\f\\\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0001\u0000\u0001\u0000\u0004"+
		"\u0000\u0019\b\u0000\u000b\u0000\f\u0000\u001a\u0001\u0000\u0001\u0000"+
		"\u0003\u0000\u001f\b\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001"+
		"\u0005\u0001%\b\u0001\n\u0001\f\u0001(\t\u0001\u0001\u0002\u0001\u0002"+
		"\u0003\u0002,\b\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0005\u00032\b\u0003\n\u0003\f\u00035\t\u0003\u0001\u0004\u0001\u0004"+
		"\u0005\u00049\b\u0004\n\u0004\f\u0004<\t\u0004\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0003\u0005A\b\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0003\u0005H\b\u0005\u0001\u0005\u0001\u0005"+
		"\u0003\u0005L\b\u0005\u0001\u0006\u0001\u0006\u0003\u0006P\b\u0006\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\t\u0001"+
		"\t\u0001\n\u0001\n\u0001\n\u0000\u0000\u000b\u0000\u0002\u0004\u0006\b"+
		"\n\f\u000e\u0010\u0012\u0014\u0000\u0003\u0002\u0000\u0002\u0003\u0007"+
		"\u0007\u0001\u0000\u0002\u0003\u0001\u0000\u0005\u0006Z\u0000\u0016\u0001"+
		"\u0000\u0000\u0000\u0002\"\u0001\u0000\u0000\u0000\u0004)\u0001\u0000"+
		"\u0000\u0000\u0006-\u0001\u0000\u0000\u0000\b6\u0001\u0000\u0000\u0000"+
		"\nK\u0001\u0000\u0000\u0000\fO\u0001\u0000\u0000\u0000\u000eQ\u0001\u0000"+
		"\u0000\u0000\u0010U\u0001\u0000\u0000\u0000\u0012W\u0001\u0000\u0000\u0000"+
		"\u0014Y\u0001\u0000\u0000\u0000\u0016\u0018\u0003\u0002\u0001\u0000\u0017"+
		"\u0019\u0003\u0004\u0002\u0000\u0018\u0017\u0001\u0000\u0000\u0000\u0019"+
		"\u001a\u0001\u0000\u0000\u0000\u001a\u0018\u0001\u0000\u0000\u0000\u001a"+
		"\u001b\u0001\u0000\u0000\u0000\u001b\u001c\u0001\u0000\u0000\u0000\u001c"+
		"\u001e\u0003\u0006\u0003\u0000\u001d\u001f\u0005\u000b\u0000\u0000\u001e"+
		"\u001d\u0001\u0000\u0000\u0000\u001e\u001f\u0001\u0000\u0000\u0000\u001f"+
		" \u0001\u0000\u0000\u0000 !\u0005\u0000\u0000\u0001!\u0001\u0001\u0000"+
		"\u0000\u0000\"&\u0005\t\u0000\u0000#%\u0005\t\u0000\u0000$#\u0001\u0000"+
		"\u0000\u0000%(\u0001\u0000\u0000\u0000&$\u0001\u0000\u0000\u0000&\'\u0001"+
		"\u0000\u0000\u0000\'\u0003\u0001\u0000\u0000\u0000(&\u0001\u0000\u0000"+
		"\u0000)+\u0005\n\u0000\u0000*,\u0007\u0000\u0000\u0000+*\u0001\u0000\u0000"+
		"\u0000+,\u0001\u0000\u0000\u0000,\u0005\u0001\u0000\u0000\u0000-3\u0003"+
		"\n\u0005\u0000./\u0003\b\u0004\u0000/0\u0003\n\u0005\u000002\u0001\u0000"+
		"\u0000\u00001.\u0001\u0000\u0000\u000025\u0001\u0000\u0000\u000031\u0001"+
		"\u0000\u0000\u000034\u0001\u0000\u0000\u00004\u0007\u0001\u0000\u0000"+
		"\u000053\u0001\u0000\u0000\u00006:\u0007\u0001\u0000\u000079\u0005\f\u0000"+
		"\u000087\u0001\u0000\u0000\u00009<\u0001\u0000\u0000\u0000:8\u0001\u0000"+
		"\u0000\u0000:;\u0001\u0000\u0000\u0000;\t\u0001\u0000\u0000\u0000<:\u0001"+
		"\u0000\u0000\u0000=>\u0003\f\u0006\u0000>@\u0003\u0010\b\u0000?A\u0005"+
		"\u0007\u0000\u0000@?\u0001\u0000\u0000\u0000@A\u0001\u0000\u0000\u0000"+
		"AB\u0001\u0000\u0000\u0000BC\u0003\u0014\n\u0000CL\u0001\u0000\u0000\u0000"+
		"DE\u0003\f\u0006\u0000EG\u0003\u0012\t\u0000FH\u0005\u0007\u0000\u0000"+
		"GF\u0001\u0000\u0000\u0000GH\u0001\u0000\u0000\u0000HI\u0001\u0000\u0000"+
		"\u0000IJ\u0003\u0014\n\u0000JL\u0001\u0000\u0000\u0000K=\u0001\u0000\u0000"+
		"\u0000KD\u0001\u0000\u0000\u0000L\u000b\u0001\u0000\u0000\u0000MP\u0003"+
		"\u000e\u0007\u0000NP\u0005\b\u0000\u0000OM\u0001\u0000\u0000\u0000ON\u0001"+
		"\u0000\u0000\u0000P\r\u0001\u0000\u0000\u0000QR\u0005\b\u0000\u0000RS"+
		"\u0005\u0001\u0000\u0000ST\u0005\b\u0000\u0000T\u000f\u0001\u0000\u0000"+
		"\u0000UV\u0005\u0004\u0000\u0000V\u0011\u0001\u0000\u0000\u0000WX\u0007"+
		"\u0002\u0000\u0000X\u0013\u0001\u0000\u0000\u0000YZ\u0005\n\u0000\u0000"+
		"Z\u0015\u0001\u0000\u0000\u0000\n\u001a\u001e&+3:@GKO";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}