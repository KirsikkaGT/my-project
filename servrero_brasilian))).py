# 1. ООП (хотел релизнуть как бота помощника, но я ленивая чурка)) ) 
# 2. Сеть
# 3. Многозадачность
# 4. Базы данных (без нее обойдемся)
# 5. Git репозиторий с красивым и внятным описанием проекта(для чего он, что нужно сделать чтобы запустить)
# - Код не должен содержать бесполезные куски.

import socket, threading
connections = []

def handle_user_connection(connection: socket.socket, address: str) -> None:
    while True:
        try:
            msg = connection.recv(1024)
            if msg:
                print(f'{address[0]}:{address[1]} - {msg.decode()}')
                
                
                msg_to_send = f'From {address[0]}:{address[1]} - {msg.decode()}'
                broadcast(msg_to_send, connection)

          
            else:
                remove_connection(connection)
                break

        except Exception as e:
            print(f'Некий пользователь лошпек не смог подключиться из за ошибки: {e}')
            remove_connection(connection)
            break


def broadcast(message: str, connection: socket.socket) -> None:
    for client_conn in connections:
        if client_conn != connection:
            try:
                client_conn.send(message.encode())
            except Exception as e:
                print('я егор, ошибка блеат какая то: {e}')
                remove_connection(client_conn)


def remove_connection(conn: socket.socket) -> None:
    if conn in connections:
        conn.close()
        connections.remove(conn)


def server() -> None:

    LISTENING_PORT = 12000
    
    try:
        socket_instance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_instance.bind(('', LISTENING_PORT))
        socket_instance.listen(1000)

        print('серверо ис рунио!!!')
        
        while True:
            socket_connection, address = socket_instance.accept()
            connections.append(socket_connection)
            threading.Thread(target=handle_user_connection, args=[socket_connection, address]).start()

    except Exception as e:
        print(f'Ошибка в создании экспемляра сокета, я гнида: {e}')
    finally:
        if len(connections) > 0:
            for conn in connections:
                remove_connection(conn)

        socket_instance.close()


if __name__ == "__main__":
    server()