import numpy as np
from sklearn.base import BaseEstimator
from sklearn.utils.validation import check_is_fitted


class OurRidgeEstimator(BaseEstimator):
    def __init__(self, gamma=0): 
        self.gamma = gamma 
        
    def fit(self, X, y):
        M  = X.shape[0] 
        X = np.c_[X, np.ones(M)]  
        XtX = X.T.dot(X)
        Xty = X.T.dot(y)
        allcoefs = np.linalg.inv(XtX + self.gamma*np.eye(M+1)).dot(Xty)
        self.coef_ = allcoefs[1:]
        self.intercept_ = allcoefs[0]    
        return self
 
    def predict(self, X):
        check_is_fitted(self)
        M  = X.shape[0] 
        X = np.c_[X, np.ones(M)] 
        allcoefs = np.append(self.coef_, self.intercept_)
        y_hat = np.dot(X, allcoefs)
        return y_hat   