import pandas as pd
import re
import requests


def export(data_merged, country):
    """
    This function will create the final report, using the columns required and choosing between a specific Country or All
    """
    if country == 'All countries':
        final_data_merged = pd.DataFrame(data_merged.groupby(['Country','Job Title', 'Gender']).agg({'Quantity':['sum'], 'Percentage':['sum']}).reset_index())
        final_data_merged.to_csv('results/final.csv', index=False)
        print('Converted to CSV!')
    elif (dataframe['Country_Name'] == country).any():
        reporting = pd.DataFrame(dataframe[(dataframe['Country_Name'] == country)].groupby(['Country_Name','title', 'gender']).agg({'Quantity':['sum'], 'Percentage':['sum']}).reset_index())
        reporting.to_csv('Output/reporting.csv', index=False)
        print('Converted to CSV!')
    else:
        print('ERROR: Country selected is not in Database')