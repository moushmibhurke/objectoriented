import multiprocessing
import time

def deposite(balance,lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value =balance.value+1
        lock.release()

def withdrawal(balance,lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value=balance.value-1
        lock.release()

if __name__=='__main__':

    balance=multiprocessing.Value('i',200)
    lock=multiprocessing.Lock()
    d=multiprocessing.Process(target=deposite,args=(balance,lock))
    w=multiprocessing.Process(target=withdrawal,args=(balance,lock))
    d.start()
    w.start()
    d.join()
    w.join()
    print(balance.value)