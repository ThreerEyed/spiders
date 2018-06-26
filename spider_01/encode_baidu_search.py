from urllib import request, parse
import urllib.request


def main(url):

    # 请求头设置，浏览器中的请求头中的设置
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/63.0.3239.132 Safari/537.36',
    }
    req = urllib.request.Request(url, headers=header)  # 这一步操作主要是为了让百度认为我们是通过浏览器访问的
    res = urllib.request.urlopen(req)      # urllib.request.urlopen()函数用于实现对目标url的访问。
    return res.read().decode('utf-8')     # 将访问url的结果内容读取出来并进行utf-8编码再返回


if __name__ == '__main__':
    msg = input('请输入查询关键字 :')
    search = parse.urlencode({'wd': msg})   # 这一步是对将我们的要输入的信息进行编码
    url = 'https://www.baidu.com/s?%s' % search   # 将我们得到的搜索关键字进行字符串粘贴
    print(main(url))  # 打印我们访问url的结果
