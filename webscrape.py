from scrap import Init, By, XpathAnd, scroll, Keys
import time

###consants
pages = 5
andrijevica = 'andrijevica'
bar = 'bar'
berane = 'berane'
bijelo = 'bijelo'
budva = 'budva'
cetinje = 'cetinje'
danilovgrad = 'danilovgrad'
herceg = 'herceg'
kolasin = 'kolasin'
kotor = 'kotor'
mojkovac = 'mojkovac'
niksic = 'niksic'
plav = 'plav'
pljevlja = 'pljevlja'
pluzine = 'pluzine'
podgorica = 'podgorica'
rozaje = 'rozaje'
tivat = 'tivat'
ulcinj = 'ulcinj'
savnik = 'savnik'
zabljak = 'zabljak'

driver, action = Init("https://estitor.com/me/nekretnine/namjena-prodaja")

def getCity(string):
    tokens = string.split("-")
    return tokens[0]


citySearch = podgorica
citiesPage = driver.find_element(By.CLASS_NAME,"cities-links ")
time.sleep(2)
citiesList = citiesPage.find_elements(By.TAG_NAME,"label")
for i in citiesList:
    city = getCity(str(i.get_attribute("for")))
    if citySearch == city:
        action.click(i).perform()
    

"""inputMinPrice = driver.find_element(By.XPATH,XpathAnd("text-dark-1 dark:text-white  border-grey-1 placeholder-grey-2 dark:placeholder-white text-sm rounded focus:ring-light-blue-1 focus:border-light-blue-1 block w-full pr-10 p-2 dark:bg-dark-2 dark:border-grey-2 dark:focus:ring-light-blue-1 dark:focus:border-light-blue-1 theme-transition min-price"))
inputMaxPrice = driver.find_element(By.XPATH,XpathAnd("text-dark-1 dark:text-white border-grey-1 placeholder-grey-2 dark:placeholder-white text-sm rounded focus:ring-light-blue-1 focus:border-light-blue-1 block w-full pr-10 p-2 dark:bg-dark-2 dark:border-grey-2 dark:focus:ring-light-blue-1 dark:focus:border-light-blue-1 theme-transition max-price"))

print(inputMinPrice.get_attribute("name"))


action.move_to_element(inputMinPrice).perform()
time.sleep(5)
inputMinPrice.send_keys('20000')
inputMaxPrice.send_keys('40000')"""

time.sleep(5000)

def extractProperties():
    properties = driver.find_elements(By.XPATH,XpathAnd("flex items-stretch"))
    for prop in properties:

        info = prop.find_element(By.TAG_NAME,"h3")
        price = prop.find_element(By.CLASS_NAME,"text-dark-green-1")
        link = prop.find_element(By.TAG_NAME,"a")
        
        print(info.text)
        print(price.text)
        print(link.get_attribute("href"))

    pagesOfWeb = driver.find_element(By.XPATH,XpathAnd("flex flex-wrap items-center mt-4 gap-2"))
    listPages = pagesOfWeb.find_elements(By.TAG_NAME,"li")
    specificPage = listPages[len(listPages)-1]

    scroll(driver,5200)
    action.click(specificPage)
    action.perform()

for page in range(pages):
    print(page)
    extractProperties()    



driver.quit()