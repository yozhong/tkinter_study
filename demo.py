import tkinter as tk

# 定義一個函式功能，供點選Button按鍵時呼叫，呼叫命令引數command=函式名
on_hit = False


def hit_me():
    global on_hit
    if on_hit:
        on_hit = False
        var.set('')
    else:
        on_hit = True
        var.set('You hit me')


# 第1步，例項化object，建立視窗window
window = tk.Tk()

# 第2步，給視窗的視覺化起名字
window.title('My Window')

# 第3步，設定視窗的大小(長x寬)
window.geometry('500x300')

# 第4步，在圖形介面上設定標籤
var = tk.StringVar()
# 將label標籤的內容設定為字元型別，用var來接收hit_me函式的傳出內容用以顯示在標籤上
label = tk.Label(window, textvariable=var, bg='green', font=('Arial', 12), width=30, height=2)
# 說明： bg為背景，font為字型，width為長，height為高，這裡的長和高是字元的長和高，比如height=2,就是標籤有2個字元這麼高
label.pack()

# 第5步，在視窗介面設定放置Button按鍵
button = tk.Button(window, text='Hit me', font=('Arial', 12), width=10, height=1, command=hit_me)
button.pack()

# 第6步，主視窗迴圈顯示
window.mainloop()
