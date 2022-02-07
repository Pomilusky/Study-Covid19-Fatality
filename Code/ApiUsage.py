import requests as req
import pandas as pd
from selenium import webdriver

# We are going to read an api of the world bank, in order to do it properly we are going to use some web scrapping,
URL = 'https://wits.worldbank.org/wits/wits/witshelp/content/codes/country_codes.htm'
driver = webdriver.Chrome(executable_path='/mnt/c/Users/marcn/Documents/Ironhack/chromedriver.exe')
# Load the web page
driver.get(URL)
table = driver.find_element_by_xpath('//*[@id="helpContent"]/table/tbody')
countries = table.find_elements_by_tag_name('tr') 
driver.implicitly_wait(3)

countries = [(e.text).split('\n')[:2] for e in countries]
countries = countries[2:]
#print(lista)
driver.quit()

table_code = pd.DataFrame(countries, columns = ['country','code'])
table_code.country = table_code.country.apply(lambda x: x.replace(' ','_').lower())
data = pd.read_csv('../Data/EuropeCovidData.csv')
table_code = table_code[table_code.country.isin(list(data.country.values))].reset_index(drop=True)
token = open ("../token.txt").readlines()[0]
params = {"Authorization": f"token {token}"}
result_PIB = dict()
for country, code in table_code.values:
    #print(country, code)
    URL = f'http://api.worldbank.org/countries/{code}/indicators/NY.GDP.MKTP.CD?format=json&date=2020:2021'
    langs = req.get(URL, headers = params)
    diccionari = langs.json()[1][0]
    result_PIB[country] = diccionari['value']

result_PIB.values()
to_df = {'country': result_PIB.keys(), 'PIB': result_PIB.values()}
df = pd.DataFrame(to_df)
df.to_csv('../Data/PIBData.csv', index = False)