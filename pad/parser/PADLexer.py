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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\21")
        buf.write("a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\3\2\3\2")
        buf.write("\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\b\3")
        buf.write("\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\5\rH\n\r\3\16\3\16\3\16\7\16M\n")
        buf.write("\16\f\16\16\16P\13\16\3\17\6\17S\n\17\r\17\16\17T\3\20")
        buf.write("\6\20X\n\20\r\20\16\20Y\3\20\3\20\3\21\3\21\3\22\3\22")
        buf.write("\2\2\23\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f")
        buf.write("\27\r\31\16\33\17\35\20\37\21!\2#\2\3\2\5\5\2\13\f\17")
        buf.write("\17\"\"\4\2C\\c|\3\2\62;\2h\2\3\3\2\2\2\2\5\3\2\2\2\2")
        buf.write("\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3")
        buf.write("\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2")
        buf.write("\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2")
        buf.write("\2\3%\3\2\2\2\5\'\3\2\2\2\7)\3\2\2\2\t+\3\2\2\2\13.\3")
        buf.write("\2\2\2\r\61\3\2\2\2\17\63\3\2\2\2\21\65\3\2\2\2\23\67")
        buf.write("\3\2\2\2\259\3\2\2\2\27;\3\2\2\2\31G\3\2\2\2\33I\3\2\2")
        buf.write("\2\35R\3\2\2\2\37W\3\2\2\2!]\3\2\2\2#_\3\2\2\2%&\7G\2")
        buf.write("\2&\4\3\2\2\2\'(\7C\2\2(\6\3\2\2\2)*\7<\2\2*\b\3\2\2\2")
        buf.write("+,\7(\2\2,-\7(\2\2-\n\3\2\2\2./\7~\2\2/\60\7~\2\2\60\f")
        buf.write("\3\2\2\2\61\62\7\u0080\2\2\62\16\3\2\2\2\63\64\7*\2\2")
        buf.write("\64\20\3\2\2\2\65\66\7+\2\2\66\22\3\2\2\2\678\7,\2\28")
        buf.write("\24\3\2\2\29:\7-\2\2:\26\3\2\2\2;<\7/\2\2<\30\3\2\2\2")
        buf.write("=H\7?\2\2>?\7#\2\2?H\7?\2\2@H\7>\2\2AB\7>\2\2BH\7?\2\2")
        buf.write("CH\7@\2\2DE\7@\2\2EH\7?\2\2FH\7\'\2\2G=\3\2\2\2G>\3\2")
        buf.write("\2\2G@\3\2\2\2GA\3\2\2\2GC\3\2\2\2GD\3\2\2\2GF\3\2\2\2")
        buf.write("H\32\3\2\2\2IN\5!\21\2JM\5!\21\2KM\5#\22\2LJ\3\2\2\2L")
        buf.write("K\3\2\2\2MP\3\2\2\2NL\3\2\2\2NO\3\2\2\2O\34\3\2\2\2PN")
        buf.write("\3\2\2\2QS\5#\22\2RQ\3\2\2\2ST\3\2\2\2TR\3\2\2\2TU\3\2")
        buf.write("\2\2U\36\3\2\2\2VX\t\2\2\2WV\3\2\2\2XY\3\2\2\2YW\3\2\2")
        buf.write("\2YZ\3\2\2\2Z[\3\2\2\2[\\\b\20\2\2\\ \3\2\2\2]^\t\3\2")
        buf.write("\2^\"\3\2\2\2_`\t\4\2\2`$\3\2\2\2\b\2GLNTY\3\b\2\2")
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
    T__9 = 10
    T__10 = 11
    BINOP = 12
    VARIABLE = 13
    INT = 14
    WS = 15

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'E'", "'A'", "':'", "'&&'", "'||'", "'~'", "'('", "')'", "'*'", 
            "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "BINOP", "VARIABLE", "INT", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "BINOP", "VARIABLE", 
                  "INT", "WS", "LETTER", "DIGIT" ]

    grammarFileName = "PAD.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None

