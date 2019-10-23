# ==================================
from __future__ import division
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import numpy.linalg as npla
import scipy.linalg as spla
import seaborn as sns
import math
# ==================================

# inbuiltfactorial=[]
# for i in range(1,11):
# 	inbuiltfactorial.append(math.factorial(i))
# print('inbuiltfactorial= ',inbuiltfactorial)

# approximationfactorial=[]
# for i in range(1,11):
# 	value=math.sqrt(2*math.pi*i)*((i/math.e)**i)
# 	approximationfactorial.append(value)
# print('approximationfactorial= ',approximationfactorial)


# nparray1=np.asarray(inbuiltfactorial)
# np.save('inbuiltfactorial', nparray1)

# nparray2=np.asarray(approximationfactorial)
# np.save('approximationfactorial', nparray2) 

# ======================================================

inbuiltfactorial=np.load('inbuiltfactorial.npy')
approximationfactorial=np.load('approximationfactorial.npy')

absoluteerror=np.subtract(inbuiltfactorial,approximationfactorial)
relativeerror=np.divide(absoluteerror,inbuiltfactorial)

range1=list(range(1,11))
print(range1)

plt.scatter(range1,absoluteerror, c='b', marker='o')
plt.ylabel('Absolute Error')
plt.xlabel('X')
plt.title('Absolute Error for Stirling Approximation')
plt.show()
plt.scatter(range1, relativeerror, c='r', marker='x')
plt.ylabel('Relative Error')
plt.xlabel('X')
plt.title('Relative Error for Stirling Approximation')
plt.show()