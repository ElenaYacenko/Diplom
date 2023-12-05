import sender_stand_request


# Елена Яценко, 11 когорта, дипломный проект, Инженер по тестированию плюс

# Проверка код ответа=200
def test_get_order_by_track():
    data_order = sender_stand_request.get_order_by_track(sender_stand_request.number_track)
    assert data_order.status_code == 200

    print("Номер заказа ", sender_stand_request.number_track,
          ". Запишите его: пригодиться, чтобы отслеживать статус")
