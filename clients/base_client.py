import json

import allure
from allure_commons.types import AttachmentType


class BaseClient:
    def __init__(self, base_url, session):
        self.base_url = base_url
        self.session = session
        self.token = None

    @allure.step('Add user token into Authorization header')
    def set_access_token(self, token):
        self.token = token

    def _get_headers(self, manual_token=None):
        target = manual_token if manual_token is not None else self.token
        headers = {}
        if target:
            headers['Authorization'] = target
        return headers

    def post(self, url, payload=None, headers=None):
        if payload is None:
            payload = {}
        with allure.step(f'sending POST request to {url}'):
            allure.attach(body=json.dumps(payload.json(), indent=4, ensure_ascii=True), name='Request payload', attachment_type=allure.attachment_type.JSON)
            response = self.session.post(self.base_url + url, data=payload, headers=headers)
            allure.attach(body=json.dumps(response.json(), indent=4, ensure_ascii=True), name='Response', attachment_type=AttachmentType.JSON, extension="json")
            return response

    def delete(self, url, payload=None, headers=None):
        if payload is None:
            payload = {}
        with allure.step(f'sending DELETE request to {url}'):
            allure.attach(body=json.dumps(payload.json(), indent=4, ensure_ascii=True), name='Request payload', attachment_type=allure.attachment_type.JSON)
            response = self.session.delete(self.base_url + url, data=payload, headers=headers)
            allure.attach(body=json.dumps(response.json(), indent=4, ensure_ascii=True), name='Response',
                      attachment_type=AttachmentType.JSON, extension="json")
            return response

    def patch(self, url, payload=None, headers=None):
        if payload is None:
            payload = {}
        with allure.step(f'sending PATCH request to {url}'):
            allure.attach(body=json.dumps(payload.json(), indent=4, ensure_ascii=True), name='Request payload', attachment_type=allure.attachment_type.JSON)
            response = self.session.patch(self.base_url + url, data=payload, headers=headers)
            allure.attach(body=json.dumps(response.json(), indent=4, ensure_ascii=True), name='Response',
                          attachment_type=AttachmentType.JSON, extension="json")
            return response

    def get(self, url, headers=None):
        with allure.step(f'sending GET request to {url}'):
            response = self.session.get(self.base_url + url, headers=headers)
            allure.attach(body=json.dumps(response.json(), indent=4, ensure_ascii=True), name='Response',
                          attachment_type=AttachmentType.JSON, extension="json")
            return response

    def put(self, url, payload=None, headers=None):
        if payload is None:
            payload = {}
        with allure.step(f'sending PUT request to {url}'):
            allure.attach(body=json.dumps(payload.json(), indent=4, ensure_ascii=True), name='Request payload', attachment_type=allure.attachment_type.JSON)
            response = self.session.put(self.base_url + url, data=payload, headers=headers)
            allure.attach(body=json.dumps(response.json(), indent=4, ensure_ascii=True), name='Response',
                          attachment_type=AttachmentType.JSON, extension="json")
            return response