from bs4 import BeautifulSoup
import requests

url = "https://msk.kassir.ru/"
site = requests.get(url).text

bs = BeautifulSoup(site, "lxml")
titles = [el.text for el in bs.select(".recommendation-item_title")]

def clear(text):
    while "\xa0" in text:
        text = text.replace("\xa0", "")

    return text

def get_events():
    events = []

    cards = [el for el in bs.select(".recommendation-item")]
    for item in cards:
        events.append({
            "title" : item.select_one(".recommendation-item_title").text,
            "time" : clear(item.select_one(".recommendation-item_date").text),
            "price" : clear(item.select(".recommendation-item_price-block span")[2].text),
            "place" : item.select_one(".recommendation-item_venue").text
        })
        

    return events

print(get_events())
