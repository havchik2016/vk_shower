# -*- coding: utf-8 -*-
import vk_api
import requests
import os
from tkinter import *
from tkinter import messagebox


def main():
    def vk_request():
        login = message.get()
        password = message1.get()
        link = message2.get()
        vk_session = vk_api.VkApi(login, password)

        try:
            vk_session.auth(token_only=True)
        except vk_api.AuthError:
            messagebox.showerror("Ошибка", "Неверный логин или пароль!")
            return
        except requests.exceptions.ConnectionError:
            messagebox.showerror("Ошибка", "Ошибка соединения!")
            return

        vk = vk_session.get_api()
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'vk_config.v2.json')
        try:
            response = vk.wall.getById(posts=link.split("wall")[1])
            os.remove(path)
        except IndexError:
            messagebox.showerror("Ошибка", "Пост удален или не существует!")
            os.remove(path)
            return
        if response:
            a = ("❤", str(response[0]["likes"]["count"]), "➦", str(response[0]["reposts"]["count"]),
                 "👁",
                 str(response[0]["views"]["count"]), "✉", str(response[0]["comments"]["count"]))
            messagebox.showinfo("Статистика", a)
        else:
            messagebox.showerror("Ошибка", "Пост удален или не существует!")

    root = Tk()
    root.title("Анализатор VK")
    root.geometry("300x250")

    def exit(event):
        root.destroy()

    lbl = Label(root, text="Телефон:")
    lbl.place(relx=.2, rely=.1, anchor="c")
    lbl1 = Label(root, text="Пароль:")
    lbl1.place(relx=.21, rely=.2, anchor="c")
    lbl2 = Label(root, text="Пост:")
    lbl2.place(relx=.23, rely=.3, anchor="c")

    message = StringVar()
    message1 = StringVar()
    message2 = StringVar()

    message_entry = Entry(textvariable=message)
    message_entry.place(relx=.5, rely=.1, anchor="c")
    message_entry1 = Entry(textvariable=message1, show="*")
    message_entry1.place(relx=.5, rely=.2, anchor="c")
    message_entry2 = Entry(textvariable=message2)
    message_entry2.place(relx=.5, rely=.3, anchor="c")

    message_button = Button(text="Выполнить запрос", command=vk_request)
    message_button.place(relx=.5, rely=.5, anchor="c")

    def enter_request(event):
        vk_request()

    root.bind('<q>', exit)
    root.bind('<Return>', enter_request)
    root.mainloop()


if __name__ == '__main__':
    main()
