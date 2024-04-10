
from typing import Any, Dict
import pandas as pd

def remove_column(df_champion: pd.DataFrame, parameters: Dict[Any,str]) -> pd.DataFrame:

    df_models = df_champion.drop(parameters['rm_variables'], axis = 1)

    return df_models