def gcd(a, b): # greatest common divider
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b

class Fraction:
    def __init__(self, fraction_arg):
        try:
            self.fraction = list(map(int,fraction_arg.split('/')))
            self.numerator = int(self.fraction[0] / gcd(abs(self.fraction[0]), abs(self.fraction[1])))
            self.denominator = int(self.fraction[1] / gcd(abs(self.fraction[0]), abs(self.fraction[1])))

            if self.denominator < 0: 
                self.denominator = abs(self.denominator)
                self.numerator = -1 * self.numerator
            if self.denominator == 0:
                raise ZeroDivisionError

        except (AttributeError, ValueError):
            print("Invalid format of input. It shpould be \"<numerator>/<denumerator>\"")
        
        except ZeroDivisionError:
            print("It's not possible to devide by zero")

    def add(self, other):
        return Fraction("{}/{}".format(self.numerator * other.denominator + \
               self.denominator * other.numerator, self.denominator*other.denominator))
    
    def sub(self, other):
        return Fraction("{}/{}".format(self.numerator * other.denominator - \
               self.denominator * other.numerator, self.denominator * other.denominator))
    
    def mul(self, other):
        return Fraction("{}/{}".format(self.numerator * other.numerator, self.denominator * other.denominator))
    
    def div(self, other):
        return Fraction("{}/{}".format(self.numerator * other.denominator, self.denominator * other.numerator))
    
    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        else:
            return '{}/{}'.format(self.numerator, self.denominator)
    
#fr1 = Fraction('3/-4')
fr1 = Fraction('3/4')
fr2 = Fraction('1/2')
fr3 = Fraction.add(fr1,fr2)
fr4 = Fraction.sub(fr1,fr2)
fr5 = Fraction.mul(fr1,fr2)
fr6 = Fraction.div(fr1,fr2)
print('fr1', fr1)
print('fr2', fr2)
print('fr3', fr3)
print('fr4', fr4)
print('fr5', fr5)
print('fr6', fr6)
        
