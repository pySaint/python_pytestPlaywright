"""
This module contains SelectorsHub practice page,
"""
from playwright.sync_api import Page, expect


class RegisterPage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.firstname_input = page.locator('#input-firstname')
        self.lastname_input = page.locator('#input-lastname')
        self.email_input = page.locator('#input-email')
        self.phone_input = page.locator('#input-telephone')
        self.password_input = page.locator('#input-password')
        self.password_confirm_input = page.locator('#input-confirm')
        self.subscribe_yes_checkbox = page.locator('text=Yes')
        self.subscribe_no_checkbox = page.locator('text=No')
        self.policy_checkbox = page.locator('input[name="agree"]')
        self.policy_view_link = page.locator('text=Privacy Policy')
        self.continue_button = page.locator('text=Continue')
        self.login_page_link = page.locator('text=login page')
        self.account_created_text = page.locator('text=Your Account Has Been Created!')
        self.right_menu_links = page.locator("//a[@class='list-group-item']")

    def register_user(self, firstname: str,
                      lastname: str,
                      email: str,
                      telephone: str,
                      password: str
                      ) -> None:
        self.firstname_input.fill(firstname)
        self.lastname_input.fill(lastname)
        self.email_input.fill(email)
        self.phone_input.fill(telephone)
        self.password_input.fill(password)
        self.password_confirm_input.fill(password)
        self.subscribe_yes_checkbox.click()
        self.policy_checkbox.check()
        self.continue_button.click()

    def verify_login_page_link_redirect(self) -> bool:
        self.login_page_link.click()
        return self.page.locator('text=New Customer').is_visible()

    def verify_privacy_policy_popup(self) -> str:
        self.policy_view_link.click()
        with self.page.expect_popup() as popup_info:
             self.policy_view_link.click()
        popup = popup_info.value
        popup.wait_for_load_state()
        return (popup.title())

    def verify_registration_sucessfull(self):
        expect(self.account_created_text).to_be_visible()


    def verify_links(self) -> bool:
        # Looping over list of locators
        locators_list = self.right_menu_links
        locators_count = locators_list.count()
        for i in range(locators_count):
             assert(locators_list.nth(i)).is_enabled()
        return True



