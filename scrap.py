from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def Init(webAddress):
    
    path = "C:\webdrivers\chromedriver.exe"
    cService = webdriver.ChromeService(executable_path=path)
    driver = webdriver.Chrome(service=cService)
    driver.get(webAddress)

    action = ActionChains(driver)

    return driver,action

def XpathAnd(listOfClasses):
    listOfClasses = listOfClasses.split(" ")
    string = "//*["

    for className in listOfClasses:
        string+=f" contains(@class, '{className}') "
        string+=" and "
    
    return string[:len(string)-5]+"]"

def scroll(driver,numberOfPixels):
    driver.execute_script(f"window.scrollTo(0, {numberOfPixels});")