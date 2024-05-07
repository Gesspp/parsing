from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

def get_weather(country, city):
    url = "https://world-weather.ru/pogoda/"
    url += f"{country}/{city}/"

    browser = webdriver.Chrome(service=Service(executable_path="E:\chromedriver-win32/chromedriver.exe"))
    browser.get(url)
    sleep(10)

    temp = browser.find_element(By.ID, "weather-now-number").text

    return temp


print(get_weather("france", "paris"))