import os
from peewee import PostgresqlDatabase
from dotenv import load_dotenv

load_dotenv()

db = PostgresqlDatabase(
    os.getenv('DATABASE_URL')
)

#     os.getenv('DATABASE_NAME'),  
#     user=os.getenv('DATABASE_USER'),  
#     password= os.getenv('DATABASE_PASSWORD'),  
#     host=os.getenv('DATABASE_HOST')