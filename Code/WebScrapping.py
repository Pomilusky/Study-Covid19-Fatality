import requests as req
from bs4 import BeautifulSoup as bs
import pandas as pd
import re
from selenium import webdriver
# I am going to scrap wikipedia,
url = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population_density'
html = req.get(url).content
soup=bs(html, 'html.parser')

table_body = soup.find('tbody') # All the elements in the table,
table = table_body.find_all('tr')
to_df ={'country':list(),'density':list(),'population':list()}
for row in table[2:]:
    info = row.text.split('\n')
    to_df['country'].append(info[1])
    #print(row)
    to_df['density'].append(float(info[6].replace(',','')))  
    to_df['population'].append(float(info[3].replace(',','')))
df = pd.DataFrame(to_df)
df.sort_values('density', ascending=False, inplace= True)

# Let's now clean this data
countries = []
for country in df.country:
    text = re.findall('\(.+\)',country.lstrip('\xa0'))
    if text != []:
        country= text[0].rstrip(')').lstrip('(')
        if country == 'UKOT' or country == 'Crown Dependency':
            country = 'United Kingdom'
        elif country == 'US':
            country = 'United States'
        elif country == 'NZ':
            country = 'New Zealand'
    elif ']' in country:
        country= re.findall('.+\[',country.lstrip('\xa0'))[0].rstrip("\u202f* [']")
    else:
        country= re.findall('.+',country.lstrip('\xa0').rstrip('\u202f*'))[0]
    #print(re.findall('(.+)', country))
    countries.append(country)
df.country = countries # Let's apply the changes
dfcopy = df.groupby('country').apply(lambda x: x[x['population'] == max(x['population'])])
dfcopy['country']=dfcopy.country.apply(lambda x: x.lower().replace(' ','_'))
dfcopy.index = [i for i in range(len(dfcopy))]
dfcopy.to_csv('../Data/DensityPopulationData.csv', index = False)

url = 'https://ec.europa.eu/eurostat/databrowser/view/hlth_ehis_sk3e/default/table?lang=en'

driver = webdriver.Chrome(executable_path='/mnt/c/Users/marcn/Documents/Ironhack/chromedriver.exe')
# Load the web page
driver.get(url)
# Wait for the page to fully load
driver.implicitly_wait(5)
table = driver.find_element_by_css_selector('#mainContent > ui-view > div.ux-panel-item.view-presentation > ng-include:nth-child(3) > div.estatcontent.col-md-12.ux-panel-item--has-tabs > div.tab-content')
f_column = table.find_element_by_xpath('//*[@id="tableDiv"]/div/div[1]/div[2]/div[3]/div[1]')
countries = f_column.find_elements_by_tag_name('div') # We get a string with all the countries
other_columns = table.find_element_by_xpath('//*[@id="tableDiv"]/div/div[1]/div[2]/div[3]/div[2]')
smok_data = other_columns.find_element_by_tag_name('div').text # We get the other columns
driver.implicitly_wait(3)

lista = smok_data.split('\n')
countries = [e.text for e in countries]
countries = countries[2:]
#print(lista)
driver.quit()


# let's work the data,
new_countries = [countries[i] for i in range(0,len(countries),2)]
data_smk = []
data_country = []
counter = 0

for i in range(0,len(lista),3):
      #data[] = lista[i:i+3]
      try:
            data_country.append(new_countries[counter])
            data_smk.append(float(lista[i+3].replace(':','0')[:4]))                                                                                                                                                                                            
            # for j in lista[i+3:i+6]:
            #       print(j[:4])    
            counter += 1
      except: break
data = {'country':data_country[1:], 'smokingpopulation': data_smk[1:]}
df2 = pd.DataFrame(data)
df2['country']=df2.country.apply(lambda x: x.lower().replace(' ','_'))
def change_germany(string):
    if string == 'germany_(until_1990_former_territory_of_the_frg)':
        return 'germany'
    if string:
        return string
df2.country = df2.country.apply(change_germany)
df2.to_csv('../Data/smokingData.csv', index = False)
# Now that we have the data we must create a table in the data base and insert it