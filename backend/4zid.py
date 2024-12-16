import selenium
import scrap
from scrap import By,XpathAnd,repeatUntilSuccess
import time
import json
import pymysql

###VARIABLES
CITY = 'Novi Sad'
MinPrice = 20000
MaxPrice = 5000000
MinSquare, MaxSquare = 10,500
jsonFile = 'jsonFolder/file1.jsonl'

driver, action = scrap.Init("https://www.4zida.rs/prodaja-stanova")
            
def writeTown_Input():
    town = driver.find_element(By.XPATH,XpathAnd("peer flex h-11 w-full rounded border border-neutral-400 px-3 py-2 text-sm transition-colors file:border-0 file:text-sm file:font-medium invalid:border-highlight invalid:text-highlight hover:border-neutral-700 hover:invalid:border-highlight focus:invalid:border-highlight focus-visible:border-2 focus-visible:border-primary focus-visible:outline-none disabled:cursor-not-allowed disabled:opacity-50 pl-9"))
    town.click()
    town.send_keys(CITY)

def findDropDownMenuForTown_Input():
    dropdownVar = driver.find_element(By.XPATH,XpathAnd("border bg-white text-card-foreground relative"))
    return dropdownVar

def clickNoviSad(dropdown):
    dropdown.find_element(By.CLASS_NAME,"text-sm").click()

def priceSquare_Input(minPriceInput,maxPriceInput,minSquareInput,maxSquareInput):
    a = driver.find_elements(By.XPATH,XpathAnd("peer flex h-11 w-full rounded border border-neutral-400 px-3 py-2 text-sm transition-colors file:border-0 file:text-sm file:font-medium invalid:border-highlight invalid:text-highlight hover:border-neutral-700 hover:invalid:border-highlight focus:invalid:border-highlight focus-visible:border-2 focus-visible:border-primary focus-visible:outline-none disabled:cursor-not-allowed disabled:opacity-50 placeholder:text-transparent"))
    minPrice = a[0]
    maxPrice = a[1]
    minSquare = a[2]
    maxSquare = a[3]
    minPrice.click()
    minPrice.send_keys(str(minPriceInput))
    maxPrice.click()
    maxPrice.send_keys(str(maxPriceInput))
    minSquare.click()
    minSquare.send_keys(str(minSquareInput))
    maxSquare.click()
    maxSquare.send_keys(str(maxSquareInput))

def searchClick_Input():
    search = driver.find_element(By.XPATH,XpathAnd("inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed bg-primary text-primary-foreground hover:bg-primary/90 focus-visible:bg-primary/80 disabled:bg-primary-300 px-4 py-2 group col-span-4 h-full space-x-2"))
    search.click()

def processLocation_Process(locationFirst,locationSecond):
    location = {"location":[]}
    location['location'].append(locationFirst.strip())
    
    locationSecondTokens = locationSecond.split(", ")
    if "Gradske lokacije" in locationSecondTokens:
        locationSecondTokens.remove("Gradske lokacije")
    
    for loc in locationSecondTokens:
       location['location'].append(loc)

    return location

def processPrice_Process(fullPrice,squarePrice):
    fullPriceTokens = ''
    squarePriceTokens = ''
    if squarePrice==None:
        fullPriceTokens = None
        squarePriceTokens = None
    else:
        fullPriceTokens = int(float(fullPrice.split('&')[0])*1000)
        squarePriceTokens = int(float(squarePrice.split("&")[0])*1000)
    
    price = {"Full price":fullPriceTokens,"square Price":squarePriceTokens}
    
    return price

def processSquareRoom_Process(squareRoom):
    squareRoomTokens = squareRoom.split(" | ")
    squareRoomTokens[0] = int(squareRoomTokens[0].split("m")[0])
    squareRoomTokens[1] = float(squareRoomTokens[1].split(" ")[0])
    
    squareRoom = {"Square metres":squareRoomTokens[0],"Rooms":squareRoomTokens[1]}
    return squareRoom

