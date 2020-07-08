import pandas as pd

def importFile(file):
    df = pd.read_csv(file, encoding = "ISO-8859-1")
    return df