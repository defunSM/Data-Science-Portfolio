#!/usr/bin/env python

""" setup.py

Initializes data/interim/pickle_items.p and data/interim/hash_for_items.p from the default items.txt file in src/data/items.txt

"""

import os, sys


from os import path

from typing import List

import constants as cnt
import hashs
import pickle_helpers as pickler

def initialize_files(item_names: List = ["Silicon"]) -> None:
    """ Checks if items.txt exists and create items.txt based on `item_names`.
    
    Args:
        item_names (List, optional): The names of the raw materials to initialize to items.txt. Defaults to ["Silicon"].

    """
    
    # Check if items.txt exists otherwise create it
    if path.exists(cnt.ABS_FILE_PATH_ITEMS):
        pass
    else:
        f = open(cnt.ABS_FILE_PATH_ITEMS, "a")
        f.writelines(item_names)
        f.close()
        
    if path.exists(cnt.HASH_PATH):
        pass
    else:
        new_hash = hashs.compute_hash(cnt.ABS_FILE_PATH_ITEMS)
        pickler.pickle_data(new_hash, cnt.HASH_PATH)
    
    if path.exists(cnt.ITEMS_PATH):
        pass
    else:
        # picklize the item_names
        pickler.pickle_data(item_names, cnt.ITEMS_PATH)
        

if __name__ == '__main__':
    print(sys.path)
    print("Initializing startup files...")
    initialize_files()
    print("Initializing files completed!")