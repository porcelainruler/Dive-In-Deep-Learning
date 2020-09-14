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

# Random Initialization of Tensors and Type of Distribution Used
# Gaussian or Normal Distribution
X3 = np.random.normal(0, 1, size=(3, 4))  # Ist Para = Mean, IInd Para = Standard Deviation

# Converting Python List / Array to Numpy Array
X4 = np.array([[1, 2, 3], [4, 5, 6]])



## Operations


# Elementwise Operations
x = np.array([1, 2, 4, 8])
y = np.array([2, 2, 2, 2])
sum_op = x + y
sub_op = x - y
mul_op = x * y
div_op = x / y
exp_op = x ** y

# Unary Exponentiation - Element-wise Exponentiation (e^x)
uExp = np.exp(x)

# Concatenation - (Axis along which to concatenate is to be mentioned)
X = np.arange(12).reshape(3, 4)
Y = np.array([[2, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])
# Axis == 1: Means along column and Axis == 0: Means along row Here
np.concatenate([X, Y], axis=0), np.concatenate([X, Y], axis=1)

# Binary Tensor (Obtained by equating 2 Tensor: Each element = True if same value in both Tensors else: False)
bin_tensor = X == Y
print('Binary Tensor Obtained from Tensors X and Y is:')
print(bin_tensor)

# Summing all Elements in a Tensor
sum_all = X.sum()
print(sum_all)


## BroadCasting Mechanism: (Element-wise Operation on 2 Tensors with Different Dimensions)
a = np.arange(3).reshape(3, 1)
b = np.arange(2).reshape(1, 2)
print('a:', a)
print('b:', b)
print('BroadCast Result:', a + b)



## Indexing and Slicing

# Indexing
a = np.arange(12)
print('Last Element:', a[-1])
print('Access Matrix', b[0, 1])

a = np.arange(12).reshape(3, 4)
print(a)

# Assigning Multiple Indices Same Value
a[0:2, :] = 12
print('Setted 1st 2 row to 12:', a)



## Saving Memory




