import pandas as pd
import random
from datetime import datetime

# Load the generated crash data
crash_df = pd.read_csv("data/crashes.csv", sep=';', encoding='latin1')

# Define some fixed or example values for road attributes
roadway_functional_classes = ['Primary', 'Secondary', 'Tertiary']
access_controls = ['Full', 'Partial', 'None']
lighting_types = ['None', 'Streetlights', 'Daylight only']
presence_types = ['Present', 'Absent']
facility_types = ['Urban', 'Rural', 'Suburban']
bicycle_route = ['Yes', 'No']
bridge_ids = ['BR-001', 'BR-002', 'None', 'Autopont 1', 'BR-004', 'BR-006', 'Autopont 2', 'Autopont 3', 'Autopont 5']
curve_surelevation = ['Yes', 'No']
railway_ids = ['RW-001', 'RW-002', 'None']

# Helper to generate random road data
def generate_road_data(crash_df):
    road_data = []
    for _, row in crash_df.iterrows():
        crash_id = row['crashId']
        road_data.append({
            "roadId": f"Road_{crash_id}",
            "typologie": "Road",
            "crashId": crash_id,
            "roadwayInclinationSlope": random.choice(["Positif(+)", "Négatif(-)"]),
            "partOfNationalHighwaySystem": random.choice(["Yes", "No"]),
            "roadwayFunctionalClass": random.choice(roadway_functional_classes),
            "accessControl": random.choice(access_controls),
            "roadwayLighting": random.choice(lighting_types),
            "edglinePresenceType": random.choice(presence_types),
            "centerlinePresenceType": random.choice(presence_types),
            "laneLineMarkings": random.choice(["Marked", "Unmarked"]),
            "facility": random.choice(facility_types),
            "signedBicycleRoute": random.choice(bicycle_route),
            "mainlineNumberOfLanesAtIntersection": random.randint(1, 4),
            "crossStreetNumberOfLanesAtIntersection": random.randint(1, 4),
            "bridgeStructureIdentification": random.choice(bridge_ids),
            "curveRadius": random.randint(10, 500),
            "curveLength": random.randint(20, 800),
            "curveSurelevation": random.choice(curve_surelevation),
            "roadwayInclinationSlopePercent": random.randint(0, 15),
            "annualDailyAverageTrafficYear": random.randint(2010, 2025),
            "truckPercentage": random.randint(1, 30),
            "motorcyclePercentage": random.randint(1, 20),
            "laneWidth": random.randint(2, 4),
            "leftShoulderWidth": random.randint(0, 3),
            "rightShoulderWidth": random.randint(0, 3),
            "medianWidth": random.randint(0, 5),
            "railwayCrossingId": random.choice(railway_ids),
            "totalEnteringVehiclesYear": random.randint(10000, 100000),
            "totalEnteringVehicles": random.randint(100, 1000),
        })
    return pd.DataFrame(road_data)

road_df = generate_road_data(crash_df)
road_csv_path = "data/roads.csv"
road_df.to_csv(road_csv_path, sep=';', index=False)

road_csv_path

