class Maths:
    """Math methods akin to fractions"""

    def mdc(self, x, y):
        """Greatest Common Divisor"""
        while y != 0:
            resto = x % y
            x = y
            y = resto
        return x