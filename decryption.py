import math
import sympy

A = 32  #  ASCIIコードのA番以降を使う(delも除外)

p = 283
q = 317

n = p * q
e  = 3251

L = math.lcm(p-1, q-1)
max = max(p, q)

x = sympy.gcdex(e, L)
d = x[0] % L

c_text = str(input('Cryptogram?= '))
c_txt_list = list(c_text)

c_ascii_list = []  #  いらない
c_len = len(c_txt_list)-1
C = 0
for i in c_txt_list:
    c_ascii_list.append(ord(i))  #  いらない
    C += ((127-A) ** c_len) * (ord(i)-A)
    print(C)
    c_len -= 1



print('n = %d, e = %d' %(n, e))
print(C)
print(c_ascii_list)