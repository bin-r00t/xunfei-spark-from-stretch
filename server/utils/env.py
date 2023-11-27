from configparser import ConfigParser

conf = ConfigParser()
conf.read('test.ini')

# ini file should be like this:
# [xunfei]
# api_key = xxx
# api_secret = xxx
# app_id = xxx

def get_config():
  return conf

def get_apikey():
  return conf['xunfei']['api_key']

def get_api_secret():
  return conf['xunfei']['api_secret']