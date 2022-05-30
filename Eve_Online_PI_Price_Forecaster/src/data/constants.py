import os
from dotenv import load_dotenv, find_dotenv

"""---------------------- env constants --------------------------"""

# find .env by walking up directories until it's found
dotenv_path = find_dotenv()

# load up the entries as environment variables
load_dotenv(dotenv_path)

"""---------------------- database constants --------------------------"""

DATABASE_URL = os.environ.get('DATABASE_URL')
DATABASE_NAME = os.environ.get("DATABASE_NAME")
DATABASE_USER = os.environ.get("DATABASE_USER")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
DATABASE_PORT = os.environ.get("DATABASE_PORT")

"""---------------------- filepath and id constants --------------------------"""

parent_dir = os.path.abspath(os.path.join('.'))

# Filepath that contains the items that we are interested in forcasting
ABS_FILE_PATH_ITEMS = parent_dir + '/src/data/items.txt'

ITEMS_PATH = parent_dir + '/data/interim/pickle_items.p'
HASH_PATH = parent_dir + '/data/interim/hash_for_items.p'

# region ids that will be used in the function collect_data 
REGIONS = [0, 30000142, 30000144, 60003760, 60008494, 60011866, 60004588, 60005686]