from playwright.sync_api import Page

class BingSearchPage:

    URL="https://www.bing.com/"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.search_input = page.locator('//input[@id="sb_form_q"]')
        self.search_button = page.locator('//label[@id="search_icon"]')

    def load(self) -> None:
        self.page.goto(self.URL)

    def search(self, phrase: str) -> None:
        self.search_input.fill(phrase)
        self.search_button.click()










