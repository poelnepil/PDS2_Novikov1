def unique_num(lst):
    try:
        setlst = sorted(set(lst))
        for i in range(len(lst)):
            if isinstance(lst[i], int) == True or isinstance(lst[i], float) == True:
                if setlst == sorted(lst):
                     return 'всі числа унікальні'
                else:
                     return 'не всі числа унікальні'
            else:
                return 'список має складатися тільки з чисел'
    except TypeError as ex:
        return 'список має складатися тільки з чисел'
    except SyntaxError as ex:
        return 'список має відповідати синтаксису Python'
    except Exception as ex:
        return 'введіть список чисел, для перевірки його на унікальнісь'