import tkinter as tk

# 第1步，例項化object，建立視窗window
window = tk.Tk()

# 第2步，給視窗的視覺化起名字
window.title('My Window')

# 第3步，設定視窗的大小(長x寬)
window.geometry('500x300')

# 第4步，在圖形介面上建立一個標籤label用以顯示並放置
label = tk.Label(window, bg='green', fg='white', width=20, text='empty')
label.pack()


# 第6步，定義一個觸發函式功能
def print_selection(v):
    label.config(text='you have selected ' + v)


# 第5步，建立一個尺度滑條，長度200字元，從0開始10結束，以2為刻度，精度為0.01，觸發呼叫print_selection函式
s = tk.Scale(window, label='try me', from_=0, to=10, orient=tk.HORIZONTAL,
             length=200, showvalue=0, tickinterval=2, resolution=0.01, command=print_selection)
s.pack()

# 第7步，主視窗迴圈顯示
window.mainloop()
