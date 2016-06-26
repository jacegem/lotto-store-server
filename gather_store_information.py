# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import json
from lotto_store_manager import LottoStoreManager

hdr = {
    'accept': 'application / json',
    'accept-encoding': 'gzip, deflate',
    'accept-language': 'en - US, en;q = 0.8',
    'user-agent': 'Mozilla / 5.0(Windows NT 10.0; WOW64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 51.0.2704.103 Safari / 537.36',
    'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8'
}

# 요청 URL
# url = 'http://nlotto.co.kr/game.do?method=sellerInfo645Result&searchType=1&nowPage=1&sltSIDO=서울&sltGUGUN=강남구'

url = 'http://nlotto.co.kr/game.do?method=sellerInfo645Result&searchType=1&'

sido = urllib.parse.quote("서울".encode('utf8'), '/:')
gugun = urllib.parse.quote("강남구".encode('utf8'), '/:')

url = url + 'sltSIDO={0}&sltGUGUN={1}'.format(sido, gugun)
print(url)

# 요청 URL
# url = 'http://nlotto.co.kr/game.do?method=sellerInfo645Result&searchType=1&nowPage=1&sltSIDO=%EC%84%9C%EC%9A%B8&sltGUGUN=%EA%B0%95%EB%82%A8%EA%B5%AC'

print(url)
request = urllib.request.Request(url, headers=hdr)

response = urllib.request.urlopen(request)
text = response.read()
print(text)

decode = text.decode('cp949', "ignore")
print(decode)


# print (json.dumps(decode, sort_keys=True, indent=4))
data = json.loads(decode)

print(data)

sm = LottoStoreManager()




print (data['arr'])

print ('-------------------------------------------')

for d in data['arr']:
    for key in d:
        print("key:{0}\tdata:{1}".format(key, d[key]))



# print (response.read().decode('utf-8'))

# print(url);

# request = urllib.request.Request(url, headers=hdr)
# response = urllib.request.urlopen(request)
# print (response.read().decode('utf-8'))


# url = 'http://example.com/'
# url = 'http://nlotto.co.kr/game.do?method=sellerInfo645Result&searchType=1&nowPage=1&sltSIDO=서울&sltGUGUN=강남구'
#
#
# req = urllib.request.Request(url, headers=hdr)
# res = urllib.request.urlopen(req)
# data = res.read()      # a `bytes` object
# text = data.decode('utf-8') # a `str`; this step can't be used if data is binary
#
# print(text)

