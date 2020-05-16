from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import os

# links from games
links = [
        "https://eshop-prices.com/games/1566-super-smash-bros-ultimate?currency=MXN"     ,#Smash
        "https://eshop-prices.com/games/164-mario-kart-8-deluxe?currency=MXN"            ,#Mario Kart
        "https://eshop-prices.com/games/4042-animal-crossing-new-horizons?currency=MXN"  ,#Animal Crossing
        
        "https://eshop-prices.com/games/3226-untitled-goose-game?currency=MXN"           ,#Untitled Goose Game
        "https://eshop-prices.com/games/4296-good-job?currency=MXN"                      ,#Good Job
        "https://eshop-prices.com/games/833-minecraft?currency=MXN"                      ,#Minecraft
        
        "https://eshop-prices.com/games/378-the-legend-of-zelda-breath-of-the-wild?currency=MXN",#Breath of Wild
        "https://eshop-prices.com/games/1209-super-mario-party?currency=MXN"             ,#Mario Party
        "https://eshop-prices.com/games/2583-super-mario-maker-2?currency=MXN"           ,#Mario Maker
        
        "https://eshop-prices.com/games/4228-moving-out?currency=MXN"                    ,#Moving Out
        "https://eshop-prices.com/games/4527-lonely-mountains-downhill?currency=MXN"     ,#Lonely Mountains
        "https://eshop-prices.com/games/236-rocket-league?currency=MXN"                  ,#Rocket League
        
        "https://eshop-prices.com/games/1696-gris?currency=MXN"                          ,#Gris
        "https://eshop-prices.com/games/970-inside?currency=MXN"                         ,#Inside
        "https://eshop-prices.com/games/969-limbo?currency=MXN"                          ,#Limbo
        
        "https://eshop-prices.com/games/231-rime?currency=MXN"                           ,#Rime
        "https://eshop-prices.com/games/1188-undertale?currency=MXN"                     ,#Undertale
        "https://eshop-prices.com/games/932-hollow-knight?currency=MXN"                   #Hollow Knight
        ]

# used x paths
price_xpath = "/html/body/div[2]/div[1]/table/tbody/tr[1]/td[4]"
country_xpath = "/html/body/div[2]/div[1]/table/tbody/tr[1]/td[2]"

# creating Chrome web driver
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome('C:\web_drivers\chromedriver.exe', options=chrome_options)
driver.minimize_window()
WebDriverWait(driver, 3)
os.system('cls')

# display game prices
counter = 0
for link in links:
    # get link
    driver.get(link)
    wait = WebDriverWait(driver, 5)
    
    # get game attributes using xpath
    game_price = driver.find_element(By.XPATH, price_xpath).text.replace("\n"," -> ")
    game_title = driver.title[0:-34]
    game_country = driver.find_element(By.XPATH, country_xpath).text
    
    # display each game information
    print("%-40s %-15s %-5s" % (game_title, game_country, game_price))
    
    # display a visual aid to check games
    if(counter >= 2):
        print("-------")
        counter = -1
    counter += 1

# close driver
driver.close()
