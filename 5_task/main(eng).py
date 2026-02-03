import os # Импортируем модуль для работы с системой

CHAT = "test_chat_2.txt" # создаем файл с именем, потом будем проверять наличие файла

def show_chat():
    if not os.path.exists(CHAT):           # проверяем, создан ил файл и есть ли в нем сообщения
        print("\nNo massage in chat.\n") # Если путь указан не верно, то имя файла другое
        return                             # показываем сообщение и выходим из функции show_chat

    print("\nHi!  Wellcome to Chat")   # Если чат создан (имеется нужный файл), то отображаем его содержание
    with open(CHAT, "r", encoding="utf-8") as f: # открываем его
        print(f.read())
    print("--------------------------------\n")


def send_message(username):                       # Функция публикации нового сообщения от пользователя
    message = input("Input massage: ")        # Ожидаем ввода сообщения от пользователя
    with open(CHAT, "a", encoding="utf-8") as f:  # a- режим открытия файла ничего не затирает
        f.write(f"{username}: {message}\n")       # f- строка позволяет в текст добавлять переменные


def main():                                       # объявляем функцию главной части программы.
    username = input("Input name: ")              # присваиваем имя пользователя#

    while True:                                   # бесконечный цикл, потом можно будет добавить 3 пункт - выход.
        print("Watch are you doing in the Chat?:") # Пользователь должен выбрать действие
        print("1. Lock massage")
        print("2. Send massage")

        choice = input("choice: ")

        if choice == "1":                            # нажал 1 - открывается функция просмотра всех сообщений чата
            show_chat()
        elif choice == "2":                          # нажал 2 - открывается функция создания нового сообщения в чате
            send_message(username)
        else:                                        # нажал каку-то фигню - сообщение об ошибке
            print("Error, go 1 or 2.\n")


if __name__ == "__main__":
    main()