import pandas as pd
import random
import uuid

# Load the crash data
crash_df = pd.read_csv("data/crashes.csv", sep=';', encoding='latin1')

vehicle_rows = []
person_rows = []

# Sample data options
countries = ["Senegal", "Gambie", "Guinee Bissau", "Mali", "France"]
brands = ["Toyota", "Peugeot", "Hyundai", "Renault", "Mercedes", "BMW", "Bentley", "Chrysler", "Ford", "Honda", "Alfa Romeo", "Mazda", "Kia", "Acura"]
models = ["Corolla", "308", "Elantra", "Clio", "Sprinter", "Mustang", "CR-V FWD", "K5", "Integra", "Equinox", "Urus", "Roma", "Highlander", "Tundra"]
genders = ["Masculin", "Feminin"]
person_types = ["Conducteur", "Pieton", "Repondant accident", "Force de l'ordre"]
injury_status = ["Souscpiçion de blessure sévère", "Souspiçion de blessure mineure", "Décédé(e)", "Pas de blessure apparente"]

def random_year(start=1990, end=2025):
    return str(random.randint(start, end))

def generate_vehicle(crash_id, seq_num):
    vehicle_id = f"Vehicle_{crash_id}_{seq_num}"
    return {
        "vehicleId": vehicle_id,
        "typologie": "Vehicle",
        "crashId": crash_id,
        "numeroIdentifiant": str(uuid.uuid4()),
        "numeroSequentiel": str(seq_num),
        "paysEnregistrement": random.choice(countries),
        "anneeEnregistrement": random_year(),
        "numeroImmatriculation": f"AA-{random.randint(1000, 9999)}-SN",
        "modele": random.choice(models),
        "anneeModele": random_year(2000, 2024),
        "marque": random.choice(brands),
        "nombreOccupants": random.randint(1, 5),
        "vitesseLimiteApplicable": random.choice(["30", "50", "70", "30", "100", "110"]),
        "nombreTotalVoies": random.randint(1, 4),
        **{f: 0 for f in [
            "alignmentHorizontaleDroite", "alignmentHorizontaleCourbureGauche",
            "alignmentHorizontaleCourbureDroite", "inclinaisonRouteNivele",
            "inclinaisonRouteHauteur", "inclinaisonRouteMontee",
            "inclinaisonRouteDescente", "inclinaisonRouteAffaissement",
            "motorVehicleUnitType", "bodyTypeCategory", "specialMotorVehicleFunction",
            "emergencyMotorVehicleUse", "directionTravelBeforeCrash",
            "trafficWayDescriptionForMotorVehicle", "presenceTrafficControlDevice",
            "trafficControlDeviceType", "motorVehicleManeuver", "vehicleDamageInitialPoint",
            "vehicleDamageAreas", "vehicleDamageExtentDamage", "sequenceOfEventsFirstEvent",
            "sequenceOfEventsSecondEvent", "sequenceOfEventsThirdEvent", "sequenceOfEventsFourthEvent",
            "mostHarmfulEventForThisVehicle"
        ]},
        "busUse": "Non lié à un bus",
        "hitAndRun": random.choice(["Oui", "Non"]),
        "vehicleAutomationSystems": "Aucun",
        "vehicleAutomationLevels": "Aucun",
        "vehicleAutomationLevelsEngaged": "Pas de niveau engagés"

    }

def generate_person(crash_id, veh_seq_num, person_seq_num):
    return {
        "personId": f"Person_{crash_id}_{person_seq_num}",
        "typologie": "Person",
        "crashId": crash_id,
        "nom": f"Nom_{uuid.uuid4().hex[:6]}",
        "dateNaissance": f"{random.randint(1950, 2015)}-01-01",
        "numeroPermis": f"D{random.randint(10000,99999)}",
        "violationCodeOne": "Excès de vitesse",
        "violationCodeTwo": "Non respect signes",
        "concentrationAlcoolSang": f"{round(random.uniform(0.0, 1.5), 2)}",
        "numeroSequentiel": str(person_seq_num),
        "identifiantRepondantServiceUrgence": str(uuid.uuid4()),
        "numeroServiceUrgenceRepondant": f"78{random.randint(1000000, 9999999)}",
        "nomOuNumeroDuRepondantDuServiceUrgence": "Urgence112",
        "genre": random.choice(genders),
        "typePersonne": random.choice(person_types),
        "involvedPersonIsIncidentResponder": random.choice(["Oui", "Non"]),
        "typeOfIncidentResponder": random.choice(["Sapeurs-Pompiers", "Policier", "SAMU"]),
        "statutBlessures": random.choice(injury_status),
        "identifiantVehicule": f"Vehicle_anonyme_{crash_id}",
        "positionAssise": "Conducteur",
        "positionAssiseAutre": "",
        "equipementsSecurite": random.choice(["Ceinture", "Airbag"]),
        "casqueSecurite": "Non",
        "airbagDeploye": random.choice(["Oui", "Non"]),
        "juridictionLivrantPermis": "Senegal",
        "classePermis": "B",
        "approbationsLieesPermis": "Approbations",
        "liaisonVitesse": "Oui lié à la vitesse",
        **{f: "" for f in [
            "driverActionAtTimeOfCrashOne", "driverActionAtTimeOfCrashTwo",
            "driverActionAtTimeOfCrashThree", "driverActionAtTimeOfCrashFour",
            "driverDistractedBy", "conditionAtTimeOfCrashOne",
            "conditionAtTimeOfCrashTwo", "lawEnforcementSuspectsAlcoholUse",
            "alcoholUseTestStatus", "alcoholUseTestType", "lawEnforcementSuspectsDrugUse",
            "drugUseTestStatus", "drugUseTestType", "drugUseTestResult", "circonstances",
            "goingFromSchool", "circonstancesAtTimeOne", "circonstancesAtTimeTwo",
            "locationAtTimeOfCrash", "safetyEquipmentUsedOne", "safetyEquipmentUsedTwo",
            "unitNumberMotorVehicleStrikingNonMotorist",
            "sourceOfTransportationForFirstMedicalFacility",
            "initialPointOfContactOnNonMotoristDropdown"
        ]}
    }

# Loop to generate all
for _, crash in crash_df.iterrows():
    crash_id = crash["crashId"]
    geo = crash["geolocations"]

    num_vehicles = random.randint(1, 3)
    for v_num in range(1, num_vehicles + 1):
        vehicle = generate_vehicle(crash_id, v_num)
        vehicle_rows.append(vehicle)
        num_persons = random.randint(1, 4)
        for p_num in range(1, num_persons + 1):
            person = generate_person(crash_id, v_num, p_num)
            person_rows.append(person)

# Export all to CSV
pd.DataFrame(vehicle_rows).to_csv("data/vehicles.csv", sep=';', index=False, encoding='latin1')
pd.DataFrame(person_rows).to_csv("data/persons.csv", sep=';', index=False, encoding='latin1')

print("✅ vehicle.csv, and person.csv generated from crash_data.csv!")

