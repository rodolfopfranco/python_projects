class Maths:
    """Math methods akin to fractions"""

    def mdc(self, x, y):
        """Greatest Common Divisor"""
        while y != 0:
            resto = x % y
            x = y
            y = resto
        return x

    def controlador(op,x,y):
        """controls the calculation based on operator"""
        if op=="+":
            return x+y
        elif op=="-":
            return x-y
        elif op=="/":
            return x/y
        elif op=="*":
            return x*y