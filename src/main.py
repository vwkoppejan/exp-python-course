## Main script
import os
import sys
sys.path.insert(0, os.path.abspath('../src'))
import preprocessing
import cat_transformer

# Import data
file = '../data/autos.csv'
data = preprocessing.importFile(file)

# Select relevant columns
columnsToKeep = ['price','brand','gearbox','powerPS','kilometer','fuelType','model','notRepairedDamage']
data = preprocessing.columnSelection(data, columnsToKeep)

# Split dataset
X_train, X_test, y_train, y_test = preprocessing.splitData(data, 0.8)