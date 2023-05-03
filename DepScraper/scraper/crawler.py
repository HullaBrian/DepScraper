from bs4 import *
import requests


def crawl_to(package: str, distribution: str):
    URL = f"https://packages.debian.org/{distribution}/{package}"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")


