import pandas as pd

def meanAir(df: pd.DataFrame, factor, tMin = 60, tMax = 80):
    return df[(df['Temp'] < tMax) & (df['Temp'] > tMin)][factor].mean()

