import os

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sbn
import streamlit as st

from keras.utils.np_utils import to_categorical
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPool2D
from keras.optimizers import RMSprop
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import ReduceLROnPlateau
from keras.utils.vis_utils import plot_model


def show_title_with_subtitle():
    # Заголовок и подзаголовок
    st.title("Digit recognizer")
    st.write("# Классификация")


def show_info_page():
    st.write("### Задача")
    st.write(
        "Построить, обучить и оценить модель для решения задачи классификации - получения высокоточных предсказаний нарисованной цифры")
    st.image("https://lh6.googleusercontent.com/FcswhDgzUC5hL9REfRn-ejF2OU50NT76RRWdhbkWGLP2WAIEKMfOhQqVvY0UJqUvTzzj0NGa6wEI2Q8HjAptUIyYylwXODvVg3MFC-sKsQRsQ8L3LifuEsC8WS-6senDCIT-Ba_q",
             use_column_width=True)
    st.write("### Описание входных данных")
    st.write(
        "Набор данных представляет из себя изображения 28 на 28 пикселей, преобразованные в строку из 784 столбцов со значениями насыщенности каждого пикселя в диапазоне от 0 до 255.")
    st.write("### Выбранная модель")
    st.write(
        "В результате анализа метрик качества нескольких классификационных моделей выбрана модель"
        "нейронной сети (https://keras.io/guides/functional_api/), обеспечивающая"
        "высокое качество предсказаний нарисованных цифр.")
    st.write("Выполненная работа представляет собой результат участия в соревновании на портале Kaggle. Более подробно"
             "ознакомиться с правилами соревнования можно по ссылке ниже:")
    st.write("https://www.kaggle.com/c/digit-recognizer")


def show_predictions_page():
    st.write("Файл для примера: https://drive.google.com/file/d/1SEKap_YuWo9VSbRNG7zZ1ZZxLXXJpsCB/view?usp=sharing")
    file = st.file_uploader(label="Выберите csv файл с предобработанными данными для прогнозирования стоимости",
                            type=["csv"],
                            accept_multiple_files=False)
    if file is not None:
        test_data = pd.read_csv(file)
        st.write("### Загруженные данные")
        st.write(test_data)
        make_predictions(get_model(), test_data)


def get_model():
    return load_model('../keras_models/c_model_1')


def make_predictions(model, X):
    st.write("### Предсказанные значения")
    X = X / 255.0
    X = X.values.reshape(-1, 28, 28, 1)
    pred = model.predict(X)
    st.write(pred)
    st.write("### Гистограмма распределения предсказаний")
    plot_hist(pred)


def plot_hist(data):
    fig = plt.figure()
    sbn.histplot(data, legend=False)
    st.pyplot(fig)


def select_page():
    # Сайдбар для смены страницы
    return st.sidebar.selectbox("Выберите страницу", ("Информация", "Прогнозирование"))


# Стиль для скрытия со страницы меню и футера streamlit
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# размещение элементов на странице
show_title_with_subtitle()
st.sidebar.title("Меню")
page = select_page()
st.sidebar.write("© Alexandr Fedchuk 2021")


if page == "Информация":
    show_info_page()
else:
    show_predictions_page()

