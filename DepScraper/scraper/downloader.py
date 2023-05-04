from bs4 import BeautifulSoup
import requests
from loguru import logger


def download_target(package: str, ref: str):
    # http://http.us.debian.org/debian/pool/main/d/debconf/debconf_1.5.71+deb10u1_all.deb
    URL = f"https://packages.debian.org/{ref}"

    logger.info(f"[{package}]: Browsing to '{URL}'")
    page = requests.get(URL)
    logger.debug(f"[{package}]: Retrieved html from site!")
    soup = BeautifulSoup(page.content, "html.parser")
    logger.info(f"[{package}]: Processing...")

    link = soup.find("a", string="http.us.debian.org/debian")
    link = link["href"]
    _download(link)


def _download(url: str):
    import urllib.request
    urllib.request.urlretrieve(url, url.split("/")[-1])
    logger.success(f"Downloaded {url}")
    return True
