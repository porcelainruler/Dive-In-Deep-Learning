# Libraries Imported
import os


## Reading the Datasets
def mkdir_if_not_exist(path):  # @save --> Save in d2l pkg
    """Make a Directory If it doesn't exist"""
    if not isinstance(path, str):
        path = os.path.join(*path)
    if not os.path.exists(path):
        os.makedirs(path)





