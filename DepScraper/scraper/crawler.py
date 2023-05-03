from bs4 import *
import requests
from loguru import logger


def crawl_to(package: str, distribution: str):
    URL = f"https://packages.debian.org/{distribution}/{package}"
    logger.info(f"Browsing to '{URL}'")
    page = requests.get(URL)
    logger.debug("Retrieved html from site!")
    soup = BeautifulSoup(page.content, "html.parser")
    logger.info("Processing...")

    logger.debug("Finding dependencies")

    depends = soup.find_all("ul", class_="uldep")[1]
    entries = depends.find_all("dt")

    links = []
    visited_dependencies = []
    for entry in entries:
        if "or" in entry.contents[0]:
            logger.debug("Skipping an 'or' dependency...")
            continue
        link = entry.find("a")["href"]
        if link in visited_dependencies:
            logger.debug(f"[{package}]: Skipped dependency that isn't of amd64 architecture")
            continue
        links.append(link)
        visited_dependencies.append(link)
        logger.info(f"[{package}]: Found dependency: '{link}'")
    logger.success(f"[{package}]: Found all dependencies!")

    logger.info(f"Downloading '{package}'")
    soup = BeautifulSoup(page.content, "html.parser")
    download_target_page = soup.find_all("div")  #
    print(download_target_page)
