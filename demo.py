import pickle
import tkinter as tk
from tkinter import messagebox

# 第1步，例項化object，建立視窗window
window = tk.Tk()

# 第2步，給視窗的視覺化起名字
window.title('My Window')

# 第3步，設定視窗的大小(長x寬)
window.geometry('500x300')

# 第4步，載入 welcome image
canvas = tk.Canvas(window, width=400, height=135, bg='green')
image_file = tk.PhotoImage(file='pic.gif')
image = canvas.create_image(200, 0, anchor='n', image=image_file)
canvas.pack(side='top')
tk.Label(window, text='Welcome', font=('Arial', 16)).pack()

# 第5步，使用者資訊
tk.Label(window, text='User name:', font=('Arial', 14)).place(x=10, y=170)
tk.Label(window, text='Password:', font=('Arial', 14)).place(x=10, y=210)

# 第6步，使用者登入輸入框entry
# 使用者名稱
var_usr_name = tk.StringVar()
var_usr_name.set('example@python.com')
entry_usr_name = tk.Entry(window, textvariable=var_usr_name, font=('Arial', 14))
entry_usr_name.place(x=120, y=175)
# 使用者密碼
var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, font=('Arial', 14), show='*')
entry_usr_pwd.place(x=120, y=215)


# 第8步，定義使用者登入功能
def usr_login():
    # 這兩行程式碼就是獲取使用者輸入的usr_name和usr_pwd
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()

    # 這裡設定異常捕獲，當我們第一次訪問使用者資訊檔案時是不存在的，所以這裡設定異常捕獲。
    # 中間的兩行就是我們的匹配，即程式將輸入的資訊和檔案中的資訊匹配。
    try:
        with open('usrs_info.pickle', 'rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        # 這裡就是我們在沒有讀取到`usr_file`的時候，程式會建立一個`usr_file`這個檔案，並將管理員
        # 的使用者和密碼寫入，即使用者名稱為`admin`密碼為`admin`。
        with open('usrs_info.pickle', 'wb') as usr_file:
            usrs_info = {'admin': 'admin'}
            pickle.dump(usrs_info, usr_file)
            usr_file.close()  # 必須先關閉，否則pickle.load()會出現EOFError: Ran out of input

    # 如果使用者名稱和密碼與檔案中的匹配成功，則會登入成功，並跳出彈窗how are you? 加上你的使用者名稱。
    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            messagebox.showinfo(title='Welcome', message='How are you? ' + usr_name)
        # 如果使用者名稱匹配成功，而密碼輸入錯誤，則會彈出'Error, your password is wrong, try again.'
        else:
            messagebox.showerror(message='Error, your password is wrong, try again.')
    else:  # 如果發現使用者名稱不存在
        is_sign_up = messagebox.askyesno('Welcome！ ', 'You have not sign up yet. Sign up now?')
        # 提示需不需要註冊新使用者
        if is_sign_up:
            usr_sign_up()


# 第9步，定義使用者註冊功能
def usr_sign_up():
    def sign_to_website():
        # 以下三行就是獲取我們註冊時所輸入的資訊
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()

        # 這裡是開啟我們記錄資料的檔案，將註冊資訊讀出
        with open('usrs_info.pickle', 'rb') as usr_file:
            exist_usr_info = pickle.load(usr_file)
        # 這裡就是判斷，如果兩次密碼輸入不一致，則提示Error, Password and confirm password must be the same!
        if np != npf:
            messagebox.showerror('Error', 'Password and confirm password must be the same!')

        # 如果使用者名稱已經在我們的資料檔案中，則提示Error, The user has already signed up!
        elif nn in exist_usr_info:
            messagebox.showerror('Error', 'The user has already signed up!')

        # 最後如果輸入無以上錯誤，則將註冊輸入的資訊記錄到檔案當中，並提示註冊成功Welcome！,You have successfully signed up!，然後銷燬視窗。
        else:
            exist_usr_info[nn] = np
            with open('usrs_info.pickle', 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
            messagebox.showinfo('Welcome', 'You have successfully signed up!')
            # 然後銷燬視窗。
            window_sign_up.destroy()

    # 定義長在視窗上的視窗
    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('300x200')
    window_sign_up.title('Sign up window')

    new_name = tk.StringVar()  # 將輸入的註冊名賦值給變數
    new_name.set('example@python.com')  # 將最初顯示定為'example@python.com'
    tk.Label(window_sign_up, text='User name: ').place(x=10, y=10)  # 將`User name:`放置在座標（10,10）。
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)  # 建立一個註冊名的`entry`，變數為`new_name`
    entry_new_name.place(x=130, y=10)  # `entry`放置在座標（150,10）.

    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='Password: ').place(x=10, y=50)
    entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
    entry_usr_pwd.place(x=130, y=50)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='Confirm password: ').place(x=10, y=90)
    entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
    entry_usr_pwd_confirm.place(x=130, y=90)

    # 下面的 sign_to_website
    btn_comfirm_sign_up = tk.Button(window_sign_up, text='Sign up', command=sign_to_website)
    btn_comfirm_sign_up.place(x=180, y=120)


# 第7步，login and sign up 按鈕
btn_login = tk.Button(window, text='Login', command=usr_login)
btn_login.place(x=120, y=240)
btn_sign_up = tk.Button(window, text='Sign up', command=usr_sign_up)
btn_sign_up.place(x=200, y=240)

# 第10步，主視窗迴圈顯示
window.mainloop()
