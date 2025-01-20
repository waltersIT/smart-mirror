from newsapi import NewsApiClient
import json

def get_news():


    with open("config.json") as config_file:
        config = json.load(config_file)

    NEWS_API_KEY = config.get("NEWS_API_KEY")

    API_KEY = NEWS_API_KEY
    headlines = []
    # Initialize
    newsapi = NewsApiClient(api_key=API_KEY)

    # Get top headlines from a specific source
    top_headlines = newsapi.get_top_headlines(sources="the-wall-street-journal")
    
    # Print article titles
    for article in top_headlines["articles"][:5]:
        headlines.append(article['title'])
    return headlines
