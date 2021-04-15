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
        buf.write("O\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\5\3\30\n\3\3\4\3\4\5")
        buf.write("\4\34\n\4\3\4\3\4\3\4\3\4\3\4\5\4#\n\4\3\4\5\4&\n\4\3")
        buf.write("\4\3\4\3\4\7\4+\n\4\f\4\16\4.\13\4\3\5\3\5\3\5\3\5\3\6")
        buf.write("\3\6\5\6\66\n\6\3\6\3\6\3\6\3\6\3\6\5\6=\n\6\3\6\5\6@")
        buf.write("\n\6\3\6\3\6\3\6\3\6\3\6\3\6\7\6H\n\6\f\6\16\6K\13\6\3")
        buf.write("\7\3\7\3\7\2\4\6\n\b\2\4\6\b\n\f\2\7\3\2\3\4\3\2\6\7\3")
        buf.write("\2\13\21\3\2\23\24\3\2\25\26\2R\2\16\3\2\2\2\4\27\3\2")
        buf.write("\2\2\6%\3\2\2\2\b/\3\2\2\2\n?\3\2\2\2\fL\3\2\2\2\16\17")
        buf.write("\5\4\3\2\17\20\5\6\4\2\20\3\3\2\2\2\21\22\t\2\2\2\22\23")
        buf.write("\7\25\2\2\23\30\5\4\3\2\24\25\t\2\2\2\25\26\7\25\2\2\26")
        buf.write("\30\7\5\2\2\27\21\3\2\2\2\27\24\3\2\2\2\30\5\3\2\2\2\31")
        buf.write("\33\b\4\1\2\32\34\7\b\2\2\33\32\3\2\2\2\33\34\3\2\2\2")
        buf.write("\34\35\3\2\2\2\35\36\7\t\2\2\36\37\5\6\4\2\37 \7\n\2\2")
        buf.write(" &\3\2\2\2!#\7\b\2\2\"!\3\2\2\2\"#\3\2\2\2#$\3\2\2\2$")
        buf.write("&\5\b\5\2%\31\3\2\2\2%\"\3\2\2\2&,\3\2\2\2\'(\f\5\2\2")
        buf.write("()\t\3\2\2)+\5\6\4\6*\'\3\2\2\2+.\3\2\2\2,*\3\2\2\2,-")
        buf.write("\3\2\2\2-\7\3\2\2\2.,\3\2\2\2/\60\5\n\6\2\60\61\t\4\2")
        buf.write("\2\61\62\5\n\6\2\62\t\3\2\2\2\63\65\b\6\1\2\64\66\7\24")
        buf.write("\2\2\65\64\3\2\2\2\65\66\3\2\2\2\66\67\3\2\2\2\678\7\t")
        buf.write("\2\289\5\n\6\29:\7\n\2\2:@\3\2\2\2;=\7\24\2\2<;\3\2\2")
        buf.write("\2<=\3\2\2\2=>\3\2\2\2>@\5\f\7\2?\63\3\2\2\2?<\3\2\2\2")
        buf.write("@I\3\2\2\2AB\f\6\2\2BC\7\22\2\2CH\5\n\6\7DE\f\5\2\2EF")
        buf.write("\t\5\2\2FH\5\n\6\6GA\3\2\2\2GD\3\2\2\2HK\3\2\2\2IG\3\2")
        buf.write("\2\2IJ\3\2\2\2J\13\3\2\2\2KI\3\2\2\2LM\t\6\2\2M\r\3\2")
        buf.write("\2\2\f\27\33\"%,\65<?GI")
        return buf.getvalue()


