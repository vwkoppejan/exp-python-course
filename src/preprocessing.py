import pandas as pd

def importFile(file):
    df = pd.read_csv(file, encoding = "ISO-8859-1")
    return df


def columnSelection(df=None, columnsToKeep=None):
    # Selects the relevant columns for this project
    # df = dataframe
    # columnsToKeep = list containing column names, for example:
    # columnsToKeep = ['brand','gearbox','powerPS','kilometer','fuelType','model','notRepairedDamage']

    # Pre-selection
    sizeBefore = df.shape[0]
    df = df[df['seller']=='privat'] 
    df = df[df['offerType']=='Angebot']
    sizeAfter = df.shape[0]
    print('Size before pre-selection: ' + str(sizeBefore) + '. Size after pre-selection: ' + str(sizeAfter) + '.')

    # Only keep selected columns
    df = df.loc[:, columnsToKeep]  

    return df


def splitData(df, test_size=0.3)
    # Splits dataset randomly into a train set and a test set.
     from sklearn.model_selection import train_test_split
    
    # Split dataframe into X and y
    X = df.drop(['price'], axis=1)
    y = df.loc[:,'price']

    # Split into train and test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size, random_state=42)

     return X_train, X_test, y_train, y_test
