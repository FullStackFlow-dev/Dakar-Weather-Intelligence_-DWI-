
from sqlalchemy import text

from app.database.connection import engine


def test_postgresql_connection():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version()"))
        version = result.scalar_one()

        print("Connexion PostgreSQL réussie.")
        print(version)


if __name__ == "__main__":
    test_postgresql_connection()
