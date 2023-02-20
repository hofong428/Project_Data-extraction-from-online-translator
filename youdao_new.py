# File Name: youdao_new.py
# Author: Codebat_Raymond
# Date: 2/20/2023

from hashlib import md5
from time import time
import requests
from Crypto.Cipher import AES
import base64

# Decrypt the text
def AES_decrypto(enc):
    key = b'\x08\x14\x9d\xa7\x3c\x59\xce\x62\x55\x5b\x01\xe9\x2f\x34\xe8\x38'
    iv = b'\xd2\xbb\x1b\xfd\xe8\x3b\x38\xc3\x44\x36\x63\x57\xb7\x9c\xae\x1c'
    aes = AES.new(key, AES.MODE_CBC, iv)
    ctx = aes.decrypt(base64.urlsafe_b64decode(enc))
    return str(ctx, encoding='utf-8').strip()


# get the params sign value
def sign():
    t = int(time()*1000)
    ctx = f'client=fanyideskweb&mysticTime={t}&product=webfanyi&key=fsdsogkndfokasodnaso'
    obj = md5()
    obj.update(ctx.encode('utf-8'))
    sign = obj.hexdigest()
    return sign
print(sign())

# send post request to get decrypted text
def post(key):
    cookies = {
        'OUTFOX_SEARCH_USER_ID': '-1823593991@196.168.60.5',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie': 'OUTFOX_SEARCH_USER_ID=-1823593991@10.105.253.23; OUTFOX_SEARCH_USER_ID_NCOO=1700791125.470006',
        'Origin': 'https://fanyi.youdao.com',
        'Pragma': 'no-cache',
        'Referer': 'https://fanyi.youdao.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'i': 'Hello',
        'from': 'en',
        'to': 'zh-CHS',
        'domain': '0',
        'dictResult': 'true',
        'keyid': 'webfanyi',
        'sign': sign(),
        'client': 'fanyideskweb',
        'product': 'webfanyi',
        'appVersion': '1.0.0',
        'vendor': 'web',
        'pointParam': 'client,mysticTime,product',
        'mysticTime': int(time()*1000),
        'keyfrom': 'fanyi.web',
    }

    response = requests.post('https://dict.youdao.com/webtranslate', cookies=cookies, headers=headers, data=data)
    return response.text

if __name__ == '__main__':
    while True:
        word = input('请输入查询的单词:')
        enc = post(word)
        ctx = AES_decrypto(enc)
        print(ctx)