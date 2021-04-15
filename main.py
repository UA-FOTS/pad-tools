import sys
from antlr4 import CommonTokenStream, FileStream, ParseTreeWalker
from parser.PADLexer import PADLexer
from parser.PADListener import PADListener
from parser.PADParser import PADParser


class FormBuilder(PADListener):
    def exitAtom(self, ctx):
        if ctx.INT() is not None:
            ctx.val = int(ctx.getText())
        else:
            ctx.val = ctx.getText()

    def exitUnaAtom(self, ctx):
        ctx.val = ctx.atom().val
        if ctx.neg is not None:
            print("neg ( " + str(ctx.val) + " )")


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
