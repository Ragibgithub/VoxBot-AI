

def open(query):
    import pyautogui
    from time import sleep
    query.lower()
    if "open" in query:
        search_query = query.replace("open", "")
        search_query.replace(" ", "")
        # speak.speak(search_query)
    elif "start" in query:
        search_query = query.replace("start", "")
        search_query.replace(" ", "")
        # speak.speak(search_query)
    elif "launch" in query:
        search_query = query.replace("launch", "")
        search_query.replace(" ", "")
        # speak.speak(search_query)
    elif "run" in query:
        search_query = query.replace("run", "")
        search_query.replace(" ", "")
        # speak.speak(search_query)
    pyautogui.press("super")
    pyautogui.typewrite(search_query)
    sleep(1)
    pyautogui.press("enter")
    return search_query

from newsapi import NewsApiClient

def get_news_by_category(api_key, category, idx=1, detail=False):
    # Initialize NewsApiClient with your API key
    newsapi = NewsApiClient(api_key=api_key)
    
    try:
        # Fetch top headlines based on the specified category
        top_headlines = newsapi.get_top_headlines(category=category, language='en', country='us')
        
        # Extract articles from the response
        articles = top_headlines['articles']
        
        # Print the titles of the news articles
        for article_idx, article in enumerate(articles, start=idx):
            if detail:
                return f"Article {article_idx}: {article['title']}: {article['description']}"
            else:
                return f"Article {article_idx}: {article['title']}"
                
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
def news(text):
    import sys
    sys.path.insert(1, 'D://jarves_backend//speak')
    from speak import speak
    text = text.lower()
    api_key = 'f15d5a474d0e4d1ba0307c6103c79c12'
    category = None
    if "business" in text:
        category = 'business'
    elif "entertainment" in text:
        category = 'entertainment'
    elif "health" in text:
        category = 'health'
    elif "science" in text:
        category = 'science'
    elif "sports" in text:
        category = 'sports'
    elif "technology" in text:
        category = 'technology'
    elif "general" in text:
        category = 'general'
    else:
        speak("I don't understand which type of news you want. Please repeat.")
        a = input()
        return news(a)

    start_idx = 1

    while True:
        a = get_news_by_category(api_key, category, start_idx, detail=False)
        speak(a)
        start_idx += 1
        i = input("To stop, type 'stop'. For details, type 'detail': ")
        if i.lower() == 'stop':
            break
        elif i.lower() == 'detail':
            start_idx -= 1
            a = get_news_by_category(api_key, category, start_idx, detail=True)
            start_idx += 1
            speak(a)


