"""
Простые API-тесты для демонстрации CI/CD
Используют публичное API jsonplaceholder
"""
import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_posts():
    """Тест получения списка постов"""
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert "title" in data[0]
    assert "body" in data[0]
    print("✅ GET /posts работает")

def test_get_post_by_id():
    """Тест получения конкретного поста"""
    post_id = 1
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == post_id
    assert data["userId"] == 1
    print(f"✅ GET /posts/{post_id} работает")

def test_create_post():
    """Тест создания поста"""
    new_post = {
        "title": "Test Post",
        "body": "This is a test post from CI/CD",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=new_post)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == new_post["title"]
    assert data["body"] == new_post["body"]
    assert "id" in data
    print("✅ POST /posts работает")

def test_update_post():
    """Тест обновления поста"""
    updated_post = {
        "id": 1,
        "title": "Updated Title",
        "body": "Updated body from CI/CD",
        "userId": 1
    }
    response = requests.put(f"{BASE_URL}/posts/1", json=updated_post)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == updated_post["title"]
    assert data["body"] == updated_post["body"]
    print("✅ PUT /posts/1 работает")

def test_delete_post():
    """Тест удаления поста"""
    response = requests.delete(f"{BASE_URL}/posts/1")
    assert response.status_code in [200, 204]  # 200 или 204 - успех
    print("✅ DELETE /posts/1 работает")

def test_non_existent_post():
    """Тест запроса несуществующего поста"""
    response = requests.get(f"{BASE_URL}/posts/999999")
    assert response.status_code == 404
    print("✅ 404 обрабатывается корректно")

def test_response_time():
    """Тест времени ответа"""
    import time
    start = time.time()
    response = requests.get(f"{BASE_URL}/posts")
    end = time.time()
    response_time = (end - start) * 1000  # в миллисекундах
    assert response_time < 1000, f"Слишком долго: {response_time:.2f} мс"
    print(f"✅ Время ответа: {response_time:.2f} мс")

def test_json_structure():
    """Тест структуры JSON"""
    response = requests.get(f"{BASE_URL}/posts/1")
    data = response.json()
    expected_keys = {"userId", "id", "title", "body"}
    assert set(data.keys()) == expected_keys
    print("✅ Структура JSON корректна")

if __name__ == "__main__":
    pytest.main(["-v", __file__])