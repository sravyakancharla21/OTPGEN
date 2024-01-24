from random import *
from string import *
class alphadigitotp:
    def __init__(self):
        a=list(ascii_letters)+list(range(0,9))
        b=choices(list(a),k=5)
        d=''.join([str(i) for i in b])
        print(d)
        c=input('enter otp')
        if d==c:
            print('Success')
        else:
            print('Invalid')
alphadigitotp()


