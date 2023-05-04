import socket

def main():
    server_socket = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM
    )
    
    # Make the socket to listen to this port
    server_socket.bind(('', 8000))
    
    # Make the socket accept any connection
    server_socket.listen(1)
    
    message = ""
    while message.lower() != "end":
        # Accept any connection
        connected_socket, address = server_socket.accept()

        message = connected_socket.recv(8).decode()
        message += connected_socket.recv(8).decode()
        print(f"received from {address}: {message}")

        connected_socket.close()
    
if __name__ == '__main__':
    main()
