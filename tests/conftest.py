import requests
import pytest
import project
from clients.base_client import BaseClient


@pytest.fixture(scope="session")
def api_session():
    session = requests.Session()
    yield session
    session.close()

@pytest.fixture(scope="function")
def api_client(api_session):
    return BaseClient(project.config.base_url, api_session)