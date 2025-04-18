import sys
sys.path.insert(0,'libraries')

from scrap import Init, By
import time
import pymysql
import json
from process import realiticaProcessData
import time
import pymysqlpool
from mysqlwrapper import insertBackend

###CONSTANTS
global undefined
undefined = None
Andrijevica = 'Andrijevica'
Bar = 'Bar'
Berane = 'Berane'
Bijelo_Polje = 'Bijelo Polje'
Budva = 'Budva'
Cetinje = 'Cetinje'
Danilovgrad = 'Danilovgrad'
Kolašin = 'Kolašin'
Kotor = 'Kotor'
Mojkovac = 'Mojkovac'
Nikšić = 'Nikšić'
Plav = 'Plav'
Pljevlja = 'Pljevlja'
Plužine = 'Plužine'
Rožaje = 'Rožaje'
Šavnik = 'Šavnik'
Tivat = 'Tivat'
Ulcinj = 'Ulcinj'
Žabljak = 'Žabljak'
Budva_Okolina = 'Budva Okolina'
Herceg_Novi = 'Herceg Novi'
Podgorica = 'Podgorica'
Podgorica_Okolina = 'Podgorica Okolina'

Home = 'Home'
Apartment = 'Apartment'
Land = 'Land'
Commercial = 'Commercial'
Hotel = 'Hotel'
Residential_lot = 'Residential_lot'
Agricultural_land = 'Agricultural_land'
Campground = 'Campground'
Garage = 'Garage'


###Variables 
pages = 2
cityFilter = []
propertyFilter = []
minPrice = 20000
maxPrice = 5000000
title = 'Danilovgrad'
description = 'Svi stanovi u Danilovgradu'
fileJSONL = 'jsonFolder/file2.jsonl'

global globalPropertyInfo
globalPropertyInfo = []

minPriceLog = 100000000
maxPriceLog = 0
minSquareLog = 3000
maxSquareLog = 0

driver, action = Init("https://www.realitica.com/nekretnine/Crna-Gora/")

def format_string(city_name):
    variable_name = city_name.replace(' ', '_')
    result = f"{variable_name} = '{city_name}'"
    return result

def string_to_int(input_string):
    digits = ''.join([char for char in input_string if char.isdigit()])
    return int(digits)

def functionCityFilter(cityFilter):
    all = driver.find_element(By.ID,"xc241")
    inputAll = all.find_element(By.TAG_NAME,"input")
    action.click(inputAll).perform()

    allCities = all.find_elements(By.ID,"search_col2_half")
    allCities = allCities + all.find_elements(By.ID,"search_col2_full")

    for city in allCities:
        input = city.find_element(By.TAG_NAME,"input")
        cityName = input.get_attribute("value")
        if cityName in cityFilter:
            action.click(input).perform()

def functionPriceFilter(minPrice,maxPrice):
    priceButton = driver.find_element(By.ID,"price-label")
    action.click(priceButton).perform()
    time.sleep(1)

    priceInputs = driver.find_element(By.CLASS_NAME,"inner ").find_elements(By.TAG_NAME,"input")
    priceInputs[0].send_keys(str(minPrice))
    priceInputs[1].send_keys(str(maxPrice))

def functionProperyFilter(propertyFilter):
    all = driver.find_element(By.ID,"types_div")
    allInputs = all.find_elements(By.TAG_NAME,"input")

    action.click(allInputs[0]).perform()

    for input in allInputs:
        propertyName = input.get_attribute("value")
        if propertyName in propertyFilter:
            action.click(input).perform()

def clickSearch():
    button = driver.find_element(By.TAG_NAME,"button")
    action.click(button).perform()
    time.sleep(1)

def upgradeConfiguration(priceList):
    global minPriceLog
    global maxPriceLog
    global minSquareLog
    global maxSquareLog
    if priceList[1]!=None and priceList[1]<minSquareLog:
        minSquareLog = priceList[1]
    if priceList[1]!=None and priceList[1]>maxSquareLog:
        maxSquareLog = priceList[1]
    if priceList[2]!=None and priceList[2]<minPriceLog:
        minPriceLog = priceList[2]
    if priceList[2]!=None and priceList[2]>maxPriceLog:
        maxPriceLog = priceList[2]


def getSpecificInfoProperty(price,location):
        priceList = [undefined,undefined,undefined]
        locationList = []

        priceInfo = price.split(",")

        for word in priceInfo:
            if "sobe" in word:
                priceList[0]=string_to_int(word)
            if "m" in word:
                priceList[1]=string_to_int(word)//10
            if "€" in word:
                priceList[2]=string_to_int(word)

        locationInfo = location.split(",")
        locationList.append((locationInfo[0]))
        if len(locationInfo)>1:
            locationList.append((locationInfo[1]))
        else:
            locationInfo.append(undefined)
        if len(locationInfo)>2:
            locationList.append((locationInfo[2]))
        else:
            locationList.append(undefined)

        return priceList,locationList

