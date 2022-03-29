# ETL Pipeline

""" 
ETL Pipeline

process_data.py, cleaning pipeline that:

    Loads the messages and categories datasets
    Merges the two datasets
    Cleans the data
    Stores it in a SQLite database
    
    Example of Usage:
    python process_data.py disaster_messages.csv disaster_categories.csv DisasterResponse.db
    
"""

# Importing libraries for ETL
import numpy as np
import pandas as pd
from sqlalchemy import create_engine
import sys

def main():

    # Checks if the ETL pipeline is given proper arguments and throws error otherwise
    # TODO: Improve this later to identify which arguments are missing
    try:
        sys.argv[1]
        sys.argv[2]
        sys.argv[3]
    except IndexError:
        print("Usage Error: This script takes 3 arguments, the messages csv, categories csv and the name of the database.")
        print("Example Usage: python process_data.py disaster_messages.csv disaster_categories.csv DisasterResponse.db")
        return -1
    
    # Reading from the disaster messages
    try:
        messages = pd.read_csv(sys.argv[1])
    except:
        print("Error: Failed to read the first csv argument")
    
    # Reading from the disaster categories
    try:
        categories = pd.read_csv(sys.argv[2])
    except:
        print("Error: Failed to read the second csv argument")
    
if __name__ == '__main__':
    main()
    