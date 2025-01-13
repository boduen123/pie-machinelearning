import  matplotlib.pyplot as plt

import numpy as np

y= np.array([12,13,14,15])

mylabe =["banana" ,"meat" , "cassava" , "bread"]

myexplode=[0.2,0,0,0]

plt.pie(y ,explode= myexplode ,labels=mylabe)
plt.show()