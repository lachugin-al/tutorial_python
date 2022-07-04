import requests

# запись контента через request
r = requests.get('http://yandex.ru')
# созраняем в файл index.html
with open('index.html', 'wb') as file:
    file.write(r.content)

r = requests.get('http://yandex.ru', stream=True)  # добавляем потоковый режим stream
with open('index_chunk.html', 'wb') as file:
    for chunk in r.iter_content(chunk_size=1024):
        file.write(chunk)
    # выгружаем файлы или большую объемную информацию по кусочкам (чтобы не забить память огромным файлом)

# Загружаем файл через пост на сервер
with open('index.html', 'wb') as file:
    requests.post('http://httpbin.org/anything', data=file)