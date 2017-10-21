from bs4 import BeautifulSoup
import requests
import time
import random
import hashlib



def getInfo(url, headers, data):
    '从url中爬取到需要的数据，并拼接成字符串返回'
    r = requests.post(url, headers=headers, data=data)
    try:
        r.raise_for_status()
        info = r.json()
        tgt = info.get('translateResult')[0][0].get('tgt') + '\n'
        rs = info.get('smartResult').get('entries')
        for i in rs[1:]:
            tgt = tgt + i
        return tgt
    except:
        return ''





def main(string):
    '必要的数据改造并调用getInfo函数拿到数据'
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    i = "rY0D^0'nM0}g5Mm1z%1G4"
    o = str(time.time()*1000 + random.randint(0,10))
    t = string
    r = hashlib.md5(('fanyideskweb' + t + o + i).encode('utf-8')).hexdigest()
    headers = {
        'Host':'fanyi.youdao.com',
        'Origin':'http://fanyi.youdao.com',
        'Referer':'http://fanyi.youdao.com/',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest',
    }
    data = {
        'i':string,
        'from':'AUTO',
        'to':'AUTO',
        'smartresult':'dict',
        'client':'fanyideskweb',
        # 'salt': a
        # a = "" + ((new Date).getTime() + parseInt(10 * Math.random(), 10)),
        'salt':o,
        # sign: r
        # r = n.md5("fanyideskweb" + o + a + t)
        'sign':r,
        'doctype':'json',
        'version':'2.1',
        'keyfrom':'fanyi.web',
        'action':'FY_BY_REALTIME',
        'typoResult':'true',
    }

    return getInfo(url, headers, data)

