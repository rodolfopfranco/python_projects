from Maths import Maths

class Fracao:
    """"Object to manage 2 integers as a fraction den and num"""

    def __init__(self,num=1, den=1):
        """"contructor"""
        if (den == 0):
            raise ValueError ("Zero denominator")
        self.num = num
        self.den = den
        if self.den < 0: #negative? Then make it positive
            self.num =-self.num
            self.den = -self.den
        self.simplifica()

    def __eq__(self,f):
        """change equals to match reduced fractions"""
        a=self.simplifica()
        b=f.simplifica()
        return(a.num==b.num and a.den==b.den)

    def __add__(self,f):
        if isinstance(f,int):
            num = self.num + f * self.den
            den = self.den
        elif isinstance(f,Fracao):
            den = self.den * f.den
            num = self.num * f.den + self.den * f.num
        else:
            raise TypeError ("__add__")
        return Fracao(num,den)

    def __iadd__(self,f):
        if isinstance(f,int):
            self.num += f * self.den
        elif isinstance(f,Fracao):
            self.den *= f.den
            self.num = self.num * f.den + self.den * f.num
        else:
            raise TypeError ("__iadd__")
        return self.simplifica()

    def __sub__(self,f):
        if isinstance(f,int):
            num = self.num - f * self.den
            den = self.den
        elif isinstance(f,Fracao):
            den = self.den * f.den
            num = self.num * f.den - self.den * f.num
        else:
            raise TypeError ("__sub__")
        return Fracao(num,den)

    def __mul__(self,f):
        if isinstance(f,int):
            num = self.num * f
            den = self.den
        elif isinstance(f,Fracao):
            num = self.num * f.num
            den = self.den * f.den
        else:
            raise TypeError("__mul__")
        return Fracao(num,den)

    def __truediv__(self, f):
        if isinstance(f,int):
            num = self.num
            den = self.den * f
        elif isinstance(f,Fracao):
            num = self.num * f.den
            den = self.den * f.num
        else:
            raise TypeError("__truediv__")
        return Fracao(num,den)

    def __str__(self):
        if self.num == 0:
            return "0"
        if self.den == 1:
            return str(self.num)
        else:
            return str(self.num) + '/' + str(self.den)

    def simplifica(self):
        """makes the fraction smaller"""
        max = 1
        m = Maths()
        if self.num != 0:
            max = m.mdc(self.num, self.den)
        if max > 1:
            self.num //=max
            self.den //=max
        return self