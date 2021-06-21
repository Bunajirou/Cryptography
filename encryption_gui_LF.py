import tkinter
from tkinter import messagebox
from tkinter.constants import END
from tkinter.scrolledtext import ScrolledText
from functools import partial

A = 32  # ASCIIコードのA番以降を使う(delも除外) 途中の処理により改行文字も使用可能

#1 0進数numをN進数に変換する関数
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

# N進数listを10進数に変換する関数
def N_to_dec(list, N):
    l=len(list)
    ans=0
    for i in range(1,l+1):
        ans+=list[-i]*(N**(i-1))
    return ans

# ウィンドウの作成
root = tkinter.Tk()
root.title("送信側（暗号化）")
root.geometry("560x670")

# 入出力欄の作成
key_box = ScrolledText(root, font=("", 10), height=5, width=72)
key_box.pack()
key_box.place(x=10, y=31)

p_box = ScrolledText(root, font=("", 15), height=10, width=50)
p_box.pack()
p_box.place(x=10, y=131)

c_box = ScrolledText(root, font=("", 15), height=10, width=50)
c_box.pack()
c_box.place(x=10, y=401)

# ラベルの作成
key_label = tkinter.Label(text="keyを入力")
key_label.place(x=10, y=10)

p_label = tkinter.Label(text="平文を入力")
p_label.place(x=10, y=110)

c_label = tkinter.Label(text="暗号文")
c_label.place(x=10, y=380)

# ボタンクリック時の動作
def encryption(x):
    key_txt = key_box.get(1.0,END)
    key_txt = key_txt[:-1]
    n, e = map(int, key_txt.split())
    P = n + 1
    p_txt = p_box.get(1.0, END)

    p_txt_list = list(p_txt)  # 文字列をリストへ変換

    p_ascii_list = []
    for i in p_txt_list:  # ASCIIコードへ変換（改行文字の場合95をリストへ追加）
        if(ord(i)==10):
            p_ascii_list.append(95) 
        else:
            p_ascii_list.append(ord(i)-A) 

    P = N_to_dec(p_ascii_list, 128-A)

    if(P < n):
        C = pow(P, e, n)
        c_ascii_list = dec_to_N(C, 128-A)

        c_txt_list = []
        for i in c_ascii_list:  # ASCIIコードを文字へ変換
            if(i==95):
                c_txt_list.append(chr(10))  # 改行文字用の処理
            else:
                c_txt_list.append(chr(i+A))

        c_txt = (''.join(c_txt_list))  # リスト内の文字を結合
        if(x==1):
            c_box.delete(1.0, END)
            c_box.insert(1.0, c_txt)
        else:
            return c_txt
    else:
        messagebox.showwarning("error","平文が長すぎます。")
# クリップボード処理（保留）
#def set_c():
#    root.clipboard_append(encryption(0))

# ボタンの作成
encry_button = tkinter.Button(text="暗号化実行",command=partial(encryption, 1))
encry_button.place(x=10, y=340)

#クリップボードへのコピーが不安定なため保留
#copy_button = tkinter.Button(text="暗号文をクリップボードにコピー",command=set_c)
#copy_button.place(x=10, y=610)


root.mainloop()