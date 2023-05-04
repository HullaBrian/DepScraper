from bs4 import BeautifulSoup
import requests
import urllib.request
import os
from loguru import logger

logger.level("DOWNLOAD", no=38, color="<yellow>", icon="🐍")


def download_target(package: str, ref: str, out_dir: str):
    # http://http.us.debian.org/debian/pool/main/d/debconf/debconf_1.5.71+deb10u1_all.deb
    URL = f"https://packages.debian.org/{ref}"

    logger.info(f"[{package}]: Browsing to '{URL}'")
    page = requests.get(URL)
    logger.debug(f"[{package}]: Retrieved html from site!")
    soup = BeautifulSoup(page.content, "html.parser")
    logger.info(f"[{package}]: Processing...")

    link = soup.find("a", string="http.us.debian.org/debian")
    link = link["href"]
    _download(link, out_dir)


def _download(url: str, out_dir: str):
    urllib.request.urlretrieve(url, os.path.join(out_dir, url.split("/")[-1]))
    logger.log("DOWNLOAD", f"Downloaded {url.split('/')[-1]}")
    return True
