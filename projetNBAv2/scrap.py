from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from time import sleep
import csv
import re
from selenium import webdriver

sleepTime = 1
statsType = ["GP","MIN","PTS","W","L","WIN%","FGM","FGA","FG%","3PM","3PA","3P%","FTM","FTA","FT%","OREB","DREB","REB","AST","TOV","STL","BLK","PF","+/-"]

class StatBase:
    def __init__(self):
        self.HOME = {}
        self.ROAD = {}
        self.WINS = {}
        self.LOSSES = {}

    def setHome(self, home):
        self.HOME = home
    
    def setRoad(self, road):
        self.ROAD = road

    def setWins(self, wins):
        self.WINS = wins
    
    def setLosses(self, losses):
        self.LOSSES = losses

class Player(StatBase):
    def __init__(self):
        self.NAME = ""
        self.CLUB = ""
        self.POSITION = ""
        self.HEIGHT = ""
        self.WEIGHT = ""
        self.COUNTRY = ""
        self.AGE = ""
        self.EXPERIENCE = ""

    def setName(self, name):
        self.NAME = name

    def setClub(self, club):
        self.CLUB = club

    def setPosition(self, position):
        self.POSITION = position

    def setHeight(self, height):
        self.HEIGHT = height

    def setWeight(self, weight):
        self.WEIGHT = weight

    def setCountry(self, country):
        self.COUNTRY = country

    def setAge(self, age):
        self.AGE = age
    
    def setExperience(self, experience):
        self.EXPERIENCE = experience

    def formatForCSV(self):
        dictTemp = {}
        dictTemp["NAME"] = self.NAME
        dictTemp["CLUB"] = self.CLUB
        dictTemp["POSITION"] = self.POSITION
        dictTemp["HEIGHT"] = self.HEIGHT
        dictTemp["WEIGHT"] = self.WEIGHT
        dictTemp["COUNTRY"] = self.COUNTRY
        dictTemp["AGE"] = self.AGE
        dictTemp["EXPERIENCE"] = self.EXPERIENCE

        for key, value in self.HOME.items():
            dictTemp["HOME."+key] = value

        for key, value in self.ROAD.items():
            dictTemp["ROAD."+key] = value

        for key, value in self.WINS.items():
            dictTemp["WINS."+key] = value

        for key, value in self.LOSSES.items():
            dictTemp["LOSSES."+key] = value

        return dictTemp

class Team(StatBase):
    def __init__(self):
        self.NAME = ""

    def setName(self, name):
        self.NAME = name

    def formatForCSV(self):
        dictTemp = {}
        dictTemp["NAME"] = self.NAME

        for key, value in self.HOME.items():
            dictTemp["HOME."+key] = value

        for key, value in self.ROAD.items():
            dictTemp["ROAD."+key] = value

        for key, value in self.WINS.items():
            dictTemp["WINS."+key] = value

        for key, value in self.LOSSES.items():
            dictTemp["LOSSES."+key] = value

        return dictTemp
    
def getListOfPlayersLinks(browser) -> list:
    browser.get("https://www.nba.com/stats/leaders?Season=2022-23")
    sleep(sleepTime)

    #affichage de tous les joueurs sur une seul page
    parent_show_all = browser.find_element(By.CSS_SELECTOR, '.Crom_cromSettings__ak6Hd')
    show_all = parent_show_all.find_element(By.CSS_SELECTOR, '.DropDown_select__4pIg9')
    dropdown_select = Select(show_all)
    dropdown_select.select_by_visible_text("All")

    #on recupere le lien de toutes les pages personnels des joueurs
    lignes_joueurs = browser.find_elements(By.CSS_SELECTOR,".Crom_text__NpR1_.Crom_stickySecondColumn__29Dwf")
    liste_liens = []

    for ligne in lignes_joueurs:
        ligne_lien = ligne.find_elements(By.CSS_SELECTOR,".Anchor_anchor__cSc3P")
        for lien in ligne_lien:
            liste_liens.append(lien.get_attribute("href"))

    return liste_liens

