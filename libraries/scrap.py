from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def Init(webAddress):
    
    path = "C:\webdrivers\chromedriver.exe"
    cService = webdriver.ChromeService(executable_path=path)
    driver = webdriver.Chrome(service=cService)
    driver.get(webAddress)
    driver.maximize_window()
    action = ActionChains(driver)

    return driver,action

def XpathAnd(stringOfClasses):
    stringOfClasses = stringOfClasses.split(" ")
    string = "//*["

    for className in stringOfClasses:
        string+=f" contains(@class, '{className}') "
        string+=" and "
    
    return string[:len(string)-5]+"]"

def repeatUntilSuccess(fun,args):
    for i in range(10):
        try:
            x = fun(*args)
            print("Success")
            return x
        except:
            print(f"{i}th time error")
            time.sleep(5)

def scroll(driver,numberOfPixels):
    driver.execute_script(f"window.scrollTo(0, {numberOfPixels});")