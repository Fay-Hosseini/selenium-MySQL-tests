from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- Pytest data-driven test ---
def test_login(driver, login_data):
    for username, password in login_data:
        driver.get("https://the-internet.herokuapp.com/login")

        wait = WebDriverWait(driver, 20)
        username_field = wait.until(EC.visibility_of_element_located((By.ID, "username")))
        username_field.clear()
        username_field.send_keys(username)

        password_field = wait.until(EC.visibility_of_element_located((By.ID, "password")))
        password_field.clear()
        password_field.send_keys(password)

        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

               # Example assertion
        assert "secure" in driver.current_url or "error" in driver.page_source



