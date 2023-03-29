from datetime import datetime
from openpyxl import Workbook
import pandas as pd

# read excel sheet "Dataset1" from "Fake_Data_Demo.xlsx" and assign data to veriable "dataframe1"
dataframe1 = pd.read_excel(r'/Users/rob/Downloads/Fake_Data_Demo.xlsx', sheet_name="Dataset1")
# Used .drop to remove the empty column "L_GENDER" and assign the resulting back to "dataframe1"
dataframe1 = dataframe1.drop(columns=['L_GENDER'])

# Target "M_SUBJECT_SSN" column and remove dashes in SSNs using the .replace method
dataframe1['M_SUBJECT_SSN'] = dataframe1['M_SUBJECT_SSN'].str.replace('-', '')

# Target "W_GRADE" column and assign it to variable "W_GRADE"
W_GRADE = dataframe1['W_GRADE']
# Filter cells with "/" and assign the filtered cells to variable "cellsWithSlash"
cellsWithSlash = dataframe1['W_GRADE'].str.contains('/')
# Used the str.split() method to split "cellsWithSlash" into two columns "W_RANK" and "W_GRADE"
dataframe1.loc[cellsWithSlash, ['W_RANK', 'W_GRADE']] = dataframe1.loc[cellsWithSlash, 'W_GRADE'].str.split('/', expand=True)

# Used the .replace method to replace all occurances of "Unclassified//For Official Use Only" with "CUI//PII"
dataframe1['B_INCIDENT_CLASSIFICATION'] = dataframe1['B_INCIDENT_CLASSIFICATION'].replace('Unclassified//For Official Use Only', 'CUI//PII')


I_INSTALLATION = dataframe1['I_INSTALLATION']
# Used the .unique method to filter unique installations
installations = I_INSTALLATION.unique()
# Used the len() method to count total unique installations
installationsCount = len(installations)
# Used the .tolist() method and assigned the Python list to the variable "uniqueInstallationList"
uniqueInstallationList = installations.tolist()
# Print the count
print("Total unique installations: ", installationsCount)
# Used .duplicated() method to identify dubplicates and assign them to the variable "duplicatedRecords"
duplicatedRecords = dataframe1[dataframe1.duplicated()]
print(duplicatedRecords)
# Used the .drop_duplicates() method to return dataset without duplicat records
dataframeNoDuplicates = dataframe1.drop_duplicates()

