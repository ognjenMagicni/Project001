import sys
sys.path.insert(0,'libraries')

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mysqlwrapper import selectBackend,updateBackend
import pymysqlpool

config={'host':'localhost', 'user':'root', 'password':'simple', 'database':'properties', 'autocommit':True}
pool = pymysqlpool.ConnectionPool(size=2, maxsize=15, pre_create_num=2, name='pool1', **config)

app = FastAPI()
origins = [
    "http://localhost:3000",
    "http://localhost:80"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/getAllSearches/')
def getAllSearches():
    searches = selectBackend(pool,"SELECT * FROM properties.search")
    return searches


@app.get("/getAllProperties/{id}")
def getAllProperties(id: int):
    properties = selectBackend(pool,"SELECT * FROM properties.property WHERE fk_search= %s",(id,))
    return properties


@app.get("/getSearch/{id}")
def getSearch(id: int):
    search = selectBackend(pool,"SELECT * FROM properties.search WHERE id= %s",(id,))
    return search


@app.get('/getTypes/')
def getTypes():
    typesOfProperties = selectBackend(pool,"SELECT * FROM properties.type")
    return typesOfProperties
    

@app.get('/getLocations/')
def getLocations():
    locations = selectBackend(pool,"SELECT * FROM properties.location")
    return locations


@app.put("/updateOnOff/{id}")
def onOffUpdate(id:int):
    updateBackend(pool,"UPDATE properties.property SET on_off = 1-on_off WHERE id_property=%s",(id,))
    
@app.delete("/deleteSearch/{id_search}")
def deleteSearch(id_search:int):
    updateBackend(pool,"DELETE FROM properties.settlements4zid WHERE fk_property=ANY(SELECT id_property FROM properties.property WHERE fk_search=%s)",(id_search,))
    updateBackend(pool,"DELETE FROM properties.property WHERE fk_search=%s",(id_search,))
    updateBackend(pool,"DELETE FROM properties.search WHERE id=%s",(id_search,))

from pydantic import BaseModel
class SubmitObject(BaseModel):
    pages: int
    location: str
    type: str
    minPrice: int
    maxPrice: int
    title: str
    description: str

@app.post("/runProgram/")
def runProgram(submitObject: SubmitObject):
    city, country = submitObject.location.strip().split(",")
    submitObject.location = city
    if country==' Montenegro':
        import realitica
        realitica.pages = submitObject.pages
        realitica.cityFilter.append(submitObject.location)
        realitica.propertyFilter.append(submitObject.type)
        realitica.minPrice = int(submitObject.minPrice)
        realitica.maxPrice = int(submitObject.maxPrice)
        realitica.title = submitObject.title
        realitica.description = submitObject.description
        try:
            realitica.run()
        except Exception as e:
            print(f"An error occurred: {e}") 
    elif country==' Serbia':
        import fourZid
        fourZid.TITLE = submitObject.title
        fourZid.DESCRIPTION = submitObject.description
        fourZid.MinPrice, fourZid.MaxPrice = submitObject.minPrice, submitObject.maxPrice
        fourZid.MinSquare, fourZid.MaxSquare = 10,500
        fourZid.PAGES = submitObject.pages
        fourZid.CITY = submitObject.location
        try:
            fourZid.run()
        except Exception as e:
            print(f"An error occured {e}")

    """import realitica
    realitica.pages = run.pages
    realitica.cityFilter.append(run.location)
    realitica.propertyFilter.append(run.type)
    realitica.minPrice = int(run.minPrice)
    realitica.maxPrice = int(run.maxPrice)
    realitica.title = run.title
    realitica.description = run.description
    try:
        realitica.run()
    except Exception as e:
        print(f"An error occurred: {e}") """

@app.get("/getAnalytics/{id_search}")
def getAnalytics(id_search:int):
    import subprocess

    script_name = "present.py"
    arguments = [str(id_search)]

    
    subprocess.run(["python", script_name] + arguments)

@app.get("/getAnalyticsCompare/{id_search1}/{id_search2}")
def getAnalyticsCompare(id_search1:int,id_search2:int):
    import subprocess

    script_name = "present.py"
    arguments = [str(id_search1),str(id_search2)]

    
    subprocess.run(["python", script_name] + arguments)

from pydantic import BaseModel
class Graph(BaseModel):
    id_search:int
    minPrice:int
    maxPrice:int
    minSquareMetres:int
    maxSquareMetres:int
    minSquarePrices:int
    maxSquarePrices:int

@app.post("/runGraph")
def runGraph(graph: Graph):
    import subprocess

    script_name = "graph.py"
    arguments = [str(graph.id_search),str(graph.minPrice),str(graph.maxPrice),str(graph.minSquareMetres),str(graph.maxSquareMetres),str(graph.minSquarePrices),str(graph.maxSquarePrices)]

    subprocess.run(["python", script_name] + arguments)


    