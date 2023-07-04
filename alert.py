from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome()
url="https://the-internet.herokuapp.com/javascript_alerts"
driver.get(url)


driver.maximize_window()
buton=driver.find_element(By.XPATH,"(//button)[2]")
buton.click()
driver.implicitly_wait(2)
WebDriverWait(driver,3).until(expected_conditions.alert_is_present())
alarm=Alert(driver)
mesaj=alarm.text
time.sleep(1)
alarm.dismiss()

sonuç=driver.find_element(By.ID ,"result").text

print("mesaj:"+mesaj)
print("sonuç:"+sonuç)


input()