def writeDataJSONL(data,file):
    json.dump(data,file,ensure_ascii=False)
    file.write('\n')

def setRightLocationCityCountry(location,city,country):
    if country == None:
        country = city
        city = location
        location = None
    return location,city,country

def upgradeConfigurationLocation(locationList):
    location,city, country = setRightLocationCityCountry(locationList[0],locationList[1],locationList[2])
    return [location,city,country]

def preprocessSearchInformation(propertyInfoList):

    Rooms = propertyInfoList[0][0]
    Square_metres = propertyInfoList[0][1]
    Full_price = propertyInfoList[0][2]
    location = propertyInfoList[1][0]
    city = propertyInfoList[1][1]
    country = propertyInfoList[1][2]
    link = propertyInfoList[2]

    location,city,country = setRightLocationCityCountry(location,city,country)

    propertyDictionary = {
        "location":location,
        "city":city,
        "country":country,
        "full price":Full_price,
        "square metres":Square_metres,
        "square price":int(Full_price/Square_metres) if Square_metres!=None else None,
        "rooms":Rooms,
        "link":link
    }

    return propertyDictionary

def proccesAndJsonl(propertyInfoList,file):
    propertyDictionary = preprocessSearchInformation(propertyInfoList)
    writeDataJSONL(propertyDictionary,file)

def gatherProperties():
    startingDiv = 5
    addDiv = 4
    div = driver.find_element(By.ID,"left_column_holder")
    all = div.find_elements(By.TAG_NAME,"div")
    
    #file = open(fileJSONL,'a',encoding='utf-8')

    while True:
        

        property = all[startingDiv]

        if property.get_attribute("class")=="responsive_left_LB":
            startingDiv+=2

        property = all[startingDiv]

        if not "padding: 15px 10px" in property.get_attribute("style"):
            break
        link = property.find_element(By.TAG_NAME,"a").get_attribute("href")

        infoProperty = property.find_elements(By.TAG_NAME,"div")[2]
        
        stringInfoProperty = infoProperty.text.split("\n")
        price = stringInfoProperty[1]
        location = stringInfoProperty[2]

        priceList,locationList = getSpecificInfoProperty(price,location)

        upgradeConfiguration(priceList)
        locationList = upgradeConfigurationLocation(locationList)

        globalPropertyInfo.append([priceList,locationList,link])

        #proccesAndJsonl([priceList,locationList,link],file)

        startingDiv+=addDiv
        if startingDiv >83:
            break
    #file.close()

def nextPage():
    orientationButtons = driver.find_elements(By.CLASS_NAME,"bt_pages")
    action.click(orientationButtons[len(orientationButtons)-1]).perform()


def runWebScrape(id_search):
    functionCityFilter(cityFilter)
    functionPriceFilter(minPrice,maxPrice)
    functionProperyFilter(propertyFilter)
    clickSearch()

    for i in range(pages):
        gatherProperties()
        try:
            buttons = driver.find_elements(By.CLASS_NAME,"bt_pages_ghost")
            if len(buttons)==4:
                break
            if i==0:
                raise Exception
            driver.find_element(By.CLASS_NAME,"bt_pages_ghost")
            break
        except(Exception):
            pass
        nextPage()


    try:
        pool = pymysqlpool.ConnectionPool(host = "localhost", user="root", password="simple", database="properties")
    
        global title
        global description
        #cursor = conn.cursor()

        for property in globalPropertyInfo:
            if property[0][2]<10 and property[0][2]>450:
                continue
            query = "INSERT INTO properties.property(fk_search,no_room,square,price,location,city,country,link,on_off,square_price) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            values = (id_search,property[0][0],property[0][1],property[0][2],property[1][0],property[1][1],property[1][2],property[2],1,property[0][2]/property[0][1] if property[0][1]!=None else None)
            insertBackend(pool,query,values)
            #cursor.execute(query,values)
            #conn.commit()
        
    except pymysql.MySQLError as e:
        print(f"Error: {e}")

    print(f'Scrape was successful with {len(globalPropertyInfo)} real estates gathered')
    #drawGraph(globalPropertyInfo)

    #time.sleep(1000) 
    driver.quit()

def getSearch():
    pool = pymysqlpool.ConnectionPool(host = 'localhost', user='root', password='simple', database='properties')
                
    global title
    global description
    #cursor = conn.cursor()
    query = "INSERT INTO properties.search(price_min,price_max,square_min,Square_max,date,title,description) VALUES(%s,%s,%s,%s,CURDATE(),%s,%s)"
    values = (minPriceLog,maxPriceLog,minSquareLog,maxSquareLog,title,description)
    #cursor.execute(query,values)
    #conn.commit()
    id = insertBackend(pool,query,values)
    
    return id

def run():
    try:
        id_search = getSearch()
        print(id_search)
        runWebScrape(id_search)
        driver.quit()
    except Exception as e: 
        print(f"An error occurred in realitica.py in function run: {e}")
        print("PROCESS IS GOING ON")
        driver.quit()
    realiticaProcessData(id_search)
