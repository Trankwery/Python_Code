import numpy as np
from matplotlib import pyplot as plt
import matplotlib.animation as animation

##
##c = 299792458 #[m/c]
##lambd = 632e-9
##f = c/lambd
##omega = 2*np.pi*f
##E0 = 1
##t = 1
##a = np.zeros((480,640))
##for i in range(480):
##    for j in range(640):
##        r = np.sqrt(((-240+i)*1e-8)**2+((-320+j)*1e-8)**2)
##        a[i,j] = (E0*np.sin(omega*t - r*2*np.pi/lambd))
##
##plt.matshow(a)
##plt.show()
c = 299792458 #[m/c]
lambd = 632e-9
f = c/lambd
k = 2*np.pi/lambd
r = 1
omega = 2*np.pi*f
E0 = 1
t = 0
r = np.linspace(0,lambd*3,100)
E = np.cos(omega*t*1e-15-k*r)**2

E2 = np.cos(omega*t*1e-15-k*r)**2
fig, ax = plt.subplots(2,1)
line, = ax[0].plot(r, E)
line2, = ax[1].plot(r, E2)
ax[1].set_ylim(0,350)


def update(t,E2):
    r = np.linspace(0,lambd*3,100)
    E = np.cos(omega*t*1e-17-k*r)**2
    E2+=E
    line.set_xdata(r)
    line.set_ydata(E)
    line2.set_xdata(r)
    line2.set_ydata(E2)
    return line,line2
anim =  animation.FuncAnimation(fig, update, fargs=(E2,),interval=10, 
                               blit=True,)

plt.show()
##
##
##fps = 30
##nSeconds = 5
##snapshots = [ np.random.rand(5,5) for _ in range( nSeconds * fps ) ]
##
### First set up the figure, the axis, and the plot element we want to animate
##fig = plt.figure( figsize=(8,8) )
##
##a = snapshots[0]
##im = plt.imshow(a, interpolation='none', aspect='auto', vmin=0, vmax=1)
##
##def animate_func(i):
##    if i % fps == 0:
##        print( '.', end ='' )
##
##    im.set_array(snapshots[i])
##    return [im]
##
##anim = animation.FuncAnimation(
##                               fig, 
##                               animate_func, 
##                               frames = nSeconds * fps,
##                               interval = 1000 / fps, # in ms
##                               )
##plt.show()
####anim.save('test_anim.mp4', fps=fps, extra_args=['-vcodec', 'libx264'])
##
##print('Done!')
