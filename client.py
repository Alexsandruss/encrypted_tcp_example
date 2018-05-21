import socket
from Crypto.Cipher import ChaCha20


host = "127.0.0.1"
port = 5000

client = socket.socket()
client.connect((host, port))

message = ""
while message != "q":
    secret_key = bytes("*****32 byte (256 bits) key*****", "utf-8")
    cipher = ChaCha20.new(key=secret_key)
    message = cipher.nonce + cipher.encrypt(bytes(input("-> "), "utf-8"))
    client.send(message)
    data = client.recv(1024)
    print('From server:', str(data, "utf-8"))
client.close()
