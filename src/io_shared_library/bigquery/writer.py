from google.cloud import bigquery
import pandas as pd
from io_shared_library.config import settings

def write_to_bigquery(df: pd.DataFrame, table_id: str, if_exists: str = "replace"):
    client = bigquery.Client(project=settings.PROJECT_ID)

    table_ref = f"{settings.PROJECT_ID}.{settings.DATASET_ID}.{table_id}"
    job_config = bigquery.LoadJobConfig(
        write_disposition=(
            bigquery.WriteDisposition.WRITE_TRUNCATE if if_exists == "replace"
            else bigquery.WriteDisposition.WRITE_APPEND
        ),
        autodetect=True
    )

    job = client.load_table_from_dataframe(df, table_ref, job_config=job_config)
    job.result()
    print(f"[✔] Loaded {job.output_rows} rows into {table_ref}")