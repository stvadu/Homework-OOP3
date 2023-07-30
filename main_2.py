import requests
import os

class YaUploader:

    base_host = 'https://cloud-api.yandex.net:443/'

    def __init__(self, token: str):
        self.token = '...'

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        url = 'v1/disk/resources/upload/'
        request_url = self.base_host + url
        headers = {'Authorization': token}
        with open(file_path) as file:
            files_list = [line.rstrip() for line in file]
        for image in files_list:
            image_name = os.path.basename(image).split('/')[-1]
            print(f'file {image_name} uploaded with code:')
            params = {'path': image_name, 'overwrite': True}
            response1 = requests.get(request_url, headers=headers, params=params).json()
            upload_link = response1.get('href', '')
            response2 = requests.put(upload_link, data=open(image, 'rb'), headers=headers)
            if 200 <= response2.status_code <= 300:
                print(response2.status_code)

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'list.txt'
    token = 'OAuth ...'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
