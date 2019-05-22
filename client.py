import socket
import sys

s = socket.socket()
s.connect(("localhost",9999))
data = input("Masukkan nama file yang akan direplikasi: ")
s.send(data.encode("ascii"))
f = open (data, "rb")
l = f.read(1024)
while (l):
    s.send(l)
    l = f.read(1024)
s.close()