import requests
from bs4 import BeautifulSoup

DOC_ROOT = "https://naver.github.io/searchad-apidoc"

def fetch_release_notes():
    """Scrape latest release-notes index"""
    r = requests.get(f"{DOC_ROOT}/release-notes")
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    return [a.text for a in soup.select("ul.release-list li a")]

def fetch_notices():
    """Scrape API notices (downtime, report changes)"""
    r = requests.get(f"{DOC_ROOT}/notice")
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    return [a.text for a in soup.select("ul.notice-list li a")]
