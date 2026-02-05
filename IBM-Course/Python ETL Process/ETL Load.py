# Load process for ETL pipeline

def load(targetfile, data_to_load):
    data_to_load.to_csv(targetfile)

targetfile = 'transformed_data.csv'

load(targetfile, transformed_data) # pyright: ignore[reportUndefinedVariable]

# Loggin Entries

from datetime import datetime

def log(message):
    timestamp_format = '%Y-%m-%d %H:%M:%S'  # Year-Month-Day Hour:Minute:Second
    now = datetime.now()  # get current date and time
    timestamp = now.strftime(timestamp_format)
    with open("logfile.txt","a") as f: #write down the log entry in a txt file
        f.write(timestamp + ',' + message + '\n')


# Final Call

log ("ETL Job Started")

log("Extraction phase Started")
extracted_data = extract()  # pyright: ignore[reportUndefinedVariable]
log("Extraction phase Ended")

log("Transformation phase Started")
transformed_data = transform(extracted_data)  # pyright: ignore[reportUndefinedVariable]
log("Transformation phase Ended")

log("Loading phase Started")
load(targetfile, transformed_data)  # pyright: ignore[reportUndefinedVariable]
log("Loading phase Ended")

log("ETL Job Ended")