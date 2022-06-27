from playwright.sync_api import APIRequestContext, expect
from pytest_testrail.plugin import pytestrail


@pytestrail.case('121')
def test_create_user(
    req_login: APIRequestContext,
    user_email='eve.holt@reqres.in',
    password= 'dummy') -> None:

    # Create a new user
    response = req_login.post(url='/api/login',
    data = {
        'email': user_email,
        'password': password
    })
    expect(response).to_be_ok()
    print(response.json())
    assert response.json()['token'] !=''