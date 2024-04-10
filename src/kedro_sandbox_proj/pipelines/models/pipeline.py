

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import find_best_model

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
        node(
            func=find_best_model,
            inputs=["X_train", "y_train", "X_test", "y_test", "parameters"],
            outputs=["best_reg", "best_params"],
            name="find_best_model",
            ),
        ],
        namespace="find_best_model",
        inputs=["X_train", "y_train", "X_test", "y_test"],
        outputs=["best_reg", "best_params"],
    )