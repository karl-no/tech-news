from tech_news.database import find_news
from collections import Counter


# Requisito 10
def top_5_categories():
    news = find_news()
    categories = []

    for info in news:
        categories.append(info["category"])

    categories_counter = Counter(
        sorted(categories)
    ).most_common(5)

    most_popular_categories = []
    for category in categories_counter:
        most_popular_categories.append(category[0])
    return most_popular_categories
