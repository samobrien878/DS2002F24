import pandas as pd
from flask import Flask
from flask import jsonify
import requests

#Data project 1, comments are references to how to use and the functions.
#This is part 1 of the project, writing an API to a csv or sql file.
#The CSV is available to download locally in this folder. 
# API link to use:
# https://data.cityofnewyork.us/api/views/25th-nujf/rows.json?accessType=DOWNLOAD

print('Now executing part 1'+'\n')

URL = input('Enter the URL of the API you want to pull from:')

#Read in the API:
url = URL
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print('Your API at: ', URL, 'has been read in. ')
else:
    print(f"Error. Theres an issue with your API link: {response.status_code} - {response.text}")

records = data['data']
columns = data['meta']['view']['columns']
print('Your API has ' + str(len(records))+ ' records ' + ' and ' + str(len(columns))+ ' columns.')

#Make some edits to the data
df = pd.DataFrame(records)
df = df.rename(columns={i: columns[i]['name'] for i in range(len(columns))})
columns_to_delete = ['sid','created_meta', 'updated_meta', 'meta', 'position']
df = df.drop(columns=[col for col in columns_to_delete if col in df.columns])

#Type csv or api
x = input('Do you want to write this API as a CSV file or SQL file?')

#Writing the file out depending on the input
if x.lower() == 'csv':
    df.to_csv('data.csv', index=False)
    print('\n'+'The csv file data.csv should be in your working directory. It now has '
          + str(len(df)) + ' records and ' + str(len(df.columns)) + ' columns.','\n' +
          'It should be tiled: data.csv')
elif x.lower() == 'sql':
    from sqlite3 import connect
    conn = connect("data_1.sql")
    curr = conn.cursor()
    df.to_sql("data", conn, if_exists="replace", index=False)
    conn.close()
    print('\n'+ 'The sql file should now be in your working directory. It now has '
          + str(len(df)) + ' records and ' + str(len(df.columns)) + ' columns.','\n' + 'It should be tiled: data_1.sql')
else:
    print('Invalid input. Please enter either "csv" or "sql".')

#### PART 2, Repeating the same thing essentially but starting with a CSV ####
#Make sure the baby names CSV in installed locally!
#note, include .csv when typing in the title of the csv
#To copy-paste: Popular_Baby_Names.csv

print('\n'+'Now executing part 2'+'\n')

answer = input('What is the title of your local csv? Please only list the name of the file:')
try:
  df = pd.read_csv(answer)
  print('Your CSV titled ' , "'" + answer + "'", 'has been read in.' + '\n' + 'It has ' + str(len(records))+ ' records ' + ' and ' + str(len(columns))+ ' columns.')
except FileNotFoundError:
  print(f"Error! File '{answer+'.csv'} not found. Please make sure the file exists and the spelling is correct")

#Made some edits to the data
#Added a popularity ranking column

popularity_threshold = 100
df['Is Popular Name'] = df['Count'].apply(lambda x: 'Yes' if x > popularity_threshold else 'No')

#Type either json or sql
y = input('Do you want to write this CSV to an JSON file or SQL file?:')

#Writing it out to either a JSON or SQL file
if y.lower() == 'json':
    data_json = df.to_json(orient = 'records', lines = False)
    with open ('data.json','w') as json_file:
        json_file.write(data_json)
    print('\n' + 'The json file should now be in your working directory.It now has '
          + str(len(df)) + ' records and ' + str(len(df.columns)) + ' columns.','\n'+
          'It should be tiled: data.json')
elif y.lower() == 'sql':
    from sqlite3 import connect
    conn = connect("data_2.sql")
    curr = conn.cursor()
    df.to_sql("data", conn, if_exists="replace", index=False)
    conn.close()
    print('\n' + 'The sql file should now be in your working directory! It now has '
          + str(len(df)) + ' records and ' + str(len(df.columns)) + ' columns','\n' +
          'It should be tiled: data_2.sql')
else:
    print('Invalid input. Please enter either "csv" or "sql" and ensure the csv is uploaded properly.')


print('This is the end of the program! Enjoy your new file formats...')
