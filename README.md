## 🦠 Intriduction 🦠
Since the appearance of Covid-19, over 1.199.029 have died of this infeccious disease, only in Europe. Covid is highly contagious, accordingly in more densly populated countries the impact should be higher. 

I have decided to study some other aspects that can have an impact on covid's impact in a country, such as the number of people that smoke, which should affect its fatality (as smoking it harms de cardio-vascular system). Or the GDP of a country, sadly richer countries tend to have a higher survivavility.

All in all, I aim to create a database that yields information about the evolution of covid, and further study of the database might rise results about how population density, tobacco consumption or the GDP in a country affect the impact and fatality of covid in European countries. 

## The data ✍🏼
I am not going to share the data that I am using in this repository, however I am publishing all the sources, so that the reader can visit them and, as I am sharing the code, they can reach the same database that I have created. In the following section I am going to explain how did obtain the data.
* **Covid Fatality data** ☠: for studying the impact of covid and its fatality I have studied a csv File obtained from kaggle, thanks to [Sourav Banerjee] (https://www.kaggle.com/iamsouravbanerjee/covid19-dataset-world-and-continent-wise). The data is divided in various csv files, I have only studied the data in Europe. 
* **Population Density**👨‍👨‍👧‍👧: I just scrapped the wikipedias entry for [List of countries and dependencies by population density](https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population_density). In this case, as my main data source was the data from the covid impact csv, the table needed a little further cleaning. I just reduced the data to that of the countries of our interest for the project. For the scrapping of this url I used Beautiful Soup.
* **Smoking Rate**🚬: I used an official european source to study the rate of people that smoke in each european country, [eurostat](https://ec.europa.eu/eurostat/databrowser/view/hlth_ehis_sk3e/default/table?lang=en). The html file in this page wasn't as easy as the wikipedia page, that is why I had to use both Selenium and Beautiful Soup libraries for the scrapping off this web. The cleaning of the data in this case wasn't very dificult, I just had to drop some of the coulmns as they were not relevant to the study. 
* **Gross Domestic Product** 📈📉: In this case I used the api of the [World Bank](https://www.worldbank.org/en/home). I needed a code to reach the data of each country so I also had to do some scrapping. 

## The database 📦:
You can find the code to generate the database in the file [DatatoSql.py](https://github.com/Pomilusky/Study-Covid19-Fatality/blob/Pomilusky/Code/DatatoSql.py). I basically created an SQL database with 4 tables, one for each of the tables I obtained as explained in the previous section. I did so using SQLalchemy. I thought it might be interesting to create some relations between the data, but I realised that the primary keys were common in all 4 tables (they were all data from the same countries), so maybe for a further study instead of creating relations between tables we should just merge them into one table. 

## Sources 📚:
# [Pandas](https://pandas.pydata.org/)
# [Requests](https://docs.python-requests.org/en/latest/)
# [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
# [Selenium](https://ghostinspector.com/landing/selenium-testing/?gclid=CjwKCAiAo4OQBhBBEiwA5KWu_3rFVm5FcLLuXY7d5AiydLvvfGUR7xUsx0rW1bOBp7MlcijlINm3ZRoCnwgQAvD_BwE)
# [SQLalchemy](https://www.sqlalchemy.org/)
# [ReGex](https://docs.python.org/3/library/re.html)