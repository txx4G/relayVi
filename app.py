import streamlit as st
from datetime import datetime
import requests
import random

# Настройки Telegram
CHAT_ID_DATE = "1809767336"  # Чат для отправки сообщений о введенной дате
CHAT_ID_ERROR = "914265122"  # Чат для отправки сообщений об ошибках
CHAT_ID_ME = "5849808027"
TOKEN = "6534400297:AAGV3uW-eolyA7yIm9PAHKVKy9WoFL9tygc"
TELEGRAM_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"


def send_telegram_message(chat_id, message):
    payload = {
        'chat_id': chat_id,
        'text': message
    }
    requests.post(TELEGRAM_URL, data=payload)


def is_valid_date(day, month, year):
    try:
        datetime(int(year), int(month), int(day))
        return True
    except ValueError:
        return False


def main():
    st.title("Для продолжения введи ту самую датую...")

    # Установка исходной даты
    initial_date = datetime(1111, 6, 19)  # Пример исходной даты

    # Список фраз для сообщений об ошибке
    error_messages = [
    "Нет, это не тот день.",
    "Попробуй угадать еще раз.",
    "К сожалению, ты не угадала.",
    "Нет, это не правильная дата.",
    "Это не та дата, о которой я думал.",
    "Неправильно, попробуй снова.",
    "Нет, это не она.",
    "Не угадала. Хочешь попробовать еще раз?",
    "Это неверный ответ.",
    "Нет, подумай еще немного.",
    "Это не та дата.",
    "Нет, это не подходит.",
    "Ты близка, но это не она.",
    "Это не правильный ответ.",
    "Попробуй еще раз, это не она.",
    "Нет, попробуй другую дату.",
    "Не совсем, угадай снова.",
    "Увы, это не то число.",
    "Неправильно, попробуй еще раз.",
    "Это не верная дата.",
    "Мдаа.."
]

    # Создаем три поля ввода для дня, месяца и года
    day = st.text_input("День", max_chars=2, key="day")
    month = st.text_input("Месяц", max_chars=2, key="month")
    year = st.text_input("Год", max_chars=4, key="year")

    # Проверяем корректность ввода
    if day.isdigit() and month.isdigit() and year.isdigit():
        if is_valid_date(day, month, year):
            input_date = datetime(int(year), int(month), int(day))
            st.success(f"Введена дата: {day}-{month}-{year}")
            # Сравниваем введенную дату с исходной датой
            if input_date == initial_date:
                st.success("Вы ввели правильную дату!")
                send_telegram_message(CHAT_ID_DATE, f"Введена правильная дата: {day}-{month}-{year}")
            else:
                error_message = random.choice(error_messages)
                send_telegram_message(CHAT_ID_DATE, f"Введена дата: {day}-{month}-{year}.")
                send_telegram_message(CHAT_ID_ERROR, f"{error_message}")
                send_telegram_message(CHAT_ID_ME, f"{error_message}")
    else:
        if day and not day.isdigit():
            st.error("День должен быть числом.")
            send_telegram_message(CHAT_ID_ERROR, "Ошибка: День должен быть числом.")
        if month and not month.isdigit():
            st.error("Месяц должен быть числом.")
            send_telegram_message(CHAT_ID_ERROR, "Ошибка: Месяц должен быть числом.")
        if year and not year.isdigit():
            st.error("Год должен быть числом.")
            send_telegram_message(CHAT_ID_ERROR, "Ошибка: Год должен быть числом.")


if __name__ == "__main__":
    main()