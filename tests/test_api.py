import pytest
from playwright.sync_api import APIRequestContext, Playwright, expect


@pytest.fixture(scope="session")
def api_request(playwright: Playwright):
    yield playwright.request.new_context()


def test_api_get(api_request: APIRequestContext):
    request = api_request
    response = request.get("https://httpbin.org/get")
    expect(response).to_be_ok()


def test_api_post(api_request: APIRequestContext):
    request = api_request
    response = request.post("https://httpbin.org/post")
    expect(response).to_be_ok()


def test_api_put(api_request: APIRequestContext):
    request = api_request
    response = request.put("https://httpbin.org/put")
    expect(response).to_be_ok()


def test_api_delete(api_request: APIRequestContext):
    request = api_request
    response = request.delete("https://httpbin.org/delete")
    expect(response).to_be_ok()
