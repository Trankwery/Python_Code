from turtle import Turtle, Screen
import numpy as np
from time import sleep

wn = Screen()
wn.tracer(0)

class Mt(Turtle):
    def __init__(self, V, alpha, dt, F):
        Turtle.__init__(self)
        self.x = 0
        self.y = 0
        self.F = 0
        self.dt = dt
        self.alpha = alpha
        self.V = V
        self.Vx = self.V*np.cos(np.pi*alpha/180)
        self.Vy = self.V*np.sin(np.pi*alpha/180)
        
    def update(self):
        self.Vx += self.F*self.dt
        self.Vy += -9.81*self.dt
        self.y += self.Vy*self.dt
        self.x += self.Vx*self.dt
        self.goto(self.x, self.y)

    def run(self):
        while self.y >= -10:
            self.update()
            sleep(self.dt)
            wn.update()

X = Mt(50,55,0.1,0)
Y = Mt(70,45,0.1,0)
Z = Mt(50,25,0.1,0)

while 1:
    X.update()
    Y.F = -5
    Y.update()
    Z.update()
    wn.update()
    sleep(X.dt)
    

