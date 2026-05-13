import socet 
HOST = "127.0.0.1"
port = 65432

server_socket = socket.socket(soket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockpot(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, port)
server_socket.listen(1)
print(f"Server is listening on {HOST}:{port}")

conn , addr = server_socket.accept()
print(f"Connected by {addr}")

while True:
    data = conn.recv(1024)
    if not data:
        brake 
    print(f"Received :{data.deecode()}"
    conn.sendall(data)
conn.close()
server_socket.close()






