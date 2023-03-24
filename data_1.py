# I decided to use a dataset I found online. Here, I've loaded the "load_iris dataset"
from sklearn.datasets import load_iris
# I also found Scikit-learn has a "preprocessing" module.  Here, I import it from the sklearn library.
from sklearn import preprocessing

# I store the "load_iris" dataset into a variable "data#
data = load_iris()

# I extract the input features from the dataset and store them in a variable "x_data"
x_data = data.data
# I extract the target variable from the dataset and store them in a variable "target"
target = data.target

# I use the preprocessing.scale() module to standardize the input features and store it in a variable "standard"
standard = preprocessing.scale(x_data)
print(standard)
