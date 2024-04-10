
from typing import Dict
from kedro.pipeline import Pipeline
from .pipelines.data_combine import pipeline as data_combine
from .pipelines.data_preprocesing import pipeline as data_preprocesing
from .pipelines.data_feature import pipeline as data_feature
from .pipelines.data_split import pipeline as data_split
from .pipelines.models import pipeline as models

def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipeline.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.

    """
    combine = data_combine.create_pipeline()
    preprocesing = data_preprocesing.create_pipeline()
    feature = data_feature.create_pipeline()
    split = data_split.create_pipeline()
    model = models.create_pipeline()

    return {
        "__default__": combine + preprocesing + feature + split + model,
        "combine": combine,
        "preprocesing": preprocesing,
        "feature": feature,
        "split": split,
        "models": model,
    }
