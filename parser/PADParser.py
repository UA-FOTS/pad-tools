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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\27")
        buf.write("U\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\5\3\26\n\3\3\4\3\4\5\4\32\n\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\5\4!\n\4\3\4\5\4$\n\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\7\4,\n\4\f\4\16\4/\13\4\3\5\3\5\3\5\3\5\3")
        buf.write("\6\3\6\5\6\67\n\6\3\6\3\6\3\6\3\6\3\6\5\6>\n\6\3\6\3\6")
        buf.write("\5\6B\n\6\3\6\5\6E\n\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\7\6P\n\6\f\6\16\6S\13\6\3\6\2\4\6\n\7\2\4\6\b\n\2")
        buf.write("\4\3\2\3\4\3\2\13\21\2]\2\f\3\2\2\2\4\25\3\2\2\2\6#\3")
        buf.write("\2\2\2\b\60\3\2\2\2\nD\3\2\2\2\f\r\5\4\3\2\r\16\5\6\4")
        buf.write("\2\16\3\3\2\2\2\17\20\t\2\2\2\20\21\7\25\2\2\21\26\5\4")
        buf.write("\3\2\22\23\t\2\2\2\23\24\7\25\2\2\24\26\7\5\2\2\25\17")
        buf.write("\3\2\2\2\25\22\3\2\2\2\26\5\3\2\2\2\27\31\b\4\1\2\30\32")
        buf.write("\7\b\2\2\31\30\3\2\2\2\31\32\3\2\2\2\32\33\3\2\2\2\33")
        buf.write("\34\7\t\2\2\34\35\5\6\4\2\35\36\7\n\2\2\36$\3\2\2\2\37")
        buf.write("!\7\b\2\2 \37\3\2\2\2 !\3\2\2\2!\"\3\2\2\2\"$\5\b\5\2")
        buf.write("#\27\3\2\2\2# \3\2\2\2$-\3\2\2\2%&\f\6\2\2&\'\7\6\2\2")
        buf.write("\',\5\6\4\7()\f\5\2\2)*\7\7\2\2*,\5\6\4\6+%\3\2\2\2+(")
        buf.write("\3\2\2\2,/\3\2\2\2-+\3\2\2\2-.\3\2\2\2.\7\3\2\2\2/-\3")
        buf.write("\2\2\2\60\61\5\n\6\2\61\62\t\3\2\2\62\63\5\n\6\2\63\t")
        buf.write("\3\2\2\2\64\66\b\6\1\2\65\67\7\24\2\2\66\65\3\2\2\2\66")
        buf.write("\67\3\2\2\2\678\3\2\2\289\7\t\2\29:\5\n\6\2:;\7\n\2\2")
        buf.write(";E\3\2\2\2<>\7\24\2\2=<\3\2\2\2=>\3\2\2\2>?\3\2\2\2?E")
        buf.write("\7\26\2\2@B\7\24\2\2A@\3\2\2\2AB\3\2\2\2BC\3\2\2\2CE\7")
        buf.write("\25\2\2D\64\3\2\2\2D=\3\2\2\2DA\3\2\2\2EQ\3\2\2\2FG\f")
        buf.write("\b\2\2GH\7\22\2\2HP\5\n\6\tIJ\f\7\2\2JK\7\23\2\2KP\5\n")
        buf.write("\6\bLM\f\6\2\2MN\7\24\2\2NP\5\n\6\7OF\3\2\2\2OI\3\2\2")
        buf.write("\2OL\3\2\2\2PS\3\2\2\2QO\3\2\2\2QR\3\2\2\2R\13\3\2\2\2")
        buf.write("SQ\3\2\2\2\16\25\31 #+-\66=ADOQ")
        return buf.getvalue()


