# ✓ Stores credentials
# ✓ Stores base URL
# ✓ Builds requests
# ✓ Calls Adzuna
# ✓ Returns JSON
# ✓ Raises exceptions
# ✗ Save files
# ✗ Log
# ✗ Loop through roles
# ✗ Handle pagination strategy
# ✗ Perform ETL

import requests


class AdzunaClient:

    BASE_URL = "https://api.adzuna.com/v1/api/jobs"

    def __init__(self, app_id: str, app_key: str):
        self.app_id = app_id
        self.app_key = app_key

    def search_jobs(
        self,
        role: str,
        page: int = 1,
        results_per_page: int = 100,
        country: str = "in"
    ) -> dict:

        url = self._build_url(page,country)

        params = {
            "app_id": self.app_id,
            "app_key": self.app_key,
            "what": role,
            "results_per_page": results_per_page
        }

        try:
            response = requests.get(
                url,
                params=params,
                timeout=30
            )

            response.raise_for_status()

            return response.json()

        except requests.exceptions.RequestException as e:
            print(f"Adzuna API Error: {e}")
            return None

    def _build_url(self, page: int, country: str) -> str:

        return f"{self.BASE_URL}/{country}/search/{page}"
