from random import *
from string import *
class alphaotp:
    def __init__(self):
        b=choices(list(ascii_letters),k=5)
        d=''.join(b)
        print(d)
        c=input('enter otp')
        if d==c:
            print('Success')
        else:
            print('Invalid')
alphaotp()


