from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import sys

main_url = 'https://www.xe.com'

driver = webdriver.Firefox()
driver.get(main_url)
assert 'XE' in driver.title
amtInput = driver.find_element_by_id("amount")
amtInput.clear()
amtInput.send_keys(sys.argv[1])
elem = driver.find_element_by_id("from")
elem.clear()
elem.send_keys(sys.argv[2])
elem.send_keys(Keys.RETURN)
elem = driver.find_element_by_id("to")
elem.clear()
elem.send_keys(sys.argv[3])
elem.send_keys(Keys.RETURN)
amtInput.send_keys(Keys.RETURN)

element_present = EC.presence_of_element_located((By.CSS_SELECTOR, ".converterresult-toAmount"))
WebDriverWait(driver, 3).until(element_present)
elem = driver.find_element_by_class_name('converterresult-toAmount')
print(sys.argv[1] + " " + sys.argv[2] + " = " + elem.text + " " + sys.argv[3])
driver.close()
