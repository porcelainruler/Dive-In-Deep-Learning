# Libraries Imported
import os

# If Lib not Installed
# !pip install pandas
import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings('ignore')


## Reading the Datasets
def mkdir_if_not_exist(path):  # @save --> Save in d2l pkg
    """Make a Directory If it doesn't exist"""
    if not isinstance(path, str):
        path = os.path.join(*path)
    if not os.path.exists(path):
        os.makedirs(path)


# Creating CSV File with Data:
def create_csv(path):
    data_file = path
    mkdir_if_not_exist('../data')
    with open(data_file, 'w') as f:
        f.write('NumRooms,Alley,Price\n')  # Column names
        f.write('NA,Pave,127500\n')  # Each row represents a data example
        f.write('2,NA,106000\n')
        f.write('4,NA,178100\n')
        f.write('NA,NA,140000\n')


# Reading CSV File
def read_csv(path):
    data = pd.read_csv(path)
    print(data)
    return data


data_file = '../data/house_tiny.csv'
# create_csv(data_file)
data = read_csv(data_file)


# Missing Data Handling

# 1. Imputation (Replacing / Substituting NaN Values)
# Case - 1 Numerical - Substitute with Mean
input_values, output_values = data.iloc[:, 0:2], data.iloc[:, 2]
input_values = input_values.fillna(input_values.mean())
print('After Replacing Nan Values in Input:')
print(input_values)

# Case - 2 Categorical Convert NaN to a Category like for 2 val (Pave, NaN) => Both Column 1 if val == col else 0
input_values = pd.get_dummies(input_values, dummy_na=True)
print(input_values)

# 2. Second Method is Deletion


## Conversion to Tensor Form:
X, y = np.array(input_values.values), np.array(output_values.values)
print(X, y)


## Exercise:
# Ques-1 Missing Data Handling - Deletion
data_file = read_csv(data_file)
mean = data_file.isnull().mean()
print(max(mean))
new_data_file_col = data_file.columns[data_file.isnull().mean() < max(mean)]
new_data_file = data_file[new_data_file_col]
print(new_data_file)

# Ques-2 Pre-processed Data --> Tensor Form

