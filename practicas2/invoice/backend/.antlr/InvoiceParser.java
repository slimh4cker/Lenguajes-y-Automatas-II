// Generated from d:/Mis trabajos/6to semestre/Lenguajes y automatas II/salva/Lenguajes-y-Automatas-II/practicas2/invoice/backend/Invoice.g4 by ANTLR 4.13.1
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
			setState(29);
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
		public List<TerminalNode> WORD() { return getTokens(InvoiceParser.WORD); }
		public TerminalNode WORD(int i) {
			return getToken(InvoiceParser.WORD, i);
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
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(36);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WORD) {
				{
				setState(32); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(31);
					match(WORD);
					}
					}
					setState(34); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==WORD );
				}
			}

			setState(38);
			match(NOMBRE);
			setState(44);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				{
				setState(40); 
				_errHandler.sync(this);
				_alt = 1;
				do {
					switch (_alt) {
					case 1:
						{
						{
						setState(39);
						match(WORD);
						}
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					setState(42); 
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
				} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
				}
				break;
			}
			setState(49);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==NOMBRE) {
				{
				{
				setState(46);
				match(NOMBRE);
				}
				}
				setState(51);
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
			setState(52);
			match(WORD);
			setState(54);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 140L) != 0)) {
				{
				setState(53);
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
		public List<TerminalNode> WORD() { return getTokens(InvoiceParser.WORD); }
		public TerminalNode WORD(int i) {
			return getToken(InvoiceParser.WORD, i);
		}
		public List<TerminalNode> DOT() { return getTokens(InvoiceParser.DOT); }
		public TerminalNode DOT(int i) {
			return getToken(InvoiceParser.DOT, i);
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
			setState(56);
			purchase();
			setState(74);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 2060L) != 0)) {
				{
				{
				setState(57);
				separator();
				setState(68);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case WORD:
					{
					setState(59); 
					_errHandler.sync(this);
					_la = _input.LA(1);
					do {
						{
						{
						setState(58);
						match(WORD);
						}
						}
						setState(61); 
						_errHandler.sync(this);
						_la = _input.LA(1);
					} while ( _la==WORD );
					}
					break;
				case DOT:
					{
					setState(64); 
					_errHandler.sync(this);
					_la = _input.LA(1);
					do {
						{
						{
						setState(63);
						match(DOT);
						}
						}
						setState(66); 
						_errHandler.sync(this);
						_la = _input.LA(1);
					} while ( _la==DOT );
					}
					break;
				case NUMBER:
					break;
				default:
					break;
				}
				setState(70);
				purchase();
				}
				}
				setState(76);
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
		public TerminalNode DOT() { return getToken(InvoiceParser.DOT, 0); }
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
			setState(77);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 2060L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(81);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==WS) {
				{
				{
				setState(78);
				match(WS);
				}
				}
				setState(83);
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
			setState(98);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(84);
				quantity();
				{
				setState(85);
				unit();
				setState(87);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==DE) {
					{
					setState(86);
					match(DE);
					}
				}

				setState(89);
				fruit();
				}
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(91);
				quantity();
				{
				setState(92);
				pieceUnit();
				setState(94);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==DE) {
					{
					setState(93);
					match(DE);
					}
				}

				setState(96);
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
			setState(102);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(100);
				fraction();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(101);
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
			setState(104);
			match(NUMBER);
			setState(105);
			match(T__0);
			setState(106);
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
			setState(108);
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
			setState(110);
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
			setState(112);
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
		"\u0004\u0001\fs\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0001\u0000\u0001\u0000\u0004"+
		"\u0000\u0019\b\u0000\u000b\u0000\f\u0000\u001a\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0001\u0004\u0001!\b\u0001\u000b\u0001\f\u0001\"\u0003"+
		"\u0001%\b\u0001\u0001\u0001\u0001\u0001\u0004\u0001)\b\u0001\u000b\u0001"+
		"\f\u0001*\u0003\u0001-\b\u0001\u0001\u0001\u0005\u00010\b\u0001\n\u0001"+
		"\f\u00013\t\u0001\u0001\u0002\u0001\u0002\u0003\u00027\b\u0002\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0004\u0003<\b\u0003\u000b\u0003\f\u0003=\u0001"+
		"\u0003\u0004\u0003A\b\u0003\u000b\u0003\f\u0003B\u0003\u0003E\b\u0003"+
		"\u0001\u0003\u0001\u0003\u0005\u0003I\b\u0003\n\u0003\f\u0003L\t\u0003"+
		"\u0001\u0004\u0001\u0004\u0005\u0004P\b\u0004\n\u0004\f\u0004S\t\u0004"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0003\u0005X\b\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0003\u0005_\b\u0005"+
		"\u0001\u0005\u0001\u0005\u0003\u0005c\b\u0005\u0001\u0006\u0001\u0006"+
		"\u0003\u0006g\b\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\b\u0001\b\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n\u0000\u0000\u000b"+
		"\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0000\u0003\u0002"+
		"\u0000\u0002\u0003\u0007\u0007\u0002\u0000\u0002\u0003\u000b\u000b\u0001"+
		"\u0000\u0005\u0006x\u0000\u0016\u0001\u0000\u0000\u0000\u0002$\u0001\u0000"+
		"\u0000\u0000\u00044\u0001\u0000\u0000\u0000\u00068\u0001\u0000\u0000\u0000"+
		"\bM\u0001\u0000\u0000\u0000\nb\u0001\u0000\u0000\u0000\ff\u0001\u0000"+
		"\u0000\u0000\u000eh\u0001\u0000\u0000\u0000\u0010l\u0001\u0000\u0000\u0000"+
		"\u0012n\u0001\u0000\u0000\u0000\u0014p\u0001\u0000\u0000\u0000\u0016\u0018"+
		"\u0003\u0002\u0001\u0000\u0017\u0019\u0003\u0004\u0002\u0000\u0018\u0017"+
		"\u0001\u0000\u0000\u0000\u0019\u001a\u0001\u0000\u0000\u0000\u001a\u0018"+
		"\u0001\u0000\u0000\u0000\u001a\u001b\u0001\u0000\u0000\u0000\u001b\u001c"+
		"\u0001\u0000\u0000\u0000\u001c\u001d\u0003\u0006\u0003\u0000\u001d\u001e"+
		"\u0005\u0000\u0000\u0001\u001e\u0001\u0001\u0000\u0000\u0000\u001f!\u0005"+
		"\n\u0000\u0000 \u001f\u0001\u0000\u0000\u0000!\"\u0001\u0000\u0000\u0000"+
		"\" \u0001\u0000\u0000\u0000\"#\u0001\u0000\u0000\u0000#%\u0001\u0000\u0000"+
		"\u0000$ \u0001\u0000\u0000\u0000$%\u0001\u0000\u0000\u0000%&\u0001\u0000"+
		"\u0000\u0000&,\u0005\t\u0000\u0000\')\u0005\n\u0000\u0000(\'\u0001\u0000"+
		"\u0000\u0000)*\u0001\u0000\u0000\u0000*(\u0001\u0000\u0000\u0000*+\u0001"+
		"\u0000\u0000\u0000+-\u0001\u0000\u0000\u0000,(\u0001\u0000\u0000\u0000"+
		",-\u0001\u0000\u0000\u0000-1\u0001\u0000\u0000\u0000.0\u0005\t\u0000\u0000"+
		"/.\u0001\u0000\u0000\u000003\u0001\u0000\u0000\u00001/\u0001\u0000\u0000"+
		"\u000012\u0001\u0000\u0000\u00002\u0003\u0001\u0000\u0000\u000031\u0001"+
		"\u0000\u0000\u000046\u0005\n\u0000\u000057\u0007\u0000\u0000\u000065\u0001"+
		"\u0000\u0000\u000067\u0001\u0000\u0000\u00007\u0005\u0001\u0000\u0000"+
		"\u00008J\u0003\n\u0005\u00009D\u0003\b\u0004\u0000:<\u0005\n\u0000\u0000"+
		";:\u0001\u0000\u0000\u0000<=\u0001\u0000\u0000\u0000=;\u0001\u0000\u0000"+
		"\u0000=>\u0001\u0000\u0000\u0000>E\u0001\u0000\u0000\u0000?A\u0005\u000b"+
		"\u0000\u0000@?\u0001\u0000\u0000\u0000AB\u0001\u0000\u0000\u0000B@\u0001"+
		"\u0000\u0000\u0000BC\u0001\u0000\u0000\u0000CE\u0001\u0000\u0000\u0000"+
		"D;\u0001\u0000\u0000\u0000D@\u0001\u0000\u0000\u0000DE\u0001\u0000\u0000"+
		"\u0000EF\u0001\u0000\u0000\u0000FG\u0003\n\u0005\u0000GI\u0001\u0000\u0000"+
		"\u0000H9\u0001\u0000\u0000\u0000IL\u0001\u0000\u0000\u0000JH\u0001\u0000"+
		"\u0000\u0000JK\u0001\u0000\u0000\u0000K\u0007\u0001\u0000\u0000\u0000"+
		"LJ\u0001\u0000\u0000\u0000MQ\u0007\u0001\u0000\u0000NP\u0005\f\u0000\u0000"+
		"ON\u0001\u0000\u0000\u0000PS\u0001\u0000\u0000\u0000QO\u0001\u0000\u0000"+
		"\u0000QR\u0001\u0000\u0000\u0000R\t\u0001\u0000\u0000\u0000SQ\u0001\u0000"+
		"\u0000\u0000TU\u0003\f\u0006\u0000UW\u0003\u0010\b\u0000VX\u0005\u0007"+
		"\u0000\u0000WV\u0001\u0000\u0000\u0000WX\u0001\u0000\u0000\u0000XY\u0001"+
		"\u0000\u0000\u0000YZ\u0003\u0014\n\u0000Zc\u0001\u0000\u0000\u0000[\\"+
		"\u0003\f\u0006\u0000\\^\u0003\u0012\t\u0000]_\u0005\u0007\u0000\u0000"+
		"^]\u0001\u0000\u0000\u0000^_\u0001\u0000\u0000\u0000_`\u0001\u0000\u0000"+
		"\u0000`a\u0003\u0014\n\u0000ac\u0001\u0000\u0000\u0000bT\u0001\u0000\u0000"+
		"\u0000b[\u0001\u0000\u0000\u0000c\u000b\u0001\u0000\u0000\u0000dg\u0003"+
		"\u000e\u0007\u0000eg\u0005\b\u0000\u0000fd\u0001\u0000\u0000\u0000fe\u0001"+
		"\u0000\u0000\u0000g\r\u0001\u0000\u0000\u0000hi\u0005\b\u0000\u0000ij"+
		"\u0005\u0001\u0000\u0000jk\u0005\b\u0000\u0000k\u000f\u0001\u0000\u0000"+
		"\u0000lm\u0005\u0004\u0000\u0000m\u0011\u0001\u0000\u0000\u0000no\u0007"+
		"\u0002\u0000\u0000o\u0013\u0001\u0000\u0000\u0000pq\u0005\n\u0000\u0000"+
		"q\u0015\u0001\u0000\u0000\u0000\u0010\u001a\"$*,16=BDJQW^bf";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}