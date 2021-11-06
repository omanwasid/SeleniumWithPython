
from selenium import webdriver
import pdb

driver = webdriver.Chrome()

driver.get("https://dotnet.microsoft.com/apps/aspnet/")
driver.find_element_by_link_text("Get Started").click()

