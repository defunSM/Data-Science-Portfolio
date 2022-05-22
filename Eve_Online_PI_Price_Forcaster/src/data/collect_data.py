#!/usr/bin/env python
# coding: utf-8

""" collect_data.py

This module contains functions that help access the API data and store in the PostgreSQL
database. Some constants are needed to make connection with the database. Once connected
attempts to fetch relevent API data using region id and typeID. Finally storing them into
a table raw_market_data.

"""

# TODO: Remove the dependency on needing items.csv and change to make less
# TODO: api calls to https://www.fuzzwork.co.uk/api/typeid.php?typename=Microorganisms to
# TODO: to get the typeID. (reducing about 30 seconds from the whole process)

# ## Imports
import psycopg2
import os
import requests
import json
from os import path
from dotenv import load_dotenv, find_dotenv
from datetime import datetime
from alive_progress import alive_bar

"""---------------------- env constants --------------------------"""

# find .env by walking up directories until it's found
dotenv_path = find_dotenv()

# load up the entries as environment variables
load_dotenv(dotenv_path)

"""---------------------- database constants --------------------------"""

DATABASE_URL = os.environ.get('DATABASE_URL')
DATABASE_NAME = os.environ.get("DATABASE_NAME")
DATABASE_USER = os.environ.get("DATABASE_USER")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
DATABASE_PORT = os.environ.get("DATABASE_PORT")

"""---------------------- filepath and id constants --------------------------"""

# Filepath that contains the items that we are interested in forcasting
FILENAME = '../src/data/items.txt'

# region ids that will be used in the function collect_data 
REGIONS = [0, 30000142, 30000144, 60003760, 60008494, 60011866, 60004588, 60005686]

# find .env by walking up directories until it's found
dotenv_path = find_dotenv()

# load up the entries as environment variables
load_dotenv(dotenv_path)

DATABASE_URL = os.environ.get('DATABASE_URL')
DATABASE_NAME = os.environ.get("DATABASE_NAME")
DATABASE_USER = os.environ.get("DATABASE_USER")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")


def get_raw_material_names():
    """ Return a list of raw material names from from FILENAME

    Returns:
        raw_material_names: item names of interest for forcast
    """
    
    
    # List that will be returned after it has been populated
    raw_material_names = []
    
    if path.exists(FILENAME):
        
        file = open(FILENAME, "r")
        
        # Read each line from FILENAME and append each item name into the list
        for item in file.readlines():
            raw_material_names.append(item.strip('\n'))

        file.close()
        
    else:
        print(FILENAME, "does not exist.")
    
    # Make sure that the item names are not repeated
    raw_material_names = list(set(raw_material_names))
    
    return raw_material_names


def get_item_id(item_name=None):
    """ Returns the item ID from using the API endpoint https://www.fuzzwork.co.uk/api/typeid.php?typename=Silicon

    Args:
        item_name (string): Name of the raw material. Defaults to None.

    Returns:
        int: ids that are of type int
    """
    
    item_id = None
    
    api_url = "https://www.fuzzwork.co.uk/api/typeid.php?typename=" + item_name
    r = requests.get(api_url)
    item_id = r.json()['typeID']
    
    if item_id:
        return item_id
    
def fetch_data(region_id, item_id):
    """ Returns JSON given an input of the region and item from an API

    Args:
        region_id (int): id that is assigned to each major market region.
        item_id (int): id that is assigned to each raw material.

    Returns:
        dict: JSON Data from https://market.fuzzwork.co.uk/aggregates/?region=30000142&types=9828
    """
    
    api_url = "https://market.fuzzwork.co.uk/aggregates/?region=" + str(region_id) + "&types=" + str(item_id)
    r = requests.get(api_url)
    
    # encoding as json
    raw_material_data = r.json()
    
    return raw_material_data

def store_data():
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
    
    items = get_raw_material_names()
    item_ids = [ get_item_id(i) for i in items ]

    json_data = {}
    time = datetime.now()

    # Fetch the data for each region and raw material id
    print("Fetching data...")
    with alive_bar(len(item_ids)*len(REGIONS), force_tty=True) as bar:
        for i in item_ids:
            for r in REGIONS:
                data = fetch_data(region_id=r, item_id=i)
                json_data.update(data)
                bar()
    
    # Connecting to the database
    print("Trying to connect to database...")
    try:
        conn = psycopg2.connect(host=DATABASE_URL,
                                database=DATABASE_NAME,
                                user=DATABASE_USER,
                                password=DATABASE_PASSWORD)
        cursor = conn.cursor()
        
        print("Connected to database and now inserting data into table...")
        
        # sql to insert the json into the raw_market_data table
        insert_command = (
        """
        INSERT INTO raw_market_data (TIME, DATA) VALUES (%s, %s)
        """
        )
        
        # Serializing json
        json_object = json.dumps(json_data)
        
        # Inserting into table
        values = (time, json_object)
        cursor.execute(insert_command, values)
        
        # Close and commit changes to database server
        conn.commit()
        conn.close()
        
        print("Successfully stored data into table.")
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    

if __name__ == '__main__':
    store_data()


