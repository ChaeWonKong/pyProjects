"""Stock Market Scraper

Scrape and return KOSPI and KOSDAQ INDEX of Korean Stock Market"""
from bs4 import BeautifulSoup
import requests


def kospi_scraper():
	"""Return real-time KOSPI Index by scraping from KRX.co.kr"""
	headers = {}
	req = requests.get("http://www.krx.co.kr/main/main.jsp", headers = headers)
	html = req.text
	soup = BeautifulSoup(html, "html.parser")
	index = soup.findAll("span", {"class": "index-price"})
	index = index[0].get_text()

	return index

# body > div > div.body-wrap > div.info-first > div.section-wap-top > div:nth-child(1) > div > div.index-info-r > span > span.index-price

def kosdaq_scraper(request):
	"""Return real-time KOSDAQ Index by scraping from KRX.co.kr"""
	return


print(kospi_scraper())