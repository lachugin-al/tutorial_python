import requests

# Создаем словарь, в заголовок может передать ключ или другую информацию
headers_dict = {
    "User-Agent": "python-requests/2.26.0"
}

# если передать заголово в запрос
response = requests.get('https://httpbin.org/get', headers=headers_dict)

if response.status_code == 200:
    print('OK!')
if response.ok:
    print('OK!')
response.raise_for_status()

print(response)
print(response.text)

# тело ответа в формате json
print(response.json())
print(response.json()['headers'])
print(response.json()['headers']['Host']) # Ключ Host в headers

# GET
# параметры возможно передать только в строке запроса
response1 = requests.get('https://httpbin.org/get?a=b', headers=headers_dict)
print(response1.text)

# но лучше делать при помощи библиотеки requests
response2 = requests.get('https://httpbin.org/get', headers=headers_dict, params={'a': 'b', 'c': 'd'})
print(response2.text)

# POST
response3 = requests.post('https://httpbin.org/post',
                          headers=headers_dict,
                          params={'a': 'b', 'c': 10},
                          json={'username':'superuser'}) # отправляем параметры внутри пост запроса

print(response3.text)

