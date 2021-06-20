import tkinter
from tkinter import messagebox

A = 32  #  ASCIIコードのA番以降を使う(delも除外) A=32で制御文字を除くすべてのASCII文字が使用可能

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
root.title("送信側")
root.geometry("620x160")

#入力欄の作成
key_box = tkinter.Entry(width=90)
key_box.place(x=10, y=31)

p_box = tkinter.Entry(width=40)
p_box.place(x=10, y=81)

#ラベルの作成
key_label = tkinter.Label(text="keyを入力")
key_label.place(x=10, y=10)

p_label = tkinter.Label(text="平文を入力")
p_label.place(x=10, y=60)

c_label = tkinter.Label(text="暗号文：")
c_label.place(x=10, y=110)

#ボタンクリック時の動作
def encryption():
    n, e = map(int, key_box.get().split())
    P = n + 1
    p_txt = p_box.get()
    p_txt_list = list(p_txt)  #  文字列をリストへ変換

    p_ascii_list = []
    for i in p_txt_list:  #  ASCIIコードへ変換
        p_ascii_list.append(ord(i)-A) 

    P = N_to_dec(p_ascii_list, 127-A)

    if(P < n):
        C = pow(P, e, n)
        c_ascii_list = dec_to_N(C, 127-A)

        c_txt_list = []
        for i in c_ascii_list:  #  ASCIIコードを文字へ変換
            c_txt_list.append(chr(i+A))

        c_txt = (''.join(c_txt_list))  #  リスト内の文字を結合
        c_label = tkinter.Label(text="暗号文：%s" %c_txt)
        c_label.place(x=10, y=110)
        return c_txt
    else:
        messagebox.showwarning("error","平文が長すぎます。")

def set_c():
        root.clipboard_append(encryption())

#ボタンの作成
encry_button = tkinter.Button(text="暗号化",command=encryption)
encry_button.place(x=260, y=78)

copy_button = tkinter.Button(text="暗号文をクリップボードにコピー",command=set_c)
copy_button.place(x=10, y=130)

root.mainloop()