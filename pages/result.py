"""
This module contains DuckDuckGoResultPage,
the page object for the DuckDuckGo result page.
"""

from playwright.sync_api import Page
from typing import List


class BingResultPage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.result_links = page.locator('//li[@class="b_algo"]//descendant::h2/a')
        self.search_input = page.locator('//input[@id="sb_form_q"]')

    def result_link_titles(self) -> List[str]:
        self.result_links.nth(3).wait_for()
        return self.result_links.all_text_contents()

    def result_link_titles_contain_phrase(self, phrase: str, minimum: int = 1) -> bool:
        titles = self.result_link_titles()
        matches = [t for t in titles if phrase.lower() in t.lower()]
        return len(matches) >= minimum
