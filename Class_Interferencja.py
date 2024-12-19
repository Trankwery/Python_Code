import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

class Ekran():
    # Stale fizycne
    c = 299792458 #[m/c]
    lambd = 632e-9
    f = c/lambd
    omega = 2*np.pi*f
    k = 2*np.pi/lambd
    E0 = 1
    # rozmiar czujnika
    ccd = np.zeros((480,640))
    # żródła światła
    points = [(240,100), (240,400)]#,(200,340), (400,340)]#,(200,15)]
    Kpix = 7e-9 # [m/Pix]
    tccd = []
    
    def __init__(self, lambd=532e-9):
        self.lambd = lambd
        
    def run(self, t=0):
        self.ccd = np.zeros((640,480))
        for p in self.points:
            for i in range(640):
                for j in range(480):
                    r = np.sqrt( ( (i-p[0])*self.Kpix )**2 + ( (j-p[1])*self.Kpix )**2 )
                    self.ccd[i,j] += self.E0*np.sin( self.omega*t - self.k*r )
        print('Done!')
        
    def run_fast(self, t=0):
        self.ccd = np.zeros((480,640))
        
        for p in self.points:
            xs, ys = np.meshgrid(np.linspace(0,639,640), np.linspace(0,479,480), sparse=True)
            r = np.sqrt(  ( (xs-p[0])*self.Kpix )**2 + ( (ys-p[1])*self.Kpix )**2 )
            self.ccd += np.add(self.ccd,(  self.E0*np.sin( self.omega*t - self.k*r )))
        print('Done!')
        
    def ShowImage(self):
        plt.imshow(self.ccd)
        plt.show()
        
    def time_anim(self):
        time = np.linspace(0,4,40)
        self.run()
        self.ims = []
        for t in time:
            self.run(t*1e-15)
            self.tccd.append(self.ccd)
            print(t)
            
    def time_anim_fast(self):
        time = np.linspace(0,4,40)
        self.run_fast()
        self.ims = []
        for t in time:
            self.run_fast(t*1e-15)
            self.tccd.append(self.ccd)
        print('Done!')
            
    def show_animation(self):
        fig, ax = plt.subplots()
        ims = []
        for c in self.tccd:
            im = ax.imshow(c**2,animated=True)
            ims.append([im])
        ani = anim.ArtistAnimation(fig,ims, interval=50, blit=True, repeat_delay=0)
        plt.show()
        
        
CCD = Ekran()
CCD.time_anim_fast()
CCD.show_animation()
