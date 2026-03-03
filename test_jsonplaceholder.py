import requests
import pytest

# Базовый URL API
BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_user():
    """Тест GET запроса: получение пользователя"""
    # Отправляем GET запрос
    response = requests.get(f"{BASE_URL}/users/1")
    
    # Проверяем статус-код
    assert response.status_code == 200
    
    # Преобразуем ответ в JSON
    data = response.json()
    
    # Проверяем ID пользователя
    assert data["id"] == 1
    
    # Проверяем наличие email
    assert "email" in data
    
    print("✅ GET запрос прошел успешно")
    print(f"   Пользователь: {data['name']}, Email: {data['email']}")

def test_create_post():
    """Тест POST запроса: создание записи"""
    # Данные для отправки
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    
    # Отправляем POST запрос
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    
    # Проверяем статус-код 201 (Created)
    assert response.status_code == 201
    
    # Получаем данные из ответа
    data = response.json()
    
    # Проверяем, что данные вернулись корректно
    assert data["title"] == "foo"
    assert data["body"] == "bar"
    assert data["userId"] == 1
    
    print("✅ POST запрос прошел успешно")
    print(f"   Создана запись с ID: {data['id']}")

def test_update_post():
    """Тест PUT запроса: обновление записи"""
    # Данные для обновления
    payload = {
        "id": 1,
        "title": "updated title",
        "body": "updated body",
        "userId": 1
    }
    
    # Отправляем PUT запрос
    response = requests.put(f"{BASE_URL}/posts/1", json=payload)
    
    # Проверяем статус-код
    assert response.status_code == 200
    
    # Получаем данные из ответа
    data = response.json()
    
    # Проверяем, что данные обновились
    assert data["title"] == "updated title"
    assert data["body"] == "updated body"
    
    print("✅ PUT запрос прошел успешно")
    print(f"   Запись обновлена: {data['title']}")

def test_get_nonexistent_user():
    """Тест GET запроса для несуществующего пользователя"""
    # Пытаемся получить пользователя с ID 999
    response = requests.get(f"{BASE_URL}/users/999")
    
    # Должны получить 404
    assert response.status_code == 404
    
    print("✅ GET запрос для несуществующего пользователя прошел успешно")
    print("   Получен статус-код 404")

def test_delete_post():
    """Тест DELETE запроса: удаление записи"""
    # Отправляем DELETE запрос
    response = requests.delete(f"{BASE_URL}/posts/1")
    
    # Для DELETE обычно возвращается 200 или 204
    assert response.status_code in [200, 204]
    
    print("✅ DELETE запрос прошел успешно")

# Запуск всех тестов
if __name__ == "__main__":
    pytest.main(["-v", __file__])