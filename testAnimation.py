import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as anima

omega = 5
t = np.linspace(0,10,550)
y = np.zeros(np.size(t))
step = 20
fig,ax = plt.subplots()
scat = ax.scatter(t[::step],y[::step])
line = ax.plot(t,y)
ax.set(xlim=[0,10],ylim=[-1.5,1.5])

def update(time):
    y[:time] = np.sin(omega*t[:time])
    line[0].set_xdata(t)
    line[0].set_ydata(y)
    return line

def update2(time):
    y[:time] = np.sin(omega*t[:time][::-1])
    data = np.stack([t[::step],y[::step]]).T
    scat.set_offsets(data)
    line[0].set_xdata(t)
    line[0].set_ydata(y)
    return (scat, line)
ani = anima.FuncAnimation(fig=fig,func=update2,frames=550,interval=1)
plt.show()