class PADParser ( Parser ):

    grammarFileName = "PAD.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'E'", "'A'", "':'", "'||'", "'&&'", "'~'", 
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
    RULE_atom = 5

    ruleNames =  [ "formula", "quants", "qfexpr", "predicate", "polynomial", 
                   "atom" ]

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
            self.state = 12
            self.quants()
            self.state = 13
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
            self.state = 21
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                localctx = PADParser.RecQuantContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                localctx.quant = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==PADParser.T__0 or _la==PADParser.T__1):
                    localctx.quant = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 16
                self.match(PADParser.VARIABLE)
                self.state = 17
                self.quants()
                pass

            elif la_ == 2:
                localctx = PADParser.QuantContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                localctx.quant = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==PADParser.T__0 or _la==PADParser.T__1):
                    localctx.quant = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 19
                self.match(PADParser.VARIABLE)
                self.state = 20
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


    class BinQFExprContext(QfexprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PADParser.QfexprContext
            super().__init__(parser)
            self.boolop = None # Token
            self.copyFrom(ctx)

        def qfexpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PADParser.QfexprContext)
            else:
                return self.getTypedRuleContext(PADParser.QfexprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinQFExpr" ):
                listener.enterBinQFExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinQFExpr" ):
                listener.exitBinQFExpr(self)


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
            self.state = 35
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = PADParser.UnaQFExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==PADParser.T__5:
                    self.state = 24
                    localctx.neg = self.match(PADParser.T__5)


                self.state = 27
                self.match(PADParser.T__6)
                self.state = 28
                self.qfexpr(0)
                self.state = 29
                self.match(PADParser.T__7)
                pass

            elif la_ == 2:
                localctx = PADParser.UnaPredContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==PADParser.T__5:
                    self.state = 31
                    localctx.neg = self.match(PADParser.T__5)


                self.state = 34
                self.predicate()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 42
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PADParser.BinQFExprContext(self, PADParser.QfexprContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_qfexpr)
                    self.state = 37
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 38
                    localctx.boolop = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==PADParser.T__3 or _la==PADParser.T__4):
                        localctx.boolop = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 39
                    self.qfexpr(4) 
                self.state = 44
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

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
            self.state = 45
            self.polynomial(0)
            self.state = 46
            localctx.pred = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PADParser.T__8) | (1 << PADParser.T__9) | (1 << PADParser.T__10) | (1 << PADParser.T__11) | (1 << PADParser.T__12) | (1 << PADParser.T__13) | (1 << PADParser.T__14))) != 0)):
                localctx.pred = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 47
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


    class UnaAtomContext(PolynomialContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PADParser.PolynomialContext
            super().__init__(parser)
            self.neg = None # Token
            self.copyFrom(ctx)

        def atom(self):
            return self.getTypedRuleContext(PADParser.AtomContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaAtom" ):
                listener.enterUnaAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaAtom" ):
                listener.exitUnaAtom(self)


    class SumPolyContext(PolynomialContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PADParser.PolynomialContext
            super().__init__(parser)
            self.op = None # Token
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
            self.state = 61
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = PADParser.UnaPolyContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==PADParser.T__17:
                    self.state = 50
                    localctx.neg = self.match(PADParser.T__17)


                self.state = 53
                self.match(PADParser.T__6)
                self.state = 54
                self.polynomial(0)
                self.state = 55
                self.match(PADParser.T__7)
                pass

            elif la_ == 2:
                localctx = PADParser.UnaAtomContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==PADParser.T__17:
                    self.state = 57
                    localctx.neg = self.match(PADParser.T__17)


                self.state = 60
                self.atom()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 71
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 69
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = PADParser.MultPolyContext(self, PADParser.PolynomialContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_polynomial)
                        self.state = 63
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 64
                        self.match(PADParser.T__15)
                        self.state = 65
                        self.polynomial(5)
                        pass

                    elif la_ == 2:
                        localctx = PADParser.SumPolyContext(self, PADParser.PolynomialContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_polynomial)
                        self.state = 66
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 67
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==PADParser.T__16 or _la==PADParser.T__17):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 68
                        self.polynomial(4)
                        pass

             
                self.state = 73
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(PADParser.INT, 0)

        def VARIABLE(self):
            return self.getToken(PADParser.VARIABLE, 0)

        def getRuleIndex(self):
            return PADParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)




    def atom(self):

        localctx = PADParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            _la = self._input.LA(1)
            if not(_la==PADParser.VARIABLE or _la==PADParser.INT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
                return self.precpred(self._ctx, 3)
         

    def polynomial_sempred(self, localctx:PolynomialContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         




