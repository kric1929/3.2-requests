import requests
#  документация https://yandex.ru/dev/translate/doc/dg/reference/translate-docpage/

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def translate_it(path_file_text, path_file_result, from_lang, to_lang):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param to_lang:
    :return:
    """

    with open(path_file_text, encoding='utf-8') as f:
        text = f.read()

    params = {
        'key': API_KEY,
        'text': text,
        'lang': from_lang+'-'+to_lang,
    }

    response = requests.get(URL, params=params)
    json_ = response.json()

    with open(path_file_result, 'w', encoding='utf-8') as f:
        f.write(json_['text'][0])


if __name__ == '__main__':
    translate_it('DE.txt', 'DE-RU.txt', 'de', 'ru')
    translate_it('ES.txt', 'ES-RU.txt', 'es', 'ru')
    translate_it('FR.txt', 'FR-RU.txt', 'fr', 'ru')
