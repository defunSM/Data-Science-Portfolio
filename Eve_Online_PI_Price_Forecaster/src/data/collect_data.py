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

# TODO: Move constants into a seperate folder to be used in other locations since
# TODO: database constants are needed in both collect_data and create_tables

from get_data import store_data
    
if __name__ == '__main__':
    store_data()


