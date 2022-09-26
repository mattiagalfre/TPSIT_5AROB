import socket
from threading import Thread

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("192.168.0.112",8000))

class receive(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.running = True
    
    def run(self):
        while self.running:
            msgS = input("Inserisci un messaggio> ")
            s.sendall(msgS.encode())

    def stop(self):
        self.running = False

            

r = receive()
r.start()

while True:
    msgR = s.recv(4096)
    msgR = msgR.decode()
    print(msgR)

s.close()