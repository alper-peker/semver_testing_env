import pytest
from app import app as flask_app

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_hello_endpoint(client):
    """Backend /api/hello endpoint test"""
    response = client.get('/api/hello')
    assert response.status_code == 200
    data = response.get_json()
    assert "Greetings from the Backend" in data['msg']
