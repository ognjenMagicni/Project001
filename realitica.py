from scrap import Init, By
import time

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
pages = 5
cityFilter = [Podgorica,Podgorica_Okolina]
propertyFilter = [Apartment]
minPrice = 25000
maxPrice = 75000
global globalPropertyInfo
globalPropertyInfo = []

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

def getSpecificInfoProperty(price,location):
        priceList = []
        locationList = []

        priceInfo = price.split(",")
        priceList.append(string_to_int(priceInfo[0]))
        if len(priceInfo)>1:
            priceList.append(string_to_int(priceInfo[1])//10)
        else:
            priceList.append(undefined)
        if len(priceInfo)>2:
            priceList.append(string_to_int(priceInfo[2]))
        else:
            priceList.append(undefined)

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
        if startingDiv==45:
            startingDiv+=2
        print(startingDiv)

        property = all[startingDiv]
        infoProperty = property.find_elements(By.TAG_NAME,"div")[2]
        
        stringInfoProperty = infoProperty.text.split("\n")
        price = stringInfoProperty[1]
        location = stringInfoProperty[2]

        priceList,locationList = getSpecificInfoProperty(price,location)

        globalPropertyInfo.append([priceList,locationList])

        startingDiv+=addDiv
        if startingDiv >83:
            break

def nextPage():
    orientationButtons = driver.find_elements(By.CLASS_NAME,"bt_pages")
    action.click(orientationButtons[len(orientationButtons)-1]).perform()



functionCityFilter(cityFilter)
functionPriceFilter(minPrice,maxPrice)
functionProperyFilter(propertyFilter)
clickSearch()

for i in range(pages):
    gatherProperties()
    nextPage()

print(len(globalPropertyInfo))
print(globalPropertyInfo)

time.sleep(100)
driver.quit()