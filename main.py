import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


executable_path = "./chromedriver"
# os.environ["webdriver.chrome.driver"] = executable_path

chrome_options = Options()
chrome_options.add_extension('buster.crx')

driver = webdriver.Chrome(executable_path=executable_path, chrome_options=chrome_options)
driver.get("https://google.com/recaptcha/api2/demo")
frame = driver.find_element_by_xpath('//iframe[contains(@src, "recaptcha")]')
driver.switch_to.frame(frame)
driver.find_element_by_xpath("//*[@id='recaptcha-anchor']").click()
time.sleep(3)
driver.find_element_by_xpath("//iframe[@name='c-i50lxov4pf2d']").click()

time.sleep(10)


driver.switch_to.default_content()


driver.quit()