class PADParser ( Parser ):

    grammarFileName = "PAD.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'E'", "'A'", "':'", "'&&'", "'||'", "'~'", 
                     "'('", "')'", "'='", "'!='", "'<'", "'<='", "'>'", 
                     "'>='", "'|'", "'*'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "VARIABLE", 
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
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    VARIABLE=19
    INT=20
    WS=21

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
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.quants()
            self.state = 11
            self.qfexpr(0)
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
            self.quant = None # Token
            self.copyFrom(ctx)

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
            self.quant = None # Token
            self.copyFrom(ctx)

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
        self._la = 0 # Token type
        try:
            self.state = 19
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                localctx = PADParser.RecQuantContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                localctx.quant = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==PADParser.T__0 or _la==PADParser.T__1):
                    localctx.quant = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 14
                self.match(PADParser.VARIABLE)
                self.state = 15
                self.quants()
                pass

            elif la_ == 2:
                localctx = PADParser.QuantContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                localctx.quant = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==PADParser.T__0 or _la==PADParser.T__1):
                    localctx.quant = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 17
                self.match(PADParser.VARIABLE)
                self.state = 18
                self.match(PADParser.T__2)
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
            self.state = 33
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = PADParser.UnaQFExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==PADParser.T__5:
                    self.state = 22
                    localctx.neg = self.match(PADParser.T__5)


                self.state = 25
                self.match(PADParser.T__6)
                self.state = 26
                self.qfexpr(0)
                self.state = 27
                self.match(PADParser.T__7)
                pass

            elif la_ == 2:
                localctx = PADParser.UnaPredContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 30
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==PADParser.T__5:
                    self.state = 29
                    localctx.neg = self.match(PADParser.T__5)


                self.state = 32
                self.predicate()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 43
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 41
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = PADParser.AndQFExprContext(self, PADParser.QfexprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_qfexpr)
                        self.state = 35
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 36
                        self.match(PADParser.T__3)
                        self.state = 37
                        self.qfexpr(5)
                        pass

                    elif la_ == 2:
                        localctx = PADParser.OrQFExprContext(self, PADParser.QfexprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_qfexpr)
                        self.state = 38
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 39
                        self.match(PADParser.T__4)
                        self.state = 40
                        self.qfexpr(4)
                        pass

             
                self.state = 45
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

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
            self.pred = None # Token
            self.copyFrom(ctx)

        def polynomial(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PADParser.PolynomialContext)
            else:
                return self.getTypedRuleContext(PADParser.PolynomialContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPred" ):
                listener.enterPred(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPred" ):
                listener.exitPred(self)



    def predicate(self):

        localctx = PADParser.PredicateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_predicate)
        self._la = 0 # Token type
        try:
            localctx = PADParser.PredContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.polynomial(0)
            self.state = 47
            localctx.pred = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PADParser.T__8) | (1 << PADParser.T__9) | (1 << PADParser.T__10) | (1 << PADParser.T__11) | (1 << PADParser.T__12) | (1 << PADParser.T__13) | (1 << PADParser.T__14))) != 0)):
                localctx.pred = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 48
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
            self.state = 66
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                localctx = PADParser.UnaPolyContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==PADParser.T__17:
                    self.state = 51
                    localctx.neg = self.match(PADParser.T__17)


                self.state = 54
                self.match(PADParser.T__6)
                self.state = 55
                self.polynomial(0)
                self.state = 56
                self.match(PADParser.T__7)
                pass

            elif la_ == 2:
                localctx = PADParser.UnaIntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==PADParser.T__17:
                    self.state = 58
                    localctx.neg = self.match(PADParser.T__17)


                self.state = 61
                self.match(PADParser.INT)
                pass

            elif la_ == 3:
                localctx = PADParser.UnaVarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==PADParser.T__17:
                    self.state = 62
                    localctx.neg = self.match(PADParser.T__17)


                self.state = 65
                self.match(PADParser.VARIABLE)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 79
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 77
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        localctx = PADParser.MultPolyContext(self, PADParser.PolynomialContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_polynomial)
                        self.state = 68
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 69
                        self.match(PADParser.T__15)
                        self.state = 70
                        self.polynomial(7)
                        pass

                    elif la_ == 2:
                        localctx = PADParser.SumPolyContext(self, PADParser.PolynomialContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_polynomial)
                        self.state = 71
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 72
                        self.match(PADParser.T__16)
                        self.state = 73
                        self.polynomial(6)
                        pass

                    elif la_ == 3:
                        localctx = PADParser.SubPolyContext(self, PADParser.PolynomialContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_polynomial)
                        self.state = 74
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 75
                        self.match(PADParser.T__17)
                        self.state = 76
                        self.polynomial(5)
                        pass

             
                self.state = 81
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

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
         




