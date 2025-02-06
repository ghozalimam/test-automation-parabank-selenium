import pytest
import time
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

def open_new_account(driver):
    # Buka website Parabank
    driver.get("https://parabank.parasoft.com/parabank/index.htm")

    # Login
    driver.find_element(By.NAME, "username").send_keys("goblin")
    driver.find_element(By.NAME, "password").send_keys("123456")
    driver.find_element(By.XPATH, "//input[@value='Log In']").click()

    wait = WebDriverWait(driver, 5)
    # Klik tombol "Open New Account"
    open_new_account_button = driver.find_element(By.CSS_SELECTOR, "a[href='openaccount.htm']")
    open_new_account_button.click()

    wait = WebDriverWait(driver, 5)
    # Pilih tipe akun "SAVINGS"
    account_type = driver.find_element(By.ID, "type")
    account_type.send_keys("SAVINGS")

    wait = WebDriverWait(driver, 5)
    # Klik tombol "Open New Account"
    driver.find_element(By.CSS_SELECTOR, "input[value='Open New Account']").click()

    wait = WebDriverWait(driver, 5)
    # Tunggu hingga nomor akun muncul
    account_number = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Account Opened!')]"))
    ).text
    
    wait = WebDriverWait(driver, 5)
    # Verifikasi apakah pembukaan akun berhasil
    assert "Account Opened!" in account_number, f"Expected 'Account Opened!' in message, but got: {account_number}"

    # Cetak nomor akun
    print("Pembukaan akun berhasil:", account_number)
