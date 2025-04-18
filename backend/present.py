import sys
sys.path.insert(0,'libraries')

import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
from mysqlwrapper import selectQuery

#51 je novi sad, 47 je pg, 56 je bg
path = '../frontend/stanovi/public/'
def extractDataFromPropertyTable(search_id):
    query = "SELECT * FROM properties.property WHERE fk_search = %s"
    values = (search_id,)
    return selectQuery(query,values)

def convertToDataFrame(search_id):
    data = extractDataFromPropertyTable(search_id)
    columns = ['id_property','fk_search','rooms','square metres','full price','location','city','country','link','on_off','description','square price']
    data = pd.DataFrame(data,columns=columns)
    data.drop(columns=['id_property','fk_search','on_off','description'],inplace=True)
    return data



def histogramOfLocations(df):
    location_counts = df['location'].value_counts()
    plt.figure(figsize=(10, 6))
    plt.bar(location_counts.index, location_counts.values, color='skyblue', edgecolor='black')
    plt.title('Counts of Locations', fontsize=16)
    plt.xlabel('Location', fontsize=14)
    plt.ylabel('Count', fontsize=14)
    plt.xticks(rotation=90, fontsize=12)
    plt.tight_layout()
    plt.savefig(path+'histogramOfLocations.png',dpi=300)
    #plt.show()

def distibutionOfSquarePrices(df):
    location_counts = df['square price']
    plt.figure(figsize=(10, 6))
    plt.hist(location_counts.values,np.arange(0,5000,250),edgecolor='black')
    plt.title('Distibution of square prices', fontsize=16)
    plt.xlabel('Square price', fontsize=14)
    plt.ylabel('Quantity', fontsize=14)
    plt.savefig(path+'distributionOfSquarePrices.png',dpi=300)
    #plt.show()

def dataOfSettlements(df):
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

def distributionByLocations(df,sortArgument = ('square price','count'),argument = 'square price', range = (0,5000,250)):    #0,5000,250
    locationData = dataOfSettlements(df)

    locationData = dict(
    sorted(locationData.items(), key=lambda item: item[1]['square price']['count'], reverse=True)
    )

    i=1
    flag = True
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
            if flag:
                plt.savefig(path+'distributionByLocation.png',dpi=300)
                flag = False
            #plt.show()
            plt.figure()
            i=1

def compareTwoLocations(location1,location2):
    data1 = df.loc[ df['location']==location1,'square price' ]
    data2 = df.loc[ df['location']==location2,'square price' ]

    plt.hist(data1,np.arange(0,5000,250),edgecolor='black',alpha=0.4)
    plt.hist(data2,np.arange(0,5000,250),edgecolor='black',alpha=0.4)
    plt.show()

def ratioFullPriceSquare(df,squareMetrePriceLine = False,fullPriceLine = False,locationList = None,priceRange = (0,300000),squareRange=(0,100)):
    df = df.loc[ (df['full price']>priceRange[0]) & (df['full price']<priceRange[1]) & (df['square metres']>squareRange[0]) & (df['square metres']<squareRange[1]) ]
    df.reset_index(drop=True,inplace=True)
    city, country = df.loc[0,'city'],df.loc[0,'country']
    newDf = [df]
    if locationList!=None:
        newDf.pop()
        for location in locationList:
            newDf.append( df.loc[ df['location']==location ]  )

    x = np.arange(0,300,10)
    y = np.arange(0,300000,10000)
    y2 = np.arange(0,600000,20000)
    y3 = np.arange(0,900000,30000)

    colors = ('blue','yellow','cyan','magenta')
    for i,location in enumerate(newDf):
        plt.scatter(location['square metres'],location['full price'],color = colors[i],label=locationList[i] if locationList != None else city+", "+country,alpha=0.5)

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

    plt.xlim(squareRange[0],squareRange[1])
    plt.ylim(priceRange[0],priceRange[1])
    plt.savefig(path+'fullAndSquarePrice.png',dpi=300)
    #plt.show()

def distributionOfSquarePriceBasedOnSquareMetres(df,range = (0,5000,250)):
    squareMetres = [(0,30),(30,40),(40,50),(50,70),(70,100),(100,150),(150,500)]

    i=1
    plt.figure(figsize=(17, 17))
    for leftSquare,rightSquare in squareMetres:
        plt.subplot(3,3,i)
        propertyBySquareMetres = df.loc[ (df['square metres']>leftSquare) & (df['square metres']<rightSquare)]
        propertyDistribution = propertyBySquareMetres['square price']
        plt.hist(propertyDistribution.values,np.arange(*range),edgecolor='black')
        plt.title(f'Properties between ({leftSquare},{rightSquare}) square metres')
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
            plt.savefig(path+'distributionOfSquarePriceBasedOnSquareMetres.png',dpi=300)
            #plt.show()
            plt.figure()
            i=1
        
def squarePriceDistributionPerSquare(df,leftSquare,rightSquare):
    propertyBySquareMetres = df.loc[ (df['square metres']>leftSquare) & (df['square metres']<rightSquare)]
    propertyDistribution = propertyBySquareMetres['square price']
    return propertyDistribution

