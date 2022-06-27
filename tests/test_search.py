import pytest
from playwright.sync_api import Page, expect

from pages.result import BingResultPage
from pages.search import BingSearchPage
from pages.practice import PracticePage

ANIMALS = [
    'panda',
    'python',
    'polar bear',
    'parrot',
    'porcupine',
    'parakeet',
    'pangolin',
    'panther',
    'platypus',
    'peacock'
]


@pytest.mark.parametrize('phrase', ANIMALS)
def test_basic_panda_search(
    phrase: str,
    page: Page,
    search_page: BingSearchPage,
    result_page: BingResultPage) -> None:

    # Given the DuckDuckGo home page is displayed
    search_page.load()

    # When the user searches for a phrase
    search_page.search(phrase)

    # Then the search result query is the phrase
    expect(result_page.search_input).to_have_value(phrase)

    # And the search result links pertain to the phrase
    assert(result_page.result_link_titles_contain_phrase(phrase))

    # And the search result title contains the phrase
    expect(page).to_have_title(f'{phrase} - Search')

def test_create_user( page: Page,
                      practice_page: PracticePage,
                      email='yoda@mailinator.com',
                      pwd='dummy',
                      company='newcompany',
                      crush="no_one") -> None:

    practice_page.navigate()
    practice_page.fill_form(email, pwd, company, crush)


def test_verify_links(page: Page,
                      practice_page: PracticePage):
    practice_page.navigate()
    practice_page.Click_Links()


def test_user_enabled(practice_page: PracticePage,
                       username='Garry White'):
    practice_page.navigate()
    assert (practice_page.select_table_row(username))
