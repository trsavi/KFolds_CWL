#!/usr/bin/env python -W ignore::DeprecationWarning

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
import pandas as pd 
#from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import accuracy_score, roc_auc_score
import sys




filename = sys.argv[1]
index = int(sys.argv[2])
k_value = int(sys.argv[3])


# import dataset
def load_dataset(filename):
	data = pd.read_csv(filename)
	X = data.iloc[:,:-1]
	y = data.iloc[:,-1]
	return X, y, data

def prepare_inputs(X_train, X_test):
	encoded_x_train = pd.get_dummies(X_train)
	encoded_x_test = pd.get_dummies(X_test)
	return encoded_x_train, encoded_x_test

def prepare_targets(y_train, y_test):
	encoded_y_train = pd.get_dummies(y_train)
	encoded_y_test = pd.get_dummies(y_test)
	return encoded_y_train, encoded_y_test

def calculate_index_range(index, k_value):
	len_data = len(data.index)
	step = round(len_data/k_value)
	indexes = []
	for i in range(0, len_data+1, step):
		indexes.append(i)

	start_index = indexes[index-1]
	try:
		stop_index = indexes[index]
	except IndexError:
		stop_index = 1000

	return start_index, stop_index
		
# Load X,y and data
X, y, data= load_dataset(filename)

# Calculate indexes
start_index, stop_index = calculate_index_range(index, k_value)


# split into train and test sets


X_test = X.iloc[start_index:stop_index,:]
X_train = data.drop(X_test.index).iloc[:,:-1]
y_test = y.iloc[start_index:stop_index]
y_train = data.drop(y_test.index).iloc[:,-1]


# prepare input data
X_train_enc, X_test_enc = prepare_inputs(X_train, X_test)
# Get missing columns in the training test
missing_cols = set( X_train_enc.columns ) - set( X_test_enc.columns )
# Add a missing column in test set with default value equal to 0
for c in missing_cols:
    X_test_enc[c] = 0
# Ensure the order of column in the test set is in the same order than in train set
X_test_enc = X_test_enc[X_train_enc.columns]

# prepare output data
y_train_enc, y_test_enc = prepare_targets(y_train, y_test)



clf = RandomForestClassifier(max_depth=12, n_estimators = 1000, random_state=0)
clf.fit(X_train_enc, y_train_enc)

predictions = clf.predict(X_test_enc)
print('Accuracy: {}\n'.format(round(accuracy_score(y_test_enc, predictions),3)))
print('Roc-Auc: {}\n'.format(round(roc_auc_score(y_test_enc, predictions),3)))

if index == 1:
	result = open('./results.txt', 'w')
	result.write


	result.write('Roc-Auc: {}\n'.format(round(roc_auc_score(y_test_enc, predictions),3)))
else:
	result = open('./results.txt', 'a')
	result.write('Accuracy: {}\n'.format(round(accuracy_score(y_test_enc, predictions),3)))
	result.write('Roc-Auc: {}\n'.format(round(roc_auc_score(y_test_enc, predictions),3)))