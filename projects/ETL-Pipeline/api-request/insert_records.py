# POPULATING THE DATABASE WITH WEATHER DATA

import psycopg2
from api_request import fetch_data, mock_fetch_data

def connect_to_db(): # Establish a connection to the PostgreSQL database
    print("Connecting to the database...")
    
    try:

        conn = psycopg2.connect(
            host="localhost", 
            port=5432,
            database="db", 
            user="root", 
            password="toor"
        )
        return conn

    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")
        raise


def create_table(conn): # Create the table to store weather data if it doesn't already exist
    print("Creating the table if it doesn't exist...")
    
    try:

        cursor = conn.cursor()
        cursor.execute("""
            CREATE SCHEMA IF NOT EXISTS dev;
            CREATE TABLE IF NOT EXISTS dev.raw_weather_data (
                id SERIAL PRIMARY KEY,
                city TEXT,
                temperature FLOAT,
                weather_descriptions TEXT,
                wind_speed FLOAT,
                time TIMESTAMP,
                inserted_at TIMESTAMP DEFAULT NOW(),
                utc_offset TEXT
            );
        """)
        conn.commit()
        print("Table created successfully.")
    
    except psycopg2.Error as e:
        print(f"Error creating the table: {e}")
        raise


def insert_records(conn, data): # Insert the fetched weather data into the database
    print("Inserting records into the database...")
    
    try:
        weather = data['current']
        location = data['location']
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO dev.raw_weather_data (
            city, 
            temperature, 
            weather_descriptions, 
            wind_speed, 
            time, 
            inserted_at,
            utc_offset
            ) VALUES (%s, %s, %s, %s, %s, NOW(), %s);
        """, (
            location['name'],
            weather['temperature'],
            weather['weather_descriptions'][0],
            weather['wind_speed'],
            location['localtime'],
            location['utc_offset']
        ))
        conn.commit()
        print("Records inserted successfully.")

    except psycopg2.Error as e:
        print(f"Error inserting records: {e}")
        raise


def main(): # Main function to orchestrate the fetching of data and inserting it into the database
    try:
        data = mock_fetch_data() 
        conn = connect_to_db()
        create_table(conn)
        insert_records(conn, data)
    except Exception as e:
        print(f"Error in main function: {e}")
        raise   
    finally:
        if 'conn' in locals() and conn:
            conn.close()
            print("Database connection closed.")
