import os
import re
import urllib.request
from json import loads
from urllib import parse
from bs4 import BeautifulSoup

import requests
from tqdm import tqdm


def get_html(url, category, tag, start=None, len=None):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/63.0.3239.132 Safari/537.36'
    }

    # url = 'http://pic.sogou.com/pics/recommend?'
    params = {
        'category': category,
        'tag': tag,
        'start': start,
        'len': len
    }

    full_url = parse.urlencode(params)
    req = urllib.request.Request(url + full_url, headers=header)
    try:
        res = urllib.request.urlopen(req)
        return res.read().decode('gbk')
    except:
        print('有问题')


def query_pic(category):
    url = 'http://pic.sogou.com/pics/recommend?'
    params = {
        'category': category,
    }
    req = requests.get(url, params=params)

    soup = BeautifulSoup(req.text, 'lxml')
    # print(soup)
    # re.compile('var jsonTag',)
    # a = soup.find_all('script')
    # print(a)
    a = re.findall('var jsonTag = \[(.*?)\].*?', str(soup))
    tag_list = []
    if a:
        b = a[0].strip('"')
        tag_list = b.split('","')
    return tag_list


def main():
    print('目前支持的分类有 : 美女，壁纸，搞笑，LOFTER，全景视觉')
    category = input('请输入查询的图片分类 : ')
    tags = query_pic(category)
    print(tags)
    input_tag = input('请输入 %s 下的子分类 : ' % category)

    start = input('请输入起始页码 : ')
    num = input('请输入需要下载的图片数目: ')
    url = 'http://pic.sogou.com/pics/channel/getAllRecomPicByTag.jsp?'
    pic_str = get_html(url, category, input_tag, start, num)
    if not os.path.exists(input_tag):
        os.mkdir(input_tag)
    pic_dict = loads(pic_str)
    # print(pic_str)
    all_items = pic_dict['all_items']

    counter = 0
    for i in tqdm(all_items):
        counter += 1
        pic_id = i.get('id')
        pic_title = i['title']
        pic_url = i.get('pic_url')
        ori_pic_url = i.get('ori_pic_url')

        filename = ori_pic_url[ori_pic_url.rfind('/') + 1:]

        title = input_tag
        # print('开始下载: %s 第 %d 张图片' % (pic_title, counter))

        BASE_DIR = os.path.dirname(__file__) + '/%s' % input_tag
        # print(BASE_DIR)
        file = os.path.join(BASE_DIR, filename)
        # print(file)
        try:
            urllib.request.urlretrieve(pic_url, file)
        except:
            print('在下载 %s 的时候出现了问题' % pic_title)
            continue

    print('下载完成')


if __name__ == '__main__':
    main()

