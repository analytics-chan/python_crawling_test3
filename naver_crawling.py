# pip install beautifulsoup4
# pip install requests

from bs4 import BeautifulSoup
import requests

base_url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query="
keyword = input('검색어를 입력하세요 ===> ')
search_url = base_url + keyword

# print(search_url)

response = requests.get(search_url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

items = soup.select('.api_txt_lines.total_tit._cross_trigger')

print(items[0].text)

for e, item in enumerate(items, 1):
    title = item.text
    print(f"{e} : {title}")

# response = requests.get(f'https://section.blog.naver.com/Search/Post.naver?pageNo=1&rangeType=ALL&orderBy=sim&keyword={keyword}')
# html = response.text

# soup = BeautifulSoup(html, 'html.parser')

# title = soup.select_one('#content > section > div.area_list_search > div:nth-child(1) > div > div.info_post > div.desc > a.desc_inner > strong > span')
# print(title)