# Helper functions

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pickle

from typing import List
import api

"""--------------------------- Pickle -----------------------------------"""

def pickle_data(item, filepath):
    """ Picklizes the 'item' and saves it to a 'filepath'.

    Args:
        item (any): Object to be picklized
        filepath (string): The filepath that you want to save the picklized object to.
    """
    
    with open(filepath, 'wb') as pickle_file:
        pickle_items = pickle.dump(item, pickle_file)
        
def load_pickle_data(filepath):
    """ Loads a picklized object from a 'filepath'.

    Args:
        filepath (string): filepath to the picklized data

    Returns:
        any: The picklized data that was stored in the filepath
    """
    
    with open(filepath, 'rb') as pickle_file:
        data = pickle.load(pickle_file)
        
    return data

"""----------------- Exploratory Data Analysis -------------------------"""

# TODO: Improve function to follow dry principles, remove the depedency of raw_material_name and market_data, one way to do this might be to remove the dependency of using market data in create item dataframe
def create_item_dataframe(raw_material_name: str, region_id: str | int = "0"):
    """ Dataframe constructed from the stats of a material and region id. Will contain stats like
    sell and buy weighted Average, median, min, max, stddev and order counts.

    Args:
        raw_material_name (str): Name of the material
        region_id (str | int, optional): The region id that associates with one of the regions in Eve Online. Defaults to "0".

    Returns:
        Dataframe: Contains all stats for a particular material
    """
    
    # TODO: fix the repetitive code below
    # Historical average buy and sell order stats for raw_material_name
    buy_market_stats = api.market_data(raw_material_name, region_id=region_id)
    buy_order_stats = [i[2] for i in buy_market_stats]
    times = [i[1] for i in buy_market_stats]
    
    sell_market_stats = api.market_data(raw_material_name, region_id=region_id, order_type="sell")
    sell_order_stats = [i[2] for i in sell_market_stats]
    times = [i[1] for i in sell_market_stats]

    # Creating dataframe for buy and sell orders and renaming columns
    df_buy = pd.DataFrame(data=buy_order_stats)
    df_buy.rename(columns=lambda x: "buy_" + x, inplace=True)
    
    df_sell = pd.DataFrame(data=sell_order_stats)
    df_sell.rename(columns=lambda x: "sell_" + x, inplace=True)
    
    df_times = pd.DataFrame(data=times, columns=["time"])

    df = pd.concat([df_times, df_buy, df_sell], axis=1)
    
    # Fixing datatype for all the columns except the time column
    for i in df.iloc[:,1:].columns:
        df[i] = pd.to_numeric(df[i])

    return df

def plot_timeseries(raw_material_name, df, cols):
    df = df[cols]
    data = pd.melt(df, ["time"])
        
    # Plot time series
    sns.set_theme(style="white")
    fig = sns.lineplot(data=data, x='time', y='value', hue='variable')
    fig.set(title=f"The Price of {raw_material_name}", ylabel="Price (ISK)")
    fig.lines[0].set_linestyle("--")
    plt.xticks(rotation=90)

def create_item_plot(raw_material_name: str, region_id: str = "0", cols: List[str]=['time', 'sell_weightedAverage']):
    
    df = create_item_dataframe(raw_material_name, region_id=region_id)
    
    if 'time' not in cols:
        cols.append('time')
        
    plot_timeseries(raw_material_name, df, cols)
    