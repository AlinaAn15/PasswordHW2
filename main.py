from tkinter import *
from tkinter.messagebox import showerror, showinfo
import hashlib

root = Tk()
root.title('Пароль')
root.geometry('375x105+300+200')

disp1 = StringVar()
disp2 = StringVar()

pas_hash = None


def savePassword_click():
    global pas_hash
    sha1 = hashlib.sha256()
    sha1.update(dis1.get().encode())
    pas_hash = sha1.hexdigest()


def checkPassword_click():
    global pas_hash
    if pas_hash is None:
        showerror('Ошибка','Сохраните пароль!')
        return
    sha2 = hashlib.sha256()
    sha2.update(dis2.get().encode())
    if pas_hash == sha2.hexdigest():
        showinfo('Результат', 'введен ВЕРНЫЙ пароль')
    else:
        showinfo('Результат', 'введен НЕВЕРНЫЙ пароль')


dis1 = Entry(root, textvariable=disp1)
dis1.grid(row=0, column=0, padx=10, pady=10)
dis2 = Entry(root, textvariable=disp2)
dis2.grid(row=1, column=0, padx=10, pady=10)

btn1 = Button(text='Сохранить пароль', command=savePassword_click)
btn1.grid(row=0, column=1, padx=(0,10))
btn2 = Button(text='Проверить пароль', command=checkPassword_click)
btn2.grid(row=1, column=1, sticky="ew", padx=(0,10))


root.mainloop()
