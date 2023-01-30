import cmath
from math import pi, cos, sin

class Complex:
    value: complex

    def __init__(self, v: complex):
        self.value = v

    def __str__(self) -> str:
        mod, pol = cmath.polar(self.value)

        return f"{mod} ∠ {pol * 180 / pi}°"

    def __repr__(self) -> str:
        return self.__str__()

    def __oper(self, other, op):
        if isinstance(other, int) or isinstance(other, float) or isinstance(other, complex):
            return Complex(op(self.value, other))

        return Complex(op(self.value, other.value))

    def __add__(self, other):
        return self.__oper(other, lambda x, y: x + y)

    def __radd__(self, other):
        return self.__oper(other, lambda x, y: x + y)

    def __sub__(self, other):
        return self.__oper(other, lambda x, y: x - y)

    def __mul__(self, other):
        return self.__oper(other, lambda x, y: x * y)

    def __rmul__(self, other):
        return self.__oper(other, lambda x, y: x * y)

    def __truediv__(self, other):
        return self.__oper(other, lambda x, y: x / y)

def pol(mod: float, deg: float):
    return Complex(cmath.rect(mod, deg * pi / 180))

# Resistência da fonte
Rin = 50
# Resistor
R = 560
# Indutor
L = 10 ** (-3)
# Capacitor
C = 100 * 10 ** (-9)

w = lambda f : 2 * pi * f

Zrin = Rin
Zr = R
Zl = lambda f : 1j * w(f) * L
Zc = lambda f : 1 / (1j * w(f) * C)

V = pol(1, 0)
I = lambda f : V / (Zrin + Zr + Zl(f) + Zc(f))

Vrin = lambda f : I(f) * Zrin
Vr = lambda f : I(f) * Zr
Vl = lambda f : I(f) * Zl(f)
Vc = lambda f : I(f) * Zc(f)
