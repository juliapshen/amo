import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib
import os

data_path = "test/"


def load_data(data_path):
    data = []
    for filename in os.listdir(data_path):
        if filename.endswith("_scaled.txt"):
            filepath = os.path.join(data_path, filename)
            df = pd.read_csv(filepath, header=None)
            data.append(df)
    return pd.concat(data, axis=0, ignore_index=True)


if __name__ == '__main__':
    # формируем один набор тестовых данных
    test_data = load_data(data_path)
    # делим выборку на тестовую и обучающую подвыборки
    X_train, X_test, y_train, y_test = train_test_split(test_data.iloc[:, :-1], test_data.iloc[:, -1], test_size=1,
                                                        random_state=42)

    # Загружаем обученную модель из файла
    model = joblib.load("trained_model.pkl")

    # Предсказание на тестовых данных
    y_pred = model.predict(X_test)
    # Оцениваем качество - рассчитываем среднеквадратическую ошибку
    mse = mean_squared_error(y_test, y_pred)

    print("Тестовые данные:\nMSE:", mse)
