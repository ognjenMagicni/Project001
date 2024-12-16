import json
import pandas as pd

###VARIABLE
inputJsonFile = 'file1.jsonl'
outputJsonFile = 'proccessedFile1.jsonl'


df = pd.read_json(inputJsonFile,lines=True)


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

processData()


