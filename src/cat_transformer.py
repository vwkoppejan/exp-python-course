from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder

def cat_pipeline():
    cat_pipeline = Pipeline(steps=[
        ("impute", SimpleImputer(strategy="most_frequent")),
        ("encode", OneHotEncoder())
    ])

    return cat_pipeline