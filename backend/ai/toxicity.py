import requests
import json
import os
from configparser import ConfigParser

class ToxicityDetector:
    def __init__(self, api_key=None):
        self.api_key = api_key
        self.url = f"https://commentanalyzer.googleapis.com/v1alpha1/comments:analyze?key={self.api_key}"

    def analyze(self, text):
        if not self.api_key or self.api_key == "your_perspective_key":
            # Mock implementation for demo if no API key is provided
            import random
            return {
                "toxicity": random.uniform(0, 0.5),
                "severe_toxicity": random.uniform(0, 0.2),
                "insult": random.uniform(0, 0.3),
                "threat": random.uniform(0, 0.1)
            }

        data = {
            "comment": {"text": text},
            "languages": ["en"],
            "requestedAttributes": {
                "TOXICITY": {},
                "SEVERE_TOXICITY": {},
                "INSULT": {},
                "THREAT": {}
            }
        }

        try:
            response = requests.post(self.url, data=json.dumps(data))
            response.raise_for_status()
            result = response.json()
            
            scores = result["attributeScores"]
            return {
                "toxicity": scores["TOXICITY"]["summaryScore"]["value"],
                "severe_toxicity": scores["SEVERE_TOXICITY"]["summaryScore"]["value"],
                "insult": scores["INSULT"]["summaryScore"]["value"],
                "threat": scores["THREAT"]["summaryScore"]["value"]
            }
        except Exception as e:
            print(f"Error in Toxicity analysis: {e}")
            return None
