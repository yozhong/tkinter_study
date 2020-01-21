import tkinter as tk

# 第1步，例項化object，建立視窗window
window = tk.Tk()

# 第2步，給視窗的視覺化起名字
window.title('My Window')

# 第3步，設定視窗的大小(長x寬)
window.geometry('500x300')

# 第4步，在圖形介面上設定標籤
label = tk.Label(window, text='你好！this is Tkinter', bg='green', font=('Arial', 12), width=30, height=2)
# 說明： bg為背景，font為字型，width為長，height為高，這裡的長和高是字元的長和高，比如height=2,就是標籤有2個字元這麼高

# 第5步，放置標籤
label.pack()  # Label內容content區域放置位置，自動調節尺寸
# 放置label的方法有：1）label.pack(); 2)label.place();

# 第6步，主視窗迴圈顯示
window.mainloop()
