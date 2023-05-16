import socket
from sys import exit

def generate_HTTP_GET_request(filename):
    header = f"GET /{filename} HTTP/1.1\n"
    header += "Host: client.py\n"
    header += "Agent: terminal\n"

    return header

def main():
    server_name = "localhost"
    server_port = 8000
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Menyambungkan client dengan server. Tangani kasus di mana
    # server sedang berada di luar jaringan (offline)
    try:
        client_socket.connect((server_name, server_port))
    except ConnectionRefusedError:
        print("Check your server connection!")
        exit(0)

    while True:
        # Minta nama dari file yang diinginkan oleh user
        filename = input("Masukkan nama file (contoh: index.html): ")

        # Buat dan kirimkan pesan HTTP GET ke server
        client_socket.send(generate_HTTP_GET_request(filename).encode())
          
        # Terima pesan (paket) yang dikirimkan oleh server
        buffer = ""
        while True:
            message = client_socket.recv(1024)
            if not(message): 
                break
            buffer += message.decode()
        print(buffer)

        # Tutup koneksi saat ini
        client_socket.close()
    
if __name__ == '__main__':
    main()
