import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep
import csv

def scrap(numberOfDesc):
    browser = webdriver.Chrome()
    url = "https://www.amazon.fr/s?k=programming+books"
    browser.get(url)

    aElems = browser.find_elements(By.CSS_SELECTOR,".a-link-normal.a-text-normal")

    links= []
    
    while numberOfDesc > len(aElems):
        browser.get(browser.find_element(By.CSS_SELECTOR,".s-pagination-next").get_attribute("href"))
        aElems.append(browser.find_element(By.CSS_SELECTOR,".a-link-normal.a-text-normal"))    

    ## keep all unique links
    i=0
    
    while len(links) < numberOfDesc:
        a = aElems[i]
        link = a.get_attribute("href")
        if link not in links:
            links.append(link)
        i+=1

    dictList = []

    for link in links:
        browser.get(link)

        title = browser.find_element(By.CSS_SELECTOR,"#productTitle").text.replace("\n"," ")

        details = BeautifulSoup(browser.find_element(By.CSS_SELECTOR,"#detailBullets_feature_div").get_attribute("innerHTML"), "html.parser").text.replace("\n"," ")

        commentsList = BeautifulSoup(browser.find_element(By.CSS_SELECTOR,"#cm-cr-global-review-list").get_attribute("innerHTML"), "html.parser").findChildren("div", recursive=False, limit=5)

        comments = []

        for comment in commentsList:
            comments.append(comment.text.replace("\n"," "))

        dictList.append({
            "title": title,
            "description": details,
            "comments": comments,
        })

        with open("books.csv","w",newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["title","description","comments"])
            for e in dictList:
                writer.writerow([e["title"], e["description"], ",".join(e["comments"])])

    browser.quit()

if __name__ == "__main__":
    numberOfDesc = int(sys.argv[1])
    scrap(numberOfDesc)