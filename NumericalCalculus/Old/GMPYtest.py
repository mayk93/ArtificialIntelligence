import gmpy2
from gmpy2 import mpz,mpq,mpfr,mpc

s = mpfr(1)
a = mpfr(3)
b = mpfr(4)
x = s + a*b
#x = s.add(a.multiply(b))

print(x)

'''
s = s.add(A[i][j].multiply(x[j]));
'''
