import requests
import sys
sys.path.insert(1, 'D://jarves_backend//speak')
import speak
def get_weather(city):
    api_key = '3437d6f73ffe4e6882f125254230412 '
    base_url = f'http://api.worldweatheronline.com/premium/v1/weather.ashx?key={api_key}&q={city}&format=json'

    try:
        response = requests.get(base_url)
        data = response.json()
        if 'data' in data and 'current_condition' in data['data']:
            weather_description = data['data']['current_condition'][0]['weatherDesc'][0]['value']
            temperature_celsius = data['data']['current_condition'][0]['temp_C']
            suggestion = ""
            if 'cloud' in weather_description.lower():
                suggestion = "It seems cloudy. You might want to carry an umbrella."
            elif 'rain' in weather_description.lower():
                suggestion = "It's raining. Don't forget your raincoat or umbrella!"
            elif 'sunny' in weather_description.lower():
                suggestion = "It's sunny outside. Wear sunscreen and sunglasses."
            elif 'snow' in weather_description.lower():
                suggestion = "It's snowing. Wear warm clothes and boots."
            elif 'clean' in weather_description.lower():
                suggestion = "Enjoy the clear weather! It's a good time to go out and relax."
            else:
                suggestion = "Weather condition information available, but no specific suggestion."

            return f"The weather in {city} is {weather_description}. The temperature is {temperature_celsius}°C. i suggested you to {suggestion}"
        else:
            return "Sorry, I couldn't fetch the weather details at the moment."
    except Exception as e:
        return f"Error fetching weather data: {str(e)}"
def google(query):
    import webbrowser
    query=query.lower()
    if "perform a web search" in query:
        search_query = query.replace("perform a web search", "")
        search_query.replace(" ", "")
        # speak.speak(search_query)
    elif "search on browser" in query:
        search_query = query.replace("search on browser", "")
        search_query.replace(" ", "")
        # speak.speak(search_query)
    elif "search the web" in query:
        search_query = query.replace("search the web", "")
        search_query.replace(" ", "")
        # speak.speak(search_query)
    elif "look up information" in query:
        search_query = query.replace("look up information", "")
        search_query.replace(" ", "")
        # speak.speak(search_query)
    elif "search" in query:
        search_query = query.replace("search", "")
        search_query.replace(" ", "")
        # speak.speak(search_query)
    if search_query.strip():
        search_url = f"https://www.google.com/search?q={search_query}"
        speak.speak(f"Here are the search results for {search_query}.")
        webbrowser.open(search_url)
    else:
        speak.speak("Sorry, I didn't catch that. Please try again.")
