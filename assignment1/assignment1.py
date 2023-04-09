import numpy as np
import matplotlib.pyplot as plt
# 1a
plt.figure()
x_list = [0,1,2,3]
y_list= [0,2,4,9]
plt.plot(x_list,y_list)


time=np.linspace(0,2*np.pi,100)
xt={}
for i in range(3):
    xt[i]=np.cos(time*(i+1)**2)

for i in range(3):
    plt.plot(time,xt[i])


plt.show()