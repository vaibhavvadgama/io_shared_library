from google.cloud import bigquery
from io_shared_library.config import settings

def read_from_bigquery(query: str):
    client = bigquery.Client(project=settings.PROJECT_ID)
    return client.query(query).to_dataframe()