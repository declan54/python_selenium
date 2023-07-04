from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

#driver.find_element(By.XPATH, "//input[@value='Log In'][@type='submit']").click() CLASS ÇALIŞMAZSA


url = "https://the-internet.herokuapp.com/login"             
driver.get(url)
driver.maximize_window()

kullaniciadi=driver.find_element(By.ID,"username")
kullaniciadi.send_keys("tomsmith")
şifre=driver.find_element(By.ID,"password")
şifre.send_keys("safsag")

driver.find_element(By.CSS_SELECTOR, "button.radius").click()



mesaj=driver.find_element(By.ID,"flash").text

if"Your password is invalid!" in mesaj:
    print("yanliş şifre kodu doğru çalişiyor")
else:
    print("şifre kodu yanliş çalişiyor")

url = "https://the-internet.herokuapp.com/login"             
driver.get(url)
driver.maximize_window()
kullaniciadi=driver.find_element(By.ID,"username")
kullaniciadi.send_keys("sagdsg")
şifre=driver.find_element(By.ID,"password")
şifre.send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, "button.radius").click()

mesaj2=driver.find_element(By.ID,"flash").text
if"Your username is invalid!" in mesaj2:
    print("yanliş kullanici kodu doğru çalişiyor")
else:
    print("yanliş kullanici kodu yanliş çalişiyor")


kullaniciadi=driver.find_element(By.ID,"username")
kullaniciadi.send_keys("tomsmith")
şifre=driver.find_element(By.ID,"password")
şifre.send_keys("SuperSecretPassword!")
#btn1=driver.find_element(By.TAG_NAME, "Log In").click()
driver.find_element(By.CSS_SELECTOR, "button.radius").click()

mesaj3=driver.find_element(By.ID,"flash").text
if"You logged into a secure area!" in mesaj3:
    print("Başarili giriş çalişiyor")
else:
    print("başarili giriş kodu çalişmiyor")

driver.find_element(By.XPATH, "//i[contains(text(),'Logout')]").click()


input()