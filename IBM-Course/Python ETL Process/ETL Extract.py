# Composite Functions for ETL - Guide

import glob
import pandas as pd # pyright: ignore[reportMissingModuleSource]

list_csv = glob.glob('*.csv') #read all csv files in the current directory
list_csv:['source1.csv', 'source2.csv', 'source3.csv'] # pyright: ignore[reportInvalidTypeForm]

# Extraction function to read the csv file and return a dataframe

def extract_from_csv(file_to_process): 
    dataframe = pd.read_csv(file_to_process)
    return dataframe

df=extract_from_csv('source1.csv')

# Extraction function to read the json file and return a dataframe

def extract_from_json(file_to_process):
    dataframe = pd.read_json(file_to_process)
    return dataframe

df=extract_from_json('source1.json')

# Example of a function to extract data from a database

def extract():

    # create an empty data frame to hold extracted data
    extracted_data = pd.DataFrame(columns=['name', 'height', 'weight'])

    # process all csv files
    for csvfile in glob.glob('*.csv'):
        extracted_data = extracted_data.append(extract_from_csv(csvfile), ignore_index=True)

    # process all json files
    for jsonfile in glob.glob('*.json'):
        extracted_data = extracted_data.append(extract_from_json(jsonfile), ignore_index=True)

    return extracted_data

# Glob function

for csvfile in glob.glob('*.csv'):
    extracted_data = extracted_data.append(extract_from_csv(csvfile), ignore_index=True)

# Ignore index result in the data frame being reindexed after each append, which can be useful to maintain a continuous index across multiple files.