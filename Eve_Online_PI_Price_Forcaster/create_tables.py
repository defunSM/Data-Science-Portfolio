#!/usr/bin/python

# This script will initialize the tables into our database.

#!/usr/bin/python

import redis
from decouple import config

HOSTNAME = config('HOSTNAME')
PASSWORD = config('PASSWORD')
PORT = config('PORT')

def create_tables():
    """ Create tables in the Redis database"""
    
    r = redis.Redis(
        host=HOSTNAME,
        port=PORT, 
        password=PASSWORD)
    
    value = r.get('foo')
    print(value)


if __name__ == '__main__':
    create_tables()