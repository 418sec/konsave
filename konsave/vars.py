## IMPORT ##
import os


## GLOBAL VARS ##
HOME = os.path.expandvars('$HOME')
CONFIG_DIR = os.path.join(HOME, '.config')
KONSAVE_DIR = os.path.join(CONFIG_DIR, 'konsave')
PROFILES_DIR = os.path.join(KONSAVE_DIR, 'profiles')
CONFIG_FILE = os.path.join(KONSAVE_DIR, "conf.yaml")

export_extension = '.knsv'

# Create PROFILES_DIR if it doesn't exist
if not os.path.exists(PROFILES_DIR):
    os.makedirs(PROFILES_DIR)

list_of_profiles = os.listdir(PROFILES_DIR)
length_of_lop = len(list_of_profiles)

# Current Version
VERSION = "1.1.5"

