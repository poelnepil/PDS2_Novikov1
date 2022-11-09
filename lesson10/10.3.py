class MyOwnError(Exception):
    def __init__(self, text, num):
        self.text = text
        self.num = num

a = int(input('Введіть ціле число більше за нуль: '))
def plus_num(a):
       if a < 0:
            raise MyOwnError('Ви ввели число менше за нуль!',a)
       return a

print(plus_num(a))
