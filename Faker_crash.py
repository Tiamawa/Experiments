import csv
import random
from datetime import datetime, timedelta
from faker import Faker
import uuid
import pandas as pd


fake = Faker('fr_FR')
Faker.seed(42)
random.seed(42)

# Regions and departments mapping
region_departments = {
    "Dakar": ["Dakar", "Guediawaye", "Pikine", "Rufisque"],
    "Thies": ["Thies Nord", "Thies Ouest", "Thies None"],
    "Ziguinchor": ["Ziguinchor", "Oussouye", "Bignona"]
}

# Constants
typologies = {
    "Crash": "Crash",
    "Road": "Road",
    "Vehicle": "Vehicle",
    "Person": "Person"
}

def generate_crash_datetime():
    base = datetime(2023, 11, 22, 0, 0, 0)
    offset = timedelta(minutes=random.randint(0, 1440))
    dt = base + offset
    return dt.strftime("%d/%m/%Y"), dt.strftime("%H:%M:%S"), dt

def get_random_geo():
    return f"{random.uniform(12.0, 16.0):.6f},{random.uniform(-17.0, -13.0):.6f}"

def generate_crash_data(n=110):
    crash_data = []
    crash_ids = []

    for _ in range(n):
        region = random.choice(list(region_departments.keys()))
        department = random.choice(region_departments[region])
        date_str, time_str, dt = generate_crash_datetime()
        crash_id = f"ACC_{region}-{department}-{date_str}-{time_str}"
        crash_ids.append(crash_id)

        crash_data.append({
            "crashId": crash_id,
            "typologie": typologies["Crash"],
            "typePropriete": random.choice(["Publique", "Privée"]),
            "situationParRapportChaussee": random.choice(["Sur chaussée", "Hors chaussée", "Pas une route"]),
            "date": date_str,
            "hour": time_str,
            "geolocations": get_random_geo(),
            "region": region,
            "department": department,
            "firstHarmfulEvent": random.choice([
                "C_Piéton", "C_Cycliste", "C_Non-Motorisé_Véhicule Ferroviaire",
                "C_Automobile Parqué", "C_Zone de Travaux ou Maintenance", "C_OF_Remblais"
            ]),
            "locationFirstHarmfulEvent": random.choice([
                "Sur la chaussée", "Accotement de Route", "Séparateur de Voies", "Passage Piéton"
            ]),
            "manerOfCrash": fake.word(),
            "weatheConditions": random.choice(["Angle", "Choc Latéral Même Sens", "Choc Latéral Direction Opposée", "e L'arrière Vers Les Côtés"
            ]),
            "lightConditions": random.choice(["Lumière du jour", "Crépuscule", "Crépuscule Sombre et Eclairé", "Crépuscule Sombre Non Eclairé"]),
            "roadSurfaceConditions": random.choice(["Sèche", "Humide", "Eau Stagnante ou Circulante", "Inconnu"]),
            "contribEnvCirconConditions": random.choice(["Obstructions visuels", "Eblouissement", "Animal sur la chaussée", "Conditions atmosphériques"]),
            "contribRoadCirconConditions": random.choice(["Backup-accident antérieur", "Backup-accident antérieur non recurrent", "Backup-embouteillage normal", "Présence de cabine de péage", "Conditions de la surface de la chaussée", "Obstruction sur la chaussée", "Débris"]),
            "relationToJunction": random.choice(["Pas un croisement", "Intersection", "Entrée/Sortie d'une rampe", "Dans une zone différente d'un échangeur", "Au niveau d'un échangeur"]),
            "typeIntersection": random.choice(["Intersection sur quatres voies", "Intersection en T", "Intersection en Y", "Intersection en L"]),
            "schoolBusRelated":   random.choice(["Non implication d'un bus scolaire", "Oui, Bus Scolaire impliqué directement", "Oui, Bus Scolaire impliqué indirectement"]),
            "workZoneRelated": random.choice(["Non lié à une zone de travaux", "Lié à une zone de travaux"]),
            "locationWorkZoneRelated": fake.word(),
            "typeWorkZoneRelated": fake.word(),
            "workersPresenceWorkZoneRelated": fake.word(),
            "lawEnforcementPresenceWorkZoneRelated": fake.word(),
        })

    return crash_data, crash_ids

crash_data, crash_ids = generate_crash_data(n=30)
crash_csv_path = "data/crashes.csv"
df_crash = pd.DataFrame(crash_data)
df_crash.to_csv(crash_csv_path, sep=';', index=False)
crash_data[:2]  # Show first two entries for verification

