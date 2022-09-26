import socket
from threading import Thread
from time import time

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
listaThread = []
contatti = {}

rubrica = {}
f = open("rubrica.csv","r")

righe = f.readlines()

for riga in righe:
    ls = riga.split(",")
    rubrica[ls[0]]=ls[1][:-1]
print(rubrica)


class Client(Thread):
    def __init__(self, connection):
        Thread.__init__(self)
        self.running = True
        self.connection = connection
    
    def run(self):
        while self.running:
            msgR = self.connection.recv(4096)
            msgR = msgR.decode()
            ls = msgR.split("|")
            print(ls)
            contatti[rubrica[ls[1]]].sendall(ls[0].encode())

    def stop(self):
        self.running = False

s.bind(("0.0.0.0",8000))
s.listen()
print("In attesa di connessione...")

while True:
    connection, address = s.accept()
    connection.sendall("Ti sei connesso".encode())
    contatti[address[0]] = connection
    c = Client(connection)
    c.start()
    listaThread.append(c)

s.close()