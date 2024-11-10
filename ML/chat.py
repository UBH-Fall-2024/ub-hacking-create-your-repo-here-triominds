import random
import requests


HUGGINGFACE_API_KEY = "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"


EMOTION_ANALYSIS_MODEL = "j-hartmann/emotion-english-distilroberta-base"

API_URL = "https://api-inference.huggingface.co/models"

def analyze_emotion(text):
    """Analyze nuanced emotions using Hugging Face emotion detection model."""
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
    payload = {"inputs": text}
    
    response = requests.post(f"{API_URL}/{EMOTION_ANALYSIS_MODEL}", headers=headers, json=payload)
    
    if response.status_code == 200:
        response_json = response.json()
        print("Emotion Analysis Response:", response_json)
        
        # Get the emotion with the highest score
        emotions = response_json[0]
        primary_emotion = max(emotions, key=lambda x: x['score'])['label'].lower()
        
        return primary_emotion
    else:
        print("Emotion Analysis Failed with status code:", response.status_code)  
        print("Response Content:", response.content)  
        return "neutral"

def generate_reframing_message(emotion):
    """Generate a relevant message based on the detected emotion."""
    reframing_messages = {
        "anger": [
            "Take a moment to reflect on what triggered this anger. Consider if there’s a constructive way to address it.",
            "Anger can be challenging. It might help to channel this energy into a positive activity, like exercise or a creative task."
        ],
        "joy": [
            "That's wonderful! Remember to savor this joyful moment.",
            "It’s great to hear you’re feeling positive! Enjoy the happiness and think of ways to spread it around."
        ],
        "fear": [
            "Fear can be overwhelming. You might consider listing out your concerns and thinking of small steps to address them.",
            "Taking things slowly might help manage this fear. Try breaking down any challenges you face into smaller steps."
        ],
        "sadness": [
            "Sadness can feel heavy. Maybe taking a walk or engaging in a comforting activity could lighten things a bit.",
            "Remember, you don’t have to go through this alone. Reaching out to someone close might provide some comfort."
        ],
        "surprise": [
            "Surprises can bring unexpected emotions. Take some time to process it and think about how you might want to respond.",
            "New things can be a little unsettling, but they might also lead to positive changes. How do you feel about this surprise?"
        ],
        "neutral": [
            "I’m here whenever you’d like to share more.",
            "Sometimes, neutral moments give us a chance to recharge. Feel free to tell me anything on your mind."
        ]
    }
    

    return random.choice(reframing_messages.get(emotion, ["I'm here to support you. Feel free to share more."]))

def handle_emotion_analysis(input_text):
    """Handle emotion and generate a response based on the detected emotion."""
    emotion = analyze_emotion(input_text)
    print("Detected Emotion:", emotion)  
    
  
    reframing_message = generate_reframing_message(emotion)
    response = f"{reframing_message} Is there anything else you’d like to discuss?"

    return response

def chatbot(text):
    """Chatbot function to process the input and generate appropriate responses."""
    if text:
       
        emotion = analyze_emotion(text)
        print("Detected Emotion:", emotion) 

   
        reframing_response = generate_reframing_message(emotion)
        reply = f"{reframing_response} Is there anything else you’d like to discuss?"

        return reply
    return "I'm here to help with your thoughts!"
