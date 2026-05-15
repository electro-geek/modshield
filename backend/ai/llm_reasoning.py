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

        try:
            try:
                # Call generate_content using the new client
                response = self.client.models.generate_content(
                    model='gemini-1.5-flash',
                    contents=prompt
                )
            except Exception as e:
                # Keep fallback logic for 404s or unsupported model errors
                if "404" in str(e) or "not found" in str(e).lower():
                    print(f"Primary model error: {e}. Trying gemini-pro fallback...")
                    response = self.client.models.generate_content(
                        model='gemini-pro',
                        contents=prompt
                    )
                else:
                    raise e

            # Simple extraction of JSON from response
            text = response.text
            json_match = re.search(r'\{.*\}', text, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
            
            return {"suggested_action": "review", "reasoning": "Could not parse AI response"}
        except Exception as e:
            print(f"Error in AI reasoning: {e}")
            return {"suggested_action": "review", "reasoning": f"Error: {str(e)}"}
