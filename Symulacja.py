from turtle import Turtle, Screen
import numpy as np
from time import sleep

class MyZut(Turtle):
    
    def __init__(self, x, y, alpha, V, dt, Fx, m):
        Turtle.__init__(self)
        self.x = x
        self.y = y
        self.alpha = alpha
        self.V = V
        self.Vx = V*np.cos(self.alpha*np.pi/180)
        self.Vy = V*np.sin(self.alpha*np.pi/180)
        self.dt = dt
        self.Fx = Fx
        self.m = m
        

    def update(self):
        self.Vx += self.Fx*self.dt/self.m
        self.Vy += -9.81*self.dt
        self.x +=  self.Vx*self.dt
        self.y +=  self.Vy*self.dt
        self.goto(self.x,self.y)

wn = Screen()

wn.tracer(0)
z = MyZut(0,0,45,50,0.1,-30,15)

while 1:
    z.update()
    wn.update()
    sleep(z.dt)
    
##
