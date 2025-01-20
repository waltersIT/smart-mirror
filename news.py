from newsapi import NewsApiClient
import json

def get_news():

    API_KEY = "YOUR API KEY"#change to you api key
    headlines = []
    # Initialize
    newsapi = NewsApiClient(api_key=API_KEY)

    # Get top headlines from a specific source
    top_headlines = newsapi.get_top_headlines(sources="the-wall-street-journal")
    
    # Print article titles
    for article in top_headlines["articles"][:5]:
        headlines.append(article['title'])
    return headlines
