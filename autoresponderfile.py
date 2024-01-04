import requests


def fetch_place_details(place_id, api_key):
    url = f"https://maps.googleapis.com/maps/api/place/details/json?placeid={place_id}&key={api_key}"

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


# Użycie funkcji
api_key = 'AIzaSyDtWk_6Dfntvt-nOaOa1xQ0ViY8JgpoTzU'
place_id = 'ChIJkYZ6jtBTEUcRB49jj4eb4e4'  # ID miejsca, które chcesz zbadać
place_details = fetch_place_details(place_id, api_key)

if place_details:
    print(place_details)  # Tutaj możesz przetwarzać dane
else:
    print("Błąd w pobieraniu danych z Google Maps API")