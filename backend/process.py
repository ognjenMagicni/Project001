import sys
sys.path.insert(0,r'C:\Users\Asus\Desktop\Ognjen\Programiranje\Stanovi\python\Project001\libraries')

import json
import pandas as pd
from scrap import Init,By,repeatUntilSuccess
import re
import time
from mysqlwrapper import selectQuery,updateQuery
import pymysql




###CODE
def locationCount():
    locationCount = {}
    for i in range(df.shape[0]):
        listOfLocations = df.loc[i, 'location']
        for location in listOfLocations:
            if location in locationCount:
                locationCount[location] = locationCount[location] + 1
            else:
                locationCount[location] = 1

    return dict(sorted(locationCount.items(), key=lambda item: item[1], reverse=True))

def setListOfSettlements():
    sortedLocationCount = locationCount()
    listOfSettlements = []
    for k,v in sortedLocationCount.items():
        if k=='Novi Sad':
            continue
        if v>10:
            listOfSettlements.append(k)
    listOfSettlements.append('Sajlovo')
    return listOfSettlements


def mapManyToOneLocations(estateDictionary,listOfSettlements):
        if any(settlement in estateDictionary['location'] for settlement in listOfSettlements):
            for settle in listOfSettlements:
                if settle in  estateDictionary['location']:
                    estateDictionary['location'] = settle
        elif 'Novi Kvart' in estateDictionary['location']:
                estateDictionary['location'] = 'Veternik'
        elif 'Futoška' in estateDictionary['location']:
                estateDictionary['location'] = 'Grbavica'
        elif 'NOVELLA Business &amp; Residence' in estateDictionary['location']:
                estateDictionary['location'] = 'Telep'
        elif 'Mali Beograd' in estateDictionary['location']:
                estateDictionary['location'] = 'Klisa'
        elif 'Futoški Put' in estateDictionary['location']:
                estateDictionary['location'] = 'Telep'
        elif 'Kamenjar' in estateDictionary['location']:
                estateDictionary['location'] = 'Adice'
        elif 'Slana Bara' in estateDictionary['location']:
             estateDictionary['location'] = 'Adice'
        elif 'Vidovdansko Naselje' in estateDictionary['location']:
             estateDictionary['location'] = 'Adice'
        else:
            return False
        return True

def processData():
    listOfSettlements = setListOfSettlements()
    f = open(inputJsonFile,'r',encoding='utf-8')
    allLines = f.readlines()

    err = 0
    proccessedFile = open(outputJsonFile,'a',encoding='utf-8')
    for i,line in enumerate(allLines):
        estateDictionary = json.loads(line)

        if not mapManyToOneLocations(estateDictionary,listOfSettlements):
            err+=1
            print(estateDictionary)

        estateDictionary['city'] = 'Novi Sad'

        json.dump(estateDictionary,proccessedFile,ensure_ascii=False)
        proccessedFile.write('\n')

    print("Total errors are",err)

def locationCount(properties):
    locationCount = {}
    for i in range(properties.shape[0]):
        listOfLocations = properties.loc[i, 'location']
        for location in listOfLocations:
            if location in locationCount:
                locationCount[location] = locationCount[location] + 1
            else:
                locationCount[location] = 1

    return dict(sorted(locationCount.items(), key=lambda item: item[1], reverse=True))

def setListOfSettlements(properties):
    sortedLocationCount = locationCount(properties)
    listOfSettlements = []
    for k,v in sortedLocationCount.items():
        if k=='Novi Sad':
            continue
        if v>10:
            listOfSettlements.append(k)
    listOfSettlements.append('Sajlovo')
    return listOfSettlements

def updateLocation(id_property,location):
     updateQuery("UPDATE properties.property SET location = %s WHERE id_property = %s",(location,id_property))
     print('Update is executed for id:',id_property)

def updateCity(id_property,city):
    updateQuery("UPDATE properties.property SET city = %s WHERE id_property = %s",(city,id_property))

def updateCountry(id_property,country):
    updateQuery("UPDATE properties.property SET country = %s WHERE id_property = %s",(country,id_property))

def propertyLocationCityCountry(id_property):
    settlements = selectQuery("SELECT settlement FROM properties.settlements4zid WHERE fk_property=%s",(id_property,))
    if len(settlements)<2:
        print(f"Property with id {id_property} has less than 2 settlements")
        return
    lastSettlement = settlements[-1][0]
    preLastSettlement = settlements[-2][0]
    updateLocation(id_property,preLastSettlement)
    updateCity(id_property,lastSettlement)
    updateCountry(id_property,'Serbia')
    

def extractData4zid(search_id):
    property = selectQuery("SELECT id_property FROM properties.property WHERE fk_search = %s", (search_id,))
    return property

def zidProcessData(id_search):  
    properties = extractData4zid(id_search)
    for property in properties:
        id_property = property[0]
        propertyLocationCityCountry(id_property)


def updatePropertySquarePrice(conn,item):
    squareMetres = item[3]
    squarePrice = item[11]
    id_property = item[0]
    cursor = conn.cursor()
    query = "UPDATE properties.property SET square = %s, square_price = %s WHERE id_property = %s"
    values = (squareMetres,squarePrice,id_property)
    cursor.execute(query,values)
    conn.commit()
    cursor.close()
    print("Update query is executed for id property:",id_property)

def realiticaCorrectionOfSquarePrice(driver,item,conn,moreThanOneMatches,didNotDoAssignment):
    driver.get(item[8])
    time.sleep(3)
    descriptionProperty = None

    for i in range(5):
        try:
            descriptionProperty = driver.find_element(By.ID,'listing_body')
            break
        except Exception as e:
            print(f"An error occurred with id {item[0]} at link {item[8]}, following error is: {e}")
            time.sleep(1)

        if i==4:
            didNotDoAssignment.append((item[0],item[8]))
            return

    pattern = r"\d+(?:\.\d+)?(?=\s?m)"
    matches = re.findall(pattern, descriptionProperty.text)

    if len(matches)>1:
        moreThanOneMatches.append((item[0],item[8]))
    try:
        realSquareMetres = int(float(matches[0]))
        item[3] = realSquareMetres
        item[11] = int(item[4] / realSquareMetres)
        
        updatePropertySquarePrice(conn,item)

    except Exception as e:
        print(f"An error occurred: {e}")
        didNotDoAssignment.append((item[0],item[8]))
        return

    

def extractIncorrectSquarePriceProperty(search_id):
    conn = pymysql.connect(host = "localhost", user="root", password="Laptop1*", database="properties" )
    cursor = conn.cursor()
    query = "SELECT * FROM properties.property WHERE (square_price < 0 or square_price IS NULL) and fk_search = %s"
    values = (search_id,)
    cursor.execute(query,values)
    result = cursor.fetchall()
    conn.close()
    return result

def realiticaProcessData(id_search):
    moreThanOneMatches = []
    didNotDoAssignment = []

    global df
    properties = extractIncorrectSquarePriceProperty(id_search)
    
    driver, action = Init('https://www.realitica.com')
    conn = pymysql.connect(host = "localhost", user="root", password="Laptop1*", database="properties" )

    numberOfProperties = len(properties)
    for index,item in enumerate(properties):
        realiticaCorrectionOfSquarePrice(driver,list(item),conn,moreThanOneMatches,didNotDoAssignment)
        print(f"Processed {index+1}/{numberOfProperties} properties")

    conn.close()

    for item in moreThanOneMatches:
        print('There is more than one match for property with id:',item[0],'at link:',item[1])
    for item in didNotDoAssignment:
         print('Did not do assignment for property with id',item[0] ,'at link:', item[1])


