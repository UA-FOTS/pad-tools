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
        buf.write("]\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\5\3\30\n\3\3\4\3\4\5")
        buf.write("\4\34\n\4\3\4\3\4\3\4\3\4\3\4\5\4#\n\4\3\4\5\4&\n\4\3")
        buf.write("\4\3\4\3\4\7\4+\n\4\f\4\16\4.\13\4\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5@\n\5")
        buf.write("\3\6\3\6\5\6D\n\6\3\6\3\6\3\6\3\6\3\6\5\6K\n\6\3\6\5\6")
        buf.write("N\n\6\3\6\3\6\3\6\3\6\3\6\3\6\7\6V\n\6\f\6\16\6Y\13\6")
        buf.write("\3\7\3\7\3\7\2\4\6\n\b\2\4\6\b\n\f\2\t\3\2\3\4\3\2\6\7")
        buf.write("\3\2\13\f\3\2\r\16\3\2\17\20\3\2\23\24\3\2\25\26\2c\2")
        buf.write("\16\3\2\2\2\4\27\3\2\2\2\6%\3\2\2\2\b?\3\2\2\2\nM\3\2")
        buf.write("\2\2\fZ\3\2\2\2\16\17\5\4\3\2\17\20\5\6\4\2\20\3\3\2\2")
        buf.write("\2\21\22\t\2\2\2\22\23\7\25\2\2\23\30\5\4\3\2\24\25\t")
        buf.write("\2\2\2\25\26\7\25\2\2\26\30\7\5\2\2\27\21\3\2\2\2\27\24")
        buf.write("\3\2\2\2\30\5\3\2\2\2\31\33\b\4\1\2\32\34\7\b\2\2\33\32")
        buf.write("\3\2\2\2\33\34\3\2\2\2\34\35\3\2\2\2\35\36\7\t\2\2\36")
        buf.write("\37\5\6\4\2\37 \7\n\2\2 &\3\2\2\2!#\7\b\2\2\"!\3\2\2\2")
        buf.write("\"#\3\2\2\2#$\3\2\2\2$&\5\b\5\2%\31\3\2\2\2%\"\3\2\2\2")
        buf.write("&,\3\2\2\2\'(\f\5\2\2()\t\3\2\2)+\5\6\4\6*\'\3\2\2\2+")
        buf.write(".\3\2\2\2,*\3\2\2\2,-\3\2\2\2-\7\3\2\2\2.,\3\2\2\2/\60")
        buf.write("\5\n\6\2\60\61\t\4\2\2\61\62\5\n\6\2\62@\3\2\2\2\63\64")
        buf.write("\5\n\6\2\64\65\t\5\2\2\65\66\5\n\6\2\66@\3\2\2\2\678\5")
        buf.write("\n\6\289\t\6\2\29:\5\n\6\2:@\3\2\2\2;<\5\n\6\2<=\7\21")
        buf.write("\2\2=>\5\n\6\2>@\3\2\2\2?/\3\2\2\2?\63\3\2\2\2?\67\3\2")
        buf.write("\2\2?;\3\2\2\2@\t\3\2\2\2AC\b\6\1\2BD\7\24\2\2CB\3\2\2")
        buf.write("\2CD\3\2\2\2DE\3\2\2\2EF\7\t\2\2FG\5\n\6\2GH\7\n\2\2H")
        buf.write("N\3\2\2\2IK\7\24\2\2JI\3\2\2\2JK\3\2\2\2KL\3\2\2\2LN\5")
        buf.write("\f\7\2MA\3\2\2\2MJ\3\2\2\2NW\3\2\2\2OP\f\6\2\2PQ\7\22")
        buf.write("\2\2QV\5\n\6\7RS\f\5\2\2ST\t\7\2\2TV\5\n\6\6UO\3\2\2\2")
        buf.write("UR\3\2\2\2VY\3\2\2\2WU\3\2\2\2WX\3\2\2\2X\13\3\2\2\2Y")
        buf.write("W\3\2\2\2Z[\t\b\2\2[\r\3\2\2\2\r\27\33\"%,?CJMUW")
        return buf.getvalue()


