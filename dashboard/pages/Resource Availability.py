import streamlit as st
import pandas as pd
import random


data_points = []

for i in range(50):
    name = "Person " + str(i+1)
    condition = random.choice(
        ["Covid-19", "Flu", "Common cold", "Neumonia", "None", "Typhoid", "Malaria", "Dengue"])
    hospitals = random.choice(
        ["Hospital 1", "Hospital 2", "Hospital 3", "Hospital 4", "Hospital 5"])
    blood_units = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    days = random.randint(1, 14)
    blood_pressure = random.choice(["High", "Normal", "Low"])
    blod_bank = hospitals
    blood_units_available = blood_units
    temperature = str(round(random.uniform(35.5, 40.0), 1)) + " °C"

    data_points.append({
        "name": name,
        "Condition": condition,
        "days": days,
        "blood bank": blod_bank,
        "blood units available": blood_units_available,
        "blood pressure": blood_pressure,
        "temperature": temperature
    })

df = pd.DataFrame(data_points)

st.table(df)