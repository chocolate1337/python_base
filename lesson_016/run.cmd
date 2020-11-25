# Запись данных о погоде в БД
python 01_weather.py write_to_base --from_ 2020-11-01 --to_ 2020-11-30

# Вывод погоды в териминал
python 01_weather.py load_from_base --from_ 2020-11-01 --to_ 2020-11-30

# Создать открытки
python 01_weather.py make_postcard --from_ 2020-11-01 --to_ 2020-11-30
