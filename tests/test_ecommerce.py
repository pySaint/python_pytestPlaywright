import time

import pytest
from pytest_testrail.plugin import pytestrail

from pages.register import RegisterPage


@pytestrail.case('C2255')
def test_new_user_registration(register_page: RegisterPage,
                               config):
    # this needs to happen from the home page not register page
    # Given user goes to url
    register_page.page.goto(config.get('url'))
    register_page.page.locator('//span[normalize-space()="My Account"]').click()
    register_page.page.locator('li[class="dropdown open"] li:nth-child(1) a:nth-child(1)').click()

    # When user successfully registers
    register_page.register_user(config.get('firstname'),
                                config.get('lastname'),
                                config.get('email'),
                                config.get('telephone'),
                                config.get('password'))
    register_page.verify_registration_sucessfull()

    # Then user is able to successfully login


@pytestrail.case('Q878')
def test_registration_page_links(register_page: RegisterPage,
                                 config):
    # this needs to happen from the home page not register page
    # Given user goes to url
    register_page.page.goto(config.get('url'))
    register_page.page.locator('//span[normalize-space()="My Account"]').click()
    register_page.page.locator('li[class="dropdown open"] li:nth-child(1) a:nth-child(1)').click()

    # Then user should be able to click on menu links
    assert (register_page.verify_links())


@pytestrail.case('C99999')
def test_func3():
    time.sleep(0.5)