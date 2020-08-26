import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


driver_path = "./chromedriver"
os.environ["webdriver.chrome.driver"] = driver_path

options = Options()
options.add_extension('buster.crx')

driver = webdriver.Chrome(executable_path=driver_path, options=options)
driver.get("https://google.com/recaptcha/api2/demo")
frame = driver.find_element_by_xpath('//iframe[contains(@src, "recaptcha")]')
driver.switch_to.frame(frame)
driver.find_element_by_xpath("//*[@id='recaptcha-anchor']").click()
time.sleep(3)
driver.find_element_by_title("Solve the challenge").click()

time.sleep(100)


driver.switch_to.default_content()


driver.quit()