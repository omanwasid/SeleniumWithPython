from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

driver: WebDriver = webdriver.Chrome()
driver.get("https://www.geeksforgeeks.org/")

# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/c-programming-language/?ref=leftbar")

# one step backward in browser history
driver.back()

# one step backward in browser history
driver.forward()