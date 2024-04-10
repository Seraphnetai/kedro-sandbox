
from kedro.pipeline import Pipeline, node, pipeline
from .nodes import remove_column

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
        node(
            func=remove_column,
            inputs=["df_champion","parameters"],
            outputs="df_models",
            name="remove_column",
            ),
        ],
        namespace="remove_column",
        inputs="df_champion",
        outputs="df_models",
    )
