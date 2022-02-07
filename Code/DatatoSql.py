import pandas as pd
import sqlalchemy

df1 = pd.read_csv('../Data/EuropeCovidData.csv')
df2 = pd.read_csv('../Data/smokingData.csv')
df3 = pd.read_csv('../Data/DensityPopulationData.csv')
df5 = pd.read_csv('../Data/PIBData.csv')
df5.dropna(inplace = True)
#df1.country.values
# for i in df3.country:
#     print(i in df1.country.values)
todrop = []
for i in df3.index:
    if df3.iloc[i]['country'] not in df1.country.values:
        todrop.append(i)
df3.drop(todrop, inplace = True)
df3.reset_index(inplace=True, drop=True)

df4 =df1.merge(df2).drop(columns=[ 'total_cases', 'total_deaths', 'total_recovered',
       '1m_population', 'fatality'])
df4.population = df4.population.apply(lambda x: int(x.replace(',','')))
df4['population']
df4['total_smok_pop'] = df4.apply(lambda x: (x['population']*x['smokingpopulation'])/100, axis = 1)  
df4['total_smok_pop'] = df4['total_smok_pop'].apply(lambda x: 'no_data' if x == 0 else x) 
str_con = 'mysql+pymysql://root:password@localhost:3306/coviddata'
engine = sqlalchemy.create_engine(str_con)
with engine.begin() as connection:
    df3.to_sql('density', con=connection, if_exists='replace',index=True)
    df1.to_sql('coviddata', con=connection,if_exists='replace',index=True )
    df4.to_sql('smokingdata', con=connection,if_exists='replace', index=True )
    df5.to_sql('pibdata', con=connection, if_exists = 'replace', index = True)
with engine.connect() as con:
    con.execute('ALTER TABLE `density` ADD PRIMARY KEY (`index`);')
    con.execute('ALTER TABLE `coviddata` ADD PRIMARY KEY (`index`);')
    con.execute('ALTER TABLE `smokingdata` ADD PRIMARY KEY (`index`);')
    con.execute('ALTER TABLE `pibdata` ADD PRIMARY KEY (`index`);')