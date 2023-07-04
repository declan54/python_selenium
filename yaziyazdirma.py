from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

url = "https://www.amazon.com/"             

driver.get(url)

ara=driver.find_element(By.ID,"twotabsearchtextbox")
ara.send_keys("phone")
ara.send_keys(Keys.RETURN)  



input()