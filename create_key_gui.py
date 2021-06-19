import sympy
import math
import tkinter
from ctypes import windll 
from tkinter import Label, Widget

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

#ウィンドウの作成
root = tkinter.Tk()
root.title("鍵の生成")
root.geometry("400x135")

#ラベルの作成
p_label = tkinter.Label(text="p = %d" %p)
p_label.place(x=20, y=10)

q_label = tkinter.Label(text="q = %d" %q)
q_label.place(x=20, y=40)

n_label = tkinter.Label(text="n = %d" %n)
n_label.place(x=20, y=70)

e_label = tkinter.Label(text="e = %d" %e)
e_label.place(x=20, y=100)

#ボタンクリック時の動作
def set_p():
    root.clipboard_append(p)
def set_q():
    root.clipboard_append(q)
def set_n():
    root.clipboard_append(n)
def set_e():
    root.clipboard_append(e)

#ボタンの作成
p_button = tkinter.Button(text="p",command=set_p)
p_button.place(x=15, y=8)

q_button = tkinter.Button(text="q",command=set_q)
q_button.place(x=15, y=38)

n_button = tkinter.Button(text="n",command=set_n)
n_button.place(x=15, y=68)

e_button = tkinter.Button(text="e",command=set_e)
e_button.place(x=15, y=98)

root.mainloop()