import math
import sympy

A = 32  #  ASCIIコードのA番以降を使う(delも除外)

p = 3559
q = 1601

n = p * q
e  = 3571

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
    c_len -= 1

P = (C ** d) % n

p_ascii_list = []
P_dumy = P
while P_dumy>0:
    p_ascii_list.append(P_dumy%(127-A)+A)
    P_dumy = int(P_dumy/(127-A))
p_ascii_list.reverse()

p_txt_list = []
for i in p_ascii_list:
    p_txt_list.append(chr(i))

p_txt = (''.join(p_txt_list))

print('n = %d, e = %d' %(n, e))

print(p_ascii_list)
print(c_ascii_list)
print('Plaintexst:',p_txt)