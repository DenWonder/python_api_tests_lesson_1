import allure
import pytest

@allure.suite("Product")

@allure.title("Get all products list")
def test_get_all_products_list(api_client):
    response = (api_client.get('productsList'))
    body = response.json()

    with allure.step("Checking response code"):
        assert response.status_code == 200

    with allure.step("Checking of response content"):
        assert (body["products"] is not None)

@allure.title("Post to all products list")
@allure.description("Post to all products list")
@pytest.mark.xfail(reason="Bug AEC-1234 Incorrect response code on post to products list")
def test_post_to_all_products_list(api_client):
    response = (api_client.post('productsList', {}))
    body = response.json()
    with allure.step("Checking response code"):
        assert response.status_code == 405

    with allure.step("Checking of response content"):
        assert (body["message"] == "This request method is not supported.")
