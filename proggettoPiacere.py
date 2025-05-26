# save this as app.py
import mysql.connector
import pandas as pd

# Connect to mysql
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="" # Ensure your MySQL root password is correct, if any
)
mycursor = mydb.cursor()
print("Successfully connected to MySQL server!")

# Create the DB (if not already exists)
mycursor.execute("CREATE DATABASE IF NOT EXISTS Education_Rich_People")
print("Database 'Education_Rich_People' checked/created.")

# Use the database
mycursor.execute("USE Education_Rich_People")

# IMPORTANT: Drop the table if it already exists to ensure the schema is updated
# This is crucial for applying changes to column types like VARCHAR for GPA.
mycursor.execute("DROP TABLE IF EXISTS Rich_People")
mydb.commit()
print("Existing table 'Rich_People' dropped (if it existed).")

# Create the table for the csv data (if not exists)
# IMPORTANT: Ensure column data types match the data you intend to insert.
# 'GPA' and 'University_Global_Ranking' need to be VARCHAR to accept 'Null' strings
# and non-numeric ranking strings.
mycursor.execute("""
    CREATE TABLE Rich_People (
        Name VARCHAR(100) NOT NULL,
        Profession VARCHAR(100),
        Degree VARCHAR(100),
        Field VARCHAR(100),
        Institution VARCHAR(100),
        Graduation_Year VARCHAR(10),       -- Changed to VARCHAR to handle 'Null' if present
        Country VARCHAR(100),
        University_Global_Ranking VARCHAR(100), -- Changed to VARCHAR for 'Null' and text ranks
        GPA VARCHAR(10),                   -- Changed to VARCHAR for 'Null' and non-numeric GPAs
        Scholarship_Award VARCHAR(255),    -- Increased length for potential longer awards
        PRIMARY KEY (Name)
    );""")
# Commit the table creation
mydb.commit()
print("Table 'Rich_People' created with updated schema.")

# Delete data from the table Rich_People before inserting new data
# This will now operate on the newly created/recreated table
mycursor.execute("DELETE FROM Rich_People")
mydb.commit()
print("Existing data deleted from 'Rich_People' table.")

# Read data from a csv file
# Make sure 'successful_educations.csv' is in the same directory or provide the full path
rich_data = pd.read_csv('./successful_educations.csv', index_col=False, delimiter=',')
# Replace NaN with 'Null' string. This string will now correctly fit into VARCHAR columns.
rich_data = rich_data.fillna('Null')
print("\nFirst 20 rows of data from CSV (after fillna):")
print(rich_data.head(20))

# Fill the table
print("\nInserting records into database...")
for i, row in rich_data.iterrows():
    cursor = mydb.cursor() # Create a new cursor for each insertion
    # Corrected SQL: 10 placeholders (%s) to match the 10 columns
    sql = """
        INSERT INTO Rich_People
        (Name, Profession, Degree, Field, Institution, Graduation_Year, Country, University_Global_Ranking, GPA, Scholarship_Award)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    # Convert the pandas Series row to a tuple for insertion
    cursor.execute(sql, tuple(row))
    print(f"Record {i+1} inserted: {row['Name']}")
    mydb.commit() # Commit each record
    cursor.close() # Close cursor after use

# Check if the table has been filled
print("\n--- Data in Rich_People table (first 10 rows from DB) ---")
mycursor.execute("SELECT * FROM Rich_People LIMIT 10") # Limit to first 10 for brevity
myresult = mycursor.fetchall()
for x in myresult:
    print(x)