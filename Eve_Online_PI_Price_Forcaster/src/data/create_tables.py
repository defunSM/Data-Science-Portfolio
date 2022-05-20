#!/usr/bin/python

import psycopg2
import os
from dotenv import load_dotenv, find_dotenv

# find .env by walking up directories until it's found
dotenv_path = find_dotenv()

# load up the entries as environment variables
load_dotenv(dotenv_path)

DATABASE_URL = os.environ.get('DATABASE_URL')
DATABASE_NAME = os.environ.get("DATABASE_NAME")
DATABASE_USER = os.environ.get("DATABASE_USER")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")

def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE raw_market_data (
            id SERIAL PRIMARY KEY,
            time TIMESTAMP,
            data JSON
        )
        """)
    
    conn = psycopg2.connect(host=DATABASE_URL,
                            database=DATABASE_NAME,
                            user=DATABASE_USER,
                            password=DATABASE_PASSWORD)
    try:

        # connect to the PostgreSQL server
        cur = conn.cursor()
        
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()