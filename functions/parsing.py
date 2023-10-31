from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

mail_address = "andmai000@pbs.edu.pl"
password_address = ""

options = wd.ChromeOptions()
options.add_argument("--headless")
driver = wd.Chrome(options=options)
driver.get("https://webmail.pbs.edu.pl/mail/")

mail = driver.find_element(By.ID, "rcmloginuser")
mail.clear()
mail.send_keys(mail_address)

password = driver.find_element(By.ID, "rcmloginpwd")
password.clear()
password.send_keys(password_address)

button = driver.find_element(By.ID, "rcmloginsubmit")
button.click()
time.sleep(0.2)