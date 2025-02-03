#Головина Анна,26 когорта,Финальный проекст- Инженер по тестированию плюс
import requests
import configuration
import data
import pytest

def post_track_order(body):
     return requests.post(configuration.server_url + configuration.create_track,json=body,headers=data.headers)


def get_order(track):
   GET_ORDER_URL = f"{configuration.server_url}{configuration.get_order}"
   return requests.get(GET_ORDER_URL.format(track) ,headers=data.headers)

def test_create_and_get_order():
    response_create= post_track_order(data.track_body)
    assert response_create.status_code == 201 , "Ошибка при создании заказа"

    track_number = response_create.json().get("track")
    assert track_number, "Отстутствует номер заказа"

    response_get = get_order(track_number)
    assert response_get.status_code == 200, "Ошибка при получении заказа по его номеру"
    print("test complete")
test_create_and_get_order()
