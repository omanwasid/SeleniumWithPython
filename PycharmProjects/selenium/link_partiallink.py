from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


driver: WebDriver = webdriver.Chrome()
driver.get("https://www.selenium.dev/")
driver.find_element_by_link_text("About").click()
driver.find_element_by_partial_link_text("Sponsors").click()