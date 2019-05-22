import socket
import sys
s = socket.socket()
s.bind(("localhost",9999))
s.listen(10)

i = 1
while True:
    sc, address = s.accept()

    print (address)
    f = open('file_'+ str(i)+".pdf",'wb')
    i=i+1
    while (True):
        l = sc.recv(1024)
        f.write(l)

        if not l:
            break

    f.close()
    sc.close()
    print('File sudah direplikasi.')

s.close()