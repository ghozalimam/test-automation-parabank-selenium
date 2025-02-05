# tests/test_registration.py
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

# Register Success

def test_register_successfully(driver):
    # Buka website Parabank
    driver.get("https://parabank.parasoft.com/parabank/index.htm")

    # Klik tombol "Register"
    register_button = driver.find_element(By.LINK_TEXT, "Register")
    register_button.click()

    # Isi formulir registrasi
    driver.find_element(By.NAME, "customer.firstName").send_keys("John")
    driver.find_element(By.NAME, "customer.lastName").send_keys("Doe")
    driver.find_element(By.NAME, "customer.address.street").send_keys("123 Main St")
    driver.find_element(By.NAME, "customer.address.city").send_keys("Anytown")
    driver.find_element(By.NAME, "customer.address.state").send_keys("CA")
    driver.find_element(By.NAME, "customer.address.zipCode").send_keys("12345")
    driver.find_element(By.NAME, "customer.phoneNumber").send_keys("123-456-7890")
    driver.find_element(By.NAME, "customer.ssn").send_keys("123-45-6789")
    driver.find_element(By.NAME, "customer.username").send_keys("johnitesting2")
    driver.find_element(By.NAME, "customer.password").send_keys("password123")
    driver.find_element(By.NAME, "repeatedPassword").send_keys("password123")

    # Klik tombol "Register"
    driver.find_element(By.XPATH, "//input[@value='Register']").click()

    # Tunggu hingga pesan selamat datang muncul
    welcome_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Welcome')]"))
    ).text

    # Verifikasi apakah registrasi berhasil
    assert "Welcome" in welcome_message, f"Expected 'Welcome' in message, but got: {welcome_message}"
    print("Registrasi berhasil:", welcome_message)

# Register Wrong Password

def test_register_wrong_password(driver):
    # Buka website Parabank
    driver.get("https://parabank.parasoft.com/parabank/index.htm")

    # Klik tombol "Register"
    register_button = driver.find_element(By.LINK_TEXT, "Register")
    register_button.click()

    # Isi formulir registrasi
    driver.find_element(By.NAME, "customer.firstName").send_keys("John")
    driver.find_element(By.NAME, "customer.lastName").send_keys("Doe")
    driver.find_element(By.NAME, "customer.address.street").send_keys("123 Main St")
    driver.find_element(By.NAME, "customer.address.city").send_keys("Anytown")
    driver.find_element(By.NAME, "customer.address.state").send_keys("CA")
    driver.find_element(By.NAME, "customer.address.zipCode").send_keys("12345")
    driver.find_element(By.NAME, "customer.phoneNumber").send_keys("123-456-7890")
    driver.find_element(By.NAME, "customer.ssn").send_keys("123-45-6789")
    driver.find_element(By.NAME, "customer.username").send_keys("johndoe123")
    driver.find_element(By.NAME, "customer.password").send_keys("password123")
    driver.find_element(By.NAME, "repeatedPassword").send_keys("wrongpassword")  # Password tidak cocok

    # Klik tombol "Register"
    register_button = driver.find_element(By.XPATH, "//input[@value='Register']")
    register_button.click()

    # Tunggu hingga pesan kesalahan muncul
    error_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='repeatedPassword.errors']"))
    ).text