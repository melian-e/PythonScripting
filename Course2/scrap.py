from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import csv

browser = webdriver.Chrome()
browser.get("http://www.amazon.fr/")

accept = browser.find_element(By.CSS_SELECTOR,"#sp-cc-accept")
accept.click()

search_bar = browser.find_element(By.CSS_SELECTOR,"#twotabsearchtextbox")
search_bar.send_keys("chaussure homme")
search_bar.submit()

prices_tab = []
names_tab = []

for i in range(3):
    sleep(5)
    prices = browser.find_elements(By.CSS_SELECTOR,".a-price-whole")

    names = browser.find_elements(By.CSS_SELECTOR,".a-size-base-plus.a-color-base.a-text-normal")

    for e in prices:
        prices_tab.append(e.text)
    for e in names:
        names_tab.append(e.text)

    next = browser.find_element(By.CSS_SELECTOR,".s-pagination-next")
    next.click()

print(prices_tab)
print(len(prices_tab))

with open("prices.csv","w",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Prix","Nom"])
    for e in prices_tab:
        writer.writerow([e, names_tab[prices_tab.index(e)]])
    

browser.quit()