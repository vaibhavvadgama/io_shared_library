from google.cloud import bigquery
from config import settings

def read_from_bigquery(query: str):
    client = bigquery.Client(project=settings.PROJECT_ID)
    return client.query(query).to_dataframe()