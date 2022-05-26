#!/usr/bin/env python

""" setup.py

Initializes data/interim/pickle_items.p and data/interim/hash_for_items.p from the default items.txt file in src/data/items.txt

"""

import path

from typing import List

from constants import ABS_FILE_PATH_ITEMS, ITEMS_PATH, HASH_PATH
from hashs import compute_hash
from database import pickle_data

def initialize_files(item_names: List = ["Silicon"]) -> None:
    """ Checks if items.txt exists and create items.txt based on `item_names`.
    
    Args:
        item_names (List, optional): The names of the raw materials to initialize to items.txt. Defaults to ["Silicon"].

    """
    
    # Check if items.txt exists otherwise create it
    if path.exists(ABS_FILE_PATH_ITEMS):
        pass
    else:
        f = open(ABS_FILE_PATH_ITEMS, "a")
        f.writelines(item_names)
        f.close()
        
        # Create new hash
        new_hash = compute_hash(ABS_FILE_PATH_ITEMS)
        pickle_data(new_hash, HASH_PATH)
        
        # picklize the item_names
        pickle_data(item_names, ITEMS_PATH)
        

if __name__ == '__main__':
    print("Initializing startup files...")
    initialize_files()
    print("Initializing files completed!")