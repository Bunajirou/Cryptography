import math
import sympy

A = 32  #  ASCIIコードのA番以降を使う(delも除外) A=32で制御文字を除くすべてのASCII文字を使用

p = int(input('p='))
q = int(input('q='))
e = int(input('e='))

n = p * q
L = math.lcm(p-1, q-1)
max = max(p, q)

x = sympy.gcdex(e, L)
d = int(x[0] % L)

def dec_to_N(N):
    keta=0
    for i in range(10**9):
        if N<(127-A)**i:
            keta+=i
            break
    ans=[0]*keta
    check=0
    for i in range(1,keta+1):
        j=N//((127-A)**(keta-i))
        ans[check]=j
        check+=1
        N-=(j)*((127-A)**(keta-i))
    return ans

def N_to_dec(list):
    l=len(list)
    ans=0
    for i in range(1,l+1):
        ans+=list[-i]*((127-A)**(i-1))
    return ans

c_text = str(input('Cryptogram?= '))
c_txt_list = list(c_text)

c_ascii_list = []
for i in c_txt_list:
    c_ascii_list.append(ord(i)-A) 

C = N_to_dec(c_ascii_list)

P = pow(C, d, n)

p_ascii_list = dec_to_N(P)

p_txt_list = []
for i in p_ascii_list:
    p_txt_list.append(chr(i+A))

p_txt = (''.join(p_txt_list))

print('n = %d, e = %d' %(n, e))

print(p_ascii_list)
print(c_ascii_list)
print('Plaintexst:',p_txt)
print('d:',d)
print('P:',P)
print('C:',C)
print('L:',L)
