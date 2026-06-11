from ingestion.clients.adzuna_client import AdzunaClient
from ingestion.config.settings import settings
from ingestion.writers.bronze_writer import BronzeWriter


client = AdzunaClient(
    app_id=settings.adzuna.app_id,
    app_key=settings.adzuna.app_key
)

writer = BronzeWriter()

data = client.search_jobs(
    role="data engineer",
    results_per_page=1
)

if data:

    file_path = writer.save(
        source="adzuna",
        data=data
    )

    print(
        f"Saved Bronze File: {file_path}"
    )

else:

    print(
        "No data received from Adzuna"
    )