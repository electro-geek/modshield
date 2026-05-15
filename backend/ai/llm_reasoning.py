import os
from google import genai
from configparser import ConfigParser
import json
import re

class AIReasoningEngine:
    def __init__(self, api_key=None):
        self.api_key = api_key
        if self.api_key and self.api_key != "your_gemini_key":
            try:
                # Using the new google-genai SDK
                self.client = genai.Client(api_key=self.api_key)
            except Exception as e:
                print(f"Error initializing Gemini Client: {e}")
                self.client = None
        else:
            self.client = None

    def generate_moderation_suggestion(self, post_title, post_content, scores):
        if not self.client:
            return {
                "suggested_action": "review",
                "reasoning": "AI model not configured. Scores: " + str(scores)
            }

        prompt = f"""
        You are a Reddit moderation assistant. Analyze the following post and the AI scores provided.
        
        Post Title: {post_title}
        Post Content: {post_content}
        
        AI Scores:
        Toxicity: {scores.get('toxicity', 0)}
        Spam: {scores.get('spam', 0)}
        Scam: {scores.get('scam', 0)}
        
        Based on this, suggest a moderation action (approve, remove, ban) and provide a brief reasoning.
        Return the result in JSON format:
        {{
            "suggested_action": "...",
            "reasoning": "..."
        }}
        """

        # List of candidate models to try in order of preference
        candidate_models = [
            'gemini-2.5-flash',
            'gemini-1.5-flash',
            'gemini-1.5-flash-latest',
            'gemini-1.5-pro',
            'gemini-pro'
        ]

        last_error = None
        response = None

        for model_name in candidate_models:
            try:
                print(f"Attempting to use model: {model_name}")
                response = self.client.models.generate_content(
                    model=model_name,
                    contents=prompt
                )
                if response:
                    print(f"Successfully used model: {model_name}")
                    break
            except Exception as e:
                last_error = e
                print(f"Model {model_name} failed: {e}")
                continue

        if not response:
            return {"suggested_action": "review", "reasoning": f"All AI models failed. Last error: {str(last_error)}"}

        try:
            # Simple extraction of JSON from response
            text = response.text
            json_match = re.search(r'\{.*\}', text, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
            
            return {"suggested_action": "review", "reasoning": "Could not parse AI response"}
        except Exception as e:
            print(f"Error in AI reasoning parsing: {e}")
            return {"suggested_action": "review", "reasoning": f"Error parsing: {str(e)}"}
