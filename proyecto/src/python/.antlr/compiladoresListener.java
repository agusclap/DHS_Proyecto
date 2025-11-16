// Generated from c:/Users/Agustin/Desktop/DHS/proyecto/src/python/compiladores.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link compiladoresParser}.
 */
public interface compiladoresListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#programa}.
	 * @param ctx the parse tree
	 */
	void enterPrograma(compiladoresParser.ProgramaContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#programa}.
	 * @param ctx the parse tree
	 */
	void exitPrograma(compiladoresParser.ProgramaContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#prototipo}.
	 * @param ctx the parse tree
	 */
	void enterPrototipo(compiladoresParser.PrototipoContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#prototipo}.
	 * @param ctx the parse tree
	 */
	void exitPrototipo(compiladoresParser.PrototipoContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#tfuncion}.
	 * @param ctx the parse tree
	 */
	void enterTfuncion(compiladoresParser.TfuncionContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#tfuncion}.
	 * @param ctx the parse tree
	 */
	void exitTfuncion(compiladoresParser.TfuncionContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#funcion}.
	 * @param ctx the parse tree
	 */
	void enterFuncion(compiladoresParser.FuncionContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#funcion}.
	 * @param ctx the parse tree
	 */
	void exitFuncion(compiladoresParser.FuncionContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#parametro}.
	 * @param ctx the parse tree
	 */
	void enterParametro(compiladoresParser.ParametroContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#parametro}.
	 * @param ctx the parse tree
	 */
	void exitParametro(compiladoresParser.ParametroContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#parametros}.
	 * @param ctx the parse tree
	 */
	void enterParametros(compiladoresParser.ParametrosContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#parametros}.
	 * @param ctx the parse tree
	 */
	void exitParametros(compiladoresParser.ParametrosContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#usofuncion}.
	 * @param ctx the parse tree
	 */
	void enterUsofuncion(compiladoresParser.UsofuncionContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#usofuncion}.
	 * @param ctx the parse tree
	 */
	void exitUsofuncion(compiladoresParser.UsofuncionContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#argumentos}.
	 * @param ctx the parse tree
	 */
	void enterArgumentos(compiladoresParser.ArgumentosContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#argumentos}.
	 * @param ctx the parse tree
	 */
	void exitArgumentos(compiladoresParser.ArgumentosContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#argumentosp}.
	 * @param ctx the parse tree
	 */
	void enterArgumentosp(compiladoresParser.ArgumentospContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#argumentosp}.
	 * @param ctx the parse tree
	 */
	void exitArgumentosp(compiladoresParser.ArgumentospContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#instrucciones}.
	 * @param ctx the parse tree
	 */
	void enterInstrucciones(compiladoresParser.InstruccionesContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#instrucciones}.
	 * @param ctx the parse tree
	 */
	void exitInstrucciones(compiladoresParser.InstruccionesContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#instruccion}.
	 * @param ctx the parse tree
	 */
	void enterInstruccion(compiladoresParser.InstruccionContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#instruccion}.
	 * @param ctx the parse tree
	 */
	void exitInstruccion(compiladoresParser.InstruccionContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#return}.
	 * @param ctx the parse tree
	 */
	void enterReturn(compiladoresParser.ReturnContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#return}.
	 * @param ctx the parse tree
	 */
	void exitReturn(compiladoresParser.ReturnContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#tdato}.
	 * @param ctx the parse tree
	 */
	void enterTdato(compiladoresParser.TdatoContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#tdato}.
	 * @param ctx the parse tree
	 */
	void exitTdato(compiladoresParser.TdatoContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#declaracionesp}.
	 * @param ctx the parse tree
	 */
	void enterDeclaracionesp(compiladoresParser.DeclaracionespContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#declaracionesp}.
	 * @param ctx the parse tree
	 */
	void exitDeclaracionesp(compiladoresParser.DeclaracionespContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#declaraciones}.
	 * @param ctx the parse tree
	 */
	void enterDeclaraciones(compiladoresParser.DeclaracionesContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#declaraciones}.
	 * @param ctx the parse tree
	 */
	void exitDeclaraciones(compiladoresParser.DeclaracionesContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#declaracion}.
	 * @param ctx the parse tree
	 */
	void enterDeclaracion(compiladoresParser.DeclaracionContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#declaracion}.
	 * @param ctx the parse tree
	 */
	void exitDeclaracion(compiladoresParser.DeclaracionContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#asignacion}.
	 * @param ctx the parse tree
	 */
	void enterAsignacion(compiladoresParser.AsignacionContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#asignacion}.
	 * @param ctx the parse tree
	 */
	void exitAsignacion(compiladoresParser.AsignacionContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#opal}.
	 * @param ctx the parse tree
	 */
	void enterOpal(compiladoresParser.OpalContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#opal}.
	 * @param ctx the parse tree
	 */
	void exitOpal(compiladoresParser.OpalContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#comparadores}.
	 * @param ctx the parse tree
	 */
	void enterComparadores(compiladoresParser.ComparadoresContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#comparadores}.
	 * @param ctx the parse tree
	 */
	void exitComparadores(compiladoresParser.ComparadoresContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#lor}.
	 * @param ctx the parse tree
	 */
	void enterLor(compiladoresParser.LorContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#lor}.
	 * @param ctx the parse tree
	 */
	void exitLor(compiladoresParser.LorContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#lorp}.
	 * @param ctx the parse tree
	 */
	void enterLorp(compiladoresParser.LorpContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#lorp}.
	 * @param ctx the parse tree
	 */
	void exitLorp(compiladoresParser.LorpContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#land}.
	 * @param ctx the parse tree
	 */
	void enterLand(compiladoresParser.LandContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#land}.
	 * @param ctx the parse tree
	 */
	void exitLand(compiladoresParser.LandContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#landp}.
	 * @param ctx the parse tree
	 */
	void enterLandp(compiladoresParser.LandpContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#landp}.
	 * @param ctx the parse tree
	 */
	void exitLandp(compiladoresParser.LandpContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#comp}.
	 * @param ctx the parse tree
	 */
	void enterComp(compiladoresParser.CompContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#comp}.
	 * @param ctx the parse tree
	 */
	void exitComp(compiladoresParser.CompContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#exp}.
	 * @param ctx the parse tree
	 */
	void enterExp(compiladoresParser.ExpContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#exp}.
	 * @param ctx the parse tree
	 */
	void exitExp(compiladoresParser.ExpContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#e}.
	 * @param ctx the parse tree
	 */
	void enterE(compiladoresParser.EContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#e}.
	 * @param ctx the parse tree
	 */
	void exitE(compiladoresParser.EContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#term}.
	 * @param ctx the parse tree
	 */
	void enterTerm(compiladoresParser.TermContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#term}.
	 * @param ctx the parse tree
	 */
	void exitTerm(compiladoresParser.TermContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#t}.
	 * @param ctx the parse tree
	 */
	void enterT(compiladoresParser.TContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#t}.
	 * @param ctx the parse tree
	 */
	void exitT(compiladoresParser.TContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#factor}.
	 * @param ctx the parse tree
	 */
	void enterFactor(compiladoresParser.FactorContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#factor}.
	 * @param ctx the parse tree
	 */
	void exitFactor(compiladoresParser.FactorContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#iwhile}.
	 * @param ctx the parse tree
	 */
	void enterIwhile(compiladoresParser.IwhileContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#iwhile}.
	 * @param ctx the parse tree
	 */
	void exitIwhile(compiladoresParser.IwhileContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#bloque}.
	 * @param ctx the parse tree
	 */
	void enterBloque(compiladoresParser.BloqueContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#bloque}.
	 * @param ctx the parse tree
	 */
	void exitBloque(compiladoresParser.BloqueContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#ifor}.
	 * @param ctx the parse tree
	 */
	void enterIfor(compiladoresParser.IforContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#ifor}.
	 * @param ctx the parse tree
	 */
	void exitIfor(compiladoresParser.IforContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#init}.
	 * @param ctx the parse tree
	 */
	void enterInit(compiladoresParser.InitContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#init}.
	 * @param ctx the parse tree
	 */
	void exitInit(compiladoresParser.InitContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#cond}.
	 * @param ctx the parse tree
	 */
	void enterCond(compiladoresParser.CondContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#cond}.
	 * @param ctx the parse tree
	 */
	void exitCond(compiladoresParser.CondContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#iter}.
	 * @param ctx the parse tree
	 */
	void enterIter(compiladoresParser.IterContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#iter}.
	 * @param ctx the parse tree
	 */
	void exitIter(compiladoresParser.IterContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#iif}.
	 * @param ctx the parse tree
	 */
	void enterIif(compiladoresParser.IifContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#iif}.
	 * @param ctx the parse tree
	 */
	void exitIif(compiladoresParser.IifContext ctx);
}