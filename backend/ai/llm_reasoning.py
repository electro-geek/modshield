import warnings
warnings.filterwarnings("ignore", category=FutureWarning, module="google.generativeai")
import google.generativeai as genai
import os
from configparser import ConfigParser

class AIReasoningEngine:
    def __init__(self, api_key=None):
        self.api_key = api_key
        if self.api_key and self.api_key != "your_gemini_key":
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel('gemini-1.5-flash')
        else:
            self.model = None

    def generate_moderation_suggestion(self, post_title, post_content, scores):
        if not self.model:
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
            response = self.model.generate_content(prompt)
            # Simple extraction of JSON from response
            text = response.text
            import json
            import re
            json_match = re.search(r'\{.*\}', text, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
            return {"suggested_action": "review", "reasoning": "Could not parse AI response"}
        except Exception as e:
            print(f"Error in AI reasoning: {e}")
            return {"suggested_action": "review", "reasoning": f"Error: {str(e)}"}
