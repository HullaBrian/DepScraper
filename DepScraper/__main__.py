import typer
from loguru import logger
from scraper.crawler import crawl_to


def main(package: str, distribution: str = "bullseye"):
    logger.info("Looking for the package with the following parameters:")
    logger.info(f"""[NAME]: {package}, [DISTRIBUTION]: {distribution}""")
    crawl_to(package, distribution)


if __name__ == "__main__":
    typer.run(main)
