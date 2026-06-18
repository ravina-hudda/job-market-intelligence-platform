# ✓ Create bronze directory if missing
# ✓ Generate timestamp filename
# ✓ Wrap response with metadata
# ✓ Save JSON file
# ✗ Call Adzuna API
# ✗ Clean data
# ✗ Transform data
# ✗ Know about Spark
# ✗ Know about PostgreSQL

import json
from pathlib import Path
from datetime import datetime


class BronzeWriter:

    BRONZE_PATH = Path("data/bronze")

    def save(
        self,
        source: str,
        role: str,
        page: int,
        data: dict
    ) -> str:


        source_path = self.BRONZE_PATH / source 
        source_path.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )
        role = role.lower().replace(" ", "_")
        filename = (
            f"{source}_{role}_page_{page}_{timestamp}.json"
        )

        file_path = source_path / filename

        payload = {
            "ingestion_timestamp":datetime.now().isoformat(),
            "source": source,
            "response": data,
            "page": page,
            "role": role
        }

        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                payload,
                file,
                indent=4,
                ensure_ascii=False
            )

        return str(file_path)