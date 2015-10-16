""" This module provides loading utilities for data set files with extensions .csv, .arff, .json.
    Author: Sean Dai
    """
from __future__ import print_function
import numpy as np
import pandas as pd


from sklearn.feature_extraction import DictVectorizer
from scipy.io.arff import loadarff


def _load_arff(filename):
    """
    Base function to load arff files.
    """
    dataset = loadarff(open(filename, 'r'))
    features = dataset[1].names()
    class_attr = features[-1]
    y = np.array(dataset[0][class_attr])
    X = np.array(dataset[0][features[:-1]])
    X = np.array([list(fv) for fv in X])
    return X, y, features


def is_numeric_type(array):
    """
    Checks if the array's datatype is a number data type.

    Args:
        array: numpy array

    Returns:
        True if array.dtype is type float, int, uint, complex, or bool
        Otherwise, we say it's a string.
    """
    numeric_dtypes = []
    numeric_strings = {'uint', 'complex', 'float', 'int'}
    for dtype, entries in np.sctypes.items():
        if dtype in numeric_strings:
            numeric_dtypes.extend(entries)
    return array.dtype.type in numeric_dtypes


def vectorize_categorical_data(X, y, features):
    """
    One-hot encoding for categorical attributes in the feature array.

    Args:
        X: (num_examples, num_features) numpy array of all the examples
        y: the class labels of size (1, num_examples)
        features: list of feature names

    Returns:
        X: new numpy array with all categorical labels becoming 1-hot encoded
        y: class labels, changed to 1-hot if labels were categorical
    """
    vec = DictVectorizer()
    assert (len(features) - 1) == len(X[0])

    # Create a dictionary for each example with the feature name as the key.
    # DictVectorizer requires feature arrays to be represented as a list
    # of dict objects. Each element of the list is 1 feature vector example from
    # the dataset.
    measurements = []
    for ex in X:
        ex_dict = dict(zip(features, ex.tolist()))
        measurements.append(ex_dict)
    measurements = _convert_dict_values_to_num(measurements)

    if not is_numeric_type(y):
        y = _convert_target_to_num(y)

    X = vec.fit_transform(measurements, y).toarray()
    return X, y


def _convert_dict_values_to_num(examples):
    """
    Convert only the numeric values formatted as strings to actual
    numeric datatypes in the feature array of dicts.

    examples - list<dict>
    """

    def is_number(s):
        """ True if string s can be converted to a number type.
        """
        try:
            float(s)
            return True
        except ValueError:
            return False

    new_examples = examples[:]
    for dct in new_examples:
        for key in dct:
            value = dct[key]
            if is_number(value):
                dct[key] = float(value)
    return new_examples


def _convert_target_to_num(target):
    """
    Convert only the numeric values formatted as strings to actual
    numeric datatypes in the feature array of dicts.

    target - nd.array of class values

    Returns:
        converted target array to float dtype
    """

    def is_number(s):
        """ True if string s can be converted to a number type.
        """
        try:
            float(s)
            return True
        except ValueError:
            return False

    if all(map(is_number, target)):
        return target.astype(float)
    else:
        return target


def load_arff(filename, vectorize_data=False, is_supervised=True):
    """
    Loads .arff dataset files.

    Args:
        filename: str

    Returns:
        X : a (num_examples, num_features) numpy array of examples X
        y : the class labels y of size (1, num_examples)
        features : name of each feature (list<str>)
    """
    X, y, features = _load_arff(filename)

    # For categorical data, we want the feature label names
    # in order to create a 1-hot encoding of the categorical
    # values in our feature array of examples.
    if not is_numeric_type(X) and vectorize_data:
        return vectorize_categorical_data(X, y, features)
    else:
        return X, y

def load_csv(filename, vectorize_data=False):
    """
    Loads csv dataset files.

    Args:
        filename: str

    Returns:
        X : a (num_examples, num_features) numpy array of examples X
        y : the class labels y of size (1, num_examples)
    """
    try:
        dataset = pd.read_csv(filename, sep=',')
        dd = dataset.ix[:, -1]
        y = np.array(dd.tolist()).T
        column_names = dataset.dtypes.index
        X = np.array(dataset[column_names[:-1]])

        if is_numeric_type(X):
            X = X.astype(float)
        if is_numeric_type(y):
            y = y.astype(float)

        # Change categorical attributes to 1-hot numerical encoding
        if vectorize_data:
            X, y = vectorize_categorical_data(X, y, column_names)
        return X, y
    except OSError:
        print('File does not exist')

def load_excel(filename, vectorize_data=False):
    """
    Loads .excel dataset files.

    Args:
        filename: str

    Returns:
        X : a (num_examples, num_features) numpy array of examples X
        y : the class labels y of size (1, num_examples)
    """
    try:
        xl = pd.ExcelFile(filename)
        sheets = xl.sheet_names
        data = xl.parse(sheets[0])
        last_col = data.ix[:, -1]
        # Assumes last column contains class value
        y = np.array(last_col.tolist()).T
        column_names = data.dtypes.index
        X = np.array(data[column_names[:-1]])

        if is_numeric_type(X):
            X = X.astype(float)
        if is_numeric_type(y):
            y = y.astype(float)

        # Change categorical attributes to 1-hot numerical encoding
        if vectorize_data:
            X, y = vectorize_categorical_data(X, y, column_names)
        return X, y
    except OSError:
        print('File does not exist')