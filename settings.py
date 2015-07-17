#put all our settings here

# don't want the consumer token public. Importing from my home directory,
#but you can change this. Should standardize this eventually for deployment

import sys, os

secretsdir = os.path.join(os.getenv("HOME"), "sensitive_data")
sys.path.append(secretsdir)
from secret_stuff import *

# TWITTER_CONSUMER_KEY and TWITTER_CONSUMER_SECRET are now defined
DATABASE_NAME = "/home/ubuntu/workspace/troll_interconnector/test.db"





