"""
This module contains SelectorsHub practice page,
"""
import locator as locator
from playwright.sync_api import Page, expect


class PracticePage:

    URL = "https://selectorshub.com/xpath-practice-page/"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.email_input = page.locator("#userId")
        self.password_input = page.locator('#pass')
        self.company_input = page.locator("div[class='element-companyId'] input[placeholder='Enter your company']")
        self.firstCrush_input = page.locator('#inp_val')
        self.submit_button = page.locator('text=Submit')
        self.download_link = page.locator('text=DownLoad Link')
        self.testers_food_link = page.frame_locator('#pact').locator('text=Testers Food')



        self.checkbox_selector_by_username = "//td[normalize-space()='{username}']/preceding-sibling::td/input[@name='chkSelectRow[]']"
        # or playwright.$("[type='checkbox']:left-of(:text(\'Joe.Root\'))")
        self.enabled_selector_by_username = "td:has-text('{username}') + td:has-text('Enabled')"

    def navigate(self):
        self.page.goto(self.URL)


    def fill_form(self, email: str, password: str, company: str, crush: str) -> None:
        if(email =='' or password =='' or  company =='' or crush ==''):
            raise Exception("No empty strings are allowed")

        # if the element is hidden, change attribute 'readonly'
        self.page.eval_on_selector(
            selector="#userId",
            expression="(el) => el.removeAttribute('readonly')",
        )
        self.email_input.fill(value=email)
        self.password_input.fill(value=password)
        self.company_input.fill(value=company)
        self.firstCrush_input.fill(value=crush)
        self.submit_button.click()
        expect(self.page).to_have_title('XPath & cssSelector Practice Page with all scenarios - SelectorsHub')


    def Click_Links(self):
        self.testers_food_link.click()

    def select_table_row(self, user_name: str) -> locator:
        username_based_table_selector = self.checkbox_selector_by_username.format(username=user_name)
        username_based_enabled_selector = self.enabled_selector_by_username.format(username=user_name)

        self.page.locator(username_based_table_selector).click()
        return self.page.locator(username_based_enabled_selector)
