from tech_news.database import search_news


# Requisito 7
def search_by_title(title):
    news = search_news({
        "title": {
            "$regex": title,
            "$options": "i",
        }
    })
    list_of_news = []

    for item in news:
        info = item["title"], item["url"]
        list_of_news.append(info)

    return list_of_news


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
