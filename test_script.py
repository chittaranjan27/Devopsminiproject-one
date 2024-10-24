# test_script.py
from selenium import webdriver
import time

# Set up the Chrome WebDriver
 driver = webdriver.Chrome()  # Ensure you have ChromeDriver installed

try:
    # Test Home Page
    driver.get('http://localhost:8081')
    assert "Welcome to Our E-Commerce Site!" in driver.page_source

    # Test About Page
    driver.get('http://localhost:8082')
    assert "About Us" in driver.page_source

    # Test Products Page
    driver.get('http://localhost:8083')
    assert "Our Products" in driver.page_source

    # Test Contact Page
    driver.get('http://localhost:8084')
    assert "Contact Us" in driver.page_source

finally:
    # Close the browser
    driver.quit()
