from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_category
)
from tech_news.analyzer.ratings import top_5_categories
import sys


# Requisitos 11 e 12
def analyzer_menu():
    menu = input("Selecione uma das opções a seguir:\n"
                 " 0 - Popular o banco com notícias;\n"
                 " 1 - Buscar notícias por título;\n"
                 " 2 - Buscar notícias por data;\n"
                 " 3 - Buscar notícias por categoria;\n"
                 " 4 - Listar top 5 categorias;\n"
                 " 5 - Sair.")

    match menu:
        case "0":
            choice = input("Digite quantas notícias serão buscadas: ")
            get_tech_news(int(choice))
        case "1":
            choice = input("Digite o título: ")
            search_by_title(choice)
        case "2":
            choice = input("Digite a data no formato aaaa-mm-dd: ")
            search_by_date(choice)
        case "3":
            choice = input("Digite a categoria: ")
            search_by_category(choice)
        case "4":
            top_5_categories()
        case "5":
            print("Encerrando script")
        case _:
            sys.stderr.write("Opção inválida\n")
