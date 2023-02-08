
# Make necessary imports
import os
from dotenv import load_dotenv
import psycopg2
import csv

# Load the environment variables
load_dotenv()

# Get the environment variables
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
PORT_ID = 5432


def clean_csv_data():
    """_summary_: This function cleans the csv data by adding missing values for the id column ensuring they remain sequential and unique.
    """
    values = []
    current_id = 0  # This variable will hold the current highest id value

    with open("MOCK_DATA.csv", "r") as f:
        reader = csv.reader(f)
        headers = next(reader)  # Get the headers
        values.append(headers)  # Add the headers to the values list
        # Convert the id column to an integer and check if it is greater than the current_id, if it is, update the current_id accordingly.
        for row in reader:
            current_id += 1
            if row[0]:
                id_value = int(row[0])
                if id_value > current_id:
                    current_id = id_value
            else:
                row[0] = str(current_id)
            values.append(row)
    # Write the cleaned data to a new csv file
    with open("CLEANED_MOCK_DATA.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(values)


clean_csv_data()  # Call the function to clean the csv data


# Connect to the database using the environment variables
conn = psycopg2.connect(
    host=DB_HOST,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)


# Open a cursor to perform database operations
cur = conn.cursor()

# Create a table to store the data
cur.execute("""
CREATE TABLE IF NOT EXISTS shamiri_data (
    id integer PRIMARY KEY,
    first_name text,
    last_name text,
    email text,
    gender text,
    ip_address text,
    is_admin boolean
);
""")

# Open the CSV file
with open("CLEANED_MOCK_DATA.csv", "r") as file:
    # Create a reader object to read the CSV data
    reader = csv.reader(file)

    # Skip the header row
    next(reader)

    # Insert the data into the database
    for row in reader:
        # Handle the empty string in the is_admin column
        if row[-1] == "":
            row[-1] = False
        # Create and execute the query
        cur.execute("""
        INSERT INTO shamiri_data (id, first_name, last_name, email, gender, ip_address, is_admin)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, row)

# Commit the changes to the database
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
