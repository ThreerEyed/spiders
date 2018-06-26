import re
import urllib.request
from urllib import parse


def get_html(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/63.0.3239.132 Safari/537.36'
    }
    req = urllib.request.Request(url, headers=header)
    res = urllib.request.urlopen(req)
    html_str = res.read().decode('utf-8')
    return html_str


def all_pattern(html_str):

    # parttern = re.compile(
    #                         '<td class="gsmc"><a href=".*" target="_blank">(.*)</a> <a' # 公司名称
    #                         '<td class="zwmc".*?target="_blank">(.*?)</a>'   # 职位名称
    #                         '<td class="zwyx">(.*)</td>'   # 职位薪水
    #                         '<td class="gzdd">(.*)</td>'   # 工作地点
    #                         '<td class="gxsj".*<span>(.*)</span>'  # 职位发布时间
    #                         '<td .* class="fk_lv".*span>(.*)</span>',  # 反馈率
    #                         re.S
    #                     )
    pattern = re.compile(
        '<td class="zwmc".*? href="(.*?)" target="_blank">(.*?)</a>.*?'  # 职位链接和职位名称
        '<td.*? class="fk_lv".*?<span>(.*?)</span>.*?'  # 反馈率
        '<td class="gsmc".*? href="(.*?)" target="_blank">(.*?)</a>.*?'  # 公司链接和公司名称  
        '<td class="zwyx">(.*?)</td>.*?'  # 月薪
        '<td class="gzdd">(.*?)</td>.*?'  # 地点  
        '<td class="gxsj".*?<span>(.*?)</span>.*?'  # 发布时间
        , re.S)
    # 匹配所有复合条件的内容
    return re.findall(pattern, html_str)
    # # 爬到的总数
    # res_num = re.findall('<em>(\d+)</em>', html_str)[0]   # 取不到第一个元素会报错，所以要做判断
    # # 公司名称
    # res_gsmc = re.findall('<td class="gsmc"><a href=".*" target="_blank">(.*)</a> <a', html_str)
    # # 职位名称
    # # res_jobname = re.findall('target="_blank">([\u4e00-\u9fa5])</a> <a>', html_str)
    # res_jobname = re.findall('<td class="zwmc".*?target="_blank">(.*?)</a>', html_str, re.S)
    # # 职位薪水
    # res_salary = re.findall('<td class="zwyx">(.*)</td>', html_str)
    # # 工作地点
    # res_workplace = re.findall('<td class="gzdd">(.*)</td>', html_str)
    # # 职位发布时间
    # res_update_time = re.findall('<td class="gxsj".*<span>(.*)</span>', html_str)
    # # 反馈率
    # res_response_rate = re.findall('<td .* class="fk_lv".*span>(.*)</span>', html_str)
    # return res_num, res_jobname, res_salary, res_gsmc, res_update_time, res_workplace


if __name__ == '__main__':
    city_name = input('请输入城市名 : ')
    job_name = input('请输入职位名称 : ')
    search = parse.urlencode({'jl': city_name, 'kw': job_name})
    url = 'https://sou.zhaopin.com/jobs/searchresult.ashx?' + search

    print(all_pattern(get_html(url)))


