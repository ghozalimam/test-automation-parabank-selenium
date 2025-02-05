import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def driver():
    # Inisialisasi WebDriver
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def login(driver, username, password):
    # Buka website Parabank
    driver.get("https://parabank.parasoft.com/parabank/index.htm")

    # Isi formulir login
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)

    # Klik tombol "Log In"
    driver.find_element(By.XPATH, "//input[@value='Log In']").click()

    try:
        # Tunggu hingga pesan selamat datang muncul
        welcome_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Accounts Overview')]"))
        ).text

        # Verifikasi apakah login berhasil
        assert "Accounts Overview" in welcome_message, f"Expected 'Accounts Overview' in message, but got: {welcome_message}"
        print("Login berhasil:", welcome_message)
        return True
    except:
        # Tunggu hingga pesan kesalahan muncul
        error_message = driver.find_element(By.XPATH, "//p[contains(text(), 'The username and password could not be verified.')]").text

        # Verifikasi apakah login gagal
        assert "The username and password could not be verified." in error_message, f"Expected 'The username and password could not be verified.' in message, but got: {error_message}"
        print("Login gagal:", error_message)
        return False

# Test Login Success
def test_login_success(driver):
    assert login(driver, "johnitesting2", "password123") == True

# Test Login Failure
def test_login_failure(driver):
    assert login(driver, "wrongusername", "wrongpassword") == False
