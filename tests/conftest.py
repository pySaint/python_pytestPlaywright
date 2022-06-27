"""
This module contains shared fixtures.
"""
import configparser
import os

import pytest

from pages.practice import PracticePage
from pages.result import BingResultPage
from pages.search import BingSearchPage
from pages.register import RegisterPage
from playwright.sync_api import Playwright, APIRequestContext, Page, expect
from typing import Generator


# To load a config file (.ini)
@pytest.fixture(scope='session')
def config() -> dict:
    config = configparser.RawConfigParser()

    # To check if the file can be accessed
    assert os.path.exists('/Users/afshin.somani/PycharmProjects/pythonProject/config.ini')

    config.read('/Users/afshin.somani/PycharmProjects/pythonProject/config.ini')
    config_values_dict = dict(config.items('general'))
    return config_values_dict

@pytest.fixture
def result_page(page: Page) -> BingResultPage:
    return BingResultPage(page)


@pytest.fixture
def search_page(page: Page) -> BingResultPage:
    return BingSearchPage(page)


@pytest.fixture
def practice_page(page: Page) -> PracticePage:
    return PracticePage(page)


@pytest.fixture
def register_page(page: Page) -> RegisterPage:
    return RegisterPage(page)

# API testing using reqres.in
@pytest.fixture(scope='session')
def req_login(playwright: Playwright) -> Generator[APIRequestContext, None, None]:
    headers = {
        "Accept": "application/json"
    }

    request_context = playwright.request.new_context(
        base_url = 'https://reqres.in',
        extra_http_headers = headers
    )

    yield request_context
    request_context.dispose()
