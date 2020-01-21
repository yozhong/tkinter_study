import tkinter as tk

# 第1步，例項化object，建立視窗window
window = tk.Tk()

# 第2步，給視窗的視覺化起名字
window.title('My Window')

# 第3步，設定視窗的大小(長x寬)
window.geometry('500x300')

# 第4步，pack 放置方法
tk.Label(window, text='P', fg='red').pack(side='top')     # 上
tk.Label(window, text='P', fg='red').pack(side='bottom')  # 下
tk.Label(window, text='P', fg='red').pack(side='left')    # 左
tk.Label(window, text='P', fg='red').pack(side='right')   # 右

# 第5步，主視窗迴圈顯示
window.mainloop()
