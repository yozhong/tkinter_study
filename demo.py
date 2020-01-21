import tkinter as tk

# 第1步，例項化object，建立視窗window
window = tk.Tk()

# 第2步，給視窗的視覺化起名字
window.title('My Window')

# 第3步，設定視窗的大小(長x寬)
window.geometry('500x300')

# 第4步，在圖形介面上建立一個標籤label用以顯示並放置
var = tk.StringVar()    # 定義一個var用來將radiobutton的值和Label的值聯絡在一起.
label = tk.Label(window, bg='yellow', fg='black', width=20, text='empty')
label.pack()


# 第6步，定義選項觸發函式功能
def print_selection():
    label.config(text='you have selected ' + var.get())


# 第5步，建立三個radiobutton選項，其中variable=var, value='A'的意思就是，當我們滑鼠選中了其中一個選項，把value的值A放到變數var中，然後賦值給variable
r1 = tk.Radiobutton(window, text='Option A', variable=var, value='A', command=print_selection)
r1.pack()
r2 = tk.Radiobutton(window, text='Option B', variable=var, value='B', command=print_selection)
r2.pack()
r3 = tk.Radiobutton(window, text='Option C', variable=var, value='C', command=print_selection)
r3.pack()

# 第7步，主視窗迴圈顯示
window.mainloop()
