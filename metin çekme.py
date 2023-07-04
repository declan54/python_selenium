from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

url = "https://tr.wikipedia.org/wiki/Anasayfa"             
#EĞER İD BULAMAZSAN CLASS VE ALTI OLUYOR driver.find_element("by.css_selector,class").tect
driver.get(url)
yazi=driver.find_element(By.ID, "mp-itn")
yazi=yazi.text
print(yazi)
input()
