# import requests
# import os
# from dotenv import load_dotenv

# load_dotenv()

# APP_ID = os.getenv("ADZUNA_APP_ID")
# APP_KEY = os.getenv("ADZUNA_APP_KEY")
import sys
import os


from ingestion.config.settings import settings

print(settings.adzuna.app_id)
print(settings.adzuna.app_key)

# url = (
#     f"https://api.adzuna.com/v1/api/jobs/in/search/1"
#     f"?app_id={APP_ID}"
#     f"&app_key={APP_KEY}"
#     f"&results_per_page=1"
#     f"&what=data engineer"
# )

# response = requests.get(url)

# print("Status:", response.status_code)
# print(response.json())

from ingestion.clients.adzuna_client import AdzunaClient

data = AdzunaClient(
    app_id=settings.adzuna.app_id,
    app_key=settings.adzuna.app_key
).search_jobs(
    role="data engineer",
    page=1,
    results_per_page=1,
    country="in"
)

if data:
    print(data)
else:
    print("No data returned")