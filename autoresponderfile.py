import googlemaps
from googlemaps import Client
from googlemaps.places import places_nearby
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')
def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)
    return sentiment

# Konfiguruje klienta API
gmaps = Client(key='tu klucz api')

# Szuka miejsca bazując na wprowadzonej lokalizacji
places = gmaps.places_nearby(location='49.95007486001696, 18.493966693112732', radius=100, keyword='...........')

# Pobiera opinie z podanego miejsca
place_id = places['results'][0]['place_id']
reviews = gmaps.place(place_id)['result']['reviews']

# Analizuje
for review in reviews:
    text = review['text']

    # używa nltk
    sentiment = analyze_sentiment(text)

    # Pisze odpowiedź w zależności od wypowiedzi
    if sentiment['compound'] >= 0.05:
        response = "Dziękujemy za pozytywną opinię! Cieszymy się że masz pozytywne wrażenia."
    elif sentiment['compound'] <= -0.05:
        response = "Bardzo przepraszamy za uniedogodnienia. Weźmiemy pod uwagę twoją opinię i postaramy się poprawić."
    else:
        response = "Dziękujemy za twoją opinię. Każda informacja zwrotna jest dla nas na wagę złota."

    print(f"Review: {text}\nSentiment: {sentiment}\nSuggested Response: {response}\n")










    
  ###  #gmaps.place(place_id, review={'text': 'Thank you for your feedback!', 'language': 'en'})
