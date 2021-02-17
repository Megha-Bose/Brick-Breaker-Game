from headers import *

class Object():
    # class for objects

    # initialises an object position
    def __init__(self, x, y):
        self._x = x                
        self._y = y

    def getx(self):
        return self._x
    
    def gety(self):
        return self._y

    def setx(self,x):
        self._x = x

    def sety(self,y):
        self._y = y