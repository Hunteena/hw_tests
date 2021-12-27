import time
import pytest
import requests

YANDEX_TOKEN = ...
SLEEP_TIME = 2

tests_for_create_folder = [
    ['test1', 201, 'Создание папки'],
    ['test1', 409, 'Создание папки с существующим именем'],
    ['', 400, 'Имя папки - пустая строка'],
    [None, 400, 'Имя папки не передано']
]


class TestYandexApi:
    def setup(self):
        time.sleep(SLEEP_TIME)

    @pytest.mark.parametrize('folder_name, expected, description',
                             tests_for_create_folder)
    def test_create_folder(self, folder_name, expected, description):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {YANDEX_TOKEN}'
        }
        params = {'path': folder_name}
        response = requests.put(url=url, params=params, headers=headers)
        assert response.status_code == expected, description
