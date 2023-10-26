from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from time import sleep
import csv

nombre_de_page = 4

browser = webdriver.Chrome()
browser.get("https://www.amazon.com")
sleep(1)
search_bar = browser.find_element(by=By.ID, value='twotabsearchtextbox')
sleep(1)
search_bar.send_keys("coding book")
search_bar.send_keys(Keys.ENTER)


codingBookAmazon = []
liste_url = []
        

for page in range(nombre_de_page):
    urlOuvrir = browser.find_elements(By.CSS_SELECTOR, ".a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal")
    for urlLivre in urlOuvrir:
        liste_url.append(urlLivre.get_attribute("href"))
    sleep(1)
    
    changer_page = browser.find_element(by=By.CSS_SELECTOR, value='.s-pagination-next')
    sleep(1)
    changer_page.click()
    sleep(2)

taille_list =len(liste_url)-1
#on retire les urls en double
for i in range(taille_list,0,-1):
    if(liste_url[i] == liste_url[i-1]):
        liste_url.pop(i)
print("Nombre url: ",len(liste_url))




    #se rend sur tous les url de la liste
for post in liste_url:
    browser.execute_script("window.open('');")
    browser.switch_to.window(browser.window_handles[1])
    browser.get(post)
    sleep(2)

    dicoBook = {}
    titre = browser.find_element(By.CSS_SELECTOR, value=".a-size-extra-large.celwidget")
    dicoBook["Titre"] = titre.text

    description = BeautifulSoup(browser.find_element(By.CSS_SELECTOR,"#bookDescription_feature_div").get_attribute("innerHTML"), "html.parser").text
    dicoBook["Description"] = description[:description.find(" Read more")]

    avis = browser.find_elements(By.CSS_SELECTOR, value=".a-expander-content.reviewText.review-text-content.a-expander-partial-collapse-content")

    limit = 5 if len(avis) >= 5 else len(avis)

    for i in range(limit):
        name = "Avis_" + str(i+1)
        dicoBook[name] = avis[i].text

    codingBookAmazon.append(dicoBook)

    sleep(1)
    browser.close()
    browser.switch_to.window(browser.window_handles[0])




print("Taille liste :",len(codingBookAmazon))

noms_de_champs = ["Titre","Description","Avis_1","Avis_2","Avis_3","Avis_4","Avis_5"]

# Nom du fichier CSV de sortie
nom_fichier_csv = 'codingBookAmazon.csv'

# Ouvrez le fichier CSV en mode écriture
with open(nom_fichier_csv, mode='w', newline='', encoding='utf-8') as fichier_csv:
    writer = csv.DictWriter(fichier_csv, fieldnames=noms_de_champs,delimiter=";")
    writer.writeheader()
    for element in codingBookAmazon:
        writer.writerow(element)


