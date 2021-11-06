from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
import time

driver: WebDriver = webdriver.Chrome()

#driver = webdriver.Firefox(executable_path="C:\Users\45422\Desktop\geckodriver-v0.30.0-win32\geckodriver.exe")
driver.get("https://www.jobindex.dk/")
print(driver.title)
print(driver.current_url)
time.sleep(2)

driver.find_element_by_id("jix-cookie-consent-accept-all").click()
#driver.find_elements_by_xpath("//*[@id='jix-cookie-consent-accept-all']")
print(driver.title)
time.sleep(2)

driver.maximize_window() # Maximize the browser window
link = driver.find_element_by_link_text('Log ind') #Click on the anchor link
link.click()
time.sleep(3)

#Enter Log-in With Email Address and Password
driver.find_element_by_xpath("//*[@id='email']").send_keys("wasidcph@gmail.com")
driver.find_element_by_xpath("//*[@id='password']").send_keys("wasidcph1507")
driver.find_element_by_xpath("//*[@id='_jix_login_contents']/div[2]/div[1]/form/div[4]/button").click()
time.sleep(3)

#Search Input Field
driver.find_element_by_xpath("//*[@id='search-component']/div[1]/div[1]/input").send_keys("QA Test Engineer")
driver.find_element_by_xpath("//input[@placeholder='Vælg eller indtast områder']").send_keys("København ")
time.sleep(1)
driver.find_element_by_xpath("//input[@placeholder='Vælg eller indtast områder']").send_keys(Keys.ARROW_DOWN)
time.sleep(1)
driver.find_element_by_xpath("//input[@placeholder='Vælg eller indtast områder']").send_keys(Keys.ENTER)
time.sleep(1)
driver.find_element_by_xpath("//div[contains(@class,'col-lg-3 d-none d-lg-block')]//button[contains(@type,'submit')][normalize-space()='Søg']").click()
time.sleep(2)

driver.find_element_by_link_text("Din jobsøgning").click()
time.sleep(2)
driver.find_element_by_partial_link_text("Din side").click()
time.sleep(2)
driver.back()

driver.find_element_by_link_text("Jobannoncer").click()
time.sleep(2)
driver.find_element_by_partial_link_text("Avanceret søgning").click()
time.sleep(2)
driver.back()

driver.find_element_by_link_text("Virksomhedsprofiler").click()
time.sleep(2)
driver.find_element_by_partial_link_text("Evaluér arbejdsplads").click()
time.sleep(2)
driver.back()

driver.find_element_by_link_text("Test dig selv").click()
time.sleep(2)
driver.find_element_by_partial_link_text("Stresstest").click()
time.sleep(2)
driver.back()

driver.find_element_by_link_text("Inspiration").click()
time.sleep(2)
driver.find_element_by_partial_link_text("Dit første job").click()
time.sleep(2)
driver.back()

driver.find_element_by_link_text("Vejledning").click()
time.sleep(2)
driver.find_element_by_partial_link_text("Jobsøgningskursus").click()
time.sleep(2)
driver.back()

driver.execute_script("window.scrollTo(2,document.body.scrollHeight)") # Scroll down browser window
time.sleep(2)
driver.find_element_by_link_text("Om Jobindex").click()
time.sleep(2)
driver.back()
driver.execute_script("window.scrollTo(2,document.body.scrollHeight)") # Scroll down browser window
driver.close()















