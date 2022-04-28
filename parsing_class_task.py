# # import requests
# # from bs4 import BeautifulSoup


# # def get_url(url):
# #     # headers = {"User-Agent":"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
# #     response = requests.get(url)
# #     return response.text


# # def get_total_pages(html):
# #     soup = BeautifulSoup(html, 'lxml')
# #     pages_url = soup.find(
# #         'div', class_="vm-pagination vm-pagination-bottom").find('ul')
# #     last_page = pages_url.find_all('li')[-3]
# #     total_pages = last_page.find('a').get('href').split(",")[-1]
# #     # return int(total_pages)


# # def get_page_data(html):
# #     soup = BeautifulSoup(html, 'lxml')
# #     product_list = soup.find('div', class_='row').find_all('table')
# #     # products = product_list.find_all('div', class_='row').find('table', class_='')
# #     # image_product = product_list.find('a', class_='product-image-link')
# #     # product-image-link
# #     print(len(product_list))
# #     for p in product_list:
# #         try:
# #             photo = p.find('tr').find(
# #                 'a', class_="product-image-link").find('img').get('src')
# #             print(photo)
# #         except:
# #             photo = ''
# #         # try:
# #         # 	title = p.find('tr').find('a', class_="product-image-link").find('img').get('src')
# #         # 	print(photo)
# #         # except:
# #         # 	photo = ''


# # def main():
# #     note_books = 'https://enter.kg/computers/noutbuki_bishkek'
# #     pages = '?page='
# #     get_total_pages(get_url(note_books))
# #     get_page_data(get_url(note_books))


# # main()

# # ! Проверка на парсинг
# # import requests
# # from bs4 import BeautifulSoup
# # def get_url(url):
# #     # headers = {"User-Agent":"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
# #     response = requests.get(url)
# #     print(response.status_code)
# # def main():
# #     note_books = 'https://www.ultra.kg/catalog/noutbuki-planshety-i-kompyutery/noutbuki/'
# #     get_url(note_books)
# # main()

# #!   site https://www.ultra.kg/catalog/noutbuki-planshety-i-kompyutery/noutbuki/
# import csv
# import requests
# from bs4 import BeautifulSoup


# def get_url(url):
#     # headers = {"User-Agent":"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
#     response = requests.get(url)
#     return response.text


# def get_total_pages(html):
#     soup = BeautifulSoup(html, 'lxml')
#     pages_url = soup.find(
#         'div', class_="bx-pagination-container row").find('ul')
#     last_page = pages_url.find_all('li')[-2]
#     total_pages = last_page.find('a').get('href').split("=")[-1]
#     return int(total_pages)
#     # ?gclid=Cj0KCQjw3v6SBhCsARIsACyrRAnIyKrE70Xkwy3qAc60TlLx9YYq5w5IWzsfh_GDn1EzT4tPhHVaNvQaAleaEALw_wcB&PAGEN_1
#    #  return int(total_pages)


# def write_to_csv(data):
#     with open("my_text.csv", 'a') as csv_file:
#         writer = csv.writer(csv_file, delimiter="/")
#         writer.writerows((data['title'],
#                           data['price'],
#                           data['photo']))


# def get_page_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     product_list = soup.find('div', class_='items productList').find_all(
#         'div', class_="item product sku")
#     for product in product_list:
#         try:
#             photo = product.find(
#                 'div', class_="productColImage").find('img').get('src')
#             # print(photo)
#         except:
#             photo = ''
#         try:
#             title = product.find('div', class_="productColText").find(
#                 'span', class_="middle").text
#         except:
#             title = ''
#         try:
#             price = product.find('div', class_="productColText").find(
#                 'a', class_="price").text
#             price_list = price.split("/")
#             # print(price_list[0])
#         except:
#             price = ''

#         data = {"photo": photo, "title": title, "price": price_list}
#         write_to_csv(data)


# def main():
#     note_books = 'https://www.ultra.kg/catalog/noutbuki-planshety-i-kompyutery/noutbuki/'
#     total_pages = get_total_pages(get_url(note_books))
#     print(total_pages)
#     pages = "?PAGEN_1="
#     for page in range(1, total_pages+1):
#         url_with_page = note_books + pages + str(page)
#         html = get_url(url_with_page)
#         get_page_data(html)


# main()


# ! task 1
# import requests
# source = requests.get('https://stackoverflow.com/questions').status_code
# print(source)
# ! task 2
# import requests
# from bs4 import BeautifulSoup
# source = requests.get('http://www.example.com/').text
# soup = BeautifulSoup(source, 'lxml')
# print(f"h1: {soup.find('div').find('h1').text}")
# print(f"p: {soup.find('div').find('p').text }")
# print(f"a: {soup.find('div').find('a').get('href') }")

# ! task 3
# import requests
# from bs4 import BeautifulSoup
# source = requests.get('https://www.wikipedia.org/').text
# soup = BeautifulSoup(source, 'lxml')
# language = soup.find('div', class_="central-featured-lang lang4").find('strong').text
# articles = soup.find('div', class_="central-featured-lang lang4").find('small').text
# print(language)
# print(articles)


# ! task 4

# import requests
# from bs4 import BeautifulSoup
# def getTitle(url):
# 	source = requests.get(url).text
# 	soup = BeautifulSoup(source, 'lxml')
# 	try:
# 		if soup.find('h1'):
# 			return soup.find('h1')
# 		else:
# 			raise Exception()
# 	except:
# 			url = "Title could not be found"
# 			return url
# print(getTitle('http://www.example.com/'))

