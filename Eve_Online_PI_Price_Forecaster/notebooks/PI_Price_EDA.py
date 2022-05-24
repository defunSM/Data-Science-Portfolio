#!/usr/bin/env python
# coding: utf-8

# ## Imports

# In[1]:


import psycopg2
import os
import requests
import json
import pathlib
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
ABS_FILE_PATH_ITEMS = 'src/data/items.txt'

# region ids that will be used in the function collect_data 
REGIONS = [0, 30000142, 30000144, 60003760, 60008494, 60011866, 60004588, 60005686]


# In[2]:


def create_tables():
    """ create tables in the PostgreSQL database"""
    command = (
        """
        CREATE TABLE market_data (
            id SERIAL PRIMARY KEY,
            time TIMESTAMP,
            region_id INTEGER,
            data JSON
        )
        """)
    
    conn = psycopg2.connect(host=DATABASE_URL,
                            database=DATABASE_NAME,
                            user=DATABASE_USER,
                            password=DATABASE_PASSWORD,
                            port=DATABASE_PORT)
    try:

        # connect to the PostgreSQL server
        cur = conn.cursor()
        
        # create table one by one
        cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
        
        print("Table created successfully")
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


# In[3]:


#create_tables()


# ## Table of Contents
# 
# 1. [Data Collection](#data-collection)
# 2. [Preprocessing](#preprocessing)

# ## Data Collection

# In[5]:


def get_raw_material_names():
    """ Return a list of raw material names from from ABS_FILE_PATH_ITEMS

    Returns:
        raw_material_names: item names of interest for forcast
    """
    
    
    # List that will be returned after it has been populated
    raw_material_names = []
    
    if path.exists(ABS_FILE_PATH_ITEMS):
        
        file = open(ABS_FILE_PATH_ITEMS, "r")
        
        # Read each line from ABS_FILE_PATH_ITEMS and append each item name into the list
        for item in file.readlines():
            raw_material_names.append(item.strip('\n'))

        file.close()
        
        # Make sure that the item names are not repeated
        raw_material_names = list(set(raw_material_names))
    
        return raw_material_names
        
    else:
        print(ABS_FILE_PATH_ITEMS, "does not exist.")

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
        item_id (int, list): id or list of ids that is/are assigned to each raw material.

    Returns:
        dict: JSON Data from https://market.fuzzwork.co.uk/aggregates/?region=30000142&types=9828
    """
    
    # Formating so that it'll be accepted by the API endpoint
    item_id = str(item_id).strip('[]').replace(" ", "")
    
    api_url = "https://market.fuzzwork.co.uk/aggregates/?region=" + str(region_id) + "&types=" + item_id
    r = requests.get(api_url)
    
    # encoding as json
    raw_material_data = r.json()
    
    return raw_material_data

def insert_data(table_name='market_data', region_id=None, json_data=None):
    """ Connects with postgresql database and inserts records into a table.

    Args:
        table_name (str, optional): _description_. Defaults to 'raw_material_data'.
        region_id (int, optional): _description_. Defaults to None.
        json_data (json, optional): _description_. Defaults to None.
    """
    
    time = datetime.now()
    
    try:
        conn = psycopg2.connect(host=DATABASE_URL,
                                database=DATABASE_NAME,
                                user=DATABASE_USER,
                                password=DATABASE_PASSWORD)
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


# In[9]:


# TODO: Implement concurrency when doing API calls

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

    # Fetch the data for each region and raw material id
    print("Attempting to fetch and insert data...")
    with alive_bar(len(REGIONS), force_tty=True) as bar:
        for r in REGIONS:
            
            # Fetching the data
            data = fetch_data(region_id=r, item_id=item_ids)
            
            # Storing the data into a postgresql table
            insert_data(table_name='market_data', region_id=r, json_data=data)
            bar()
    
    print("Successfully stored data for all regions!")
    
    


# In[11]:





# In[10]:


if __name__ == "__main__":
    store_data()


# ## Preprocessing
