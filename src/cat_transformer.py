from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder

def cat_pipeline():
        """Create a categorical pipeline.

        Imputes with most_frequent strategy followed by onehotencoding

        Parameters
        ----------
        none

        Returns
        -------
        cat_pipeline : return a categorical pipeline.
        """
    cat_pipeline = Pipeline(steps=[
        ("impute", SimpleImputer(strategy="most_frequent")),
        ("encode", OneHotEncoder())
    ])

    return cat_pipeline