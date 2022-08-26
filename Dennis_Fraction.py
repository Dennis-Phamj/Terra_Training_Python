class Fraction:
    def __init__(self, nr: int, dr: int):
        if nr < 0 and dr <0:
            self.nr, self.dr = self.__reduce(-nr, -dr)
        else:
            self.nr, self.dr = self.__reduce(nr, dr)
            
    def show(self):
        print(f"{self.nr}/{self.dr}")
        
    @staticmethod
    def HighestCommonFractor(x: int, y: int):
        if y == 0: return x
        return Fraction.HighestCommonFractor(y, x % y)
    
    def __reduce(self, x , y):
        gcd = self.HighestCommonFractor(x, y)
        return int(x / gcd), int(y / gcd)
    
    def __add__(self, other):
        nr = self.nr*other.dr + self.dr*other.nr
        dr = self.dr*other.dr
        return Fraction(nr, dr)
    
    def __sub__(self, other):
        nr = self.nr*other.dr - self.dr*other.nr
        dr = self.dr*other.dr
        return Fraction(nr, dr)
    
    def __mul__(self, other):
        nr = self.nr*other.nr
        dr = self.dr*other.dr
        return Fraction(nr, dr)
    
    def __truediv__(self, other):
        nr = self.nr*other.dr
        dr = self.dr*other.nr
        return Fraction(nr, dr)
