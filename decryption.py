import math
import sympy

A = 32  #  ASCIIコードのA番以降を使う(delも除外)

p = 283
q = 317

n = p * q
e  = 3251

L = math.lcm(p, q)
max = max(p, q)
x = sympy.gcdex(e, L)
d = x[0] % L


print('n = %d, e = %d' %(n, e))

print(d)