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


class SnowflakeSettings:

    def __init__(self):

        self.account = os.getenv(
            "SNOWFLAKE_ACCOUNT"
        )

        self.user = os.getenv(
            "SNOWFLAKE_USER"
        )

        self.password = os.getenv(
            "SNOWFLAKE_PASSWORD"
        )

        self.database = os.getenv(
            "SNOWFLAKE_DATABASE"
        )

        self.schema = os.getenv(
            "SNOWFLAKE_SCHEMA"
        )

        self.warehouse = os.getenv(
            "SNOWFLAKE_WAREHOUSE"
        )

        self._validate()

    def _validate(self):

        required_settings = {
            "SNOWFLAKE_ACCOUNT":
                self.account,

            "SNOWFLAKE_USER":
                self.user,

            "SNOWFLAKE_PASSWORD":
                self.password,

            "SNOWFLAKE_DATABASE":
                self.database,

            "SNOWFLAKE_SCHEMA":
                self.schema,

            "SNOWFLAKE_WAREHOUSE":
                self.warehouse
        }

        for key, value in required_settings.items():

            if not value:

                raise ValueError(
                    f"{key} is missing"
                )


class Settings:

    def __init__(self):

        self.adzuna = AdzunaSettings()

        self.snowflake = SnowflakeSettings()


settings = Settings()