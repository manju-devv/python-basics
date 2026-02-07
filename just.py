import requests

news_api = "01359dd4396d42dbb043815646365989"


r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={news_api}")

if r.status_code == 200:
    data = r.json()
    # print(data.get("articles"))
    art = data.get("articles",[])
    for article in art[:5]:
        print(article["title"])
    # for article in data["articles"][:5]:
    #     print(article["title"])
else:
    print("Request failed:", r.status_code)
