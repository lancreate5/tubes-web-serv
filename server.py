import socket
from sys import exit

def send_404():
    with open("/index.html") as file:
        return file.read()

def handle_GET():
    content = ""
    try:
        with open("./index.html") as file:
            content = file.read()
    except FileNotFoundError:
        send_404()
    return content

def main():
    server_port = 8000
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', server_port))
    server_socket.listen(1)
    print("Server's ready!")
    
    while True:
        # Accept any connection
        connected_socket, _ = server_socket.accept()
        
        message = connected_socket.recv(1024).decode()
        if message == "GET":
            content = handle_GET()
            print(len(content))
            for i in range(0, len(content)):
                connected_socket.send(content[i].encode())
            print("hell")
            connected_socket.send("\r\n".encode())
        else:
            print("apaan dah")
            exit(0)

        connected_socket.close()
        server_socket.listen(0)
    
if __name__ == '__main__':
    main()
