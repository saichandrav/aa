import sqlite3
from pathlib import Path

import pandas as pd

# Build paths relative to this script so it works from any current directory.
BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "students_sample.csv"
DB_PATH = BASE_DIR / "students.db"
TABLE_NAME = "students"


def main() -> None:
    # 1) Read CSV into a pandas DataFrame.
    df = pd.read_csv(CSV_PATH)

    # 2) Connect to SQLite database and write DataFrame as a SQL table.
    with sqlite3.connect(DB_PATH) as conn:
        df.to_sql(TABLE_NAME, conn, if_exists="replace", index=False)

        # 3) Example SQL query using pandas.
        result = pd.read_sql_query(
            """
            SELECT course, ROUND(AVG(marks), 2) AS avg_marks
            FROM students
            GROUP BY course
            ORDER BY avg_marks DESC;
            """,
            conn,
        )

    print("CSV loaded into SQLite successfully!")
    print(f"Database file: {DB_PATH}")
    print("\nAverage marks by course:")
    print(result)


if __name__ == "__main__":
    main()
