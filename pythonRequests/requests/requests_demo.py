import requests
"""
# Proxy
proxy_dict = {"http://": "localhost:8888",
              'https://': 'localhost:8888'}
requests.get("https://ya.ru", proxies=proxy_dict, verify=False) # verify =False отключаем проверку сертификатов для https


# Cookie
# предварительно нужно чтобы сервер установил куки от вернул в ответе
# смотрит set-cookie в browser networks
# yandexuid=3008022341629402459; Expires=Sun, 17-Aug-2031 19:47:39 GMT; Domain=.yandex.ru; Path=/; Secure; SameSite=None

# но так как скрипт поставить сам куки не может необходимо сделать запрос к серверу и прочитать ответ
header = {'cookie': 'i=iytTKNN3swucRnqTp5lmMTtsrKR2fPFVGG+nKycAqeI4QxPHF4qnjs4U/UCqFAiClFfyhFAl3ZXzW1DHggo03S8NrV0=;yandex_gid=2'}

r_cookie = requests.get("https://ya.ru", proxies=proxy_dict, verify=False)
# print(r_cookie.cookies.items())

# Достаем элементы куки
for el in r_cookie.cookies.items():
    print(el)

# передаем куки в запросе в хэдере
r_cookie2 = requests.get("https://ya.ru", proxies=proxy_dict, headers=header, verify=False)
for el in r_cookie2.cookies.items():
    print(el)

# можно отправить куки в формате ключ:значение
cookies = {
    'i': 'u4I7guqAwpp+r86N8OsZzTISQoPp0mZraxF6Rn0yMM/JvjCKGBdoyQ69WdRe3N//2AydZg716EKB0o4clUZtQ9FLB48=',
    'yandexuid': '2400296551629403674',
    '_yasc': '3Beo2ymETTM/08P2Xt3i2aWn4IFrn8Ya1mFPHZ2svzdwAw==',
    'yandex_gid': '2',
    'mda': '0',
    'yp': '1631995873.ygu.1',
    'is_gdpr': '0',
    'is_gdpr_b': 'CJywbhDXQCgC'
}
r_cookie3 = requests.get("https://ya.ru", proxies=proxy_dict, cookies=cookies, verify=False)
for el in r_cookie3.cookies.items():
    print(el)
"""
# Redirects
# можно запретить редиректы (бывают относительными и абсолютными)
hbin = 'http://httpbin.org/redirect/3'
r = requests.get(hbin, allow_redirects=False).history

for el in r:
    print(el)
# В заголовках редирект смотреть в Location