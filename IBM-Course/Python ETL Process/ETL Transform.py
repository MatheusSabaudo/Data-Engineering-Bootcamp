# Transform data for ETL process

# Conversion function

def transform(data):
    # Convert height which is in inches to milimeters
     # Convert inches to meters and round off to two decimals (1 inch = 0.0254 meters)
    data['height'] = round(data['height'] * 0.0254, 2)

    # Convert weight which is in pounds to kilograms
     # Convert pounds to kilograms and round off to two decimals (1 pound = 0.453592 kilograms)
    data['weight'] = round(data['weight'] * 0.453592, 2)

    return data