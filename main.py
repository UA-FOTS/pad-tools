import sys
from antlr4 import CommonTokenStream, FileStream
from parser.PADLexer import PADLexer
from parser.PADParser import PADParser


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = PADLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = PADParser(stream)
    tree = parser.formula()
    print(tree.toStringTree(recog=parser))


if __name__ == '__main__':
    main(sys.argv)
