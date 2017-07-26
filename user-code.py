
# Sockets client script
import socket, time, re, threading
import sys, os

s = socket.socket()
print("Connecting to server...")
time.sleep(2)
flag=0
rname=""
while True:
    try:
        s.connect(("localhost", 1911))
        break
    except:
        print("Retrying connection to server...")
        time.sleep(1)
print("Connection Matched!")
name=input("Enter you name: ")
uname=name.encode('utf-8')
s.send(uname)

#print("Waiting for other user..")
while True:
    file=open("testfile.txt", "r")
    if file.read()=="permit":
        sys.stdout.write("\r" + "Connected..")
        break
    for i in range(4):
        sys.stdout.write("\r" + "Waiting for other user" + "." * i)
        time.sleep(1)
        sys.stdout.flush()
print("")
class Mithread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        run_client()
def run_client():
    while True:
        rname=s.recv(128)
        rname=rname.decode('utf-8')
        r = s.recv(128)
        a = r.decode('utf-8')
        # CURSOR_UP_ONE = '\x1b[1A'
        # ERASE_LINE = '\x1b[1K'
        # print(CURSOR_UP_ONE)

        #print("\033[A                             \033[A")
        sys.stdout.write("\r" + "Received from " + rname + "=>> " + a)

t=Mithread()
t.start()
while True:
        #sys.stdout.write("\r" + "Enter message here: ")
        file1 = open("testfile1.txt", "r")
        if file1.read() == "quit":
            break
        keyboardInput = input("Enter message here: ")
        # s.send(bytes(message, 'UTF-8'))
        message = keyboardInput.encode('utf-8')
        s.send(message)
        if keyboardInput == "quit":
            with open("testfile1.txt", "w") as txt_file:
                txt_file.write("quit")
            break
print("Good bye")

s.close()
os._exit(1)