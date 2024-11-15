'''
2024.11.15 15.38
Visita Wikipedia, cerca "Python (programming language)", e stampa il titolo della pagina dei risultati
'''


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()

driver.get("https://it.wikipedia.org/wiki/Pagina_principale")

time.sleep(1)

search_bar = driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[2]/div/form/div/input[1]")
time.sleep(1)
search_bar.send_keys("Python (programming language)"+ Keys.ENTER)
time.sleep(1)

title = driver.title
time.sleep(1)

driver.quit()
time.sleep(1)

print(f"Titolo della pagina: {title}")
