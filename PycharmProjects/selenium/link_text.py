from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

driver: WebDriver = webdriver.Chrome()
driver.get("https://www.selenium.dev/")
driver.find_element_by_link_text("About").click()
driver.find_element_by_partial_link_text("Sponsors").click()
'''

driver.find_element_by_css_selector("#gsc-i-id1").send_keys("Grid")

driver.get("https://www.google.com/")
driver.find_element_by_name("q").send_keys("Selenium")
driver.find_element_by_name("btnK").click()
driver.get("https://dotnet.microsoft.com/apps/aspnet/")
driver.find_element_by_link_text("Get Started").click()
driver.get('https://pythonspot.com');
driver.save_screenshot("screenshot.png");

driver.get("https://www.geeksforgeeks.org/")

# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/c-programming-language/?ref=leftbar")

# one step backward in browser history
driver.back()

# one step backward in browser history
driver.forward()'''
