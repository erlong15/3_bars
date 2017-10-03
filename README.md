# Ближайшие бары

Скрипт анализирует список баров в формате json и выводит в консоль информацию по барам:
1) самый большой бар ( наибольшее количество мест)
2) самый маленький бар ( наиименьшее количество мест)
3) самый ближний бар (ближайший к введенным координатам)

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5
В качестве параметра нужно задать имя json файла со списком баров 
```
$ python3 bars.py -h
usage: bars.py [-h] -i INPUT

The script for searching a bar.

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        JSON file with bars
```

Запуск на Linux:

```
$ python3 bars.py -i bars.json
Самый большой бар:
    Бар: Спорт бар «Красная машина»
    Мест в баре: 450
    Адрес: Автозаводская улица, дом 23, строение 1, Даниловский район
    Координаты: 37.638228501070095, 55.70111462948684

Самый маленький бар:
    Бар: БАР. СОКИ
    Мест в баре: 0
    Адрес: Дубравная улица, дом 34/29, район Митино
    Координаты: 37.35805920566864, 55.84614475898795

input your longitude: 37.35805920566864
input your latitude: 55.84614475898795
Ближайший бар:
    Бар: БАР. СОКИ
    Мест в баре: 0
    Адрес: Дубравная улица, дом 34/29, район Митино
    Координаты: 37.35805920566864, 55.84614475898795


```


# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
