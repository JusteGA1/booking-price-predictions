import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()


class Database:
    """Creates database structure and adds or extracts records."""
    def __init__(self):
        self.__connection = psycopg2.connect(
            os.getenv("DATABASE_URL")
        )

    def create_db_structure(self) -> None:
        """
        Creates database structure.
        NOTE: deletes tables if exist and creates new empty tables.
        """
        with self.__connection.cursor() as cur:
            cur.execute("DROP TABLE IF EXISTS Predictions;")

            cur.execute("""
                CREATE TABLE Predictions (
                    id serial PRIMARY KEY,
                    Date TIMESTAMP DEFAULT NOW(),
                    Input varchar,
                    Output varchar
                );
                """)
            self.__connection.commit()

    def add_record(self, request: str, response: str) -> None:
        """Adds input and output records to the prediction table."""
        with self.__connection.cursor() as cur:
            cur.execute("""
                        INSERT INTO Predictions(Input, Output) 
                        VALUES (%(user_input)s, %(output)s);
                        """,
                        {
                            "user_input": request,
                            "output": response
                        })
            self.__connection.commit()

    def get_last_records(self, number_of_records: int) -> list:
        """Extracts specified number of input and output records to list."""
        with self.__connection.cursor() as cur:
            cur.execute("""
                        SELECT Input, Output
                        FROM Predictions
                        ORDER BY Date DESC
                        LIMIT %(number)s;
                        """,
                        {
                            "number": number_of_records
                        })
            return cur.fetchall()


if __name__ == "__main__":
    database = Database()
    database.create_db_structure()
