import os
import pathlib
import re
import socket

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 8000

def create_server() -> socket.socket:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(1)
    print("Server created")

    return server_socket

def close_server(server: socket.socket) -> None:
    server.close()

def start_listening(server: socket.socket) -> None:
    print(f"Server listening on {SERVER_HOST}:{SERVER_PORT}")
    while True:
        client_conn, client_port = server.accept()

        request = client_conn.recv(1024).decode()
        print(request)

        split = request.split("\n")
        first_line = split[0]
        matches = re.search("GET \/(.+) HTTP\/1\.(?:\d)", first_line)
        try:
            print(pathlib.Path().resolve())
            print(pathlib.Path(__file__).parent.resolve())
            filename = str(pathlib.Path(__file__).parent.resolve()) + matches.group(1)
            print(filename)
            file = open(matches.group(1), "r")
            print("file opened")
            with open(matches.group(1), "r") as f:
                line = f.readline()
                print(line)
                s = line.split()
                print(s)
                nums = list(map(int, s))
                print(nums)
            response = "HTTP/1.1 200 OK\n\n{}\n\n".format(sum(nums))
        except FileNotFoundError as e:
            response = "HTTP/1.1 400 Bad Request\n\n"


        #response = "HTTP/1.1 200 OK\n\nHi\n"
        client_conn.sendall(response.encode())
        client_conn.close()

if __name__ == "__main__":
    server = create_server()
    start_listening(server)
    close_server(server)