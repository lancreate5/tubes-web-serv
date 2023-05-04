from socket import *
import sys

serverSocket = socket(AF_INET, SOCK_STREAM)
SERVER_PORT = 8000
SERVER_ADDRESS = "localhost"
serverSocket.bind((SERVER_ADDRESS, SERVER_PORT))
serverSocket.listen(1)

def create_http_header(code):
    header = ""
    if(code == 200):
        header = "HTTP/1.1 200 OK\n"

    elif(code == 404):
        header = "HTTP/1.1 404 Page not found\n"
        

    header += "Server: HawariValen's Web Server\n"
    header += "Connection: Alive\n\n"
    return header


while True:
    print("Ready to serve...")
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(2048).decode()
        print(message)

        filename = message.split()[1]
        if filename == "/":
             filename = "/index.html"


        f = open(filename[1:])    
        outputdata = f.read()
        f.close()

        header = create_http_header(200)
        print("HTTP Response:\n" + header)
        connectionSocket.sendall(header.encode())
        
        print(outputdata)
              
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        header = create_http_header(404)
        print("HTTP Response:\n" + header + "\n")
        connectionSocket.sendall(header.encode())     
        connectionSocket.close()
    serverSocket.close()
    sys.exit()