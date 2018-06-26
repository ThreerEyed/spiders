
from lxml import etree

import requests
from bs4 import BeautifulSoup


def start_crawl(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/63.0.3239.132 Safari/537.36'
    }

    # 使用request.get 在请求头中添加headers 获取到url的响应
    res = requests.get(url, headers=header)
    # html = etree.HTML(res.text)
    # a = html.xpath()   # xpath 解析

    #
    soup = BeautifulSoup(res.text, 'html5lib')
    print(soup)
    # a_list = soup.find_all('a')
    # print(a_list)

def main():
    # url = 'https://movie.douban.com/explore#!type=movie&tag=%E7%83%AD%E9%97%A8&sort=time&page_limit=20&page_start=0'
    # url = 'https://movie.douban.com/explore#!'
    url = 'https://movie.douban.com/j/search_tags?type=movie&tag=%E5%8F%AF%E6%92%AD%E6%94%BE'
    start_crawl(url)


if __name__ == '__main__':
    main()