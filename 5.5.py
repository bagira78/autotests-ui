from time import sleep
from playwright.sync_api import sync_playwright, expect
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    button = page.get_by_test_id("registration-page-registration-button")
    expect(button).to_be_disabled()

    email_input=page.get_by_test_id("registration-form-email-input").locator('input')
    email_input.fill('user.name@gmail.com')
    user_name_input = page.get_by_test_id("registration-form-username-input").locator('input')
    user_name_input.fill('username')
    password_input=page.get_by_test_id("registration-form-password-input").locator('input')
    password_input.fill('Password')

    expect(button).to_be_enabled()

    