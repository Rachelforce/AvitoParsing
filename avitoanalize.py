import json

metro_list = ['Чернышевская',
              'Василеостровская',
              'Адмиралтейская',
              'Горьковская',
              'Маяковская',
              'Невский проспект',
              'Обводный канал',
              'Петроградская',
              'Площадь Восстания',
              'Площадь А. Невского I',
              'Площадь А. Невского II'
              'Садовая',
              'Сенная площадь',
              'Спасская',
              'Спортивная',
              'Технологический ин-т I',
              'Технологический ин-т II',
              'Фрунзенская'
              ]


def json_export(data):
    with open('anylized.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False)


def get_json():
    with open('hati.json', encoding='utf-8') as json_file:
        return json.load(json_file)


def main():
    data = []
    flat_list = get_json()
    for flat in flat_list:
        if flat['metro'] in metro_list:
            data.append(flat)
    json_export(data)


if __name__ == '__main__':
    main()