def distributionOfSquarePriceBasedOnSquareMetresCompare(df1,df2,range = (0,5000,250)):
    squareMetres = [(0,30),(30,40),(40,50),(50,70),(70,100),(100,150),(150,500)]

    i=1
    plt.figure(figsize=(17, 17))
    for leftSquare,rightSquare in squareMetres:
        plt.subplot(3,3,i)
        propertyDistribution1 = squarePriceDistributionPerSquare(df1,leftSquare,rightSquare)
        propertyDistribution2 = squarePriceDistributionPerSquare(df2,leftSquare,rightSquare)
        plt.hist(propertyDistribution1.values,np.arange(*range),edgecolor='black',alpha=0.5,label=df1.loc[0,'city'],density=True)
        plt.hist(propertyDistribution2.values,np.arange(*range),edgecolor='black',alpha=0.5,label=df2.loc[0,'city'],density=True)
        plt.title(f'Properties between ({leftSquare},{rightSquare}) square metres')
        plt.xlabel('Square price')
        plt.ylabel('Quantity')
        plt.legend()
        if i==7:
            plt.subplots_adjust(left=0.1,
                            bottom=0.1, 
                            right=0.9, 
                            top=0.9,
                            wspace=0.4, 
                            hspace=0.4)
            plt.savefig(path+'distributionOfSquarePriceBasedOnSquareMetresCompare.png',dpi=300)
            #plt.show()
            i=1
        i+=1

def ratioFullPriceSquareCompare(df1,df2,squareMetrePriceLine = False,fullPriceLine = False,locationList = None,priceRange = (0,300000),squareRange=(0,100)):
    plt.figure(figsize=(10,6))
    df1 = df1.loc[ (df1['full price']>priceRange[0]) & (df1['full price']<priceRange[1]) & (df1['square metres']>squareRange[0]) & (df1['square metres']<squareRange[1]) ]
    df1.reset_index(drop=True,inplace=True)
    df2 = df2.loc[ (df2['full price']>priceRange[0]) & (df2['full price']<priceRange[1]) & (df2['square metres']>squareRange[0]) & (df2['square metres']<squareRange[1]) ]
    df2.reset_index(drop=True,inplace=True)
    city1, country1 = df1.loc[0,'city'],df1.loc[0,'country']
    city2, country2 = df2.loc[0,'city'],df2.loc[0,'country']

    x = np.arange(0,300,10)
    y = np.arange(0,300000,10000)
    y2 = np.arange(0,600000,20000)
    y3 = np.arange(0,900000,30000)

    label = True
    for (index1, row1), (index2, row2) in zip(df1.iterrows(), df2.iterrows()):
        if label:
            plt.scatter(row1['square metres'], row1['full price'], color='blue', label=city1+", "+country1, alpha=0.2)
            plt.scatter(row2['square metres'], row2['full price'], color='red', label=city2+", "+country2, alpha=0.2)
            label = False
        plt.scatter(row1['square metres'], row1['full price'], color='blue', alpha=0.2)
        plt.scatter(row2['square metres'], row2['full price'], color='red', alpha=0.2)

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

    plt.xlim(squareRange[0],squareRange[1])
    plt.ylim(priceRange[0],priceRange[1])
    plt.savefig(path+'fullAndSquarePriceCompare.png',dpi=300)
    #plt.show()


def distributionOfSquarePricesCompare(df1, df2):
    prices1 = df1['square price']
    prices2 = df2['square price']

    city1, country1 = df1.loc[0,'city'],df1.loc[0,'country']
    city2, country2 = df2.loc[0,'city'],df2.loc[0,'country']
    
    bins = np.arange(0, 5000, 250)
    
    plt.figure(figsize=(10, 6))
    plt.hist(prices1, bins, alpha=0.5, color='blue',density=True, label=f"{city1}, {country1}", edgecolor='black')
    plt.hist(prices2, bins, alpha=0.5, color='red',density=True, label=f"{city2}, {country2}", edgecolor='black')
    
    plt.title('Distribution of Square Prices', fontsize=16)
    plt.xlabel('Square Price', fontsize=14)
    plt.ylabel('Quantity', fontsize=14)
    plt.legend(fontsize=12)
    plt.savefig(path+'distributionOfSquarePricesCompare.png',dpi=300)
    
    #plt.show()
#print(df.describe())

#print(df.loc[ df['Square metres']>250 ])


def run(id_search):
    df = convertToDataFrame(id_search)
    df = df.loc[ (df['square metres']>10) & (df['full price']>5000)]
    ratioFullPriceSquare(df,squareMetrePriceLine=True)
    histogramOfLocations(df)
    distibutionOfSquarePrices(df)
    distributionByLocations(df)
    distributionOfSquarePriceBasedOnSquareMetres(df)

def runCompare(id_search1, id_search2):
    df1 = convertToDataFrame(id_search1)
    df1 = df1.loc[ df1['square metres']>10 ]
    df1 = df1.loc[ df1['square metres']<500 ]
    df1.reset_index(drop=True,inplace=True)

    df2 = convertToDataFrame(id_search2)
    df2 = df2.loc[ df2['square metres']>10 ]
    df2 = df2.loc[ df2['square metres']<500 ]
    df2.reset_index(drop=True,inplace=True)

    distributionOfSquarePricesCompare(df1,df2)
    distributionOfSquarePriceBasedOnSquareMetresCompare(df1,df2)
    ratioFullPriceSquareCompare(df1,df2,squareMetrePriceLine=True)

import sys

if __name__ == "__main__":
    # Check the number of arguments
    if len(sys.argv) == 2:  # One argument
        run(int(sys.argv[1]))
    elif len(sys.argv) == 3:  # Two arguments
        runCompare(int(sys.argv[1]), int(sys.argv[2]))

