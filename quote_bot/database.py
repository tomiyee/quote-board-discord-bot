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
    POSTGRES_URL = os.getenv("POSTGRES_URL")
    POSTGRES_DATABASE = os.getenv("POSTGRES_DATABASE")
    POSTGRES_USERNAME = os.getenv("POSTGRES_USERNAME")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
else:
    POSTGRES_URL = os.getenv("DEV_POSTGRES_URL")
    POSTGRES_DATABASE = os.getenv("DEV_POSTGRES_DATABASE")
    POSTGRES_USERNAME = os.getenv("DEV_POSTGRES_USERNAME")
    POSTGRES_PASSWORD = os.getenv("DEV_POSTGRES_PASSWORD")

engine = create_engine(
    f"postgresql://{POSTGRES_USERNAME}:{POSTGRES_PASSWORD}@{POSTGRES_URL}:5432/{POSTGRES_DATABASE}"
)
engine.connect()