# ! task 5
# import requests
# from bs4 import BeautifulSoup
# source = requests.get("https://www.makers.kg").text
# soup = BeautifulSoup(source, 'lxml')
# navbar_main = soup.find_all('div', class_="feature-cards-card-wrapper")
# for a in navbar_main:
# 	print(a.find('h3', class_="feature-cards-card-info-title").text)
# ! task 6
# import requests
# from bs4 import BeautifulSoup
# source = requests.get("https://www.makers.kg").text
# url = "https://www.makers.kg"
# soup = BeautifulSoup(source, 'lxml')
# navbar_main = soup.find_all('div', class_="feature-cards-card-wrapper")
# for img in navbar_main:
# 	a = img.find('img').get('src')
# 	print(url+a[1::])

# ! task 7
# import requests
# from bs4 import BeautifulSoup
# source = requests.get("https://www.makers.kg").text
# soup = BeautifulSoup(source, 'lxml')
# navbar_main = soup.find_all('div', class_="feature-cards-card-wrapper")
# for a in navbar_main:
# 	print(a.find('div', class_="feature-cards-card-info-subtitle").text)


# ! task 8
# import requests
# from bs4 import BeautifulSoup
# def get_info(url):
# 	list_of_names = []
# 	source = requests.get(url).text
# 	soup = BeautifulSoup(source, 'lxml')
# 	blocks_of_contents = soup.find_all('div', 'feature-cards-card-wrapper')
# 	for contents in blocks_of_contents:
# 		name = contents.find('h3', class_="feature-cards-card-info-title").text
# 		description = contents.find('div', class_="feature-cards-card-info-subtitle").text
# 		image = url+contents.find('img').get('src')[1::]
# 		list_of_names.append({'name':name, "description":description, "image_link":image})
# 	return list_of_names
# print(get_info('https://www.makers.kg'))

# ! task 9
# import requests
# from bs4 import BeautifulSoup
# source = requests.get("https://enter.kg/").text
# url = "https://enter.kg/"
# soup = BeautifulSoup(source, 'lxml')
# list_ = []
# leftcol = soup.find('ul', class_= 'VMmenu')

# for a in leftcol:
# 		try:
# 			category_list = a.find('a').text
# 		except:
# 			categories = ''
# def main(categories):
# 	source = requests.get(url+categories).text
# 	soup = BeautifulSoup(source, 'lxml')
# 	list_.append(soup.find('h2' , class_='search-category-name').text)
# 	try:
# 		site_content = soup.find_all('span', class_="category-product-count")
# 	except:
# 		site_content = ''
# 	try:
# 		for i in site_content:
# 			list_.append(i.text)

# 		return list_
# 	except:
# 		print("error")

# def find_category(category_list, keyword):
# 	for a in leftcol:
# 		try:
# 			categories = a.find('a').get('href')
# 			category_list = a.find('a').text

# 			if keyword.lower() in category_list.lower():
# 				return main(categories)
# 		except:
# 			categories = ''
# print(find_category(category_list, 'Звуковые карты (5)'))


# import requests
# from bs4 import BeautifulSoup
# URL = "https://enter.kg/"
# html = requests.get(url=URL).text
# category_list = []
# soup = BeautifulSoup(html, 'lxml')
# all_li = soup.find("ul", class_="VMmenu").find_all('li')
# category_list = []
# list_ = []
# for i in all_li:
# 	try:
# 		texts=[i.find('a').text]
# 		category_list.append(texts)
# 	except:
# 		texts =''

# def find_category(categories, keyword):
# 	for i in categories:
# 		if str(keyword).lower() in str(i).lower():
# 			list_.append(str(*i))
# 	return list_
# print(find_category(category_list, 'Ноутбуки'))

# ! task 10
# import requests
# from bs4 import BeautifulSoup
# source = requests.get("https://www.imdb.com/chart/top").text
# soup = BeautifulSoup(source, 'lxml')
# table_tr = soup.find('table', class_='chart full-width').find_all('tr')
# title_list = []
# for tr in table_tr:
# 	table_td = tr.find_all('td', class_="titleColumn")
# 	for a in table_td:
# 		list_ = a.find('a').text
# 		link = 'https://www.imdb.com' + a.find('a').get('href')
# 		title_list.append({list_: link})
# def get_link(title_list, name):
# 	link = ''
# 	for word in title_list:
# 		if str(name).lower() in str(word).lower():
# 			link= [w for w in word.values()]
         
# 			break
		
# 	return link[0]
# print(get_link(title_list, 'shawshank'))
# ! code.py
# import requests
# from bs4 import BeautifulSoup

# URL = "https://www.kivano.kg/noutbuki"

# def get_html(url: str) -> str:
#     """
#     Возаращает html response
#     """
#     html = requests.get(url=url).text
#     return html

# def get_data(html:str):
#     soup = BeautifulSoup(html, "lxml")
#     data = soup.find("div", class_="list-view")
#     products = data.find_all("div", class_='item')
#     return products

# html = get_html(url=URL)
# data = get_data(html=html)

# def main(data: list):
#     product1 = data[0].find("div", class_="pull-right").find("div", class_="product_text").find("strong").find("a").text
#     print(product1)

# main(data=data)
