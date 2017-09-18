# Ближайшие бары

Скрипт анализирует список баров в формате json и выводит в консоль информацию по барам:
1) самый большой бар ( наибольшее количество мест)
2) самый маленький бар ( наиименьшее количество мест)
3) самый ближний бар (ближайший к введенным координатам)

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```#!bash

$ python3 bars.py bars.json
The biggest bar is {
    "geometry": {
        "type": "Point",
        "coordinates": [
            37.638228501070095,
            55.70111462948684
        ]
    },
    "properties": {
        "Attributes": {
            "IsNetObject": "нет",
            "global_id": 169375059,
            "Address": "Автозаводская улица, дом 23, строение 1",
            "PublicPhone": [
                {
                    "PublicPhone": "(905) 795-15-84"
                }
            ],
            "SocialPrivileges": "нет",
            "District": "Даниловский район",
            "SeatsCount": 450,
            "OperatingCompany": null,
            "AdmArea": "Южный административный округ",
            "Name": "Спорт бар «Красная машина»"
        },
        "VersionNumber": 2,
        "ReleaseNumber": 2,
        "DatasetId": 1796,
        "RowId": "fbe6c340-4707-4d74-b7ca-2b84a23bf3a8"
    },
    "type": "Feature"
}
The smallest bar is {
    "geometry": {
        "type": "Point",
        "coordinates": [
            37.35805920566864,
            55.84614475898795
        ]
    },
    "properties": {
        "Attributes": {
            "IsNetObject": "нет",
            "global_id": 20675518,
            "Address": "Дубравная улица, дом 34/29",
            "PublicPhone": [
                {
                    "PublicPhone": "(495) 258-94-19"
                }
            ],
            "SocialPrivileges": "нет",
            "District": "район Митино",
            "SeatsCount": 0,
            "OperatingCompany": null,
            "AdmArea": "Северо-Западный административный округ",
            "Name": "БАР. СОКИ"
        },
        "VersionNumber": 2,
        "ReleaseNumber": 2,
        "DatasetId": 1796,
        "RowId": "17adc22c-5c41-4e4b-872f-815b521f2b53"
    },
    "type": "Feature"
}
input your longitude: 37.35805920566864
input your latitude: 55.84614475898795
The closest bar: {
    "geometry": {
        "type": "Point",
        "coordinates": [
            37.35805920566864,
            55.84614475898795
        ]
    },
    "properties": {
        "Attributes": {
            "IsNetObject": "нет",
            "global_id": 20675518,
            "Address": "Дубравная улица, дом 34/29",
            "PublicPhone": [
                {
                    "PublicPhone": "(495) 258-94-19"
                }
            ],
            "SocialPrivileges": "нет",
            "District": "район Митино",
            "SeatsCount": 0,
            "OperatingCompany": null,
            "AdmArea": "Северо-Западный административный округ",
            "Name": "БАР. СОКИ"
        },
        "VersionNumber": 2,
        "ReleaseNumber": 2,
        "DatasetId": 1796,
        "RowId": "17adc22c-5c41-4e4b-872f-815b521f2b53"
    },
    "type": "Feature"
}

```


# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
