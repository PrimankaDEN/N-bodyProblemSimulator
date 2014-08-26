__author__ = 'PrimankaDEN'

RUNGE_KUTTA_4="Methods.RUNGE_KUTTA_4"
RUNGE_KUTTA_7="Methods.RUNGE_KUTTA_7"
EULER_METHOD ="Methods.EULER_METHOD"

class Methods:


    def __init__(self, method):
        if (method==RUNGE_KUTTA_4):
            print 1
        elif (method==RUNGE_KUTTA_7):
            print 2
        elif (method==EULER_METHOD):
            print 3
