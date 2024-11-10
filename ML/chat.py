import random
import requests

# Set your Hugging Face API token
HUGGINGFACE_API_KEY = "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"

# Set the Hugging Face endpoint for sentiment analysis and text generation models
SENTIMENT_ANALYSIS_MODEL = "distilbert-base-uncased-finetuned-sst-2-english"  # A model for sentiment analysis
TEXT_GENERATION_MODEL = "gpt-2"  # A model for text generation

# Hugging Face API URL for inference
API_URL = "https://api-inference.huggingface.co/models"

def analyze_sentiment(text):
    """Analyze sentiment using Hugging Face sentiment model."""
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
    payload = {"inputs": [text]}  # Adjusted to ensure compatibility
    
    response = requests.post(f"{API_URL}/{SENTIMENT_ANALYSIS_MODEL}", headers=headers, json=payload)
    
    if response.status_code == 200:
        response_json = response.json()
        print("Sentiment Analysis Response:", response_json)
        
        # Access the first element in the outer and inner lists
        sentiment = response_json[0][0]['label'].lower()  
        return sentiment
    else:
        print("Sentiment Analysis Failed with status code:", response.status_code)  
        print("Response Content:", response.content)  
        return "neutral"  

def generate_reframing_message(negative_thought):
    """Generate a reframing message based on the negative thought."""
    if negative_thought:
        reframing_messages = [
            "Let's explore this thought. Can you recall a time when things turned out better than expected?",
            "It’s okay to feel this way, but let’s challenge this belief. Can you think of one instance where you overcame a similar situation?",
            "Remember, every step forward, no matter how small, is progress. You've got this!",
            "It's completely normal to feel like this sometimes, but it doesn’t define your ability. Let's shift the focus to your strengths."
        ]
        return random.choice(reframing_messages)
    return "I couldn't generate a reframing message. Please try again."

def handle_sentiment_analysis(input_text):
    """Handle sentiment and generate a response based on sentiment."""
    sentiment = analyze_sentiment(input_text)  # Assuming you have this function implemented
    
    # For Positive Sentiment
    if sentiment == 'positive':
        response = "That's great! You're on the right track. Keep nurturing this positive mindset."
    
    # For Negative Sentiment
    elif sentiment == 'negative':
        reframing_message = generate_reframing_message(input_text)
        response = f"{reframing_message} Would you like to try a breathing exercise?"
    else:
        response = "I'm not sure about the sentiment. Could you share more thoughts?"

    return response

def chatbot(text):
    """Chatbot function to process the input and generate appropriate responses."""
    if text:
        # Step 1: Analyze sentiment to determine if the thought needs reframing
        sentiment = analyze_sentiment(text)
        print("Detected Sentiment:", sentiment)  # Debug print

        # Step 2: If sentiment is negative, generate a reframing response
        if sentiment == "negative":
            reframing_response = generate_reframing_message(text)
            reply = f"{reframing_response} Would you like to try a breathing exercise?"
        else:
            reply = "This thought doesn't appear negative. Keep up the positive mindset!"

        return reply
    return "I'm here to help with your thoughts!"
