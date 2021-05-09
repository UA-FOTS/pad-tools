import sys
from pad.formula.Formula import Formula


def main(fname):
    formula = Formula.fromFile(fname)
    print(str(formula))
    formula.getExpression().dumpDot("exp.dot")
    lnf = formula.getExpression().LNF()
    print(str(lnf))
    lnf.dumpDot("lnf-exp.dot")
    for s in lnf.allConsSystems():
        print("System: ")
        for p in s:
            print(str(p))
        print("System end")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Expected an argument: input file name", file=sys.stderr)
        sys.exit(1)
    main(sys.argv[1])
    sys.exit(0)
