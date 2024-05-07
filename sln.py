from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

url = "https://www.ticketland.ru/?utm_campaign=tl-afisha&utm_source=direct.yandex.ru&utm_medium=cpc&utm_term=---autotargeting&utm_content=ad_id:16001398903/source_type:search/source:none/position_type:premium/position:2/campaign_id:109114353/gbid:5426970487/phrase_id:51033916387/region_id:213/device_type:desktop/addphrases:no&yclid=7538674304266272767"

browser = webdriver.Chrome(service=Service(executable_path="E:\chromedriver-win32/chromedriver.exe"))
browser.get(url)
sleep(3)

els = browser.find_elements(By.ID, "card__title-text")
print([el.text for el in els if len(el.text) > 0])

