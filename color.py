import tkinter as tk

# メインウィンドウ
root = tk.Tk()

# スケールの値を格納する
red = tk.IntVar()
red.set(0)
blue = tk.IntVar()
blue.set(0)
green = tk.IntVar()
green.set(0)

# ボタンの背景色を変更
def change_color(n):
    color = '#{:02x}{:02x}{:02x}'.format(red.get(),green.get(),blue.get())
    button.configure(highlightbackground=color)

# ボタン
button = tk.Button(root,text='button',highlightbackground='#000')
button.pack(fill='both')

# スケール
s1 = tk.Scale(root,label='red',orient='h',from_=0,to=255,variable=red,command=change_color)

s2 = tk.Scale(root,label='blue',orient='h',from_=0,to=255,variable=blue,command=change_color)

s3 = tk.Scale(root,label='green',orient='h',from_=0,to=255,variable=green,command=change_color)

# ウィジェットの配置
s1.pack(fill='both')
s2.pack(fill='both')
s3.pack(fill='both')

# メインループ
root.mainloop()