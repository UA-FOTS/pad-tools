import sys
import numpy as np
from linarith.semilinear.HyLinSet import HyLinSet
# from pad.formula.Formula import Formula


def main(fname):
    #    formula = Formula.fromFile(fname)
    #    print(str(formula))
    #    formula.getExpression().dumpDot("exp.dot")
    #    lnf = formula.getExpression().LNF()
    #    print(str(lnf))
    #    lnf.dumpDot("lnf-exp.dot")
    #    for s in lnf.allConsSystems():
    #        print("System: ")
    #        for p in s:
    #            print(str(p))
    #        print("System end")
    A = np.array([[4, 1],
                  [2, 2]])
    b = np.array([0, 0]).transpose()
    slset = HyLinSet(None, None, A, b)
    print(str(slset))
    print(str(np.array([0, 0]).transpose() in slset))
    print(str(np.array([-1, 1]).transpose() in slset))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Expected an argument: input file name", file=sys.stderr)
        sys.exit(1)
    main(sys.argv[1])
    sys.exit(0)
