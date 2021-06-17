import math

A = 32  #  ASCIIコードのA番以降を使う(delも除外)

n = 89711
e  = 3251

print('n = %d, e = %d' %(n, e))

p_text = str(input('Plaintexst?= '))
p_txt_list = list(p_text)

p_ascii_list = []  #  いらない
p_len = len(p_txt_list)-1
P = 0
for i in p_txt_list:
    p_ascii_list.append(ord(i))  #  いらない
    P += ((127-A) ** p_len) * (ord(i)-A)
    p_len -= 1

C = (P ** e) % n

c_ascii_list = []
C_dumy = C
while C_dumy>0:
    c_ascii_list.append(C_dumy%(127-A)+A)
    C_dumy = int(C_dumy/(127-A))
c_ascii_list.reverse()

c_txt_list = []
for i in c_ascii_list:
    c_txt_list.append(chr(i))

c_txt = (''.join(c_txt_list))

print(c_ascii_list)
print('Cryptogram:\n',c_txt)