import math
import sympy
import tkinter
from tkinter import messagebox

A = 32  #  ASCIIコードのA番以降を使う(delも除外) A=32で制御文字を除くすべてのASCII文字が使用可能

max_prime = pow(10, 21)
min_prime = pow(10, 20)

p = sympy.randprime(min_prime, max_prime)
q = sympy.randprime(min_prime, max_prime)
while(p == q):
    q = sympy.randprime(min_prime, max_prime)

n = p * q
L = math.lcm(p-1, q-1)
max = max(p, q)
e = sympy.randprime(max+1, L)

x = sympy.gcdex(e, L)
d = int(x[0] % L)
key = str(n) + " " +str(e)

#10進数numをN進数に変換する関数
def dec_to_N(num,N):
    keta=0
    for i in range(10**9):
        if num<N**i:
            keta+=i
            break
    ans=[0]*keta
    check=0
    for i in range(1,keta+1):
        j=num//(N**(keta-i))
        ans[check]=j
        check+=1
        num-=(j)*(N**(keta-i))
    return ans

#N進数listを10進数に変換する関数
def N_to_dec(list, N):
    l=len(list)
    ans=0
    for i in range(1,l+1):
        ans+=list[-i]*(N**(i-1))
    return ans

#ウィンドウの作成
root = tkinter.Tk()
root.title("受信側")
root.geometry("600x150")

#入力欄の作成
input_box = tkinter.Entry(width=40)
input_box.place(x=10, y=81)

#ラベルの作成
key_label = tkinter.Label(text="key = %s" %key)
key_label.place(x=10, y=10)

input_label = tkinter.Label(text="暗号文を入力")
input_label.place(x=10, y=60)

output_label = tkinter.Label(text="平文：")
output_label.place(x=10, y=110)

#ボタンクリック時の動作
def set_key():
    root.clipboard_append(key)
def decryption():
    c_text = input_box.get()
    c_txt_list = list(c_text)  #  文字列をリストへ変換

    c_ascii_list = []
    for i in c_txt_list:  #  ASCIIコードへ変換
        c_ascii_list.append(ord(i)-A) 

    C = N_to_dec(c_ascii_list, 127-A)
    P = pow(C, d, n)
    p_ascii_list = dec_to_N(P, 127-A)

    p_txt_list = []
    for i in p_ascii_list:  #  ASCIIコードを文字へ変換
        p_txt_list.append(chr(i+A))
    p_txt = (''.join(p_txt_list))  #  リスト内の文字を結合

    P_label = tkinter.Label(text="平文：%s" %p_txt)
    P_label.place(x=10, y=110)

#ボタンの作成
key_button = tkinter.Button(text="keyの値をクリップボードにコピー",command=set_key)
key_button.place(x=10, y=30)

q_button = tkinter.Button(text="復号",command=decryption)
q_button.place(x=260, y=78)


root.mainloop()