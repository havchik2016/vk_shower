# -*- coding: utf-8 -*-
import vk_api
import time
import os
from tkinter import *
from tkinter import messagebox


def main():
    def vk_request():
        login = message.get()
        password = message1.get()
        link = message2.get()

        """ Пример получения последнего сообщения со стены """
        vk_session = vk_api.VkApi(login, password)

        try:
            vk_session.auth(token_only=True)
        except vk_api.AuthError as error_msg:
            print(error_msg)
            return

        vk = vk_session.get_api()

        """ VkApi.method позволяет выполнять запросы к API. В этом примере
            используется метод wall.get (https://vk.com/dev/wall.get) с параметром
            count = 1, т.е. мы получаем один последний пост со стены текущего
            пользователя.
        """
        response = vk.wall.getById(posts=link.split("wall")[1])  # Используем метод wall.get
        if response:
            a = ("Лайки:", str(response[0]["likes"]["count"]), "Репосты:", str(response[0]["reposts"]["count"]), "Просмотры:",
                  str(response[0]["views"]["count"]), "Комменты:", str(response[0]["comments"]["count"]))
            messagebox.showinfo("Статистика", a)
            

    root = Tk()
    root.title("Анализатор VK")
    root.geometry("300x250")

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
    message_entry1 = Entry(textvariable=message1)
    message_entry1.place(relx=.5, rely=.2, anchor="c")
    message_entry2 = Entry(textvariable=message2)
    message_entry2.place(relx=.5, rely=.3, anchor="c")

    message_button = Button(text="Выполнить запрос", command=vk_request)
    message_button.place(relx=.5, rely=.5, anchor="c")

    root.mainloop()


if __name__ == '__main__':
    main()
