
import pandas as pd
import numpy as np
from sklearn import preprocessing

def create_default(df,var1):

    df["default_7days"]= np.where(df["dpd"] > var1, 1, 0)

    return df

def create_lbl(df):

    colsNum = df.select_dtypes(np.number).columns
    colsObj = df.columns.difference(colsNum)

    df[colsNum] = df[colsNum].fillna(df[colsNum].mean() // 1)
    df[colsObj] = df[colsObj].fillna(df[colsObj].mode().iloc[0])
    print(df.head())

    encoder = {}

    for col in colsObj:
        encoder[col] = preprocessing.LabelEncoder()
        df[col] = encoder[col].fit_transform(df[col])

    return df

def default_assign(db_champion: pd.DataFrame) -> pd.DataFrame:

    db_champion = create_default(db_champion,7)
    df_champion = create_lbl(db_champion)

    return  df_champion