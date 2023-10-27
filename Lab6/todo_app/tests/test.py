from fastapi.testclient import TestClient
from src import main

client = TestClient(main.app)


def test_first_api():
    response = client.get("/api")
    assert response.status_code == 200
    assert response.json() == {"msg": "hello_world"}


def test_first_apiV2():
    response = client.get("/books/test_path_param")
    assert response.status_code == 200
    assert response.json() == {"msg": "test_path_param"}


def test_first_apiV3():
    response = client.get("/books/", params={"title": "test_title"})
    assert response.status_code == 200
    assert response.json() == {"msg": "test_title"}


def test_first_apiV5():
    response = client.get("/books/test_path_param/", params={"title": "test_title"})
    assert response.status_code == 200
    assert response.json() == {"msg": "test_path_param and test_title"}


def test_create_book():
    new_book = {"name": "Test Book", "author": "John Doe"}
    response = client.post("/books/create_book", json=new_book)
    assert response.status_code == 200
    assert response.json() == {"msg": new_book}


def test_update_book():
    updated_data = {"name": "Updated Book", "author": "Jane Doe"}
    response = client.put("/books/update_book/1", json=updated_data)
    assert response.status_code == 200
    assert response.json() == {"book_id": 1, "updated_book": updated_data}


def test_delete_book():
    response = client.delete("/books/delete_book/1")
    assert response.status_code == 200
    assert response.json() == {"msg": "Book with id 1 has been deleted!"}
