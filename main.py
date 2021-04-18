import sys
from antlr4 import CommonTokenStream, FileStream, ParseTreeWalker
from pad.parser.PADLexer import PADLexer
from pad.parser.FormulaBuilder import FormulaBuilder
from pad.parser.PADParser import PADParser


def main(fname):
    input_stream = FileStream(fname)
    lexer = PADLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = PADParser(stream)
    tree = parser.formula()
    # we can traverse the concrete tree and create
    # our internal-representation tree now
    builder = FormulaBuilder()
    walker = ParseTreeWalker()
    walker.walk(builder, tree)
    print(str(builder.getFormula()))
    builder.getFormula().getExpression().dumpDot("exp.dot")
    print(str(builder.getFormula().getExpression().eval({"x1": 2,
                                                         "x2": -5,
                                                         "y3": 8})))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Expected an argument: input file name", file=sys.stderr)
        sys.exit(1)
    main(sys.argv[1])
    sys.exit(0)
