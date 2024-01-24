from random import *
class digitotp:
    def __init__(self):
        b=randint(100000,999999)
        print(b)
        c=int(input('enter otp'))
        if b==c:
            print('Success')
        else:
            print('Invalid')
digitotp()


