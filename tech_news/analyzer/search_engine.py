from tech_news.database import search_news
from datetime import date as data


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
    try:
        news = search_news({
            "timestamp": data.fromisoformat(date).strftime("%d/%m/%Y")
        })
        list_of_news = []

        for item in news:
            info = item["title"], item["url"]
            list_of_news.append(info)

        return list_of_news

    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
