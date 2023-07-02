import requests

def test_get_weather():
    # Test case 1: Get weather for a valid city
    response = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London&appid=API_KEY')
    assert response.status_code == 200
    assert 'name' in response.json()
    assert 'weather' in response.json()

    # Test case 2: Get weather for an invalid city
    response = requests.get('http://api.openweathermap.org/data/2.5/weather?q=InvalidCity&appid=API_KEY')
    assert response.status_code == 404
    assert 'message' in response.json()

    # Test case 3: Get weather with invalid API key
    response = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London&appid=INVALID_API_KEY')
    assert response.status_code == 401
    assert 'message' in response.json()

    # Test case 4: Get weather with missing API key
    response = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London')
    assert response.status_code == 401
    assert 'message' in response.json()

    # Test case 5: Get weather with invalid query parameter
    response = requests.get('http://api.openweathermap.org/data/2.5/weather?invalid_param=London&appid=API_KEY')
    assert response.status_code == 400
    assert 'message' in response.json()