import subprocess
import sys


PIPELINE_STEPS = [
    "python -m ingestion.main",
    "python -m pyspark_etl.jobs.bronze_to_silver",
    "python -m pyspark_etl.jobs.silver_to_gold_role",
    "python -m pyspark_etl.jobs.silver_to_gold_company",
    "python -m pyspark_etl.jobs.silver_to_gold_location"
]


def main() -> None:

    for step in PIPELINE_STEPS:

        print(f"\n{'=' * 60}")
        print(f"RUNNING: {step}")
        print(f"{'=' * 60}\n")

        result = subprocess.run(
            step,
            shell=True
        )

        if result.returncode != 0:

            print(
                f"\nPIPELINE FAILED AT: {step}"
            )

            sys.exit(1)

    print(
        "\nPIPELINE COMPLETED SUCCESSFULLY"
    )


if __name__ == "__main__":
    main()