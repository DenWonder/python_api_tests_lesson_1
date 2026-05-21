import allure

from src.endpoints import BRAND_LIST


@allure.suite('brand')
class TestBrand:
    @allure.title('Get all brands list')
    def test_get_all_brands_list(self, api_client):
        response = api_client.get(BRAND_LIST)
        body = response.json()
        with allure.step('Checking response code'):
            assert response.status_code == 200
        with allure.step('Checking of response content'):
            assert len(body.get('brands')) > 0

    @allure.title('Put to all brands list')
    @allure.description('Test with expectation of response code 200, in case, when this is an appropriate way in team')
    def test_put_to_all_brands_list(self, api_client):
        response = api_client.put(BRAND_LIST)
        body = response.json()
        with allure.step('Checking response code'):
            assert response.status_code == 200
        with allure.step('Checking of response content'):
            assert body.get('message') == 'This request method is not supported.'
            assert body.get('responseCode') == 405