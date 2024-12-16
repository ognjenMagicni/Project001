import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_json('proccessedFile1.jsonl',lines=True)


def histogramOfLocations():
    location_counts = df['location'].value_counts()
    plt.figure(figsize=(10, 6))
    plt.bar(location_counts.index, location_counts.values, color='skyblue', edgecolor='black')
    plt.title('Counts of Locations', fontsize=16)
    plt.xlabel('Location', fontsize=14)
    plt.ylabel('Count', fontsize=14)
    plt.xticks(rotation=90, fontsize=12)
    plt.tight_layout()
    plt.show()

def distibutionOfSquarePrices():
    location_counts = df['square Price']
    plt.figure(figsize=(10, 6))
    plt.hist(location_counts.values,np.arange(0,5000,250),edgecolor='black')
    plt.title('Distibution of square prices', fontsize=16)
    plt.xlabel('Square price', fontsize=14)
    plt.ylabel('Quantity', fontsize=14)
    plt.show()

def dataOfSettlements():
    statDataSettlement = {}
    uniqueLocations = df['location'].unique()
    for location in uniqueLocations:
        statDataSettlement[location] = {}

        descriptionOdLocations = df.loc[ df['location']==location ].describe()
        for column in descriptionOdLocations:
            count = descriptionOdLocations.loc['count',column]
            mean = descriptionOdLocations.loc['mean',column]
            median = descriptionOdLocations.loc['50%',column]
            statDataSettlement[location][column] = {'count':count,'mean':mean,'median':median}

    return statDataSettlement

def distributionByLocations(sortArgument = ('square Price','count'),argument = 'square Price', range = (0,5000,250)):    #0,5000,250
    locationData = dataOfSettlements()

    locationData = dict(
    sorted(locationData.items(), key=lambda item: item[1]['square Price']['count'], reverse=True)
    )

    i=1
    plt.figure(figsize=(17, 17))
    for k,v in locationData.items():
        plt.subplot(3,3,i)
        locationEstate = df.loc[ df['location']==k]
        locationEstateSquarePrice = locationEstate[argument]
        plt.hist(locationEstateSquarePrice.values,np.arange(*range),edgecolor='black')
        plt.title(k)
        plt.xlabel('Square price')
        plt.ylabel('Quantity')
        i+=1
        if i==10:
            plt.subplots_adjust(left=0.1,
                            bottom=0.1, 
                            right=0.9, 
                            top=0.9,
                            wspace=0.4, 
                            hspace=0.4)
            plt.show()
            plt.figure()
            i=1

def compareTwoLocations(location1,location2):
    data1 = df.loc[ df['location']==location1,'square Price' ]
    data2 = df.loc[ df['location']==location2,'square Price' ]

    plt.hist(data1,np.arange(0,5000,250),edgecolor='black',alpha=0.4)
    plt.hist(data2,np.arange(0,5000,250),edgecolor='black',alpha=0.4)
    plt.show()

def ratioFullPriceSquare(squareMetrePriceLine = False,fullPriceLine = False,locationList = None):
    newDf = [df]
    if locationList!=None:
        newDf.pop()
        for location in locationList:
            newDf.append( df.loc[ df['location']==location ]  )

    x = np.arange(0,300,10)
    y =np.arange(0,300000,10000)
    y2 = np.arange(0,600000,20000)
    y3 = np.arange(0,900000,30000)

    colors = ('blue','yellow','cyan','magenta')
    for i,location in enumerate(newDf):
        plt.scatter(location['Square metres'],location['Full price'],color = colors[i],label=locationList[i] if locationList != None else 'Novi Sad')

    if squareMetrePriceLine:
        plt.plot(x,y,color='green',label='1000 epsq')
        plt.plot(x,y2,color='brown',label='2000 epsq')
        plt.plot(x,y3,color='red',label='3000 epsq')

    if fullPriceLine:
        fullPriceList = [50000,100000,150000,200000,250000,300000]
        for price in fullPriceList:
            plt.plot(np.arange(0,300,10),[price]*30,color='black')

    plt.title('Distribution of full and square price')
    plt.legend()
    plt.show()

def distributionOfSquarePriceBasedOnSquareMetres(range = (0,5000,250)):
    squareMetres = [(0,30),(30,40),(40,50),(50,70),(70,100),(100,150),(150,500)]

    i=1
    plt.figure(figsize=(17, 17))
    for leftSquare,rightSquare in squareMetres:
        plt.subplot(3,3,i)
        propertyBySquareMetres = df.loc[ (df['Square metres']>leftSquare) & (df['Square metres']<rightSquare)]
        propertyDistribution = propertyBySquareMetres['square Price']
        plt.hist(propertyDistribution.values,np.arange(*range),edgecolor='black')
        plt.title(f'Properties between ({leftSquare},{rightSquare})')
        plt.xlabel('Square price')
        plt.ylabel('Quantity')
        i+=1
        if i==7:
            plt.subplots_adjust(left=0.1,
                            bottom=0.1, 
                            right=0.9, 
                            top=0.9,
                            wspace=0.4, 
                            hspace=0.4)
            plt.show()
            plt.figure()
            i=1
        

print(df.describe())

#print(df.loc[ df['Square metres']>250 ])

#ratioFullPriceSquare(squareMetrePriceLine=True)
#histogramOfLocations()
#distibutionOfSquarePrices()
#distributionByLocations()
distributionOfSquarePriceBasedOnSquareMetres()
