# -*- coding: utf-8 -*-
"""WEEK 1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1439ZkwPDmCWxSNbCYUfYwRPi4Zw6Ju1-
"""

# Importing libraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
Data = pd.read_csv('/content/world_air_quality_with_locations.csv')

# Check the first few rows of the dataset
print(Data.head())

# understanding data structure
Data.shape
Data.columns

Data.dtypes

# checking missing values
Data.isnull().sum()

# fill missing values
Data.fillna(0, inplace=True)

# checking unique values
print("unique values in Countries:",Data["Countries"].unique())
print("unique values in BC:",Data["BC"].unique())
print("unique values in CO:",Data["CO"].unique())
print("unique values in NO:",Data["NO"].unique())
print("unique values in NOX:",Data["NOX"].unique())
print("unique values in NO2:",Data["NO2"].unique())
print("unique values in O3:",Data["O3"].unique())
print("unique values in PM1:",Data["PM1"].unique())
print("unique values in PM10:",Data["PM10"].unique())
print("unique values in PM2.5:",Data["PM2.5"].unique())
print("unique values in SO2:",Data["SO2"].unique())

# Summary statistics
Data.describe()

# checking for duplicate data
Data.duplicated().sum()

# Data Cleaning
# Handle missing values
Data.fillna(0, inplace=True)

# Drop duplicate rows
Data.drop_duplicates(inplace=True)

Data.head()

# Data Visualization
import matplotlib.pyplot as plt
plt.figure(figsize=(6, 4))
BCconcentration = Data['BC']
plt.hist(BCconcentration, bins=20, color='skyblue', edgecolor='black')
plt.xlabel('BC Concentration')
plt.ylabel('Frequency')
plt.title('Distribution of BC Concentration')
plt.show()

COconcentration = Data['CO']
plt.hist(COconcentration, bins=20, color='pink', edgecolor='black')
plt.xlabel('CO Concentration')
plt.ylabel('Frequency')
plt.title('Distribution of CO Concentration')
plt.show()

NOconcentration = Data['NO']
plt.hist(NOconcentration, bins=20, color='red', edgecolor='black')
plt.xlabel('NO Concentration')
plt.ylabel('Frequency')
plt.title('Distribution of NO Concentration')
plt.show()

NO2concentration = Data['NO2']
plt.hist(NO2concentration, bins=20, color='green', edgecolor='black')
plt.xlabel('NO2 Concentration')
plt.ylabel('Frequency')
plt.title('Distribution of NO2 Concentration')
plt.show()

NOXconcentration = Data['NOX']
plt.hist(NOXconcentration, bins=20, color='purple', edgecolor='black')
plt.xlabel('NOX Concentration')
plt.ylabel('Frequency')
plt.title('Distribution of NOX Concentration')
plt.show()

O3concentration = Data['O3']
plt.hist(O3concentration, bins=20, color='grey', edgecolor='black')
plt.xlabel('O3 Concentration')
plt.ylabel('Frequency')
plt.title('Distribution of O3 Concentration')
plt.show()

PM1concentration = Data['PM1']
plt.hist(PM1concentration, bins=20, color='orange', edgecolor='black')
plt.xlabel('PM1 Concentration')
plt.ylabel('Frequency')
plt.title('Distribution of PM1 Concentration')
plt.show()

PM10concentration = Data['PM10']
plt.hist(PM10concentration, bins=20, color='yellow', edgecolor='black')
plt.xlabel('PM10 Concentration')
plt.ylabel('Frequency')
plt.title('Distribution of PM10 Concentration')
plt.show()

PM25concentration = Data['PM2.5']
plt.hist(PM25concentration, bins=20, color='cyan', edgecolor='black')
plt.xlabel('PM2.5 Concentration')
plt.ylabel('Frequency')
plt.title('Distribution of PM2.5 Concentration')
plt.show()

SO2concentration = Data['SO2']
plt.hist(SO2concentration, bins=20, color='olive', edgecolor='black')
plt.xlabel('SO2 Concentration')
plt.ylabel('Frequency')
plt.title('Distribution of SO2 Concentration')
plt.show()

import matplotlib.pyplot as plt
import pandas as pd

# Assuming 'Countries' is a column in your DataFrame for the x-axis
# Replace 'pollutants' with the list of pollutants you are interested in
pollutants = ['SO2']

# Set a threshold for high concentration (you might need to adjust this)
threshold = 50  # Example threshold, adjust based on your data

# Filter data for countries with high concentration for at least one pollutant
high_concentration_countries = Data[Data[pollutants].max(axis=1) > threshold]['Countries'].unique()

# Create a new DataFrame with only the filtered data
filtered_data = Data[Data['Countries'].isin(high_concentration_countries)]

# Scatter plot
# The figsize argument should only have two values (width, height)
plt.figure(figsize=(10, 6))  # Changed from (6, 4, 3) to (6, 4)

for pollutant in pollutants:
    plt.scatter(filtered_data['Countries'], filtered_data[pollutant], label=pollutant, alpha=0.5)

plt.xlabel('Countries')
plt.ylabel('SO2 Concentration')  # Use a general y-label
plt.title('Scatter Plot of Countries with High S02 Concentrations')
plt.legend()  # Add a legend to identify each pollutant
plt.xticks(rotation=90)  # Rotate x-axis labels for better readability if needed
plt.tight_layout()  # Adjust layout to prevent overlapping elements
plt.show()