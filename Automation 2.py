#Give username and password through automation on webbrowser.
import os
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
username=input("enter your username:")
password=input("enter your password:")
driver=webdriver.Chrome()
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(5)
driver.find_element(By.NAME,"username").send_keys(username)
driver.find_element(By.NAME,"password").send_keys(password)
driver.find_element(By.XPATH,"//button[@type='submit']").click()
print("you are logged in")