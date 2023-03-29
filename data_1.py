# I decided to use a dataset I found online. Here, I've loaded the "load_iris dataset"
from sklearn.datasets import load_iris
# I also found Scikit-learn has a "preprocessing" module.  Here, I import it from the sklearn library.
from sklearn import preprocessing

# I store the "load_iris" dataset into a variable "dataset"
dataset = load_iris()

# I extract the input features from the dataset and store them in a variable "extract_data"
extract_data = dataset.data
# I extract the target variable from the dataset and store them in a variable "target"
target = dataset.target

# I use the preprocessing.scale() module to standardize the input features and store it in a variable "standard"
standardized = preprocessing.scale(extract_data)
print(standardized)
