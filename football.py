from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

url = "https://www.championat.com/stat/football/#2024-05-07"

browser = webdriver.Chrome(service=Service(executable_path="E:\chromedriver-win32/chromedriver.exe"))
browser.get(url)
sleep(3)

matches = browser.find_elements(By.CLASS_NAME, "table-item__name")

print([el.text for el in matches])