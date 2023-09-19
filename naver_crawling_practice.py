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

items = soup.select('.total_wrap.api_ani_send')

# print(items[0].text)

for e, item in enumerate(items, 1):
    user = item.select_one('.sub_txt.sub_name').text
    title = item.select_one('.api_txt_lines.total_tit._cross_trigger').text
    link = item.select_one('.api_txt_lines.total_tit._cross_trigger').attrs['href']
    # title = item.text
    print(f"{e} : 작성자 >> {user} \n 제목 >> {title} \n 링크 >> {link}")
