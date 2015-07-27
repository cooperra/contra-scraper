from .scraper import Scraper

def load(inputstream):
    scraper = Scraper()
    return scraper.load(inputstream)
