from fastapi.testclient import TestClient
from main import app

# Create a TestClient instance to interact with the FastAPI app
client = TestClient(app)

def test_get_all_books():
    # Test the GET /api/v1/books endpoint
    response = client.get("/api/v1/books")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)  # Ensure the response is a dictionary
    assert len(response.json()) > 0  # Ensure there are books in the response

def test_get_book_by_id():
    # Test the GET /api/v1/books/{book_id} endpoint with a valid book ID
    response = client.get("/api/v1/books/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "publication_year": 1937,
        "genre": "Science Fiction",
    }

    # Test the GET /api/v1/books/{book_id} endpoint with an invalid book ID
    response = client.get("/api/v1/books/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Book not found"}

def test_create_book():
    # Test the POST /api/v1/books endpoint
    new_book = {
        "id": 4,
        "title": "New Book",
        "author": "New Author",
        "publication_year": 2023,
        "genre": "Mystery",
    }
    response = client.post("/api/v1/books/", json=new_book)
    assert response.status_code == 201
    assert response.json() == new_book

def test_update_book():
    # Test the PUT /api/v1/books/{book_id} endpoint
    updated_book = {
        "id": 1,
        "title": "Updated Title",
        "author": "Updated Author",
        "publication_year": 2023,
        "genre": "Updated Genre",
    }
    response = client.put("/api/v1/books/1", json=updated_book)
    assert response.status_code == 200
    assert response.json() == updated_book

def test_delete_book():
    # Test the DELETE /api/v1/books/{book_id} endpoint
    response = client.delete("/api/v1/books/1")
    assert response.status_code == 204
    assert response.content == b""  # Ensure the response body is empty

    # Verify the book was deleted
    response = client.get("/api/v1/books/1")
    assert response.status_code == 404
    assert response.json() == {"detail": "Book not found"}
