import sys

import requests


def service_restored() -> bool:
    URL = 'http://www.zjrmfy.suzhou.gov.cn:8089/szsf/'
    headers = {
        'Host': 'www.zjrmfy.suzhou.gov.cn:8089',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    }
    # Proxy-Connection: keep-alive
    # Cache-Control: max-age=0
    # Upgrade-Insecure-Requests: 1
    # Accept-Encoding: gzip, deflate
    # Accept-Language: en,zh-CN;q=0.9,zh;q=0.8,zh-TW;q=0.7
    # Cookie: JSESSIONID=B6AA9935E18A9E0EA0A031DB73B6F3CC
    # If-None-Match: W/"60739c41-375"
    # If-Modified-Since: Mon, 12 Apr 2021 01:02:57 GMT
    response = requests.get(URL, headers=headers)
    body = response.content.decode()
    return '由于软件后台升级维护，系统暂停服务！' not in body


if __name__ == '__main__':
    restored = service_restored()
    # if not restored:
    #     sys.exit('Still not serving.')
