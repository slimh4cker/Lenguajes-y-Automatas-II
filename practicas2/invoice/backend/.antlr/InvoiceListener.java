// Generated from d:/Mis trabajos/6to semestre/Lenguajes y automatas II/salva/Lenguajes-y-Automatas-II/practicas2/invoice/backend/Invoice.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link InvoiceParser}.
 */
public interface InvoiceListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link InvoiceParser#invoice}.
	 * @param ctx the parse tree
	 */
	void enterInvoice(InvoiceParser.InvoiceContext ctx);
	/**
	 * Exit a parse tree produced by {@link InvoiceParser#invoice}.
	 * @param ctx the parse tree
	 */
	void exitInvoice(InvoiceParser.InvoiceContext ctx);
	/**
	 * Enter a parse tree produced by {@link InvoiceParser#header}.
	 * @param ctx the parse tree
	 */
	void enterHeader(InvoiceParser.HeaderContext ctx);
	/**
	 * Exit a parse tree produced by {@link InvoiceParser#header}.
	 * @param ctx the parse tree
	 */
	void exitHeader(InvoiceParser.HeaderContext ctx);
	/**
	 * Enter a parse tree produced by {@link InvoiceParser#verb}.
	 * @param ctx the parse tree
	 */
	void enterVerb(InvoiceParser.VerbContext ctx);
	/**
	 * Exit a parse tree produced by {@link InvoiceParser#verb}.
	 * @param ctx the parse tree
	 */
	void exitVerb(InvoiceParser.VerbContext ctx);
	/**
	 * Enter a parse tree produced by {@link InvoiceParser#purchaseList}.
	 * @param ctx the parse tree
	 */
	void enterPurchaseList(InvoiceParser.PurchaseListContext ctx);
	/**
	 * Exit a parse tree produced by {@link InvoiceParser#purchaseList}.
	 * @param ctx the parse tree
	 */
	void exitPurchaseList(InvoiceParser.PurchaseListContext ctx);
	/**
	 * Enter a parse tree produced by {@link InvoiceParser#separator}.
	 * @param ctx the parse tree
	 */
	void enterSeparator(InvoiceParser.SeparatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link InvoiceParser#separator}.
	 * @param ctx the parse tree
	 */
	void exitSeparator(InvoiceParser.SeparatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link InvoiceParser#purchase}.
	 * @param ctx the parse tree
	 */
	void enterPurchase(InvoiceParser.PurchaseContext ctx);
	/**
	 * Exit a parse tree produced by {@link InvoiceParser#purchase}.
	 * @param ctx the parse tree
	 */
	void exitPurchase(InvoiceParser.PurchaseContext ctx);
	/**
	 * Enter a parse tree produced by {@link InvoiceParser#quantity}.
	 * @param ctx the parse tree
	 */
	void enterQuantity(InvoiceParser.QuantityContext ctx);
	/**
	 * Exit a parse tree produced by {@link InvoiceParser#quantity}.
	 * @param ctx the parse tree
	 */
	void exitQuantity(InvoiceParser.QuantityContext ctx);
	/**
	 * Enter a parse tree produced by {@link InvoiceParser#fraction}.
	 * @param ctx the parse tree
	 */
	void enterFraction(InvoiceParser.FractionContext ctx);
	/**
	 * Exit a parse tree produced by {@link InvoiceParser#fraction}.
	 * @param ctx the parse tree
	 */
	void exitFraction(InvoiceParser.FractionContext ctx);
	/**
	 * Enter a parse tree produced by {@link InvoiceParser#unit}.
	 * @param ctx the parse tree
	 */
	void enterUnit(InvoiceParser.UnitContext ctx);
	/**
	 * Exit a parse tree produced by {@link InvoiceParser#unit}.
	 * @param ctx the parse tree
	 */
	void exitUnit(InvoiceParser.UnitContext ctx);
	/**
	 * Enter a parse tree produced by {@link InvoiceParser#pieceUnit}.
	 * @param ctx the parse tree
	 */
	void enterPieceUnit(InvoiceParser.PieceUnitContext ctx);
	/**
	 * Exit a parse tree produced by {@link InvoiceParser#pieceUnit}.
	 * @param ctx the parse tree
	 */
	void exitPieceUnit(InvoiceParser.PieceUnitContext ctx);
	/**
	 * Enter a parse tree produced by {@link InvoiceParser#fruit}.
	 * @param ctx the parse tree
	 */
	void enterFruit(InvoiceParser.FruitContext ctx);
	/**
	 * Exit a parse tree produced by {@link InvoiceParser#fruit}.
	 * @param ctx the parse tree
	 */
	void exitFruit(InvoiceParser.FruitContext ctx);
}