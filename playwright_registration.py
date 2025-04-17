from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
   chromium=playwright.chromium.launch(headless=False)
   page=chromium.new_page()


   page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')


   email_input=page.locator('//div[@data-testid="registration-form-email-input"]//div//input')
   email_input.fill('user.name@gmail.com')


   username_input=page.locator('//div[@data-testid="registration-form-username-input"]//div//input')
   username_input.fill('username')


   password_input=page.locator('//div[@data-testid="registration-form-password-input"]//div//input')
   password_input.fill('username')


   registration_btn=page.locator('//button[@data-testid="registration-page-registration-button"]')
   registration_btn.click()


   dashboard=page.get_by_test_id("dashboard-toolbar-title-text")
   expect(dashboard).to_be_visible()
