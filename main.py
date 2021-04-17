import sys
from antlr4 import CommonTokenStream, FileStream, ParseTreeWalker
from formula.LinearPolynomial import LinearPolynomial
from parser.PADLexer import PADLexer
from parser.PADListener import PADListener
from parser.PADParser import PADParser


class FormBuilder(PADListener):
    def exitUnaInt(self, ctx):
        coefficient = int(ctx.INT().getText())
        if ctx.neg is not None:
            coefficient *= -1
        ctx.poly = LinearPolynomial({"": coefficient})
        print(ctx.poly)

    def exitUnaVar(self, ctx):
        coefficient = 1
        if ctx.neg is not None:
            coefficient *= -1
        ctx.poly = LinearPolynomial({ctx.VARIABLE().getText(): coefficient})
        print("unavar " + str(ctx.poly))

    def exitUnaPoly(self, ctx):
        ctx.poly = ctx.polynomial().poly
        if ctx.neg is not None:
            ctx.poly.negate()
        print("unapoly " + str(ctx.poly))

    def exitSumPoly(self, ctx):
        ctx.poly = ctx.polynomial(0).poly + ctx.polynomial(1).poly
        print("sum " + str(ctx.poly))

    def exitSubPoly(self, ctx):
        ctx.poly = ctx.polynomial(0).poly - ctx.polynomial(1).poly
        print(ctx.poly)

    def exitMultPoly(self, ctx):
        ctx.poly = ctx.polynomial(0).poly * ctx.polynomial(1).poly
        print("left " + ctx.polynomial(0).getText() + " = " + str(ctx.polynomial(0).poly))
        print("right " + ctx.polynomial(1).getText() + " = " +
                str(ctx.polynomial(1).poly))
        print("prod " + str(ctx.poly))


def main(fname):
    input_stream = FileStream(fname)
    lexer = PADLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = PADParser(stream)
    tree = parser.formula()
    # we can traverse the concrete tree and create
    # our internal-representation tree now
    builder = FormBuilder()
    walker = ParseTreeWalker()
    walker.walk(builder, tree)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Expected an argument: input file name", file=sys.stderr)
        sys.exit(1)
    main(sys.argv[1])
    sys.exit(0)
