import os
from orator import DatabaseManager

from dotenv import load_dotenv

load_dotenv(verbose=True)

DB_HOST = os.getenv("DB_HOST") or 'localhost'
DB_PORT = int(os.getenv("DB_PORT")) or 3306
DB_USERNAME = os.getenv("DB_USERNAME") or ''
DB_PASSWORD = os.getenv("DB_PASSWORD") or ''
DB_NAME = os.getenv("DB_NAME") or ''

DATABASES = {
    'default': 'mysql',
    'mysql': {
        'driver': 'mysql',
        'host': DB_HOST,
        'port': DB_PORT,
        'user': DB_USERNAME,
        'password': DB_PASSWORD,
        'database': DB_NAME,
        'prefix': ''
    }
}

db = DatabaseManager(DATABASES)
