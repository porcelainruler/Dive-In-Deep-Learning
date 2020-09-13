import numpy as np
import warnings

warnings.filterwarnings('ignore')

x = np.arange(12)

print(x)
# Dimension of Numpy Array
print(x.shape)

# No. of elements in Array
print(x.size)

# Change the shape of a Tensor without altering either the number of elements or their values
X = x.reshape(3, 4)
print(X)

# Automatically Inferring One Dimension by providing rest and putting -1 for Unknown Dim
X1 = x.reshape(-1, 4)
X2 = x.reshape(3, -1)

print(X1)
print(X2)

# Setting Arrays with Initial Value Zero
print('Setting Arrays with Initial Value Zero')
A1 = np.zeros((2, 3, 4))
print(A1)

# Setting Arrays with Initial Value One
print('Setting Arrays with Initial Value One')
A2 = np.ones((2, 3, 4))
print(A2)