def getListOfTeamsLinks(browser) -> list:
    browser.get("https://www.nba.com/teams")
    sleep(sleepTime)

    #on récupere le lien pour les pages de toutes les équipes
    liste_teams = browser.find_elements(By.CSS_SELECTOR, ".Anchor_anchor__cSc3P.TeamFigureLink_teamFigureLink__uqnNO")
    liens_teams = []

    for team in liste_teams:
        if(team.get_attribute("innerHTML") == "Profile"):
            liens_teams.append(team.get_attribute("href"))
    return liens_teams

def getStatsFromTableList(liste_tables) -> dict:
    dictOfStats = {}

    #recupération des statistiques de l'équipe pour les matchs a domicile, matchs a l'extérieur, les victoires et les défaites
    for table in liste_tables:
        header_text = table.find_element(By.CSS_SELECTOR,".Crom_text__NpR1_.Crom_primary__EajZu.Crom_sticky__uYvkp")

        if header_text.text == "LOCATION" or header_text.text == "WINS/LOSSES":
            tableSoup = BeautifulSoup(table.get_attribute("innerHTML"), "html.parser")
            allTr = tableSoup.find_all("tr")
            for tr in allTr:
                allTd = tr.find_all("td")

                #on casse la boucle si l'on a pas de td
                if(len(allTd) == 0):
                    continue

                #on isole le titre pour savoir où placer les données
                tmpDict = {}
                subHeader = allTd[0].text
                allTd = allTd[1:]

                for i,td in enumerate(allTd):
                    tmpDict[statsType[i]]=td.text

                if("Home" in subHeader):
                    dictOfStats["Home"] = tmpDict
                elif("Road" in subHeader):
                    dictOfStats["Road"] = tmpDict
                elif("Wins" in subHeader):
                    dictOfStats["Wins"] = tmpDict
                elif("Losses" in subHeader):
                    dictOfStats["Losses"] = tmpDict
    return dictOfStats

def getPlayerFromLink(browser, lien) -> Player:
    browser.get(lien)
    sleep(sleepTime)

    #on selectionne l'année 2022-23
    annee = browser.find_element(By.CSS_SELECTOR, '.DropDown_select__4pIg9')
    dropdown_select = Select(annee)
    dropdown_select.select_by_visible_text("2022-23")
    sleep(sleepTime)

    playerTmp = Player()

    #récupération du nom
    nom = browser.find_elements(By.CSS_SELECTOR,".PlayerSummary_playerNameText___MhqC")
    nom = nom[0].text+" "+nom[1].text
    playerTmp.NAME = nom

    #récupération de l'equipe et du poste
    infos_club = browser.find_element(By.CSS_SELECTOR,".PlayerSummary_mainInnerInfo__jv3LO")
    playerTmp.CLUB = re.search(r'^([^|]+)', infos_club.text).group(1).strip()
    playerTmp.POSITION = re.search(r'\| ([^|]+)$', infos_club.text).group(1).strip()

    #récupération de la taille, poids, pays, age et années d'expériences
    infos_perso = browser.find_elements(By.CSS_SELECTOR,".PlayerSummary_playerInfoValue__JS8_v")   
    playerTmp.HEIGHT = re.search(r'(\d+\.\d+)m', infos_perso[0].text).group(1)
    playerTmp.WEIGHT = re.search(r'\((\d+)kg\)', infos_perso[1].text).group(1)
    playerTmp.COUNTRY = infos_perso[2].text
    playerTmp.AGE = infos_perso[4].text.replace(" years","")
    playerTmp.EXPERIENCE = infos_perso[7].text.replace(" Year","").replace("s","")

    liste_tables = browser.find_elements(By.CSS_SELECTOR,".Crom_table__p1iZz")

    stats = getStatsFromTableList(liste_tables)

    playerTmp.setHome(stats["Home"])
    playerTmp.setRoad(stats["Road"])
    playerTmp.setWins(stats["Wins"])
    playerTmp.setLosses(stats["Losses"])

    return playerTmp

