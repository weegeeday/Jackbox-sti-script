import os
import openai
import configparser
config = configparser.ConfigParser()
with open('OpenAI.ini',"r") as configfille:
    key = config.get("api_key",str)
    org = config.get("org_id",str)
openai.organization = org
openai.api_key = key
openai.Model.list()