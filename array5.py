import numpy as np
a=np.arange(1,13).reshape(3,4)
print(a)
print(np.max(a))
print(np.min(a))
#axis0=vertical operation
#axis1=horizontal operation
print(np.max(a,axis=0))
print(np.min(a,axis=0))
print(np.max(a,axis=1))
print(np.min(a,axis=1))