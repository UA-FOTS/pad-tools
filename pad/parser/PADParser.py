# Generated from PAD.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("X\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2")
        buf.write("\3\2\5\2\21\n\2\3\3\3\3\3\3\3\3\3\3\3\3\5\3\31\n\3\3\4")
        buf.write("\3\4\5\4\35\n\4\3\4\3\4\3\4\3\4\3\4\5\4$\n\4\3\4\5\4\'")
        buf.write("\n\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4/\n\4\f\4\16\4\62\13\4")
        buf.write("\3\5\3\5\3\5\3\5\3\6\3\6\5\6:\n\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\5\6A\n\6\3\6\3\6\5\6E\n\6\3\6\5\6H\n\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\7\6S\n\6\f\6\16\6V\13\6\3\6\2\4")
        buf.write("\6\n\7\2\4\6\b\n\2\2\2a\2\20\3\2\2\2\4\30\3\2\2\2\6&\3")
        buf.write("\2\2\2\b\63\3\2\2\2\nG\3\2\2\2\f\r\5\4\3\2\r\16\5\6\4")
        buf.write("\2\16\21\3\2\2\2\17\21\5\6\4\2\20\f\3\2\2\2\20\17\3\2")
        buf.write("\2\2\21\3\3\2\2\2\22\23\7\f\2\2\23\24\7\16\2\2\24\31\5")
        buf.write("\4\3\2\25\26\7\f\2\2\26\27\7\16\2\2\27\31\7\3\2\2\30\22")
        buf.write("\3\2\2\2\30\25\3\2\2\2\31\5\3\2\2\2\32\34\b\4\1\2\33\35")
        buf.write("\7\6\2\2\34\33\3\2\2\2\34\35\3\2\2\2\35\36\3\2\2\2\36")
        buf.write("\37\7\7\2\2\37 \5\6\4\2 !\7\b\2\2!\'\3\2\2\2\"$\7\6\2")
        buf.write("\2#\"\3\2\2\2#$\3\2\2\2$%\3\2\2\2%\'\5\b\5\2&\32\3\2\2")
        buf.write("\2&#\3\2\2\2\'\60\3\2\2\2()\f\6\2\2)*\7\4\2\2*/\5\6\4")
        buf.write("\7+,\f\5\2\2,-\7\5\2\2-/\5\6\4\6.(\3\2\2\2.+\3\2\2\2/")
        buf.write("\62\3\2\2\2\60.\3\2\2\2\60\61\3\2\2\2\61\7\3\2\2\2\62")
        buf.write("\60\3\2\2\2\63\64\5\n\6\2\64\65\7\r\2\2\65\66\5\n\6\2")
        buf.write("\66\t\3\2\2\2\679\b\6\1\28:\7\13\2\298\3\2\2\29:\3\2\2")
        buf.write("\2:;\3\2\2\2;<\7\7\2\2<=\5\n\6\2=>\7\b\2\2>H\3\2\2\2?")
        buf.write("A\7\13\2\2@?\3\2\2\2@A\3\2\2\2AB\3\2\2\2BH\7\17\2\2CE")
        buf.write("\7\13\2\2DC\3\2\2\2DE\3\2\2\2EF\3\2\2\2FH\7\16\2\2G\67")
        buf.write("\3\2\2\2G@\3\2\2\2GD\3\2\2\2HT\3\2\2\2IJ\f\b\2\2JK\7\t")
        buf.write("\2\2KS\5\n\6\tLM\f\7\2\2MN\7\n\2\2NS\5\n\6\bOP\f\6\2\2")
        buf.write("PQ\7\13\2\2QS\5\n\6\7RI\3\2\2\2RL\3\2\2\2RO\3\2\2\2SV")
        buf.write("\3\2\2\2TR\3\2\2\2TU\3\2\2\2U\13\3\2\2\2VT\3\2\2\2\17")
        buf.write("\20\30\34#&.\609@DGRT")
        return buf.getvalue()


