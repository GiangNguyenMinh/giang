from decimal import*
from fractions import*
import math 
from complex import*
getcontext().prec = 3 # so luong chu so phan thuc va phan ao cua kieu decimal
print(Fraction(6,9))
print(Decimal(10)/Decimal(3))
print(10//3) #chi lay phan nguyen 



a = complex(2,3)
print(a)
print(a.real)
print(a.imag)