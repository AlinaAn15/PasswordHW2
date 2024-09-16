from tkinter import *
from tkinter.messagebox import showerror, showinfo
import hashlib

root = Tk()
root.title('Пароль')
root.geometry('375x150+300+200')

disp1 = StringVar()
disp2 = StringVar()

pas_hash = None


def gen_salt(str):
    def strShift(text, shift):
        result = []
        for char in text:
            if char.isalpha():
                start = ord('A') if char.isupper() else ord('a')
                result.append(chr(start + (ord(char) - start + shift) % 26))
            else:
                result.append(char)
        return ''.join(result)

    shift = 3
    newstr = strShift(str, shift)
    new2str = newstr[::-1]
    mystr = "PYTHONISMYFAVOURITEOBJECT"
    return f"{new2str}_{mystr}"


def savePassword_click():
    global pas_hash
    password = disp1.get()
    salt = gen_salt(password)
    sha1 = hashlib.sha256()
    sha1.update(salt.encode() + password.encode())
    pas_hash = sha1.hexdigest()
    showinfo('Сохранено', 'Пароль успешно сохранен!')


def checkPassword_click():
    global pas_hash
    if pas_hash is None:
        showerror('Ошибка', 'Сохраните пароль!')
        return
    password = disp2.get()
    salt = gen_salt(password)
    sha2 = hashlib.sha256()
    sha2.update(salt.encode() + password.encode())
    if pas_hash == sha2.hexdigest():
        showinfo('Результат', 'введен ВЕРНЫЙ пароль')
    else:
        showinfo('Результат', 'введен НЕВЕРНЫЙ пароль')


dis1 = Entry(root, textvariable=disp1)
dis1.grid(row=0, column=0, padx=10, pady=10)
dis2 = Entry(root, textvariable=disp2)
dis2.grid(row=1, column=0, padx=10, pady=10)

btn1 = Button(text='Сохранить пароль', command=savePassword_click)
btn1.grid(row=0, column=1, padx=(0, 10))
btn2 = Button(text='Проверить пароль', command=checkPassword_click)
btn2.grid(row=1, column=1, sticky="ew", padx=(0, 10))

root.mainloop()
