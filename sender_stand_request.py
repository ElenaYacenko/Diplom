import data
import configuration
import requests


# Создание нового заказа
def create_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREAT_ORDERS, json=order_body)


# Сохранение номера заказа
number_track = create_order(data.order_body).json()["track"]


#  Получение заказа по треку
def get_order_by_track(number_track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDERS + str(number_track))
