// Generated from d:/Mis trabajos/6to semestre/Lenguajes y automatas II/Lenguajes-y-Automatas-II/practicas2/words_analyzer/backend/Words.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link WordsParser}.
 */
public interface WordsListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link WordsParser#texto}.
	 * @param ctx the parse tree
	 */
	void enterTexto(WordsParser.TextoContext ctx);
	/**
	 * Exit a parse tree produced by {@link WordsParser#texto}.
	 * @param ctx the parse tree
	 */
	void exitTexto(WordsParser.TextoContext ctx);
	/**
	 * Enter a parse tree produced by {@link WordsParser#seccion_mes}.
	 * @param ctx the parse tree
	 */
	void enterSeccion_mes(WordsParser.Seccion_mesContext ctx);
	/**
	 * Exit a parse tree produced by {@link WordsParser#seccion_mes}.
	 * @param ctx the parse tree
	 */
	void exitSeccion_mes(WordsParser.Seccion_mesContext ctx);
	/**
	 * Enter a parse tree produced by {@link WordsParser#fruta}.
	 * @param ctx the parse tree
	 */
	void enterFruta(WordsParser.FrutaContext ctx);
	/**
	 * Exit a parse tree produced by {@link WordsParser#fruta}.
	 * @param ctx the parse tree
	 */
	void exitFruta(WordsParser.FrutaContext ctx);
	/**
	 * Enter a parse tree produced by {@link WordsParser#otro}.
	 * @param ctx the parse tree
	 */
	void enterOtro(WordsParser.OtroContext ctx);
	/**
	 * Exit a parse tree produced by {@link WordsParser#otro}.
	 * @param ctx the parse tree
	 */
	void exitOtro(WordsParser.OtroContext ctx);
}