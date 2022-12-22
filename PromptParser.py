import json
import os
import time

class PromptParser:
    def __init__(self):
        self.file_names = [
            "STIPrompt.jet",
            "STIJobPrompt.jet",
            "STIPhotoPrompt.jet",
            "STIStorePrompt.jet",
        ]
        self.data = []

    def read(self):
        for file_name in self.file_names:
            with open(file_name, "r") as f:
                content = json.loads(f.read())["content"]
                self.data.extend(content)

    def write(self, prompt_number):
        prompt = self.data[prompt_number - 1]
        with open("STIContent to put in content/STIPrompt.jet", "w") as f:
            f.write(json.dumps({"content": [prompt]}))
