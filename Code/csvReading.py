import functions as fun
import pandas as pd

# This is going to be quite simple, we are going to read the cvs and transform it with the function I created to clean it,
df_Europe = pd.read_csv('../Data/CDEurope.csv')
def_Clean_Europe = fun.cleaning_csvData(df_Europe)
def_Clean_Europe.rename(columns = {'country,_other': 'country'}, inplace=True)
def_Clean_Europe.country = def_Clean_Europe.country.apply(lambda x: x.lower().replace(' ','_').replace('uk','united_kingdom'))
def_Clean_Europe.to_csv('../Data/EuropeCovidData.csv',index=False)
