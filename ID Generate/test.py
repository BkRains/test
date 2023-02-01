import requests,re,time
from urllib import parse
from bs4 import BeautifulSoup
import bs4
header = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
          "Accept-Encoding": "gzip, deflate",
          "Accept-Language": "zh-CN,zh;q=0.9",
          "Connection": "keep-alive",
          "Host": "www.stats.gov.cn",
          "Referer": "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/index.html",
          "Upgrade-Insecure-Requests": "1",
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"}
url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2020/index.html'
def gethtml(url_str='data'):
    try:
        html_s = req.get(url_str)
        if html_s.status_code == 200:
            test_html = html_s.text.encode("latin1").decode("gbk")
            while re.findall('charset=(.*?)"',test_html) != ['gb2312']:
                print('进入while')
                html_s = req.get(url_str)
                test_html = html_s.text.encode("latin1").decode("gbk")
                return test_html
    except BaseException as e:
        print('抓取出现错误：', e)

def writetxt(str,str_type):
    if str_type == 'url':
        file_str = 'D:\curl.txt'
    else:
        file_str = 'D:\city.txt'
        with open(file_str, 'a+') as s_f:
            s_f.writelines(str + '\n')

def province(url_str):
    if url_str != '':
        soup_html = re.findall("<table>\r\n(.*)\r\n</table>", gethtml(url_str), re.S)
        soup_html = soup_html[0] if soup_html != [] else ''
        soup = BeautifulSoup(soup_html, 'lxml')
        for soup_tr in soup.findAll('tr', class_='provincetr'):
            for soup_td in soup_tr.find_all(name='a'):
                soup_sid = soup_td['href'].split('.')[0]
                soup_txt = soup_td.get_text()
                soup_url = parse.urljoin(url_str, soup_td['href'])
                print('level_1', ['0', soup_sid, soup_txt, soup_url])
                writetxt(str(['level_1', '0', soup_sid, soup_txt, soup_url]), 'data')
                writetxt(soup_url, 'url')
def getcity(url_str):
    if url_str != '':
        soup_html = re.findall("</td></tr>\r\n(.*)\r\n</table>", gethtml(url_str), re.S)
        soup_html = soup_html[0] if soup_html != [] else ''
        soup = BeautifulSoup(soup_html, 'lxml')
        Parent_url = re.findall("(\d+).html", url_str)
        Parent_url = Parent_url[0] if Parent_url != [] else ''
        level = str(int(len(Parent_url)/2+1))
        class_str = {'2': 'citytr', '3': 'countytr' ,'4': 'towntr' ,'5': 'villagetr'}
        for soup_tr in soup.findAll('tr', class_=class_str[level]):
            soup_sid = re.findall(r'\d+', soup_tr.get_text())
            soup_sid = soup_sid[0] if soup_sid != [] else ''
            soup_txt = re.findall(r'\D+', soup_tr.get_text())
            soup_txt = soup_txt[0] if soup_txt != [] else ''
            soup_url = re.findall('href="(.*?)">', str(soup_tr))
            soup_url = parse.urljoin(url_str, soup_url[0]) if soup_url != [] else ''
            print('level_'+level, [Parent_url, soup_sid, soup_txt, soup_url])
            writetxt(str(['level_'+level, Parent_url, soup_sid, soup_txt, soup_url]), 'data')
            writetxt(soup_url, 'url')

def updateurl():
    file_str = 'D:\curl.txt'
    with open(file_str, 'r') as f:
        lines = f.readlines()
        with open(file_str, 'w+') as f_w:
            if lines != []:
                lines[0] = ''
                f_w.writelines(lines)

def geturl():
    file_str = 'D:\curl.txt'
    lines_str = ''
    with open(file_str, 'r') as f:
        lines = f.readlines()
        if lines !=[]:
            lines_str = lines[0].strip()
            return lines_str

req = requests.session()
req.headers = header
province(url)

while 1 != 2:
    try:
        current_url = geturl()
        getcity(current_url)
        updateurl()
    except BaseException as e:
        print(e)
        time.sleep(1)