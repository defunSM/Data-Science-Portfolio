#!/usr/bin/env python

import requests
from os import path

from src.data.constants import ABS_FILE_PATH_ITEMS

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