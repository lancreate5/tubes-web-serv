from socket import *
from sys import exit

SERVER_SOCKET = socket(AF_INET, SOCK_STREAM)
SERVER_PORT = 8000
SERVER_ADDRESS = "localhost"
SERVER_SOCKET.bind((SERVER_ADDRESS, SERVER_PORT))
SERVER_SOCKET.listen(1)

def create_http_header(code):
    header = ""
    if(code == 200):
        header = "HTTP/1.1 200 OK\n"
    elif(code == 404):
        header = "HTTP/1.1 404 Page not found\n"

    header += "Server: HawariValent's Web Server\n"
    header += "Connection: Alive\n\n"
    return header

def main():
    while True:
        print("Ready to serve...")
        connection_socket, address = SERVER_SOCKET.accept()

        message = connection_socket.recv(2048).decode()
        print(message)

        filename = message.split()[1]
        filename = "/index.html" if filename == "/" else filename

        output_data, header = "", ""
        try:
            with open(filename[1:]) as f:
                output_data = f.read()
            header = create_http_header(200)
        except IOError:
            header = create_http_header(404)
            with open("404.html") as f:
                output_data = f.read()

        print("HTTP Response:\n" + header + "\n")
        connection_socket.sendall(header.encode())     

        for i in range(0, len(output_data)):
            connection_socket.send(output_data[i].encode())
        connection_socket.send("\r\n".encode())
        connection_socket.close()

    # Indent this to end connection immediately
    SERVER_SOCKET.close()
    exit(0)

if __name__ == "__main__":
    main()