def processSearchInformation_Process(locationFirst,locationSecond,fullPrice,squarePrice,squareRoom):
    location = processLocation_Process(locationFirst,locationSecond)
    price = processPrice_Process(fullPrice, squarePrice)
    squareRoom = processSquareRoom_Process(squareRoom)

    dict = {}
    dict.update(location)
    dict.update(price)
    dict.update(squareRoom)
    return dict

def preprocessSearchInformation_Process(locationPrice,squareRoomLink):    #p -> locationPrice, a->quareRoomLink
    argument1 = []
    for i in locationPrice:
        argument1.append(i.get_attribute("innerHTML"))

    argument2 = []
    argument2.append(squareRoomLink[1].get_attribute("innerHTML"))
    argument2.append(squareRoomLink[1].get_attribute("href"))

    #There is a chance instead of full and square price to get just price query, hence this if handles this problem
    result = {}
    if len(argument1)==4:                                                                                              
        result = processSearchInformation_Process(argument1[0],argument1[1],argument1[2],argument1[3],argument2[0])
    else:
        result = processSearchInformation_Process(argument1[0],argument1[1],argument1[2],None,argument2[0])
    
    result.update({'Link':argument2[1]})

    return result

def writeDataJSONL_Process(data,file):
    json.dump(data,file,ensure_ascii=False)
    file.write('\n')
    
def writeDatabase():
    conn = pymysql.connect(host = "localhost", user="root", password="Laptop1*", database="properties" )

    try:
        title = "title"
        description = 'description'
        cursor = conn.cursor()
        query = "INSERT INTO properties.search(price_min,price_max,square_min,Square_max,date,title,description) VALUES(%s,%s,%s,%s,CURDATE(),%s,%s)"
        values = (MinPrice,MaxPrice,MinSquare,MaxSquare,title,description)
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


def pickUpAllProperties():
    file = open(jsonFile,'a',encoding='utf-8')
    estates = driver.find_elements(By.XPATH,XpathAnd("flex w-2/3 flex-col justify-between py-2"))
    
    for e in estates:
        p = e.find_elements(By.TAG_NAME,"p")    #ovo vraca ['Klisa'   'Gradska lokacija,novi sad'  84000    2000]
        a = e.find_elements(By.TAG_NAME,"a")                #[neka glupost         63m2,1.5 soba]
        
        estate = preprocessSearchInformation_Process(p,a)
        writeDataJSONL_Process(estate,file)

    writeDatabase():
def removeCookieWindow():
    boringCookieButton = driver.find_element(By.XPATH,XpathAnd("inline-flex items-center justify-center whitespace-nowrap rounded-md font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed bg-highlight text-white hover:bg-highlight/90 focus-visible:bg-highlight/80 disabled:bg-gray-300 text-md h-7 border-0 px-2 py-1"))
    boringCookieButton.click()
        
def clickNextPage():
    time.sleep(5)
    navigationBar = driver.find_element(By.XPATH,XpathAnd("mx-auto flex w-max items-center justify-center overflow-clip rounded-md shadow-md"))
    buttonsInNavigationBar = navigationBar.find_elements(By.TAG_NAME,'a')
    for i,button in enumerate(buttonsInNavigationBar):
        if i==0:
            continue
        if button.text=="":
            button.click()
            return True
    return False        

def runAndScrapeWebSite():

    repeatUntilSuccess(writeTown_Input,[])
    time.sleep(3)
    dropdown = repeatUntilSuccess(findDropDownMenuForTown_Input,[])
    repeatUntilSuccess(clickNoviSad,[dropdown])

    repeatUntilSuccess(priceSquare_Input,[MinPrice,MaxPrice,MinSquare,MaxSquare])
    repeatUntilSuccess(removeCookieWindow,[])
    repeatUntilSuccess(searchClick_Input,[])

    variable = True
    while variable:
        time.sleep(5)
        pickUpAllProperties()
        variable = repeatUntilSuccess(clickNextPage,[])
            
runAndScrapeWebSite()

driver.quit()