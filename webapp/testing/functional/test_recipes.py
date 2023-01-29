from webapp import create_app


def test_home(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is is posted to (GET)
    THEN check that a '200' status code is returned
    ДАНО приложение Flask, настроенное для тестирования
    КОГДА страница '/' будет размещена на (GET)
    ЗАТЕМ убедитесь, что возвращен код состояния "200"
    """

    # Create a test client using the Flask application configured for testing

    response = test_client.get("/")
    assert response.status_code == 200
    assert f"Рестораны Санкт-Петербурга" in response.text
    assert f"Карта города" in response.text
    assert f"Список заведений" in response.text


def test_home_page_post_with_fixture(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is is posted to (POST)
    THEN check that a '405' status code is returned

    ДАНО приложение Flask, настроенное для тестирования
    КОГДА страница '/' размещена на (POST)
    ЗАТЕМ убедитесь, что возвращен код состояния '405'
    """
    response = test_client.post('/')
    assert response.status_code == 405


def test_home_page_post():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is is posted to (POST)
    THEN check that a '405' status code is returned

    ДАНО приложение Flask, настроенное для тестирования
    КОГДА страница '/' размещена на (POST)
    ЗАТЕМ убедитесь, что возвращен код состояния '405'
    """
    flask_app = create_app('flask_test.cfg')

    # Create a test client using the Flask application configured for testing

    with flask_app.test_client() as test_client:
        response = test_client.post('/')
        assert response.status_code == 405
