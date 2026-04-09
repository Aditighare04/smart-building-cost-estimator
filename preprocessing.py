import pandas as pd

def preprocess_data(df):
    # Mapping categorical values to numbers

    location_map = {'Rural': 1, 'Urban': 2, 'Metro': 3}
    material_map = {'Low': 1, 'Medium': 2, 'High': 3}
    building_map = {'Residential': 1, 'Commercial': 2}

    # Apply mapping
    df['location'] = df['location'].map(location_map)
    df['material'] = df['material'].map(material_map)
    df['building_type'] = df['building_type'].map(building_map)

    return df