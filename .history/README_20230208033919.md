# Shamiri Institute - Tech Product Intern Assessment


Project solely for the purpose of satisfying job requirements for the position of `Tech Product Intern` at Shamiri Institute.

## Overview
The purpose of this project is to create a script that will clean and insert data from a csv file into a Postgres database.
The project entails:
- Cleaning data from the csv file and handling missing values.
- Creating a Postgres database and table using the csv file as a reference for the table structure.
- Inserting the cleaned data from the csv file into the Postgres table.
- Handling ambiguous data in the csv file.
- Updating the .env file with the connection details for the database.
- Updating the requirements.txt file with the dependencies for the project.
### Suggested improvements to the script
To make the script more efficient, the following improvements can be made:
- _Better handling of missing values_: Save for the is_admin column, the script currently inputs an empty string for all missing values. This can be improved by using null values in the databae instead of empty strings for missing values.
- _Use of dynamic column names_: The script currently uses static column names for the table. This can be improved by using the column names from the csv file as the column names for the table. This will make the script more dynamic and reusable for other csv files. The code for the query would look something like this:

```python:
   query = 'INSERT INTO shamiri ({0}) VALUES ({1})'
```

### How to ensure the script is running whenever the csv file is updated
To ensure the script is running whenever the csv file is updated, the following can be done:
- _Use of a scheduler or cron:_ A `Task Scheduler` (Windows) or `cron` (Linux) can be used to run the script at a specified time or interval, depending on how often the csv file is updated.
- _Use of a cloud service:_ A cloud service like `AWS Lambda` can be used to run the script whenever the csv file is updated. This can be done by using `AWS S3` to store the csv file and `AWS Lambda` to run the script whenever the csv file is updated.
- _Use of `watchdog`:_ The watchdog library in Python can be used to run the script whenever the csv file is updated.
- _Use of `CI/CD`:_ The script can be integrated into a CI/CD pipeline such as Circle CI or Jenkins to run whenever the csv file is updated.

### Deployment Notes

#### Prerequisites
- Python 3+
- Postgres 12+

#### Installation
- Create a virtual environment and activate it
- Clone the repository into the virtual environment.
- Install the dependencies in the requirements.txt file using `pip install -r requirements.txt`
- Run the script using `python script.py`


#### You can contact me on <jonesdeelder@gmail.com> or <hello@lukorito.dev> for any questions or clarifications.