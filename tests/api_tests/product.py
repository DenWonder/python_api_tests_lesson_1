import allure
import pytest

from src.endpoints import PRODUCT_LIST, PRODUCT_SEARCH


@allure.suite('product')
class TestProduct:
    def test_get_all_products_list(self, api_client):
        response = api_client.get(PRODUCT_LIST)
        body = response.json()
        with allure.step('Checking response code'):
            assert response.status_code == 200
        with allure.step('Checking of response content'):
            assert len(body['products']) > 0

    @allure.description('Test with expectation of response code 405')
    @pytest.mark.xfail(reason='Bug AEC-1234 Incorrect response code on post to products list')
    def test_post_to_all_products_list(self, api_client):
        response = api_client.post(PRODUCT_LIST)
        body = response.json()
        with allure.step('Checking response code'):
            assert response.status_code == 405
        with allure.step('Checking of response content'):
            assert body['message'] == 'This request method is not supported.'

    @pytest.mark.parametrize('product', ['Top', 'Tshirt'])
    def test_search_product_with_valid_parameters(self, api_client, product):
        response = api_client.post(PRODUCT_SEARCH, {'search_product': product})
        body = response.json()
        with allure.step('Checking response code'):
            assert response.status_code == 200
        with allure.step('Checking of response content'):
            assert len(body['products']) > 0

    @pytest.mark.parametrize('product', ['000000000', 'xxxxxxxx', 'null'])
    def test_search_product_with_invalid_parameters(self, api_client, product):
        response = api_client.post(PRODUCT_SEARCH, {'search_product': product})
        body = response.json()
        with allure.step('Checking response code'):
            assert response.status_code == 200
        with allure.step('Checking of response content'):
            assert len(body['products']) == 0

    @allure.description('Test with expectation of response code 400, but response code is 200, and code 400 is inside the response body')
    @pytest.mark.xfail(reason='Bug AEC-1235 Incorrect response code on product search without parameters')
    def test_search_product_without_parameters(self, api_client):
        response = api_client.post(PRODUCT_SEARCH)
        body = response.json()
        with allure.step('Checking response code'):
            assert response.status_code == 400
        with allure.step('Checking of response content'):
            assert body['message'] == 'Bad request, search_product parameter is missing in POST request.'