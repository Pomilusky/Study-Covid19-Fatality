import pandas as pd
import numpy as np
# Functions to clean csv data:

######################################################################################################
def cleaning_csvData(df):
    # Basic cleaning,
    dfnew = df.dropna(axis = 0, how = 'all')

    # Renaming columns,
    new_dict = {i: i.strip().replace(" ", "_").replace('.','').lower() for i in df.columns}
    dfnew.rename(columns=new_dict, inplace = True)

    # let's drop the columns we are not interested with,
    dfnew.drop(columns =['active_cases','serious_/_critical_condition', 'deaths_/_1m_population', 'total_tests', 'tests_/_1m_population'], inplace=True) 
    dfnew.total_cases = pd.to_numeric(dfnew.total_cases.astype(str).str.replace(',',''), errors='coerce')
    dfnew.total_deaths = pd.to_numeric(dfnew.total_deaths.astype(str).str.replace(',',''), errors='coerce')

    # Let's, now add another column,
    dfnew['fatality'] =  dfnew.apply(lambda x: (x['total_deaths']/x['total_cases'])*100, axis=1)
    dfnew.total_recovered = dfnew.total_recovered.apply(lambda x: int(x.replace(',','')))
    #dfnew.fatality.apply(lambda x: int(x.replace(',','')))
    #dfnew['total_cases_/_1m_population']= dfnew['total_cases_/_1m_population'].apply(lambda x: int(x.replace(',','')))
    #dfnew.population = dfnew.population.apply(lambda x: int(x.replace(',','')))
    dfnew.total_deaths = dfnew.total_deaths.fillna(0)
    dfnew.total_deaths = dfnew.total_deaths.apply(lambda x: int(x))
    
    dfnew.rename(columns = {'total_cases_/_1m_population': '1m_population'}, inplace = True)
    #dfnew.drop(index=224 )
    return dfnew

######################################################################################################

######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
