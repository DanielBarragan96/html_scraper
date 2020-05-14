from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import os

links = [
        "https://eshop-prices.com/games/1566-super-smash-bros-ultimate?currency=MXN"     ,#Smash
        "https://eshop-prices.com/games/164-mario-kart-8-deluxe?currency=MXN"            ,#Mario Kart
        "https://eshop-prices.com/games/4042-animal-crossing-new-horizons?currency=MXN"   #Animal Crossing
        ]

price_xpath = "/html/body/div[2]/div[1]/table/tbody/tr[1]/td[4]"

chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome('C:\web_drivers\chromedriver.exe', options=chrome_options)
driver.minimize_window()
WebDriverWait(driver, 3)
os.system('cls')

for link in links:
    driver.get(link)
    wait = WebDriverWait(driver, 5)
    game_price = driver.find_element(By.XPATH, price_xpath)
    game_title = driver.title[0:-34]
    print(game_title + " = " + game_price.text)

driver.close()
