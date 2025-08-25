import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

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

engine = create_engine(
    "postgresql://{user}:{pwd}@{url}:5432/{db_name}".format(**config)
)
engine.connect()

Base = declarative_base()
