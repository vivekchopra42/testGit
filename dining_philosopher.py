import threading
import random
import time
from random import randint

class Philosper(threading.Thread):
    running = True

    def __init__(self,name,forkLeft,forlRight):
        threading.Thread.__init__(self)
        self.name=name
        self.forkLeft=forkLeft
        self.forkRight=forlRight

    def run(self):
        while(self.running):
            time.sleep(random.uniform(1,10))
            print("{0} is hungry".format(self.name))
            self.getlock()

    def getlock(self):
        fork1=self.forkLeft
        fork2=self.forkRight
        while self.running:
            fork1.acquire()
            fork_available= fork2.acquire(False)

            if(fork_available):
                break
            fork1.release()
        else:
            return

        self.eating()
        fork2.release()
        fork1.release()


    def eating(self):
        print("{0} starts eating".format(self.name))
        time.sleep(random.uniform(1,10))
        print("{0} done eating and leaving forks".format(self.name))

#if __name__=="__main__":
def lol():
        forks = [threading.Lock() for n in range(5)]
        philosperNames = ('A', 'B', 'C', 'D', 'E')

        philospers = [Philosper(philosperNames[i], forks[i % 5], forks[(i + 1) % 5]) for i in range(5)]

        Philosper.running = True

        phil={}

        for p,key in zip(philospers, random.sample( range(1,100), len(philospers)) ):
            phil[key] = p
        print(phil)

        for key in sorted(phil.keys()):
            print("calling {0} : {1}".format(key,phil[key].name))
            phil[key].start()


        time.sleep(60)
        Philosper.running = False
        print("Now we're finishing.")

lol()