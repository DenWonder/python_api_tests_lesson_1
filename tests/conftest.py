import allure
import requests
import pytest
import project
from clients.base_client import BaseClient
from src.endpoints import CREATE_ACCOUNT, DELETE_ACCOUNT
from utils.helpers import generate_user_data


@pytest.fixture(scope="session")
def api_session():
    session = requests.Session()
    yield session
    session.close()


@pytest.fixture(scope="function")
def api_client(api_session):
    return BaseClient(project.config.base_url, api_session)


@pytest.fixture(scope="session")
def registered_user(api_session):
    user = generate_user_data()
    client = BaseClient(project.config.base_url, api_session)
    client.post(CREATE_ACCOUNT, payload=user.to_dict())
    yield user
    client.delete(
        DELETE_ACCOUNT,
        payload={"email": user.email, "password": user.password},
    )


@pytest.hookimpl(trylast=True, hookwrapper=True)
def pytest_runtest_call(item):
    """Allure dynamic title"""
    yield
    allure.dynamic.title(" ".join(item.name.split("_")[1:]).title())