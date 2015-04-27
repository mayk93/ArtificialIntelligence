from gmpy2 import mpfr as real
f = open('bigAssNumber.txt', 'w')
f.write(str(real(real(2**(853))%real(2579))))
