import ssl
import urllib.request


url = 'https://www.baidu.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/63.0.3239.132 Safari/537.36',

}


req = urllib.request.Request(url, headers=headers)

content = ssl._create_unverified_context()
res = urllib.request.urlopen(req, context=content)
print(res.read().decode('utf-8'))
