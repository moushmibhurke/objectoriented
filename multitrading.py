import time
import threading

def calc_square(numbers):
    print("calculate square of numbers")
    for n in numbers:
        time.sleep(0.2)
        print("square : "+str(n*n))

def calc_cube(numbers):
    print("calculate cube of numbers")
    for n in numbers:
        time.sleep(0.2)
        print("cube : "+str(n*n*n))

arr=[2,4,7,8]
t=time.time()
#calc_square(arr)
#calc_cube(arr)
t1=threading.Thread(target=calc_square,args=(arr,))
t2=threading.Thread(target=calc_cube,args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print("done in:",time.time()-t)
print("finally i am done")