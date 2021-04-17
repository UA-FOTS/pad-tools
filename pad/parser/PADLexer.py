# Generated from PAD.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("]\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t")
        buf.write("\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\5\fD\n\f\3\r\3\r\3\r\7\rI\n\r\f\r\16\rL\13\r\3\16")
        buf.write("\6\16O\n\16\r\16\16\16P\3\17\6\17T\n\17\r\17\16\17U\3")
        buf.write("\17\3\17\3\20\3\20\3\21\3\21\2\2\22\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37")
        buf.write("\2!\2\3\2\6\4\2CCGG\5\2\13\f\17\17\"\"\4\2C\\c|\3\2\62")
        buf.write(";\2d\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2")
        buf.write("\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23")
        buf.write("\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3")
        buf.write("\2\2\2\2\35\3\2\2\2\3#\3\2\2\2\5%\3\2\2\2\7(\3\2\2\2\t")
        buf.write("+\3\2\2\2\13-\3\2\2\2\r/\3\2\2\2\17\61\3\2\2\2\21\63\3")
        buf.write("\2\2\2\23\65\3\2\2\2\25\67\3\2\2\2\27C\3\2\2\2\31E\3\2")
        buf.write("\2\2\33N\3\2\2\2\35S\3\2\2\2\37Y\3\2\2\2![\3\2\2\2#$\7")
        buf.write("<\2\2$\4\3\2\2\2%&\7(\2\2&\'\7(\2\2\'\6\3\2\2\2()\7~\2")
        buf.write("\2)*\7~\2\2*\b\3\2\2\2+,\7\u0080\2\2,\n\3\2\2\2-.\7*\2")
        buf.write("\2.\f\3\2\2\2/\60\7+\2\2\60\16\3\2\2\2\61\62\7,\2\2\62")
        buf.write("\20\3\2\2\2\63\64\7-\2\2\64\22\3\2\2\2\65\66\7/\2\2\66")
        buf.write("\24\3\2\2\2\678\t\2\2\28\26\3\2\2\29D\7?\2\2:;\7#\2\2")
        buf.write(";D\7?\2\2<D\7>\2\2=>\7>\2\2>D\7?\2\2?D\7@\2\2@A\7@\2\2")
        buf.write("AD\7?\2\2BD\7\'\2\2C9\3\2\2\2C:\3\2\2\2C<\3\2\2\2C=\3")
        buf.write("\2\2\2C?\3\2\2\2C@\3\2\2\2CB\3\2\2\2D\30\3\2\2\2EJ\5\37")
        buf.write("\20\2FI\5\37\20\2GI\5!\21\2HF\3\2\2\2HG\3\2\2\2IL\3\2")
        buf.write("\2\2JH\3\2\2\2JK\3\2\2\2K\32\3\2\2\2LJ\3\2\2\2MO\5!\21")
        buf.write("\2NM\3\2\2\2OP\3\2\2\2PN\3\2\2\2PQ\3\2\2\2Q\34\3\2\2\2")
        buf.write("RT\t\3\2\2SR\3\2\2\2TU\3\2\2\2US\3\2\2\2UV\3\2\2\2VW\3")
        buf.write("\2\2\2WX\b\17\2\2X\36\3\2\2\2YZ\t\4\2\2Z \3\2\2\2[\\\t")
        buf.write("\5\2\2\\\"\3\2\2\2\b\2CHJPU\3\b\2\2")
        return buf.getvalue()


class PADLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    QUANT = 10
    BINOP = 11
    VARIABLE = 12
    INT = 13
    WS = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':'", "'&&'", "'||'", "'~'", "'('", "')'", "'*'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "QUANT", "BINOP", "VARIABLE", "INT", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "QUANT", "BINOP", "VARIABLE", "INT", "WS", 
                  "LETTER", "DIGIT" ]

    grammarFileName = "PAD.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


