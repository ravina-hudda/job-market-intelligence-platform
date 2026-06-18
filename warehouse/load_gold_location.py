import pandas as pd

from snowflake.connector.pandas_tools import (
    write_pandas
)

from warehouse.snowflake_client import conn


def main() -> None:

    df = pd.read_parquet(
        "data/gold/jobs_by_location"
    )

    df.columns = [
        column.upper()
        for column in df.columns
    ]

    print(df.columns.tolist())
    print(df.head())

    success, nchunks, nrows, _ = write_pandas(
        conn,
        df,
        "JOBS_BY_LOCATION",
        auto_create_table=True,
        overwrite=True
    )

    if success:

        print(
            f"SUCCESS | Loaded {nrows} rows into JOBS_BY_LOCATION"
        )

    else:

        print(
            "FAILED | Could not load data into JOBS_BY_LOCATION"
        )

    conn.close()


if __name__ == "__main__":
    main()