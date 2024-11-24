# pip install requests (a tool used for sending request)
import requests

# pip install lxml (a tool like XPATH in browser)
from lxml import etree

# sending requests
# sending whom?
with open('IP agent.txt', 'w', encoding='utf-8') as f:
    for i in range(1, 8):
        url = f'http://www.ip3366.net/?stype=1&page={i}'
        print(f'正在获取 {url}')

        # mask self - pretend send requests from browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
        }
        resp = requests.get(url, headers = headers)

        # encoding before print: utf-8, gbk
        resp.encoding = 'gbk'

        # receive responses
        print()

        # handle results
            # create an object that extract data
        e = etree.HTML(resp.text)
        # extract IP
        ips = e.xpath('//div/table/tbody/tr/td[1]/text()')

        # extract Port
        ports = e.xpath('//div/table/tbody/tr/td[2]/text()')

        # extract Address
        addrs = e.xpath('//div/table/tbody/tr/td[6]/text()')

        # for i, p, a in zip(ips, ports, addrs):
        #     print(f'IP地址: {i:<20} port端口号: {p:<10} 地址: {a:<30}')

        # save result as .txt
        for i, p, a in zip(ips, ports, addrs):
            f.write(f'IP地址: {i:<20} port端口号: {p:<10} 地址: {a:<30}\n')