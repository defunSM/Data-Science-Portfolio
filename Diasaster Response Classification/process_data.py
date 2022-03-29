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
        
    # Merge both datasets
    df = pd.merge(messages, categories)
    
    # Split categories into seperate category columns
    categories = categories['categories'].str.split(";", expand=True)
    
    # rename column names
    row = categories.iloc[0]
    category_colnames = [i.split('-')[0] for i in row]
    categories.columns = category_colnames
    
    # Convert category values to numberic either 0 or 1
    for column in categories:
        # set each value to be the last character of the string
        categories[column] = categories[column].str.split('-', expand=True)[1]
    
        # convert column from string to numeric
        categories[column] = pd.to_numeric(categories[column])
        
    # Replace categories colum in df to new category columns
    df = df.drop(columns=['categories'])
    
    # concatenate the original dataframe with the new categories dataframe
    df = pd.concat([df, categories], axis=1)
    
    # Remove duplicates
    df = df.drop_duplicates
    
    # Save and clean dataset into sqlite database
    engine = create_engine('sqlite:///' + sys.argv[3])
    df.to_sql(sys.argv[3], engine, index=False)
    
if __name__ == '__main__':
    main()
    