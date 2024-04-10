
from kedro.pipeline import Pipeline, node
from kedro.pipeline.modular_pipeline import pipeline

from .nodes import create_model_input_table, db_pocco_champ, db_lending_beh_champ, db_lending_fin_champ


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=db_pocco_champ,
                inputs="champion_model_pocco",
                outputs="data_model_pocco",
                name="combine_pocco_node",
            ),
            node(
                func=db_lending_beh_champ,
                inputs="champion_model_lending_beh",
                outputs="data_model_lending_beh",
                name="combine_lending_beh_node",
            ),
            node(
                func=db_lending_fin_champ,
                inputs="champion_model_lending_fin",
                outputs="data_model_lending_fin",
                name="preprocess_lending_fin_node",
            ),
            node(
                func=create_model_input_table,
                inputs=["data_model_pocco","data_model_lending_beh","data_model_lending_fin","parameters"],
                outputs="db_champion",
                name="create_model_input_table_node",
            ),
        ],
        namespace="data_combine",
        inputs=["champion_model_pocco", "champion_model_lending_beh", "champion_model_lending_fin"],
        outputs="db_champion",
    )