def getTeamFromLink(browser, lien) -> Team:
    browser.get("https://www.nba.com/stats/team/"+re.search(r'\d+', lien).group()+"/traditional")
    sleep(sleepTime)

    teamTmp = Team()

    #selection de l'année 2022-23
    annee = browser.find_element(By.CSS_SELECTOR, '.DropDown_select__4pIg9')
    dropdown_select = Select(annee)
    dropdown_select.select_by_visible_text("2022-23")
    sleep(sleepTime)
    
    #récupération du nom de l'équipe
    nom = browser.find_element(By.CSS_SELECTOR,".TeamHeader_name__MmHlP").get_attribute("innerHTML")
    nom = nom.replace("<div>", "")
    nom = nom.replace("<!-- -->&nbsp;", " ")
    nom = nom.replace("</div>", "")
    teamTmp.setName(nom)

    liste_tables = browser.find_elements(By.CSS_SELECTOR,".Crom_table__p1iZz")

    stats = getStatsFromTableList(liste_tables)

    teamTmp.setHome(stats["Home"])
    teamTmp.setRoad(stats["Road"])
    teamTmp.setWins(stats["Wins"])
    teamTmp.setLosses(stats["Losses"])

    return teamTmp

def savePlayersToCSV(CSVName, arrayPlayer):
    with open(CSVName, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=arrayPlayer[0].formatForCSV().keys())
        writer.writeheader()
        for player in arrayPlayer:
            writer.writerow(player.formatForCSV())

def saveTeamsToCSV(CSVName, arrayTeams):
    with open(CSVName, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=arrayTeams[0].formatForCSV().keys())
        writer.writeheader()
        for team in arrayTeams:
            writer.writerow(team.formatForCSV())

def printProgressBar (iteration, total, prefix = '', suffix = '', itterationTime = 1):
    percent = ("{0:." + str(1) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(50 * iteration // total)
    bar = "█" * filledLength + '-' * (50 - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix} estimated at least {itterationTime * (total - iteration)}s left', end = "\r")
    # Print New Line on Complete
    if iteration == total: 
        print()

def __main__():
    print("Scraping NBA players informations for statistics studies\n")

    browser = webdriver.Chrome()

    liste_liens = getListOfPlayersLinks(browser)

    #on crée les clés de notre dictionnaire
    arrayPlayer = []

    #on se rend sur toutes les pages des infos personnels des joueurs
    for i,lien in enumerate(liste_liens):
        printProgressBar(i, len(liste_liens), prefix = 'Retrieving players infos:', suffix = 'Complete', itterationTime=2*sleepTime)
        arrayPlayer.append(getPlayerFromLink(browser, lien))

    print("\n")
    print("Done !")

    #écriture dans un fichier csv
    savePlayersToCSV("nba_players.csv", arrayPlayer)



    print("\n")
    print("Scraping NBA teams informations for statistics studies\n")

    #on se rend sur la page des équipes et on récupère tous les liens d'équipes
    liens_teams = getListOfTeamsLinks(browser)

    #on crée les clés de notre dictionnaire
    arrayTeams = []

    #on se rend sur toutes les pages d'équipes pour récupérer les informations
    for lien in liens_teams:
        printProgressBar(i, len(liste_liens), prefix = 'Retrieving teams infos:', suffix = 'Complete', itterationTime=2*sleepTime)
        arrayTeams.append(getTeamFromLink(browser, lien))

    print("\n")
    print("Done !")

    #écriture dans un fichier csv
    saveTeamsToCSV("nba_teams.csv", arrayTeams)

    print("\n")
    print("Scraping done !")
    browser.close()

if __name__ == "__main__":
    __main__()