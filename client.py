#1. ООП
# 2. Сеть
# 3. Многозадачность
# 4. Базы данных
# 5. Git репозиторий с красивым и внятным описанием проекта(для чего он, что нужно сделать чтобы запустить)
# - Код не должен содержать бесполезные куски.



import socket, threading

def handle_messages(connection: socket.socket):
    while True:
        try:
            msg = connection.recv(1024)
            if msg:
                print(msg.decode())
            else:
                connection.close()
                break

        except Exception as e:
            print(f'ОШИБКА, СТОП 000000000!!!: {e}')
            connection.close()
            break

def client() -> None:
    SERVER_ADDRESS = '127.0.0.1'
    SERVER_PORT = 12000

    try:
       
        socket_instance = socket.socket()
        socket_instance.connect((SERVER_ADDRESS, SERVER_PORT))
        threading.Thread(target=handle_messages, args=[socket_instance]).start()

        print('Добро пожаловать в Anonimus Chat)))\nПосле отправки одного сообщения, вы соглашаетесь с нашим пользовательским соглашением\nпрочитать которое можно в файле REDMI.TXT\nнастоятельно рекомендуем перейти в папку и прочитать пользовательское соглашение!')
        while True:
            msg = input("Я:")

            if msg == 'quit':
                break
            socket_instance.send(msg.encode())
        socket_instance.close()

    except Exception as e:
        print(f'Ероро то конекшан серверо, плис чек ю айпи адрессо ор ю изернет конекшн {e}')
        socket_instance.close()


if __name__ == "__main__":
    client()
