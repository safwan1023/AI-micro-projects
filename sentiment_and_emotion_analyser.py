from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
import nltk

# Download necessary nltk data
nltk.download('vader_lexicon')

# Simple keywords dictionary for emotions
EMOTION_KEYWORDS = {
    'joy': ['happy', 'joy', 'glad', 'delighted', 'pleased', 'excited', 'love', 'wonderful', 'fantastic', 'great', 'awesome'],
    'anger': ['angry', 'mad', 'furious', 'annoyed', 'irritated', 'hate', 'disgust', 'frustrated', 'rage'],
    'sadness': ['sad', 'unhappy', 'depressed', 'down', 'hurt', 'lonely', 'miserable', 'cry', 'tears'],
    'fear': ['afraid', 'scared', 'fearful', 'nervous', 'anxious', 'worried', 'terrified'],
    'surprise': ['surprised', 'shocked', 'amazed', 'astonished', 'unexpected'],
    'disgust': ['disgusted', 'revolted', 'nauseated', 'gross', 'sick']
}

def detect_emotions(text):
    text_lower = text.lower()
    detected = []
    for emotion, keywords in EMOTION_KEYWORDS.items():
        if any(word in text_lower for word in keywords):
            detected.append(emotion)
    return detected if detected else ['neutral']

def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    scores = sia.polarity_scores(text)
    compound = scores['compound']

    if compound >= 0.05:
        sentiment = "Positive 😀"
    elif compound <= -0.05:
        sentiment = "Negative 😞"
    else:
        sentiment = "Neutral 😐"

    return sentiment, scores

def analyze_text(text):
    sentiment, scores = analyze_sentiment(text)
    emotions = detect_emotions(text)
    print(f"\nInput Text: {text}")
    print(f"Sentiment: {sentiment}")
    print(f"Emotions Detected: {', '.join(emotions)}")
    print(f"Sentiment Scores: {scores}")

if __name__ == "__main__":
    print("Enhanced Sentiment & Emotion Analyzer (type 'exit' to quit)")
    while True:
        user_text = input("\nEnter text: ")
        if user_text.lower() == 'exit':
            print("Exiting...")
            break
        analyze_text(user_text)
