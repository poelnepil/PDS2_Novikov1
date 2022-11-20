import time
import random
from random_words import RandomWords

int_list = []
float_list = []
str_list = []


for i in range(1, 5000):
    int_list.append(random.randint(1, 1000))
    float_list.append(random.uniform(1.0, 100.0))
    str_list.append(RandomWords().random_words())

def bubble_sort(list, n_iter):
    n = len(list)
    c = []
    for m in range(1, n_iter+1):
        start = time.time()
        for i in range(n - 1):
            flag = True
            for j in range(n - i - 1):
                if list[j] > list[j + 1]:
                    list[j], list[j + 1] = list[j + 1], list[j]
                    flag = False
            if flag == True:
                break
        end = time.time()
        sort_time = end - start
        c.append(sort_time)
    return (f'середній час обчислення - {sum(c)/n_iter}с')

print(bubble_sort(str_list, 10))