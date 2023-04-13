import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)

    try:
        response = requests.get(
            url,
            headers={"user-agent": "Fake user-agent"},
            timeout=3,
        )
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    href = selector.css(
        "div.post-outer a.cs-overlay-link::attr(href)"
    ).getall()
    return href


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page_url = selector.css("a.next::attr(href)").get()
    if not (next_page_url):
        None
    return next_page_url


# Requisito 4
def scrape_news(html_content):
    selector = Selector(text=html_content)
    piece_of_news = {
        "url": selector.css("link[rel=canonical]::attr(href)").get(),
        "title": selector.css("h1.entry-title::text").get().strip(),
        "timestamp": selector.css("li.meta-date::text").get(),
        "writer": selector.css("a.url.fn.n::text").get(),
        "reading_time": int(
            selector.css("li.meta-reading-time::text").get().split()[0]
        ),
        "summary": selector.css(".entry-content p")
        .xpath("string()").get().strip(),
        "category": selector.css("a.category-style .label::text").get(),
    }
    return piece_of_news


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
