"""Stock Market Scraper

Scrape and return KOSPI and KOSDAQ INDEX of Korean Stock Market"""
from bs4 import BeautifulSoup
import requests


def kospi_scraper(request):
	"""Return real-time KOSPI Index by scraping from KRX.co.kr"""
	headers = {}
	r = requests.get("http://www.krx.co.kr/main/main.jsp", headers = headers)
	r.text
	return


def kosdaq_scraper(request):
	"""Return real-time KOSDAQ Index by scraping from KRX.co.kr"""
	return