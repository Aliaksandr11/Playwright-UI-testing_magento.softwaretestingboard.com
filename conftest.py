import pytest
from playwright.sync_api import Page, BrowserContext

from pages.create_account_page import CreateAccountPage
from pages.eco_friendly_collection_page import EcoCollectionPage
from pages.sale_page import SalePage


@pytest.fixture()
def page(context: BrowserContext):
    page: Page = context.new_page()
    return page


@pytest.fixture()
def create_account_page(page):
    return CreateAccountPage(page)


@pytest.fixture()
def eco_collection_page(page):
    return EcoCollectionPage(page)


@pytest.fixture()
def sale_page(page):
    return SalePage(page)
