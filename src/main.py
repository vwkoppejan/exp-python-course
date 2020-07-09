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
columnsToKeep = ['brand','gearbox','powerPS','kilometer','fuelType','model','notRepairedDamage']
data = preprocessing.columnSelection(data, columnsToKeep)