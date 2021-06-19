import math

A = 32  #  ASCIIコードのA番以降を使う(delも除外)

n = int(input('n='))
e = int(input('e='))

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

P = n + 1
while(P > n):
    p_txt = str(input('Plaintexst?= '))
    p_txt_list = list(p_txt)

    p_ascii_list = []
    for i in p_txt_list:
        p_ascii_list.append(ord(i)-A) 

    P = N_to_dec(p_ascii_list)

    if(P > n):
        print('Unbreakable!!')

C = pow(P, e, n)

c_ascii_list = dec_to_N(C)

c_txt_list = []
for i in c_ascii_list:
    c_txt_list.append(chr(i+A))

c_txt = (''.join(c_txt_list))

print(p_ascii_list)
print(c_ascii_list)
print('Cryptogram:',c_txt)
print('P:',P)
print('C:',C)