# Functions related to serialization

import pickle

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