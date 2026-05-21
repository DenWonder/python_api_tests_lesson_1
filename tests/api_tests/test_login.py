import allure
import pytest

from src.endpoints import VERIFY_LOGIN


@allure.suite('login')
class TestLogin:
    def test_verify_login_success(self, api_client, registered_user):
        response = api_client.post(VERIFY_LOGIN, payload={'email': registered_user.email, 'password': registered_user.password})
        body = response.json()
        with allure.step('Checking response code'):
            assert response.status_code == 200
        with allure.step('Checking of response content'):
            assert body.get('message') == 'User exists!'


    @pytest.mark.parametrize(
        'empty_parameter',
        ['email', 'password'],
        ids=['Without email', 'Without password'],
    )
    def test_verify_login_without_parameter(self, api_client, registered_user, empty_parameter):
        full_payload = {'email': registered_user.email, 'password': registered_user.password}
        payload = {key: value for key, value in full_payload.items() if key != empty_parameter}
        response = api_client.post(VERIFY_LOGIN, payload=payload)
        body = response.json()
        with allure.step('Checking response code'):
            assert response.status_code == 200
        with allure.step('Checking of response content'):
            assert body.get('responseCode') == 400
            assert body.get('message') == "Bad request, email or password parameter is missing in POST request."


    @pytest.mark.xfail(reason='Bug AEC-1236 Incorrect response code on delete request to login')
    def test_send_delete_request_to_verify_login_endpoint(self, api_client, registered_user):
        response = api_client.delete(VERIFY_LOGIN, payload={'email': registered_user.email, 'password': registered_user.password})
        body = response.json()
        with allure.step('Checking response code'):
            assert response.status_code == 405
        with allure.step('Checking of response content'):
            assert body.get('message') == 'This request method is not supported.'


    @pytest.mark.parametrize(
        'invalid_parameter',
        ['email', 'password'],
        ids=['Invalid email', 'Invalid password'],
    )
    def test_verify_login_with_invalid_parameter(self, api_client, registered_user, invalid_parameter):
        payload = {'email': registered_user.email, 'password': registered_user.password}
        payload[invalid_parameter] = 'invalid_' + payload[invalid_parameter]
        response = api_client.post(VERIFY_LOGIN, payload=payload)
        body = response.json()
        with allure.step('Checking response code'):
            assert response.status_code == 200
        with allure.step('Checking of response content'):
            assert body.get('responseCode') == 404
            assert body.get('message') == "User not found!"
