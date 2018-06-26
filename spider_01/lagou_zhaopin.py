
import urllib.request
from urllib import parse


def main(gzjy, city):

    # url = 'https://www.lagou.com/jobs/list_Python?px=default\
    #      &gj=3%E5%B9%B4%E5%8F%8A%E4%BB%A5%E4%B8%8B&city=%E6%88%90%E9%83%BD#filterBox'


    # 请求头设置 伪装成浏览器
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/63.0.3239.132 Safari/537.36'
    }
    # 在url请求头中添加header  用于伪装
    data = parse.urlencode({'gj': gzjy, 'city': city})
    url = 'https://www.lagou.com/jobs/list_Python?px=default&' + data

    url1 = urllib.request.Request(url, headers=header)
    # 访问url
    res = urllib.request.urlopen(url1)
    # 将返回的html网页解码再返回
    res_html = res.read().decode('utf-8')
    # 将获得的结果返回
    return res_html


if __name__ == '__main__':

    print(main('不限', '成都'))
