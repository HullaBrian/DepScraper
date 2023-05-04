from bs4 import BeautifulSoup
import requests
from loguru import logger

from .downloader import download_target


visited_dependencies = []


def crawl_to(package: str, distribution: str):
    global visited_dependencies
    URL = f"https://packages.debian.org/{distribution}/{package}"
    logger.info(f"[{package}]: Browsing to '{URL}'")
    page = requests.get(URL)
    logger.debug(f"[{package}]: Retrieved html from site!")
    soup = BeautifulSoup(page.content, "html.parser")
    logger.info(f"[{package}]: Processing...")

    logger.debug(f"[{package}]: Finding dependencies")

    try:
        depends = soup.find_all("ul", class_="uldep")[1]
        entries = depends.find_all("dt")

        links = []
        for entry in entries:
            if "or" in entry.contents[0]:
                logger.debug(f"[{package}]Skipping an 'or' dependency...")
                continue
            link = entry.find("a")["href"]
            if link in visited_dependencies:
                logger.debug(f"[{package}]: Skipped dependency that isn't of amd64 architecture")
                continue
            links.append(link)
            visited_dependencies.append(link)
            logger.info(f"[{package}]: Found dependency: '{link}'")
            crawl_to(link.split("/")[-1], distribution)
        logger.success(f"[{package}]: Found all dependencies!")
    except IndexError:
        logger.info("Reached end of dependency tree branch!")

    logger.info(f"Downloading '{package}'")
    download_page_target = f"/{distribution}/amd64/{package}/download"
    download_target(package, download_page_target)
