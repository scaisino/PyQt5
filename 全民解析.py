# -*-coding：utf-8-*-
import webbrowser
import requests
import re
import tkinter as tk

url = 'http://www.qmaile.com/'
req = requests.get(url)
req.encoding = req.apparent_encoding
reg = re.compile('<option value="(.*?)" selected="">')
res = re.findall(reg, req.text)
print(res)
one = res[0]
two = res[1]
three = res[2]
four = res[3]
five = res[4]
six = res[5]
Seven = res[6]

root = tk.Tk()  # 实例化窗口

root.geometry('680x380')  # 设置窗口尺寸

root.title('VIP电影播放器')  # 设置窗口标题

l1 = tk.Label(root, text='播放器接口：', font=12)
l1.grid(row=0, column=0)

var = tk.StringVar(value=None)

r1 = tk.Radiobutton(root, text='播放器接口1',variable=var,value=one,)
r1.grid(row=0, column=1)
var.set(r1)
r2 = tk.Radiobutton(root, text='播放器接口2',variable=var,value=two,)
r2.grid(row=1, column=1)
r3 = tk.Radiobutton(root, text='播放器接口3',variable=var,value=three,)
r3.grid(row=2, column=1)
r4 = tk.Radiobutton(root, text='播放器接口4',variable=var,value=four,)
r4.grid(row=3, column=1)
r5 = tk.Radiobutton(root, text='播放器接口5',variable=var,value=five,)
r5.grid(row=4, column=1)
r6 = tk.Radiobutton(root, text='播放器接口6',variable=var,value=six,)
r6.grid(row=5, column=1)
r7 = tk.Radiobutton(root, text='播放器接口7',variable=var,value=Seven,)
r7.grid(row=6, column=1)
l2 = tk.Label(root, text='播放链接：', font=12)
l2.grid(row=7, column=0)
t1 = tk.Entry(root, text='', width=80)
t1.grid(row=7, column=1)


def play_movie():
    webbrowser.open(var.get() + t1.get())


b1 = tk.Button(root, text='播放', font=("Arial", 12), width=8, command=play_movie)
b1.grid(row=8, column=1)


def del_text():
    t1.delete(0, 'end')


b2 = tk.Button(root, text='清除', font=("Arial", 12), width=8, command=del_text)
b2.grid(row=9, column=1)

root.mainloop()
