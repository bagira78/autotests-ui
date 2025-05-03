import pytest
from playwright.sync_api import sync_playwright, expect, Page


@pytest.fixture(scope="session")
def initialize_browser_state():
    with sync_playwright() as playwright:
       browser=playwright.chromium.launch(headless=False)
       context=browser.new_context()
       page=context.new_page()
       page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

       email_input = page.get_by_test_id("registration-form-email-input").locator('input')
       email_input.fill('user.name@gmail.com')

       user_name_input = page.get_by_test_id("registration-form-username-input").locator('input')
       user_name_input.fill('username')

       password_input = page.get_by_test_id("registration-form-password-input").locator('input')
       password_input.fill('Password')

       button = page.get_by_test_id("registration-page-registration-button")
       button.click()

       context.storage_state(path="browser-state.json")



@pytest.fixture
def chromium_page_with_state(initialize_browser_state)->Page:
   with sync_playwright() as playwright:
      browser = playwright.chromium.launch(headless=False)
      context = browser.new_context(storage_state="browser-state.json")
      yield context.new_page()
      browser.close()