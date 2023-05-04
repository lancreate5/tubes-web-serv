import socket
from sys import exit

def main():
    server_name = "localhost"
    server_port = 8000
    client_socket = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM
    )
    
    # Connect client to server
    try:
        client_socket.connect((server_name, server_port))
    except ConnectionRefusedError:
        print("Check your server connection!")
        exit(0)

    temp = input("Masukkan teks:")
    while temp != "end":
        # Send this to server
        client_socket.send(temp.encode())

        # Enter next item
        temp = input("Masukkan teks:")

    # Close connection
    client_socket.close()
    
if __name__ == '__main__':
    main()
