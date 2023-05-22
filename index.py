from socket import *
from sys import exit

SERVER_SOCKET = socket(AF_INET, SOCK_STREAM)
SERVER_PORT = 8000
SERVER_ADDRESS = "localhost"
SERVER_SOCKET.bind((SERVER_ADDRESS, SERVER_PORT))
SERVER_SOCKET.listen(1)

# Membuat header respon
def create_http_header(code):
    # Baris pertama header ditentukan berdasarkan kode
    # status yang di-pass
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

        # Terima pesan request yang dikirim oleh client
        message = connection_socket.recv(2048).decode()
        print(message)
        
        # Ubah nilai default file menjadi index.html
        filename = message.split()[1]
        filename = "/index.html" if filename == "/" else filename
        
        # Cari data yang diminta
        # Jika ada, kirim pesan header 200 OK
        # Jika tidak ada, kirim pesan header 404 Not Found
        output_data, header = "", ""
        try:
            with open(filename[1:]) as f:
                output_data = f.read()
            header = create_http_header(200)
        except IOError:
            header = create_http_header(404)
            with open("404.html") as f:
                output_data = f.read()

        # Buat header berdasarkan hasil pencarian file
        print("HTTP Response:\n" + header + "\n")
        connection_socket.sendall(header.encode())     
        
        # Cetak file yang ingin dikirim di konsol server
        # Kirim file satu per satu
        print(output_data)
        for i in range(0, len(output_data)):
            connection_socket.send(output_data[i].encode())
        connection_socket.send("\r\n".encode())
        connection_socket.close()

    # Indent this to end connection immediately
    SERVER_SOCKET.close()
    exit(0)

if __name__ == "__main__":
    main()
