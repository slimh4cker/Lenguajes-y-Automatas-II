// Generated from c:/Users/monte/OneDrive/Documentos/proyecto/Lenguajes-y-Automatas-II/expr_simplified/Expr.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link ExprParser}.
 */
public interface ExprListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(ExprParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(ExprParser.ExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#expr_prime}.
	 * @param ctx the parse tree
	 */
	void enterExpr_prime(ExprParser.Expr_primeContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#expr_prime}.
	 * @param ctx the parse tree
	 */
	void exitExpr_prime(ExprParser.Expr_primeContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#term}.
	 * @param ctx the parse tree
	 */
	void enterTerm(ExprParser.TermContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#term}.
	 * @param ctx the parse tree
	 */
	void exitTerm(ExprParser.TermContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#term_prime}.
	 * @param ctx the parse tree
	 */
	void enterTerm_prime(ExprParser.Term_primeContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#term_prime}.
	 * @param ctx the parse tree
	 */
	void exitTerm_prime(ExprParser.Term_primeContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#factor}.
	 * @param ctx the parse tree
	 */
	void enterFactor(ExprParser.FactorContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#factor}.
	 * @param ctx the parse tree
	 */
	void exitFactor(ExprParser.FactorContext ctx);
}