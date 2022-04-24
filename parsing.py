import requests
from bs4 import BeautifulSoup
from urllib import response
import csv
"""
Вы можете изменить категории и все работать будеть попробуйде например:
https://kg.wildberries.ru/catalog/elektronika/igry-i-razvlecheniya/aksessuary/garnitury
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!изменил на !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
https://kg.wildberries.ru/catalog/elektronika/smart-chasy

попробуйте
"""
URL = "https://kg.wildberries.ru/catalog/elektronika/igry-i-razvlecheniya/aksessuary/garnitury"
def get_html(url: str): 
	html = requests.get(url=URL)
	return html.text

def get_last_page(html):
	soup = BeautifulSoup(html, 'lxml')
	pagination = soup.find('div', class_="pager i-pager pagination").find_all("a", class_="pagination-item pagination__item")[-1].text
	return int(pagination)


def write_to_csv(data: list) -> None:
	"""Запись в csv формате"""
	with open("data/info.csv", "w") as file:
		writer = csv.writer(file)
		writer.writerow(["id","name", "price", "description", "image"])
		for item in data:
			writer.writerow([item.get("id"), 
								  item.get("name"),
								  item.get("price"),
								  item.get("description"),
								  item.get("image")]
								  )		
			# download_image(url=item.get("image"), 
			# 					name=item.get("name"))


DATA = []
def get_description(url, name, price, id_):
	URL = url
	html2 = requests.get(URL).text
	soup2 = BeautifulSoup(html2, 'lxml')
	try:
		description = soup2.find("div", class_="collapsable__content j-description").text
	except:
		description = ''
	try:
		image = soup2.find('img', class_="photo-zoom__preview j-zoom-preview").get('src')
		image = "https:"+image
	except:
		image = ''
	dep = {"id": id_, 
		"name": name, 
		"price": price, 
		"description": description, 
		"image": image
		} 
	DATA.append(dep)

# def download_image(url: str, name: str) -> None:
# 	response = requests.get(url = url)
# 	with open(f"data/image/{name}.jpg", "wb") as file:
# 		file.write(response.content)

s = 0
def get_data(html):
	soup = BeautifulSoup(html, 'lxml')
	all_things = soup.find("div", class_="product-card-list").find_all('div', class_="product-card j-card-item")
	global s
	for cards in all_things:
		s+=1
		try:
			price = cards.find('div', class_="product-card__price j-cataloger-price").find('ins', class_='lower-price').text
			# print(price)
		except:
			price = ''
		try:
			name = cards.find('div', class_="product-card__brand-name").text
			# print(name)
		except:
			name = ''
		try:
			link = cards.find('div', class_='product-card__wrapper').find('a', class_='product-card__main').get('href')
			link = "https://kg.wildberries.ru" + link
		except:
			link = ''
		id_ = s
		
		get_description(link, name, price, id_)
		
def main():
	html = get_html(url = URL)
	for i in range(1, get_last_page(html)+1):
		URL_PAGE = URL +"?sort=popular&page=" + str(i)
		html = get_html(url = URL_PAGE)
		get_data(html=html)
	write_to_csv(DATA)
main()
# mains
