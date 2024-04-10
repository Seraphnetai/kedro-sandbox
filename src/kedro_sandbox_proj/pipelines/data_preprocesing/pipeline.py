
from kedro.pipeline import Pipeline, node
from kedro.pipeline.modular_pipeline import pipeline

from .nodes import default_assign


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=default_assign,
                inputs="db_champion",
                outputs="df_champion",
                name="preprocesing_champion",
            ),
        ],
        namespace="data_preprocesing",
        inputs="db_champion",
        outputs="df_champion",
    )