#!/usr/bin/env python

import requests

from typing import List
from os import path
from pydantic import validate_arguments

import constants as cnt
import database as db

def get_raw_material_names():
    """ Return a list of raw material names from from ABS_FILE_PATH_ITEMS

    Returns:
        raw_material_names: item names of interest for forcast
    """
    
    # List that will be returned after it has been populated
    raw_material_names = []
    
    if path.exists(cnt.ABS_FILE_PATH_ITEMS):

        file = open(cnt.ABS_FILE_PATH_ITEMS, "r")
        
        # Read each line from ABS_FILE_PATH_ITEMS and append each item name into the list
        for item in file.readlines():
            raw_material_names.append(item.strip('\n'))

        file.close()
        
        # Make sure that the item names are not repeated
        raw_material_names = list(set(raw_material_names))
        
        return raw_material_names
        
    else:
        print(cnt.ABS_FILE_PATH_ITEMS, "does not exist.")
        
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
    
def fetch_data(region_id: int, item_id: int | List[int]):
    
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

@validate_arguments
def market_data(item_name: str, region_id: int | str , order_type: str = "buy", stat: str = "weightedAverage") -> List:
    """ Makes a query to the postgresql database market_data based on the parameters specified.

    Args:
        item_name (str): Provide the name of the raw material,
        
        region_id (str, int): Select region id of the market data. defaults to "0".
        
            - There are 7 Regions
                - Global - 0
                - Jita - 30000142
                - Perimeter - 30000144
                - Jita 4-4 CNAP - 60003760
                - Amarr VIII - 60008494
                - Dodixie - 60011866
                - Rens - 60004588
                - Hek - 60005686
                
        order_type (str, optional): Either 'buy' or 'sell' orders. Defaults to "buy".
        
        stat(str): Select the summary statistic to return

            - Valid args for stat:
                - weightedAverage
                - max
                - min
                - stddev
                - median
                - volume
                - orderCount
                - percentile

    Returns:
        List: Contains a list of tuples containing id, time, and data from market_data
    """
    # Validating and reformating arguments into proper format
    order_type = order_type.lower()
    itemid = get_item_id(item_name)
    
    # Postgresql query unpacking JSON data field
    command = (
        f"""
        SELECT id, time, data -> '{itemid}' -> '{order_type}'
        FROM market_data
        WHERE region_id = {region_id}
        """
        )
    
    results = db.postgresql_command(command, results=True)
    
    return results
    