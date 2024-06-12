from turtle import Screen, Turtle

wn = Screen()

wn.setup(700,600)

robot = Turtle()
robot.shape('turtle')


##robot2 = Turtle()
##robot2.shape('turtle')
##robot2.lt(90)
##robot2.fd(50)

def tree(robot, wiek,bok):
    if wiek ==0:
        return
    robot.fd(bok)
    robot.lt(30)
    tree(robot,wiek-1,bok/1.5)
    robot.rt(60)
    tree(robot,wiek-1,bok/1.5)
    robot.lt(30)
    robot.fd(-bok)
robot.lt(90)
robot.pu()
robot.fd(-150)
robot.pd()
tree(robot,7,150)
