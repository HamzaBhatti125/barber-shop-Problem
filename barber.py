# EXAMPLE 2
import threading
import time

# numberOfChairs = 0
test = 0

class barberThread(threading.Thread):
    def __init__(self, threadId, name, count):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.count = count

    def run(self):
        print("Starting: " + self.name + "\n")
        cutHair(self.name, 1,self.count)
        print("Exiting: " + self.name + "\n")

def cutHair(name,delay,count):
    while count:
        time.sleep(delay)
        print ("%s: %s %s" % (name, time.ctime(time.time()), count) + "\n")
        count -= 1

class customerThread(threading.Thread):
    def __init__(self, threadId, name, count):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.count = count

    def run(self):
        print("Entering: " + self.name + "\n")
        getHairCut(self.name, 1,self.count)
        print("Exiting: " + self.name + "\n")

def getHairCut(name, delay, count):
    while count:
        if test > 5:
            name.exit()
        time.sleep(delay)
        print ("%s: %s %s" % (name, time.ctime(time.time()), count) + "\n")
        count -= 1



barberLock = threading.Lock()
customerLock = threading.Lock()

# thread1 = myThread(1, "Payment", 5)
# thread2 = myThread2(2, "Sending Email", 10)
# thread3 = myThread2(3, "Loading Page", 3)

# thread1.start()
# thread2.start()
# thread3.start()
# thread1.join()
# thread2.join()
# thread3.join()
print("Done main thread")       
