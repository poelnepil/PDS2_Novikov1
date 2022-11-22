import concurrent.futures
import time

def_numbers = [357, 48, 57, 39, 729]

def fact(n):
    for i in range(1, n):
        n *= i
    return (n)

def Threadpoolexecutor_time():
    start1 = time.time()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for number, fact_num in zip(def_numbers, executor.map(fact, def_numbers)):
           a = f'{number} is factorial: {fact_num}'
           # return a
    end1 = time.time()
    threadpoolexecutor_time = end1 - start1
    return (threadpoolexecutor_time)

def Processpoolpxecutor_time():
    start1 = time.time()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, fact_num in zip(def_numbers, executor.map(fact, def_numbers)):
            a = f'{number} is factorial: {fact_num}'
            # return a
    end1 = time.time()
    processpoolpxecutor_time = end1 - start1
    return (processpoolpxecutor_time)


if __name__ == '__main__':
    if Processpoolpxecutor_time() > Threadpoolexecutor_time():
        print('Thread time is faster', Threadpoolexecutor_time())
    else:
        print('Process time is faster', Processpoolpxecutor_time())