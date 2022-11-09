import requests
from config import API_KEY

query={"country":"us"}
def getNews(query:dict):
    print(query)
    query_string=""
    for key in query.keys():
        preference=query.get(key)
        query_string+="{0}={1}&".format(key,preference)

    main_url="https://newsapi.org/v2/top-headlines?"
    final_url="{0}{1}apiKey={2}".format(main_url,query_string,API_KEY)
    print(final_url)
    article=requests.get(final_url)
    # print(article.json()['articles'])
    return article.json()['articles']
    
# getNews(query)