from bs4 import BeautifulSoup
import requests
import urllib.request
import urllib.parse
import time


search = urllib.parse.quote_plus(input('검색어 : '))
page_num = 1
page_last = int(input('페이지수 : '))


while page_num < page_last + 1:
    url = f'https://www.p.com/video/search?search={search}&page={page_num}'
    
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    title = soup.select('ul.videos.search-video-thumbs > li.pcVideoListItem.js-pop.videoblock.videoBox > div.wrap > div.phimage > a')
    thumb = soup.select('ul.videos.search-video-thumbs > li.pcVideoListItem.js-pop.videoblock.videoBox > div.wrap > div.phimage > a > img')

    print(f'\n************************[{page_num}페이지]************************\n')
    for title, thumb in zip(title, thumb):
        
        print(thumb.attrs['data-mediabook']) #썸네일
        print(thumb.attrs['alt']) #이름
        print('https://p.com'+title.attrs['href']) #주소
        print()

    page_num += 1

