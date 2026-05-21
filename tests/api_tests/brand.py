import allure

@allure.suite('brand')

@allure.title('Get all brands list')
def test_get_all_brands_list(api_client):
    response = api_client.get('brandsList')
    body = response.json()
    with allure.step('Checking response code'):
        assert response.status_code == 200

    with allure.step('Checking of response content'):
        assert (body['brands'] is not None)

@allure.title('Put to all brands list')
def test_put_to_all_brands_list(api_client):
    response = api_client.put('brandsList')
    body = response.json()

    with allure.step('Checking response code'):
        assert response.status_code == 200

    with allure.step('Checking of response content'):
        assert (body['message'] == 'This request method is not supported.')
        assert (body['responseCode'] == 405)