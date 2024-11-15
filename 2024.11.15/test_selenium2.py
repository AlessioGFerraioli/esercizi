'''
2024.11.15 16.40
https://practicetestautomation.com/practice-test-login/
andate a questo link e prendete user e psw, inseritele nel login e cliccate su submit, arrivati nella pagina di accesso 
vi prendete il testo e lo stampate e poi cliccate su log out, 
successivamente stampate il driver.title e chiudete il driver
'''


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()

driver.get("https://practicetestautomation.com/practice-test-login/")

time.sleep(10)

username_xpath = "/html/body/div/div/section/section/ul/li[2]/b[1]"
username = driver.find_element(By.XPATH, username_xpath).text

password_xpath = "/html/body/div/div/section/section/ul/li[2]/b[2]"
password = driver.find_element(By.XPATH, password_xpath).text



xpath_username_bar = "/html/body/div/div/section/section/div[1]/div[1]/input" 


username_bar = driver.find_element(By.XPATH, xpath_username_bar)

time.sleep(1)

username_bar.send_keys(username)

xpath_password_bar = "/html/body/div/div/section/section/div[1]/div[2]/input"

password_bar = driver.find_element(By.XPATH, xpath_password_bar)

time.sleep(1)

password_bar.send_keys(password)
time.sleep(1)
submit_button_xpath = "/html/body/div/div/section/section/div[1]/button"

submit_button = driver.find_element(By.XPATH, submit_button_xpath)
submit_button.click()
time.sleep(5)

title_text_xpath = "/html/body/div/div/section/div/div/article/div[1]/h1"
title_text = driver.find_element(By.XPATH, title_text_xpath).text
time.sleep(1)


subtitle_text_xpath = "/html/body/div/div/section/div/div/article/div[2]/p[1]/strong"
subtitle_text = driver.find_element(By.XPATH, subtitle_text_xpath).text
time.sleep(1)

logout_button_xpath = "/html/body/div/div/section/div/div/article/div[2]/div/div/div/a"
logout_button = driver.find_element(By.XPATH, logout_button_xpath)
logout_button.click()
time.sleep(5)


driver.quit()
time.sleep(1)

print(title_text, subtitle_text)
