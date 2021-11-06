from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
driver: WebDriver = webdriver.Chrome()
driver.get('https://google.com');
driver.save_screenshot("screenshot1.png");