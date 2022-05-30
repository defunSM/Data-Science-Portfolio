#!/usr/bin/env python

""" database.py

This module contains functions that help access the PostgreSQL
database. Some constants are needed to make connection with the database. Once connected tables can be created and data can be stored.

Contains:

connect_to_database
postgresql_command
create_table
insert_data_into_table
store_api_data
 
"""

import json
import psycopg2
import sys

from datetime import datetime
from alive_progress import alive_bar

import constants as cnt

import api
import hashs
import pickle_helpers as pickler

# TODO: Add check if .env exists

def connect_to_database():
    """ Connects to the postgresql database using .env file.

    Returns:
        database connection: used to execute sql queries or creating tables.
    """
    
    conn = psycopg2.connect(host=cnt.DATABASE_URL,
                            database=cnt.DATABASE_NAME,
                            user=cnt.DATABASE_USER,
                            password=cnt.DATABASE_PASSWORD,
                            port=cnt.DATABASE_PORT)
    return conn

def postgresql_command(command: str, results: bool = False) -> None | list[tuple]:
    """ Execute a postgresql command, if results is True will also return the query results.

    Args:
        command (str): The postgresql query as a string.
        results (bool, optional): Determine whether to return the results of command. Defaults to False.
    """
    
    conn = connect_to_database()
    try:

        # connect to the PostgreSQL server
        cur = conn.cursor()
        
        # create table one by one
        cur.execute(command)
        
        if results:
            query_results = cur.fetchall()
        
        # close communication with the PostgreSQL database server
        cur.close()
        
        # commit the changes
        conn.commit()
        
        print("Command executed successfully")
        
        if results:
            return query_results
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def insert_data_into_table(table_name='market_data', region_id=None, json_data=None):
    """ Connects with postgresql database and inserts records into a table.

    Args:
        table_name (str, optional): The name of the table that the data will be inserted into. Defaults to 'raw_material_data'.
        
        region_id (int, optional): The region of the market. Defaults to None.
        json_data (json, optional): The JSON market data from the API endpoint. Defaults to None.
    """
    
    time = datetime.now()
    
    try:
        conn = connect_to_database()
        cursor = conn.cursor()
        
        # sql to insert the json into table
        insert_command ="INSERT INTO " + table_name + " (TIME, REGION_ID, DATA) VALUES (%s, %s, %s)"
        
        # Serializing json
        json_object = json.dumps(json_data)
        
        # Inserting into table
        values = (time, region_id, json_object)
        cursor.execute(insert_command, values)
        
        # Close and commit changes to database server
        conn.commit()
        conn.close()
        
        print("Successfully stored data into table for region ID: " + str(region_id) + ".")
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            
def create_table(table_name):
    """ create a table by the name of 'table_name' provided in the PostgreSQL database"""
    command = (
        """
        CREATE TABLE """ + table_name + """ (
            id SERIAL PRIMARY KEY,
            time TIMESTAMP,
            region_id INTEGER,
            data JSON
        )
        """)
    
    postgresql_command(command)

    
    
            
# TODO: Implement concurrency when doing API calls

def fetch_and_store_data(table_name="market_data"):
    """ GET Requests the Eve Online API endpoint https://market.fuzzwork.co.uk/aggregates/?region=30000142&types=9828 
    which takes two params region and types. This JSON data is then stored
    
    Region: The location that the markets are located in
    - There are 7 Regions
        - Global - 0
        - Jita - 30000142
        - Perimeter - 30000144
        - Jita 4-4 CNAP - 60003760
        - Amarr VIII - 60008494
        - Dodixie - 60011866
        - Rens - 60004588
        - Hek - 60005686
        
    Types: The ID of the raw material, List of IDs: https://docs.google.com/spreadsheets/d/1X7mi7j-_yV5lq-Yd2BraE-t4QE_a4IKv2ZuCBSLD6QU/edit?usp=sharing
    """
    
    # Checks if items in items.txt has changed and if it did makes api calls
    old_hash = pickler.load_pickle_data(cnt.HASH_PATH)
    new_hash = hashs.compute_hash(cnt.ABS_FILE_PATH_ITEMS)
    
    if old_hash != new_hash:
        items = api.get_raw_material_names()
        item_ids = [ api.get_item_id(i) for i in items ]
        pickler.pickle_data(item_ids, cnt.HASH_PATH)
        
    else:
        item_ids = pickler.load_pickle_data(cnt.ITEMS_PATH)
        
    json_data = {}

    # Fetch the data for each region and raw material id
    print("Attempting to fetch and insert data...")
    with alive_bar(len(cnt.REGIONS), force_tty=True) as bar:
        for r in cnt.REGIONS:
            
            # Fetching the data
            data = api.fetch_data(region_id=r, item_id=item_ids)
            
            # Storing the data into a postgresql table
            insert_data_into_table(table_name, region_id=r, json_data=data)
            bar()
    
    print("Successfully stored data for all regions!")


if __name__=='__main__':
    if sys.argv[1]:
        fetch_and_store_data(sys.argv[1])
    else:
        fetch_and_store_data() 