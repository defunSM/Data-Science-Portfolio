# !/usr/bin/env python

# A class that contains all the market data for a particular material
# The goal of this class is to simplify the code written in notebooks
# and prevent unnessary code executions like API calls or postgresql calls.
# We can approach this by implementing a cache and an update function whenever we
# need to get the latest data.

from dataclasses import dataclass

@dataclass
class Material:
    """ Keeping track of a material's market stats in a particular region.
    """
    material_name: str
    region_id: str | int
        
    def plot():
        """ Returns a seaborn lineplot of the time series of various regions
        """
        pass
    
    def dataframe():
        """ Forms the dataframe of the market stats
        """
        return df
    
    def update():
        """ Updates the dataframe with the relevent dataframe and plot with new market data
        """