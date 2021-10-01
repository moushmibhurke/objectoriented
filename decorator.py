import time

def time_it(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print(func.__name__ + " took " + str((end - start) * 1000) + "mil sec")
        return result
    return wrapper

@time_it
def cal_square(numbers):
    #start=time.time()
    result=[]
    for number in numbers:
        result.append(number*number)
    #end=time.time()
    #print("time taken by cal_square : "+str((end-start)*1000))
    return result

@time_it
def cal_cube(numbers):
    #start = time.time()
    result=[]
    for number in numbers:
        result.append(number*number*number)
    #end = time.time()
    #print("time taken by cal_square : " + str((end - start) * 1000))
    return result

array=range(1,100000)
out_square=cal_square(array)
out_cube=cal_cube(array)

#args and **kwargs, they're used when we not sure how many arguments will be passed through
# when the function be called. and 1 star (*) means that the arguments are non-keyword argument,
# and 2 stars (*) for argument with keywords.