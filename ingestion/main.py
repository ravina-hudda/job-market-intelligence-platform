
from ingestion.clients.adzuna_client import AdzunaClient
from ingestion.config.settings import settings
from ingestion.config.validators import validate_ingestion_config, validate_roles_config
from ingestion.config.yaml_loader import load_yaml
from ingestion.writers.bronze_writer import BronzeWriter


def main() -> None:

    client = AdzunaClient(
        app_id=settings.adzuna.app_id,
        app_key=settings.adzuna.app_key
    )

    writer = BronzeWriter()

    
    
    roles = validate_roles_config("config/roles.yaml")
    ingestion_config = validate_ingestion_config("config/ingestion.yaml")

    

    for role in roles:
        for page in range(1, ingestion_config["max_pages"] + 1):
            try:

                data = client.search_jobs(
                    role=role,
                    page=page,
                    results_per_page=ingestion_config["results_per_page"],
                )

                if not data:
                    print(
                        f"No data received for role: {role}"
                    )
                    break

                file_path = writer.save(
                    source="adzuna",
                    role=role,
                    page =page,
                    data=data
                )

                print(
                    f"SUCCESS | Role: {role} | File: {file_path}"
                )

            except Exception as e:

                print(
                    f"FAILED | Role: {role} | Error: {e}"
                )

                continue


if __name__ == "__main__":
    main()