import hashlib

cap = 50
data = [None for _ in range(cap)]

def encoding(fresh_data):
    hash = hashlib.sha256(fresh_data.encode()).hexdigest()

    return hash

def tindex(login):
    hashsum = 0

    for idx, val in enumerate(login):
        hashsum += (idx + len(login)) ** ord(val)
        hashsum = hashsum % cap

    return hashsum

def tindex2(login):
    import random
    import string

    hashsum = 0
    login2 = login + random.choice(string.ascii_letters)

    for idx, val in enumerate(login2):
        hashsum += (idx + len(login2)) ** ord(val)
        hashsum = hashsum % cap

    return hashsum

def registration():

    login = input('input login: ')
    password = input('input password: ')
    repassword  = input('repeat your password: ')

    if password != repassword:
        print('you entered two different passwords, try again.')
        return registration()

    else:
        hashpass = encoding(password)
        indx = tindex(login)

        if data[indx] is None:
            data[indx] = [login, hashpass]

        else:
            if data[indx][0] == login:
                print('try another login')
                registration()

            else:
                indx2 = tindex2(login)
                data[indx2] = [login, hashpass]

        print('you are registered')
        print('now you have to pass the verification')
        verification()


def verification():
    login = input('input your login:')
    password = input('input your password:')
    indxz = tindex(login)
    hashpass = encoding(password)

    if data[indxz] is None:
        return bad_answer()

    elif data[indxz] is not None:
        l1, p1 = data[indxz]
        if l1 == login:
            if p1 == hashpass:
                user_data = []
                for i in data:
                    if i is not None:
                        user_data.append(i)
                print(user_data)

    else:
        indxz2 = tindex2(login)
        hashpass2 = encoding(password)

        if data[indxz2] is None:
            return bad_answer()

        elif data[indxz2] is not None:
            l2, p2 = data[indxz2]
            if l2 == login:
                if p2 == hashpass2:
                    user_data = []
                    for i in data:
                        if i is not None:
                            user_data.append(i)
                    print(user_data)

def bad_answer():
    print('this user was not found')
    answer = input('do you want to register? yes/no ')
    if answer == 'yes':
        registration()
    else:
        print('goodbye')

while True:
    answer = input('are you registered? yes/no ')

    if answer == 'yes':
        verification()

    elif answer == 'no':
        registration()

    else:
        print('sorry, i do not understand')