from dotenv import load_dotenv
import os

load_dotenv()


class AdzunaSettings:

    def __init__(self):
        self.app_id = os.getenv("ADZUNA_APP_ID")
        self.app_key = os.getenv("ADZUNA_APP_KEY")

        self._validate()

    def _validate(self):

        if not self.app_id:
            raise ValueError(
                "ADZUNA_APP_ID is missing"
            )

        if not self.app_key:
            raise ValueError(
                "ADZUNA_APP_KEY is missing"
            )


class Settings:

    def __init__(self):
        self.adzuna = AdzunaSettings()


settings = Settings()