class PADParser ( Parser ):

    grammarFileName = "PAD.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'E'", "'A'", "':'", "'||'", "'&&'", "'~'", 
                     "'('", "')'", "'='", "'!='", "'<'", "'<='", "'>'", 
                     "'>='", "'%'", "'*'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "VARIABLE", 
                      "INT", "WS" ]

    RULE_formula = 0
    RULE_quants = 1
    RULE_qf_expr = 2
    RULE_predicate = 3
    RULE_polynomial = 4
    RULE_atom = 5

    ruleNames =  [ "formula", "quants", "qf_expr", "predicate", "polynomial", 
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


        def qf_expr(self):
            return self.getTypedRuleContext(PADParser.Qf_exprContext,0)


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
            self.qf_expr(0)
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

        def VARIABLE(self):
            return self.getToken(PADParser.VARIABLE, 0)

        def quants(self):
            return self.getTypedRuleContext(PADParser.QuantsContext,0)


        def getRuleIndex(self):
            return PADParser.RULE_quants

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuants" ):
                listener.enterQuants(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuants" ):
                listener.exitQuants(self)




    def quants(self):

        localctx = PADParser.QuantsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_quants)
        self._la = 0 # Token type
        try:
            self.state = 21
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                _la = self._input.LA(1)
                if not(_la==PADParser.T__0 or _la==PADParser.T__1):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 16
                self.match(PADParser.VARIABLE)
                self.state = 17
                self.quants()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                _la = self._input.LA(1)
                if not(_la==PADParser.T__0 or _la==PADParser.T__1):
                    self._errHandler.recoverInline(self)
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


    class Qf_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def qf_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PADParser.Qf_exprContext)
            else:
                return self.getTypedRuleContext(PADParser.Qf_exprContext,i)


        def predicate(self):
            return self.getTypedRuleContext(PADParser.PredicateContext,0)


        def getRuleIndex(self):
            return PADParser.RULE_qf_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQf_expr" ):
                listener.enterQf_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQf_expr" ):
                listener.exitQf_expr(self)



    def qf_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PADParser.Qf_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_qf_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==PADParser.T__5:
                    self.state = 24
                    self.match(PADParser.T__5)


                self.state = 27
                self.match(PADParser.T__6)
                self.state = 28
                self.qf_expr(0)
                self.state = 29
                self.match(PADParser.T__7)
                pass

            elif la_ == 2:
                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==PADParser.T__5:
                    self.state = 31
                    self.match(PADParser.T__5)


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
                    localctx = PADParser.Qf_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_qf_expr)
                    self.state = 37
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 38
                    _la = self._input.LA(1)
                    if not(_la==PADParser.T__3 or _la==PADParser.T__4):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 39
                    self.qf_expr(4) 
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

        def polynomial(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PADParser.PolynomialContext)
            else:
                return self.getTypedRuleContext(PADParser.PolynomialContext,i)


        def getRuleIndex(self):
            return PADParser.RULE_predicate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPredicate" ):
                listener.enterPredicate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPredicate" ):
                listener.exitPredicate(self)




    def predicate(self):

        localctx = PADParser.PredicateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_predicate)
        self._la = 0 # Token type
        try:
            self.state = 61
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self.polynomial(0)
                self.state = 46
                _la = self._input.LA(1)
                if not(_la==PADParser.T__8 or _la==PADParser.T__9):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 47
                self.polynomial(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.polynomial(0)
                self.state = 50
                _la = self._input.LA(1)
                if not(_la==PADParser.T__10 or _la==PADParser.T__11):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 51
                self.polynomial(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 53
                self.polynomial(0)
                self.state = 54
                _la = self._input.LA(1)
                if not(_la==PADParser.T__12 or _la==PADParser.T__13):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 55
                self.polynomial(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 57
                self.polynomial(0)
                self.state = 58
                self.match(PADParser.T__14)
                self.state = 59
                self.polynomial(0)
                pass


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

        def polynomial(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PADParser.PolynomialContext)
            else:
                return self.getTypedRuleContext(PADParser.PolynomialContext,i)


        def atom(self):
            return self.getTypedRuleContext(PADParser.AtomContext,0)


        def getRuleIndex(self):
            return PADParser.RULE_polynomial

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPolynomial" ):
                listener.enterPolynomial(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPolynomial" ):
                listener.exitPolynomial(self)



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
            self.state = 75
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==PADParser.T__17:
                    self.state = 64
                    self.match(PADParser.T__17)


                self.state = 67
                self.match(PADParser.T__6)
                self.state = 68
                self.polynomial(0)
                self.state = 69
                self.match(PADParser.T__7)
                pass

            elif la_ == 2:
                self.state = 72
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==PADParser.T__17:
                    self.state = 71
                    self.match(PADParser.T__17)


                self.state = 74
                self.atom()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 85
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 83
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        localctx = PADParser.PolynomialContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_polynomial)
                        self.state = 77
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 78
                        self.match(PADParser.T__15)
                        self.state = 79
                        self.polynomial(5)
                        pass

                    elif la_ == 2:
                        localctx = PADParser.PolynomialContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_polynomial)
                        self.state = 80
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 81
                        _la = self._input.LA(1)
                        if not(_la==PADParser.T__16 or _la==PADParser.T__17):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 82
                        self.polynomial(4)
                        pass

             
                self.state = 87
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

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
            self.state = 88
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
        self._predicates[2] = self.qf_expr_sempred
        self._predicates[4] = self.polynomial_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def qf_expr_sempred(self, localctx:Qf_exprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

    def polynomial_sempred(self, localctx:PolynomialContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         




