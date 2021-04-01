import threading
import random

global x              
x = 0
wlock = threading.Lock()
rlock = threading.Lock()

def Reader(Threa):
    global x
    try:
        wlock.acquire()
        print('Reader is Reading!')
        print('Shared Data:', x)
        wlock.release()
        print()
    except:
        print("Reader couldn't read, as Writing is taking place.")

def Writer():
    global x
    try:
        wlock.acquire()
        rlock.acquire()
        print('Writer is Writing!')
        x += 1
        print('Writer is Releasing the lock!')
        wlock.release()
        rlock.release()
        print()
    except:
        print("Writer couldn't write, as Reading or Writing is taking place.")

# threading1 = ""
# threading2 = ""
if __name__ == 'main':
    for i in range(0, 10):
        randomNumber = random.randint(0, 100) 
        if(randomNumber > 50):
            threading1 = threading.Thread(name =" ", target = Reader)
            threading1.start()
        else:
            threading2 = threading.Thread(name = " ",target = Writer)
            threading2.start()

threading1.join()
threading2.join()

print("Final value : ",x)