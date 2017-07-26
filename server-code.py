
#socket server script
import threading, socket
import time, sys
open('testfile.txt', 'w').close()   #for removing content
open('testfile1.txt', 'w').close()

s = socket.socket()
s.bind(("localhost", 1911))
s.listen(1)
conn0=0
conn1=0
users=[]
name=""
flag=True
print("Connection Waiting...")
print("")

class MiThread(threading.Thread):   # Defines the class MiThread, subclass of Thread
    def __init__(self, sc, *users):
        threading.Thread.__init__(self)
        self.sc=sc
        self.users=users

    def run(self):  # this method is the code of the thread, it will works when be called by .start() method
        run_socket(sc, users)
        doQuit(sc)
        stop(self)

def run_socket(sc, *users):
    while True:
        print("\nWaiting message...")
        receive = sc.recv(128)
        # print(type(received))
        a = receive.decode('utf-8')
        if a == "quit":
            #flag=False
            break
        else:
            if sc==conn0:
                print (users[0][0], " msg=> ", a, " - ", time.ctime(time.time()))
                conn1.send(users[0][0])
                conn1.send(receive)
            elif sc==conn1:
                print (users[0][1], " msg=> ", a, " - ", time.ctime(time.time()))
                conn0.send(users[0][1])
                conn0.send(receive)
    return 0
def doQuit(sc):
    if flag==False:
        sc.close
        s.close()
def stop(self):
  self._is_running = False

count=0
while True:
    sc, addr1 = s.accept()

    count=count+1
    name=sc.recv(128)
    #ename=name.decode('utf-8')
    users.append(name)
    if(conn0==0):
        conn0=sc
    else:
        conn1=sc
    time.sleep(1)
    sys.stdout.write("\r" + "Connected with " + addr1[0] + ":" + str(addr1[1]))
    if count>1:
        with open("testfile.txt", "w") as txt_file:
            txt_file.write("permit")
    t = MiThread(sc, users)  # creates an object of class MiThread, subclass Thread
    t.start()

sys.exit()
sc.close()
