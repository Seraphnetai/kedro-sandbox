
from typing import Any, Dict
import pandas as pd
from functools import reduce


def db_pocco_champ(champion_model_pocco: pd.DataFrame) -> pd.DataFrame:

    data_model_pocco = champion_model_pocco

    return  data_model_pocco

def db_lending_beh_champ(champion_model_lending_beh: pd.DataFrame) -> pd.DataFrame:

    data_model_lending_beh = champion_model_lending_beh
    return  data_model_lending_beh

def db_lending_fin_champ(champion_model_lending_fin: pd.DataFrame) -> pd.DataFrame:

    data_model_lending_fin = champion_model_lending_fin

    return  data_model_lending_fin

def create_model_input_table(
    data_model_pocco: pd.DataFrame, data_model_lending_beh: pd.DataFrame, data_model_lending_fin: pd.DataFrame, parameters: Dict[str, Any]
) -> pd.DataFrame:
    """Combines all data to create a model input table.
    Args:
        shuttles: Preprocessed data for shuttles.
        companies: Preprocessed data for companies.
        reviews: Raw data for reviews.
    Returns:
        Model input table.
    """
    db_lst = [data_model_pocco, data_model_lending_beh, data_model_lending_fin]

    db_champion = reduce(lambda left,right: pd.merge(left,right,on=parameters['merge'],how='inner'),db_lst)

    return db_champion