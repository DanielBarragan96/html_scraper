from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import os

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')

driver = webdriver.Chrome('C:\web_drivers\chromedriver.exe', options=chrome_options)
#driver.minimize_window()
#os.system('cls')

games = [
		"Smash",
		"Mario Kart",
		"Animal Crossing"
		]

links = [
		"https://eshop-prices.com/games/1566-super-smash-bros-ultimate?currency=MXN"	,#Smash
		"https://eshop-prices.com/games/164-mario-kart-8-deluxe?currency=MXN"			,#Mario Kart
		"https://eshop-prices.com/games/4042-animal-crossing-new-horizons?currency=MXN"	 #Animal Crossing
		]

price_xpath = "/html/body/div[2]/div[1]/table/tbody/tr[1]/td[4]"

for index in range(len(links)):
	driver.get(links[index])
	# wait 10 seconds
	wait = WebDriverWait(driver, 10)
	game_price = wait.until(EC.visibility_of_element_located((By.XPATH, price_xpath)))
	print(games[index] + " = " + game_price.text)

driver.close()
