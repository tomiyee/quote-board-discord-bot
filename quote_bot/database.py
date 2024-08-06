import os

from dotenv import find_dotenv, load_dotenv
from sqlalchemy import create_engine

from quote_bot.models.create_tables import sync_create_tables

env_path = find_dotenv()
load_dotenv(override=True)


# Decide between using the Production or Development Database
USE_PRODUCTION_DB = os.getenv("USE_PROD_DB") == "true"
if USE_PRODUCTION_DB:
    print("Using Production DB on AWS")
else:
    print("Using Local DB")

if USE_PRODUCTION_DB:
    config = {
        "url": os.getenv("PROD_POSTGRES_URL"),
        "db_name": os.getenv("PROD_POSTGRES_DB"),
        "user": os.getenv("PROD_POSTGRES_USER"),
        "pwd": os.getenv("PROD_POSTGRES_PASSWORD"),
    }
else:
    config = {
        "url": os.getenv("POSTGRES_URL"),
        "db_name": os.getenv("POSTGRES_DB"),
        "user": os.getenv("POSTGRES_USER"),
        "pwd": os.getenv("POSTGRES_PASSWORD"),
    }
database_url = "postgresql://{user}:{pwd}@{url}:5432/{db_name}".format(**config)
engine = create_engine(database_url)


sync_create_tables(engine)
