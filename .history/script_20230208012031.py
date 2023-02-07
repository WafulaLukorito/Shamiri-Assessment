
#  code here  : please structure your code in a way that it is easy to read and understand

# Please read the following instructions carefully and follow them. They are important for the evaluation of your code.
# You are required to write a python script that will read the MOCK_DATA csv file and insert the data into a Postgres database.
# The script should be able to run on any machine and should not require any manual intervention to run.

# Steps:
# 1. Create a Postgres database
# 2. Create a table in the database using the csv file as a reference for the table structure
# 3. Clean the data and insert the data from the csv file into the postgres table
# 4. Update .env file with the connection details for the database (Note: You can use a local connection or a remote connection * if you are using a remote connection, please provide the connection details in the readme file)
# 5. Update requirements.txt file with the dependencies for the project
# 6. How would you improve the script to make it more efficient? (Note: You are not required to implement the improvements but list them in the readme file)
# 7. How you you ensure the script is running whenever the csv file is updated? (Note: You are not required to implement the improvements but list them in the readme file)
# 8. Upload the final project to github and provide the link to the repository

# Path: script.py

import os
from dotenv import load_dotenv
import psycopg2
import csv

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
PORT_ID = 5432


def clean_csv_data():
    values = []
    current_id = 0

    with open("MOCK_DATA.csv", "r") as f:
        reader = csv.reader(f)
        headers = next(reader)
        values.append(headers)
        for row in reader:
            current_id += 1
            if row[0]:
                id_value = int(row[0])
                if id_value > current_id:
                    current_id = id_value
            else:
                row[0] = str(current_id)
            values.append(row)

    with open("CLEANED_MOCK_DATA.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(values)


clean_csv_data()


conn = psycopg2.connect(
    host=DB_HOST,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)

cursor = conn.cursor()

with open('CLEANED_MOCK_DATA.csv', 'r') as f:
    reader = csv.reader(f)
    columns = next(reader)
    query = 'CREATE TABLE IF NOT EXISTS Shamiri ({0})'
    cursor.execute(query.format(','.join(columns)))
    for data in reader:
        query = 'INSERT INTO Shamiri ({0}) VALUES ({1})'
        cursor.execute(query.format(','.join(columns),
                       ','.join("'"+item+"'" for item in data)))

conn.commit()
cursor.close()
conn.close()
