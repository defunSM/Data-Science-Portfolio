import sys
import numpy as np
import pandas as pd
from sqlalchemy import create_engine

def load_data(messages_filepath, categories_filepath):
    """Loading messages and categories csv"""
    
    # Reading from the disaster messages
    try:
        messages = pd.read_csv(messages_filepath)
    except:
        print("Error: Failed to read the first csv argument")
    
    # Reading from the disaster categories
    try:
        categories = pd.read_csv(categories_filepath)
    except:
        print("Error: Failed to read the second csv argument")
        
    # Merge both datasets
    df = pd.merge(messages, categories)
    
    # Create a dataframe of the 36 individual category columns
    categories = df['categories'].str.split(';', expand = True)
    
    # select the first row of the categories dataframe
    row = categories.iloc[0]

    # use this row to extract a list of new column names for categories.
    # one way is to apply a lambda function that takes everything 
    # up to the second to last character of each string with slicing
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
    

    
    return df


def clean_data(df):
    """Doing any data set cleaning such as removing duplicates on the dataframe"""
    
    # Remove duplicates
    df.drop_duplicates
    
    # Want to drop child_alone as well since there are no samples for that category
    #df.drop(columns=['child_alone'])
    
    # Dropping rows that have a value of 2
    print(df.head(5))
    df = df[df['related'] != 2]
    
    return df


def save_data(df, database_filename):
    """Save and clean dataset into sqlite database"""
    
    engine = create_engine('sqlite:///' + database_filename)
    df.to_sql(database_filename, engine, index=False)

def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()