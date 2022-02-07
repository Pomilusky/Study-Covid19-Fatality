import mysql.connector as conn

# Let's first create the data base, and then insert the data in tables,

crea_db=conn.connect(host='localhost',
                     user='root',
                     passwd='password')

cursor=crea_db.cursor()

cursor.execute('drop database if exists coviddata')
cursor.execute('create database coviddata')

db=conn.connect(host='localhost',
                     user='root',
                     passwd='password',
                     database='coviddata')

cursor=db.cursor()


# Now that we have created the database and we have accesed it, we can write the tables,
# crea una tabla
cursor.execute('drop table if exists coviddata')


tabla='''
            create table coviddata(
                id int,
                country varchar(50),
                total_cases int,
                total_deaths int,
                total_recovered int,
                1m_population varchar(50),
                population varchar(50),
                fatality float
            );
'''

cursor.execute(tabla)

cursor.execute('drop table if exists density')


tabla='''
            create table density(
                id int,
                country varchar(50),
                denisty_pop float,
                population int
            );
'''


cursor.execute(tabla)


cursor.execute('drop table if exists smokingdata')


tabla='''
            create table smokingdata(
                id int,
                country varchar(50),
                smokingpopulation float
            );
'''

cursor.execute(tabla)