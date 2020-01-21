import tkinter as tk

# 第1步，例項化object，建立視窗window
window = tk.Tk()

# 第2步，給視窗的視覺化起名字
window.title('My Window')

# 第3步，設定視窗的大小(長x寬)
window.geometry('500x300')

# 第4步，在圖形介面上建立一個標籤用以顯示內容並放置
label = tk.Label(window, text='      ', bg='green')
label.pack()

# 第10步，定義一個函式功能，用來代表選單選項的功能，這裡為了操作簡單，定義的功能比較簡單
counter = 0


def do_job():
    global counter
    label.config(text='do ' + str(counter))
    counter += 1


# 第5步，建立一個選單欄，這裡我們可以把他理解成一個容器，在視窗的上方
menubar = tk.Menu(window)

# 第6步，建立一個File選單項（預設不下拉，下拉內容包括New，Open，Save，Exit功能項）
filemenu = tk.Menu(menubar, tearoff=0)
# 將上面定義的空選單命名為File，放在選單欄中，就是裝入那個容器中
menubar.add_cascade(label='File', menu=filemenu)

# 在File中加入New、Open、Save等小選單，即我們平時看到的下拉選單，每一個小選單對應命令操作。
filemenu.add_command(label='New', command=do_job)
filemenu.add_command(label='Open', command=do_job)
filemenu.add_command(label='Save', command=do_job)
filemenu.add_separator()  # 新增一條分隔線
filemenu.add_command(label='Exit', command=window.quit)  # 用tkinter裡面自帶的quit()函式

# 第7步，建立一個Edit選單項（預設不下拉，下拉內容包括Cut，Copy，Paste功能項）
editmenu = tk.Menu(menubar, tearoff=0)
# 將上面定義的空選單命名為 Edit，放在選單欄中，就是裝入那個容器中
menubar.add_cascade(label='Edit', menu=editmenu)

# 同樣的在 Edit 中加入Cut、Copy、Paste等小命令功能單元，如果點選這些單元, 就會觸發do_job的功能
editmenu.add_command(label='Cut', command=do_job)
editmenu.add_command(label='Copy', command=do_job)
editmenu.add_command(label='Paste', command=do_job)

# 第8步，建立第二級選單，即選單項裡面的選單
submenu = tk.Menu(filemenu)  # 和上面定義選單一樣，不過此處實在File上建立一個空的選單
filemenu.add_cascade(label='Import', menu=submenu, underline=0)  # 給放入的選單submenu命名為Import

# 第9步，建立第三級選單命令，即選單項裡面的選單項裡面的選單命令
submenu.add_command(label='Submenu_1', command=do_job)  # 這裡和上面建立原理也一樣，在Import選單項中加入一個小選單命令Submenu_1

# 第11步，建立選單欄完成後，配置讓選單欄menubar顯示出來
window.config(menu=menubar)

# 第12步，主視窗迴圈顯示
window.mainloop()