class PADParser ( Parser ):

    grammarFileName = "PAD.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "'&&'", "'||'", "'~'", "'('", "')'", 
                     "'*'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "QUANT", "BINOP", "VARIABLE", 
                      "INT", "WS" ]

    RULE_formula = 0
    RULE_quants = 1
    RULE_qfexpr = 2
    RULE_predicate = 3
    RULE_polynomial = 4

    ruleNames =  [ "formula", "quants", "qfexpr", "predicate", "polynomial" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    QUANT=10
    BINOP=11
    VARIABLE=12
    INT=13
    WS=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class FormulaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def quants(self):
            return self.getTypedRuleContext(PADParser.QuantsContext,0)


        def qfexpr(self):
            return self.getTypedRuleContext(PADParser.QfexprContext,0)


        def getRuleIndex(self):
            return PADParser.RULE_formula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormula" ):
                listener.enterFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormula" ):
                listener.exitFormula(self)




    def formula(self):

        localctx = PADParser.FormulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_formula)
        try:
            self.state = 14
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PADParser.QUANT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 10
                self.quants()
                self.state = 11
                self.qfexpr(0)
                pass
            elif token in [PADParser.T__3, PADParser.T__4, PADParser.T__8, PADParser.VARIABLE, PADParser.INT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 13
                self.qfexpr(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuantsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PADParser.RULE_quants

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class RecQuantContext(QuantsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PADParser.QuantsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def QUANT(self):
            return self.getToken(PADParser.QUANT, 0)
        def VARIABLE(self):
            return self.getToken(PADParser.VARIABLE, 0)
        def quants(self):
            return self.getTypedRuleContext(PADParser.QuantsContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRecQuant" ):
                listener.enterRecQuant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRecQuant" ):
                listener.exitRecQuant(self)


    class QuantContext(QuantsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PADParser.QuantsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def QUANT(self):
            return self.getToken(PADParser.QUANT, 0)
        def VARIABLE(self):
            return self.getToken(PADParser.VARIABLE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuant" ):
                listener.enterQuant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuant" ):
                listener.exitQuant(self)



    def quants(self):

        localctx = PADParser.QuantsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_quants)
        try:
            self.state = 22
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = PADParser.RecQuantContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 16
                self.match(PADParser.QUANT)
                self.state = 17
                self.match(PADParser.VARIABLE)
                self.state = 18
                self.quants()
                pass

            elif la_ == 2:
                localctx = PADParser.QuantContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 19
                self.match(PADParser.QUANT)
                self.state = 20
                self.match(PADParser.VARIABLE)
                self.state = 21
                self.match(PADParser.T__0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QfexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PADParser.RULE_qfexpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AndQFExprContext(QfexprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PADParser.QfexprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def qfexpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PADParser.QfexprContext)
            else:
                return self.getTypedRuleContext(PADParser.QfexprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndQFExpr" ):
                listener.enterAndQFExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndQFExpr" ):
                listener.exitAndQFExpr(self)


    class UnaQFExprContext(QfexprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PADParser.QfexprContext
            super().__init__(parser)
            self.neg = None # Token
            self.copyFrom(ctx)

        def qfexpr(self):
            return self.getTypedRuleContext(PADParser.QfexprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaQFExpr" ):
                listener.enterUnaQFExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaQFExpr" ):
                listener.exitUnaQFExpr(self)


    class UnaPredContext(QfexprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PADParser.QfexprContext
            super().__init__(parser)
            self.neg = None # Token
            self.copyFrom(ctx)

        def predicate(self):
            return self.getTypedRuleContext(PADParser.PredicateContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaPred" ):
                listener.enterUnaPred(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaPred" ):
                listener.exitUnaPred(self)


    class OrQFExprContext(QfexprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PADParser.QfexprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def qfexpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PADParser.QfexprContext)
            else:
                return self.getTypedRuleContext(PADParser.QfexprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrQFExpr" ):
                listener.enterOrQFExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrQFExpr" ):
                listener.exitOrQFExpr(self)



    def qfexpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PADParser.QfexprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_qfexpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = PADParser.UnaQFExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 26
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==PADParser.T__3:
                    self.state = 25
                    localctx.neg = self.match(PADParser.T__3)


                self.state = 28
                self.match(PADParser.T__4)
                self.state = 29
                self.qfexpr(0)
                self.state = 30
                self.match(PADParser.T__5)
                pass

            elif la_ == 2:
                localctx = PADParser.UnaPredContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==PADParser.T__3:
                    self.state = 32
                    localctx.neg = self.match(PADParser.T__3)


                self.state = 35
                self.predicate()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 46
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 44
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = PADParser.AndQFExprContext(self, PADParser.QfexprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_qfexpr)
                        self.state = 38
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 39
                        self.match(PADParser.T__1)
                        self.state = 40
                        self.qfexpr(5)
                        pass

                    elif la_ == 2:
                        localctx = PADParser.OrQFExprContext(self, PADParser.QfexprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_qfexpr)
                        self.state = 41
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 42
                        self.match(PADParser.T__2)
                        self.state = 43
                        self.qfexpr(4)
                        pass

             
                self.state = 48
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PredicateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PADParser.RULE_predicate

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PredContext(PredicateContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PADParser.PredicateContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def polynomial(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PADParser.PolynomialContext)
            else:
                return self.getTypedRuleContext(PADParser.PolynomialContext,i)

        def BINOP(self):
            return self.getToken(PADParser.BINOP, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPred" ):
                listener.enterPred(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPred" ):
                listener.exitPred(self)



    def predicate(self):

        localctx = PADParser.PredicateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_predicate)
        try:
            localctx = PADParser.PredContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.polynomial(0)
            self.state = 50
            self.match(PADParser.BINOP)
            self.state = 51
            self.polynomial(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PolynomialContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PADParser.RULE_polynomial

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class UnaIntContext(PolynomialContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PADParser.PolynomialContext
            super().__init__(parser)
            self.neg = None # Token
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(PADParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaInt" ):
                listener.enterUnaInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaInt" ):
                listener.exitUnaInt(self)


    class SumPolyContext(PolynomialContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PADParser.PolynomialContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def polynomial(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PADParser.PolynomialContext)
            else:
                return self.getTypedRuleContext(PADParser.PolynomialContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSumPoly" ):
                listener.enterSumPoly(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSumPoly" ):
                listener.exitSumPoly(self)


    class UnaPolyContext(PolynomialContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PADParser.PolynomialContext
            super().__init__(parser)
            self.neg = None # Token
            self.copyFrom(ctx)

        def polynomial(self):
            return self.getTypedRuleContext(PADParser.PolynomialContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaPoly" ):
                listener.enterUnaPoly(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaPoly" ):
                listener.exitUnaPoly(self)


    class UnaVarContext(PolynomialContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PADParser.PolynomialContext
            super().__init__(parser)
            self.neg = None # Token
            self.copyFrom(ctx)

        def VARIABLE(self):
            return self.getToken(PADParser.VARIABLE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaVar" ):
                listener.enterUnaVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaVar" ):
                listener.exitUnaVar(self)


    class MultPolyContext(PolynomialContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PADParser.PolynomialContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def polynomial(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PADParser.PolynomialContext)
            else:
                return self.getTypedRuleContext(PADParser.PolynomialContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultPoly" ):
                listener.enterMultPoly(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultPoly" ):
                listener.exitMultPoly(self)


    class SubPolyContext(PolynomialContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PADParser.PolynomialContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def polynomial(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PADParser.PolynomialContext)
            else:
                return self.getTypedRuleContext(PADParser.PolynomialContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubPoly" ):
                listener.enterSubPoly(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubPoly" ):
                listener.exitSubPoly(self)



    def polynomial(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PADParser.PolynomialContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_polynomial, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                localctx = PADParser.UnaPolyContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==PADParser.T__8:
                    self.state = 54
                    localctx.neg = self.match(PADParser.T__8)


                self.state = 57
                self.match(PADParser.T__4)
                self.state = 58
                self.polynomial(0)
                self.state = 59
                self.match(PADParser.T__5)
                pass

            elif la_ == 2:
                localctx = PADParser.UnaIntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==PADParser.T__8:
                    self.state = 61
                    localctx.neg = self.match(PADParser.T__8)


                self.state = 64
                self.match(PADParser.INT)
                pass

            elif la_ == 3:
                localctx = PADParser.UnaVarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==PADParser.T__8:
                    self.state = 65
                    localctx.neg = self.match(PADParser.T__8)


                self.state = 68
                self.match(PADParser.VARIABLE)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 82
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 80
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = PADParser.MultPolyContext(self, PADParser.PolynomialContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_polynomial)
                        self.state = 71
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 72
                        self.match(PADParser.T__6)
                        self.state = 73
                        self.polynomial(7)
                        pass

                    elif la_ == 2:
                        localctx = PADParser.SumPolyContext(self, PADParser.PolynomialContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_polynomial)
                        self.state = 74
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 75
                        self.match(PADParser.T__7)
                        self.state = 76
                        self.polynomial(6)
                        pass

                    elif la_ == 3:
                        localctx = PADParser.SubPolyContext(self, PADParser.PolynomialContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_polynomial)
                        self.state = 77
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 78
                        self.match(PADParser.T__8)
                        self.state = 79
                        self.polynomial(5)
                        pass

             
                self.state = 84
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.qfexpr_sempred
        self._predicates[4] = self.polynomial_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def qfexpr_sempred(self, localctx:QfexprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

    def polynomial_sempred(self, localctx:PolynomialContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         




