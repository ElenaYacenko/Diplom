import data
import configuration
import requests
#Елена Яценко, 11 когорта, диплом

def post_create_orders(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREAT_ORDERS, json=order_body)


track = str({"t": post_create_orders(data.order_body).json()["track"]})


def get_order():
    return requests.get(configuration.URL_SERVICE + configuration.CET_ORDERS, params=track)


def test_get_order_by_track():
    get_order_result = get_order()
    assert get_order_result.status_code == 200
    print("Номер заказа ", track, ". Запишите его: пригодиться, чтобы отслеживать статус")
