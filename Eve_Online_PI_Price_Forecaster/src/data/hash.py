import hashlib

def compute_hash(filepath):
    """ Hashlib library to compute a hash for a file using sha256 algo.

    Args:
        filepath (string): path to the file in which we want to hash

    Returns:
        string: A hexadecimal string of the hash
    """
    
    # The size of each read from the file (64Kb)
    BLOCK_SIZE = 65536 

    # Create the hash object
    file_hash = hashlib.sha256() 
    
    with open(filepath, 'rb') as f:
        fb = f.read(BLOCK_SIZE)
        
        # While there is still data being read from the file
        while len(fb) > 0: 
            file_hash.update(fb) 
            fb = f.read(BLOCK_SIZE) 

    return file_hash.hexdigest() # Get the hexadecimal digest of the hash