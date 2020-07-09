#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'notebooks'))
	print(os.getcwd())
except:
	pass
#%%
import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline


class ColumnExtractor(BaseEstimator, TransformerMixin):
    '''
    ColumnExtractor up with SimpleImputer + StandardScaler (poc)
    column selector build to select only numerical (=float) columns from a dataframe

    '''    
    def __init__(self, columns): 
        self.columns = columns
        
    def fit(self, X, y=None, **kwargs):
        return self                     
        
    def transform(self, X, columns=[]): # returns a pandas.DataFrame with the selected columns as output
        return X.loc[self.columns]


#%%

def NumTransPipeline(numcolumns=[]):
    nt_pipeline = PipeLine(steps=[
        ("column_select", ColumnExtractor(numcolumns)),
        ("impute", SimpleImputer(strategy="mean")),
        ("scale", StandardScaler())
        ])
    return nt_pipeline


