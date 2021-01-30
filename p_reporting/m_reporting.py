import pandas as pd
from functools import reduce

def merged_final_data(data_merged, countries_df):
    print('Exporting the Data Frame...')
    data_list2 = [data_merged, countries_df]
    data_merged = reduce(lambda left, right: pd.merge(left, right, on='country_code'), data_list2)
    data_merged = data_merged[['Country', 'Job Title', 'Gender', 'Quantity', 'Percentage']]
    data_merged.to_csv('results/data_merged.csv')
    return data_merged

def export(data_merged, country):

        if country == 'all countries':
            print('Exporting All countries data...')
            data_merged.to_csv('results/all_countries_data.csv')
            return print('File exported')

        else:
            if country in data_merged['Country'].unique().tolist():
                data_merged= [data_merged['Country'] == country].to_csv(f'results/{country} results.csv')
                print('Exporting country data...')
            else:
                raise ValueError("Input is not in database")
            return print('File exported')