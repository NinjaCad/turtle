def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n

class Fraction:
    def __init__(self, top, bottom):
        if bottom < 0:
            top = -top
            bottom = -bottom
        common = gcd(abs(top), abs(bottom))
        self.num = top // common
        self.den = bottom // common

    def __str__(self):
        common = gcd(self.num, self.den)
        return str(self.num // common) + "/" + str(self.den // common)

    def show(self):
        print(self.num, "/", self.den)

    def __add__(self,otherfraction):
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum
    
    def __sub__(self, other):
        newnum = self.num * other.den - self.den * other.num
        newden = self.den * other.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)
    
    def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)
    
    def __truediv__(self, other):
        if other.num == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        newnum = self.num * other.den
        newden = self.den * other.num
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)
    
    def __lt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum < secondnum
    
    def __le__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum <= secondnum
    
    def __gt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum > secondnum

    def __ge__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum >= secondnum

class MixedFraction(Fraction):
    def __init__(self, fraction):
        if not isinstance(fraction, Fraction):
            raise TypeError("MixedFraction requires a Fraction.")
        common = gcd(fraction.num, fraction.den)
        num = fraction.num // common
        den = fraction.den // common
        super().__init__(num, den)

    def __str__(self):
        num = self.num
        den = self.den
        if den < 0:
            num = -num
            den = -den
        whole = abs(num) // den
        remainder = abs(num) % den
        if remainder != 0:
            common = gcd(remainder, den)
            remainder //= common
            den //= common
        else:
            den = 1
        if num < 0:
            sign = "-"
        else:
            sign = ""
        return str(sign) + str(whole) + "_(" + str(remainder) + "/" + str(den) + ")"
        
    def __add__(self, other):
        result = super().__add__(other)
        return MixedFraction(result)
    
    def __sub__(self, other):
        result = super().__sub__(other)
        return MixedFraction(result)
    
    def __mul__(self, other):
        result = super().__mul__(other)
        return MixedFraction(result)
    
    def __truediv__(self, other):
        result = super().__truediv__(other)
        return MixedFraction(result)
    
    def __lt__(self, other):
        result = super().__lt__(other)
        return result
    
    def __le__(self, other):
        result = super().__le__(other)
        return result
    
    def __gt__(self, other):
        return super().__gt__(other)

    def __ge__(self, other):
        return super().__ge__(other)


def main():
    print("*" * 30 + "\nPrinting main() source code:\n" + "*" * 30)
    import inspect
    print(str(inspect.getsource(main)))
    print("*" * 30 + "\nPrinting main() source output:\n" + "*" * 30)
    f1 = Fraction(-10, 2)
    f2 = Fraction(-10, -3)
    f3 = Fraction(10, -4)
    f4 = Fraction(10, 5)
    f5 = f1 - f2 * f3 / f4
    print("f1: " + str(f1))
    print("f2: " + str(f2))
    print("f3: " + str(f3))
    print("f4: " + str(f4))
    print("f5: " + str(f5))
    print("isinstance(f5, Fraction): " + str(isinstance(f5, Fraction)))
    print("isinstance(f5, MixedFraction): " + str(isinstance(f5, MixedFraction)))
    m1 = MixedFraction(f1)
    m2 = MixedFraction(f2)
    m3 = MixedFraction(f3)
    m4 = MixedFraction(f4)
    m5 = m1 - m2 * m3 / m4
    print("m1: " + str(m1))
    print("m2: " + str(m2))
    print("m3: " + str(m3))
    print("m4: " + str(m4))
    print("m5: " + str(m5))
    print("isinstance(m5, Fraction): " + str(isinstance(m5, Fraction)))
    print("isinstance(m5, MixedFraction): " + str(isinstance(m5, MixedFraction)))
    print("(f5 == m5) : " + str(f5 == m5))
    print("(f5 != m5) : " + str(f5 != m5))
    print("(f1 < m2) : " + str(f1 < m2))
    print("(f2 <= m3) : " + str(f2 <= m3))
    print("(f3 > m4) : " + str(f3 > m4))
    print("(f4 >= m5) : " + str(f4 >= m5))

main()