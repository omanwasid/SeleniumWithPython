from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
driver: WebDriver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.find_element_by_name("q").send_keys("Selenium")
driver.find_element_by_name("btnK").click()