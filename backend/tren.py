import selenium
import scrap
from scrap import By,XpathAnd,repeatUntilSuccess
import time
import json

###VARIABLES
CITY = 'Novi Sad'
MinPrice = 50000
MaxPrice = 150000
MinSquare, MaxSquare = 25,70

driver, action = scrap.Init("https://www.4zida.rs/prodaja-stanova/novi-sad")

el = driver.find_element(By.XPATH,"//path[@d='m9 18 6-6-6-6']")
el.click()
time.sleep(10)