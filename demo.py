import tkinter as tk

# 第1步，例項化object，建立視窗window
window = tk.Tk()

# 第2步，給視窗的視覺化起名字
window.title('My Window')

# 第3步，設定視窗的大小(長x寬)
window.geometry('500x300')

# 第4步，在圖形介面上設定輸入框控制元件entry框並放置
e = tk.Entry(window)
e.pack()


# 第5步，定義兩個觸發事件時的函式insert_point和insert_end（注意：因為Python的執行順序是從上往下，所以函式一定要放在按鈕的上面）
def insert_point():  # 在滑鼠焦點處插入輸入內容
    var = e.get()
    t.insert('insert', var)


def insert_end():  # 在文字框內容最後接著插入輸入內容
    var = e.get()
    t.insert('end', var)


# 第6步，建立並放置兩個按鈕分別觸發兩種情況
b1 = tk.Button(window, text='insert point', width=10, height=2, command=insert_point)
b1.pack()
b2 = tk.Button(window, text='insert end', width=10, height=2, command=insert_end)
b2.pack()

# 第7步，建立並放置一個多行文字框text用以顯示，指定height=3為文字框是三個字元高度
t = tk.Text(window, height=3)
t.pack()

# 第8步，主視窗迴圈顯示
window.mainloop()
