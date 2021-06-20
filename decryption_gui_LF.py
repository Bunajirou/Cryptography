import math
from tkinter.constants import END
import sympy
import tkinter
from tkinter.scrolledtext import ScrolledText

A = 32  #  ASCIIコードのA番以降を使う(delも除外) A=32で制御文字を除くすべてのASCII文字が使用可能

max_prime = pow(10, 201)
min_prime = pow(10, 200)

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
root.title("受信側（復号）")
root.geometry("560x670")

#入出力欄の作成
key_box = ScrolledText(root, font=("", 10), height=5, width=72)
key_box.pack()
key_box.place(x=10, y=31)
key_box.insert(1.0, key)

c_box = ScrolledText(root, font=("", 15), height=10, width=50)
c_box.pack()
c_box.place(x=10, y=166)

p_box = ScrolledText(root, font=("", 15), height=10, width=50)
p_box.pack()
p_box.place(x=10, y=436)

#ラベルの作成
key_label = tkinter.Label(text="key")
key_label.place(x=10, y=10)

input_label = tkinter.Label(text="暗号文を入力")
input_label.place(x=10, y=145)

p_label = tkinter.Label(text="平文")
p_label.place(x=10, y=415)

#ボタンクリック時の動作
def decryption():
    c_text = c_box.get(1.0,END)
    c_txt_list = list(c_text)  #  文字列をリストへ変換
    c_txt_list.pop()

    c_ascii_list = []
    for i in c_txt_list:  #  ASCIIコードへ変換
        if(ord(i)==10):
            c_ascii_list.append(95)
        else:
            c_ascii_list.append(ord(i)-A) 

    C = N_to_dec(c_ascii_list, 128-A)
    P = pow(C, d, n)
    p_ascii_list = dec_to_N(P, 128-A)

    p_txt_list = []
    for i in p_ascii_list:  #  ASCIIコードを文字へ変換
        if(i==95):
            p_txt_list.append(chr(10))
        else:
            p_txt_list.append(chr(i+A))
    p_txt = (''.join(p_txt_list))  #  リスト内の文字を結合
    p_box.insert(1.0, p_txt)

def set_key():
    root.clipboard_append(key)

#ボタンの作成
key_button = tkinter.Button(text="keyの値をクリップボードにコピー",command=set_key)
key_button.place(x=10, y=105)

decry_button = tkinter.Button(text="復号実行",command=decryption)
decry_button.place(x=10, y=375)

root.mainloop()