from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from time import sleep
import csv
import re
from selenium import webdriver

browser = webdriver.Chrome()

browser.get("https://www.nba.com/teams")
sleep(1)

#on récupere le lien pour les pages de toutes les équipes
liste_teams = browser.find_elements(By.CSS_SELECTOR, ".Anchor_anchor__cSc3P.TeamFigureLink_teamFigureLink__uqnNO")
liens_teams = []

for team in liste_teams:
    if(team.get_attribute("innerHTML") == "Profile"):
        liens_teams.append(team.get_attribute("href"))

#on crée les clés de notre dictionnaire
arrayDict = []
names1 = ["GP","MIN","PTS","W","L","WIN%","FGM","FGA","FG%","3PM","3PA","3P%","FTM","FTA","FT%","OREB","DREB","REB","AST","TOV","STL","BLK","PF","+/-"]
names2 = ["HOME","ROAD","WINS","LOSSES"]
dictNames = []

for name2 in names2:
    for name1 in names1:
        dictNames.append(name2+"."+name1)

dictNames = ["NAME"] + dictNames

#on se rend sur totues les pages d'équipe pour récupérer les informations
for lien in liens_teams:
    browser.get("https://www.nba.com/stats/team/"+re.search(r'\d+', lien).group()+"/traditional")
    sleep(1)

    statTmp = {}

    #selection de l'année 2022-23
    annee = browser.find_element(By.CSS_SELECTOR, '.DropDown_select__4pIg9')
    dropdown_select = Select(annee)
    dropdown_select.select_by_visible_text("2022-23")
    sleep(1)
    
    #récupération du nom de l'équipe
    nom = browser.find_element(By.CSS_SELECTOR,".TeamHeader_name__MmHlP").get_attribute("innerHTML")
    nom = nom.replace("<div>", "")
    nom = nom.replace("<!-- -->&nbsp;", " ")
    nom = nom.replace("</div>", "")
    statTmp["NAME"] = nom

    liste_tables = browser.find_elements(By.CSS_SELECTOR,".Crom_table__p1iZz")

    j = 1

    #recupération des statistiques de l'équipe pour les matchs a domicile, matchs a l'extérieur, les victoires et les défaites
    for table in liste_tables:
        sous_partie = table.find_element(By.CSS_SELECTOR,".Crom_text__NpR1_.Crom_primary__EajZu.Crom_sticky__uYvkp")

        if sous_partie.text == "LOCATION" or sous_partie.text == "WINS/LOSSES":
            tableSoup = BeautifulSoup(table.get_attribute("innerHTML"), "html.parser")
            allTr = tableSoup.find_all("tr")
            for tr in allTr:
                allTd = tr.find_all("td")
                for i,td in enumerate(allTd):
                    if i != 0:
                        statTmp[dictNames[j]] = td.text
                        j+=1
    arrayDict.append(statTmp)

#écriture dans le fichier csv
with open("nba_teams.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=dictNames)
    writer.writeheader()
    for dict in arrayDict:
        writer.writerow(dict)

browser.close()