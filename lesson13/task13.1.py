import random
from random_words import RandomWords

int_list = []
float_list = []
str_list = []

for i in range(1, 5000):
    int_list.append(random.randint(1, 1000))
    float_list.append(random.uniform(1.0, 100.0))
    str_list.append(RandomWords().random_word())

print(int_list, float_list, str_list)