import re

class ScamDetector:
    def __init__(self):
        self.scam_keywords = [
            r"free crypto", r"giveaway", r"send me", r"wallet", r"private key",
            r"guaranteed returns", r"investment opportunity", r"click here",
            r"phishing", r"login to", r"verify your account"
        ]

    def analyze(self, text):
        text_lower = text.lower()
        matches = 0
        for pattern in self.scam_keywords:
            if re.search(pattern, text_lower):
                matches += 1
        
        # Calculate a simple score based on matches
        score = min(1.0, (matches * 0.3))
        
        # Add some randomness for demo realism if score is 0
        if score == 0:
            import random
            score = random.uniform(0, 0.1)
            
        return {
            "scam_score": score,
            "detected_patterns": matches
        }
