from configparser import ConfigParser

def read_file(section, key):
    config = ConfigParser()
    config.read("config.ini")
    return config.get(section, key)