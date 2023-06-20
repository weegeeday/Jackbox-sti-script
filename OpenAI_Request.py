import os
import openai
import configparser
import json
config = configparser.ConfigParser()
config.read("OpenAI.ini")
key = config["OPENAI"]["api_key"]
org = config["OPENAI"]["org_id"]
openai.organization = org
openai.api_key = key
class OpenAIRequest():
    @staticmethod
    def Completion(Model,Prompt,Temperature):
        response = openai.Completion.create(
            model = Model,
            prompt = Prompt,
            temperature = Temperature
        )
        print(response)
#My openAI account has no credits, until i get a job i wont be able to finish this.