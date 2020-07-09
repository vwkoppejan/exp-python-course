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