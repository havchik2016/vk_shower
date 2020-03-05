# -*- coding: utf-8 -*-
import vk_api


def main():
    """ Пример получения последнего сообщения со стены """
    login = input("Введите номер телефона: ")
    password = input("Введите пароль: ")
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
    link = input("Введите ссылку на запись, статистику которй вы хотите посмотреть: ")
    response = vk.wall.getById(posts=link.split("wall")[1])  # Используем метод wall.get

    if response:
        #print(response[0])
        print("Лайки:", response[0]["likes"]["count"], "Репосты:", response[0]["reposts"]["count"], "Просмотры:",
              response[0]["views"]["count"], end="")


if __name__ == '__main__':
    main()
