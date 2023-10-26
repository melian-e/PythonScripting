from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from time import sleep
import csv

browser = webdriver.Chrome()


year1 = 23

limitYearForScraping = 10

browser.get("https://www.nba.com/stats/leaders?Season=20"+str(year1)+"-"+str(year1+1))

dictNames = ["year"]

thead = browser.find_element(By.CSS_SELECTOR, value=".Crom_headers__mzI_m").get_attribute("innerHTML")

theadSoup = BeautifulSoup(thead, "html.parser")

allTh = theadSoup.find_all("th")

for th in allTh:
    dictNames.append(th.text)


arrayDict = []

for y in range(limitYearForScraping):
    print("20"+str(year1)+"-"+str(year1+1))

    parent_show_all = browser.find_element(By.CSS_SELECTOR, '.Crom_cromSettings__ak6Hd')
    show_all = parent_show_all.find_element(By.CSS_SELECTOR, '.DropDown_select__4pIg9')
    dropdown_select = Select(show_all)
    dropdown_select.select_by_visible_text("All")

    tbody = browser.find_element(By.CSS_SELECTOR, value=".Crom_body__UYOcU").get_attribute("innerHTML")

    tbodySoup = BeautifulSoup(tbody, "html.parser")

    allTr = tbodySoup.find_all("tr")

    for tr in allTr:
        allTd = tr.find_all("td")
        dictTemp = {}
        dictTemp["year"] = "20"+str(year1)+"-"+str(year1+1)
        for i in range(1,len(allTd)+1):
            dictTemp[dictNames[i]] = allTd[i-1].text
        arrayDict.append(dictTemp)

    year1 -= 1
    browser.get("https://www.nba.com/stats/leaders?Season=20"+str(year1)+"-"+str(year1+1))

with open("nba.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=dictNames)
    writer.writeheader()
    for dict in arrayDict:
        writer.writerow(dict)

browser.close()