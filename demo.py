import tkinter as tk
from tkinter import messagebox

# 第1步，例項化object，建立視窗window
window = tk.Tk()

# 第2步，給視窗的視覺化起名字
window.title('My Window')

# 第3步，設定視窗的大小(長x寬)
window.geometry('500x300')


# 第5步，定義觸發函式功能
def hit_me():
    messagebox.showinfo(title='Hi', message='你好！')  # 提示資訊對話窗
    messagebox.showwarning(title='Hi', message='有警告！')       # 提出警告對話窗
    messagebox.showerror(title='Hi', message='出錯了！')         # 提出錯誤對話窗
    print(messagebox.askquestion(title='Hi', message='你好！'))  # 詢問選擇對話窗return 'yes', 'no'
    print(messagebox.askyesno(title='Hi', message='你好！'))     # return 'True', 'False'
    print(messagebox.askokcancel(title='Hi', message='你好！'))  # return 'True', 'False'


# 第4步，在圖形介面上建立一個標籤用以顯示內容並放置
tk.Button(window, text='hit me', bg='green', font=('Arial', 14), command=hit_me).pack()

# 第6步，主視窗迴圈顯示
window.mainloop()
