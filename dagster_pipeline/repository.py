from dagster import repository
from .pipeline import full_pipeline

@repository
def kara_repo():
    return [full_pipeline]
