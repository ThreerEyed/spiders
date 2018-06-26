
import urllib.request
from lxml import etree


def decode_html(html_bytes, charsets=('utf-8', 'gbk')):

    html_str = ''
    for charset in charsets:
        try:
            html_str = html_bytes.decode(charset)

        except Exception as e:
            print(e, '不能以此编码格式解码')
    return html_str


def main():

    url = 'http://sports.sohu.com/2018wcausvsper/'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/63.0.3239.132 Safari/537.36'
    }
    req = urllib.request.Request(url, headers=header)
    res = urllib.request.urlopen(req)
    a = res.read()

    sports_html = decode_html(a)

    b = etree.HTML(sports_html)
    print(b)

    # c = b.xpath('')
    # print(c)


if __name__ == '__main__':
    main()