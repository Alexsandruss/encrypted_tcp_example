import socket
from Crypto.Cipher import ChaCha20


host = '127.0.0.1'
port = 5000

server = socket.socket()
server.bind((host, port))

server.listen(1)
connection, address = server.accept()
print("Connection from:", str(address))
while True:
    data = connection.recv(1024)
    if not data:
        break
    secret_key = bytes("*****32 byte (256 bits) key*****", "utf-8")
    cipher = ChaCha20.new(key=secret_key, nonce=data[:8])
    data = cipher.decrypt(data[8:])
    data = str(data, "utf-8", errors="ignore")
    print("From client:", data)
    connection.send(bytes("message received", "utf-8"))
connection.close()
