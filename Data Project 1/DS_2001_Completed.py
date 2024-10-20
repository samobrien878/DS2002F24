import pandas as pd
from flask import Flask
from flask import jsonify
import requests

# API link to use in this case:
# https://data.cityofnewyork.us/api/views/25th-nujf/rows.json?accessType=DOWNLOAD
# Link to download the CSV locally:
# https://catalog.data.gov/dataset/popular-baby-names/resource/02e8f55e-2157-4cb2-961a-2aabb75cbc8b

print('Now executing part 1'+'\n')

URL = input('Enter the URL of the API you want to pull from:')

#Read in the API:
url = URL
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
else:
    print(f"Error. Theres an issue with your API link: {response.status_code} - {response.text}")

#Clean and delete some columns
records = data['data']
columns = data['meta']['view']['columns']

df = pd.DataFrame(records)
df = df.rename(columns={i: columns[i]['name'] for i in range(len(columns))})
columns_to_delete = ['sid','created_meta', 'updated_meta', 'meta', 'position']
df = df.drop(columns=[col for col in columns_to_delete if col in df.columns])

# Deciding in what format to write the file to
x = input('Do you want to write this API as a CSV file or SQL file?: ')

if x.lower() == 'csv':
    df.to_csv('data.csv', index=False)
    print('Print the csv file data.csv should be in your working directory. Congrats!')
elif x.lower() == 'sql':

    from sqlite3 import connect
    conn = connect("data.sql")
    curr = conn.cursor()
    df.to_sql("data", conn, if_exists="replace", index=False)
    conn.close()
    print('The sql file should now be in your working directory. Congrats!')
else:
    print('Invalid input. Please enter either "csv" or "sql".')
#### PART 2, Repeating the same thing essentially but starting with a CSV ####
#Make sure the baby names CSV in installed locally!

print('Now executing part 2'+'\n')

answer = input('what is the title of your local csv without the .csv?')
try:
  df = pd.read_csv(answer + '.csv')

except FileNotFoundError:
  print(f"Error! File '{answer+'.csv'} not found. Please make sure the file exists and the spelling is correct")

#Add a popularity column!

popularity_threshold = 100
df['Is Popular Name'] = df['Count'].apply(lambda x: 'Yes' if x > popularity_threshold else 'No')

#Writing it out to either a JSON or SQL file
y = input('Do you want to write this CSV to an JSON file or SQL file?: ')

# Check if the input variable y equals 'api'
if y.lower() == 'json':
    data_json = df.to_json(orient = 'records', lines = False)
    with open ('data.json','w') as json_file:
        json_file.write(data_json)
    print('The json file should now be in your working directory. Congrats!')
elif y.lower() == 'sql':

    from sqlite3 import connect
    conn = connect("data_2.sql")
    curr = conn.cursor()
    df.to_sql("data", conn, if_exists="replace", index=False)
    conn.close()
    print('The sql file should now be in your working directory! Congrats!')

else:
    print('Invalid input. Please enter either "csv" or "sql" and ensure the csv is uploaded properly.')
