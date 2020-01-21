import tkinter as tk

# 第1步，例項化object，建立視窗window
window = tk.Tk()

# 第2步，給視窗的視覺化起名字
window.title('My Window')

# 第3步，設定視窗的大小(長x寬)
window.geometry('500x300')

# 第4步，在圖形介面上建立一個標籤label用以顯示並放置
label = tk.Label(window, bg='yellow', fg='black', width=20, text='empty')
label.pack()


# 第6步，定義選項觸發函式功能
def print_selection():
    if (var1.get() == 1) & (var2.get() == 0):
        label.config(text='I love only Python ')
    elif (var1.get() == 0) & (var2.get() == 1):
        label.config(text='I love only C++')
    elif (var1.get() == 0) & (var2.get() == 0):
        label.config(text='I do not love either')
    else:
        label.config(text='I love both')


# 第5步，定義兩個Checkbutton選項並放置
var1 = tk.IntVar()
var2 = tk.IntVar()
c1 = tk.Checkbutton(window, text='Python', variable=var1, onvalue=1, offvalue=0, command=print_selection)
c1.pack()
c2 = tk.Checkbutton(window, text='C++', variable=var2, onvalue=1, offvalue=0, command=print_selection)
c2.pack()

# 第7步，主視窗迴圈顯示
window.mainloop()
