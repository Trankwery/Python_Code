import numpy as np
import matplotlib.pyplot as plt

ccd = np.zeros((640,480))
x0,y0 = 320,240
omega =  2.91e15
k = 9.66e6 #[nm]
t =1
E0=1
for i in range(640):
    for j in range(480):
        r1 = np.sqrt(((i-x0)*7e-9)**2+((j-y0)*7e-9)**2)
        r2 = np.sqrt(((i-x0+100)*7e-9)**2+((j-y0+100)*7e-9)**2)
        ccd[i,j] = E0*np.sin( omega*t - k*r1 )+E0*np.sin( omega*t - k*r2 )
plt.imshow(ccd)
plt.show()
