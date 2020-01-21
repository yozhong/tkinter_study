import tkinter as tk

# 第1步，例項化object，建立視窗window
window = tk.Tk()

# 第2步，給視窗的視覺化起名字
window.title('My Window')

# 第3步，設定視窗的大小(長x寬)
window.geometry('500x300')

# 第4步，在圖形介面上建立一個標籤label用以顯示並放置
var1 = tk.StringVar()  # 建立變數，用var1用來接收滑鼠點選具體選項的內容
label = tk.Label(window, bg='green', fg='yellow', font=('Arial', 12), width=10, textvariable=var1)
label.pack()


# 第6步，建立一個方法用於按鈕的點選事件
def print_selection():
    value = lb.get(lb.curselection())  # 獲取當前選中的文字
    var1.set(value)  # 為label設定值


# 第5步，建立一個按鈕並放置，點選按鈕呼叫print_selection函式
b1 = tk.Button(window, text='print selection', width=15, height=2, command=print_selection)
b1.pack()

# 第7步，建立Listbox併為其新增內容
var2 = tk.StringVar()
var2.set((1, 2, 3, 4))

lb = tk.Listbox(window, listvariable=var2)

list_items = [11, 22, 33, 44]
for item in list_items:
    lb.insert('end', item)  # 從最後一個位置開始加入值

lb.insert(1, 'first')   # 在第一個位置加入'first'字元
lb.insert(2, 'second')  # 在第二個位置加入'second'字元
lb.delete(2)            # 刪除第二個位置的字元
lb.pack()

# 第8步，主視窗迴圈顯示
window.mainloop()
