# Dagster job definition
from dagster import job, op

@op
def scrape():
    from scripts.scrape_telegram import scrape
    scrape()

@op
def load():
    from scripts.load_to_postgres import load_data
    load_data()

@op
def enrich():
    from scripts.run_yolo import run
    run()

@job
def full_pipeline():
    enrich(load(scrape()))
