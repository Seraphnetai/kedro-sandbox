
from typing import Tuple, Dict

import pandas as pd
from sklearn.model_selection import train_test_split

def split_data(df_models: pd.DataFrame,parameters: [Dict,str]) -> Tuple:

    X = df_models.drop("default_7days", axis=1)
    y = df_models.default_7days
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=parameters['random_state']
    )

    return X_train, X_test, y_train, y_test