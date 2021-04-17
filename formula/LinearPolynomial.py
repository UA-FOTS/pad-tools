class LinearPolynomial:
    def __init__(self, coeffs):
        self.poly = coeffs

    def negate(self):
        for k in self.poly:
            self.poly[k] *= -1

    def __add__(self, f):
        g = dict(self.poly)
        for k in f.poly:
            if k in self.poly:
                g[k] += f.poly[k]
            else:
                g[k] = f.poly[k]
        return LinearPolynomial(g)

    def __sub__(self, f):
        g = dict(self.poly)
        for k in f.poly:
            if k in self.poly:
                g[k] -= f.poly[k]
            else:
                g[k] = f.poly[k]
        return LinearPolynomial(g)

    def __mul__(self, f):
        # Either self is a constant polynomial
        if len(self.poly.keys()) == 1 and "" in self.poly:
            g = dict(f.poly)
            for k in f.poly:
                g[k] *= self.poly[""]
            return LinearPolynomial(g)
        # or f is the constant
        elif len(f.poly.keys()) == 1 and "" in f.poly:
            f = dict(self.poly)
            for k in self.poly:
                g[k] *= f.poly[""]
            return LinearPolynomial(g)
        else:
            raise Exception("Found a nonlinear polynomial!")

    def __str__(self):
        return self.poly.__str__()

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.poly == other.poly
