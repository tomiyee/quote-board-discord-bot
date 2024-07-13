import os
from dotenv import load_dotenv


from sqlalchemy import create_engine

load_dotenv()

# Decide between using the Production or Development Database
USE_PRODUCTION_DB = os.getenv("USE_PROD_DB") == "true"
if USE_PRODUCTION_DB:
    print("Using Production DB on AWS")
else:
    print("Using Local DB")

if USE_PRODUCTION_DB:
    config = {
        "user": os.getenv("POSTGRES_USERNAME"),
        "pwd": os.getenv("POSTGRES_PASSWORD"),
        "url": os.getenv("POSTGRES_URL"),
        "db_name": os.getenv("POSTGRES_DATABASE"),
    }
else:
    config = {
        "user": os.getenv("DEV_POSTGRES_USERNAME"),
        "pwd": os.getenv("DEV_POSTGRES_PASSWORD"),
        "url": os.getenv("DEV_POSTGRES_URL"),
        "db_name": os.getenv("DEV_POSTGRES_DATABASE"),
    }

engine = create_engine(
    "postgresql://{user}:{pwd}@{url}:5432/{db_name}".format(**config)
)
engine.connect()
