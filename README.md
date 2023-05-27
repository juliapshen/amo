# Проект "amo"
## Лабораторные работы по продемету "Автоматизация машинного обучения"
### В данном проекте решается задача по созданию автоматического конвейера проекта машинного обучения.

## Автор:  Пшеничникова Юлия

## Структура проекта:

### amo
*
* data_creation.py
* model_preprocessing.py
* model_preparation.py
* model_testing.py
* test
* * data0.csv
* * data1.csv
* * data2.csv
* train
* * data0.csv
* * data1.csv
* * data2.csv
* pipeline.sh

## Описание скриптов:
 * data_creation.py создает различные наборыданных, описывающие изменение дневной температуры).
Таких наборов создается 10, в некоторые данные включены аномалии и шумы. 70% наборов данных сохранены в папке“train”,
30% - в папке “test”. 
* model_preprocessing.py выполняет предобработку данных с помощью sklearn.preprocessing.StandardScaler.
* model_preparation.py создает и обучает модель машинного обучения на построенных данных из папки “train”. 
* model_testing.py проверяет модель машинного обучения на построенных данных из папки “test”.
* pipeline.sh последовательно запускает python-скрипты: 
* * data_creation.py 
* * model_preprocessing.py
* * model_preparation.py
* * model_testing.py    

## Используемые библиотеки
* os 
* numpy
* pandas
* joblib
* sklearn.metrics
* sklearn.model_selection 
* sklearn.linear_model

## Запуск проекта

bash  
./pipeline.sh