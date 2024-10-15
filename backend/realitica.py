from scrap import Init, By
import time
from graph import drawGraph
import pymysql

###CONSTANTS
global undefined
undefined = -99
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
pages = 20
cityFilter = []
propertyFilter = []
minPrice = 25000
maxPrice = 75000
title = ''
description = ''

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

def upgradeConfiguration(priceList):
    global minPriceLog
    global maxPriceLog
    global minSquareLog
    global maxSquareLog
    if priceList[1]<minSquareLog and priceList[1]!=-99:
        minSquareLog = priceList[1]
    if priceList[1]>maxSquareLog and priceList[1]!=-99:
        maxSquareLog = priceList[1]
    if priceList[2]<minPriceLog and priceList[2]!=-99:
        minPriceLog = priceList[2]
    if priceList[2]>maxPriceLog and priceList[2]!=-99:
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
        
def gatherProperties():
    startingDiv = 5
    addDiv = 4
    div = driver.find_element(By.ID,"left_column_holder")
    all = div.find_elements(By.TAG_NAME,"div")
    
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

        globalPropertyInfo.append([priceList,locationList,link])

        startingDiv+=addDiv
        if startingDiv >83:
            break

def nextPage():
    orientationButtons = driver.find_elements(By.CLASS_NAME,"bt_pages")
    action.click(orientationButtons[len(orientationButtons)-1]).perform()


def run():
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



    conn = pymysql.connect(host = "localhost", user="root", password="Laptop1*", database="properties" )

    try:
        global title
        global description
        cursor = conn.cursor()
        query = "INSERT INTO properties.search(price_min,price_max,square_min,Square_max,date,title,description) VALUES(%s,%s,%s,%s,CURDATE(),%s,%s)"
        values = (minPriceLog,maxPriceLog,minSquareLog,maxSquareLog,title,description)
        cursor.execute(query,values)
        conn.commit()
        id = cursor.lastrowid

        for property in globalPropertyInfo:
            query = "INSERT INTO properties.property(fk_search,no_room,square,price,location,city,country,link,on_off) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            values = (id,property[0][0],property[0][1],property[0][2],property[1][0],property[1][1],property[1][2],property[2],1)
            cursor.execute(query,values)
            conn.commit()

    except pymysql.MySQLError as e:
        print(f"Error: {e}")
        conn.rollback()

    print(len(globalPropertyInfo))
    print(globalPropertyInfo)
    #drawGraph(globalPropertyInfo)

    #time.sleep(1000) 
    driver.quit()