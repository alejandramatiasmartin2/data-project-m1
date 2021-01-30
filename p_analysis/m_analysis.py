import pandas as pd
from functools import reduce
def get_quantity(data_merged):
    # Creating Quantity column and renaming columns
    data_merged = data_merged.groupby(['country_code','Job Title','gender'])['uuid'].count().reset_index().rename(columns = {'gender':'Gender','uuid':'Quantity'})
    print('Quantity column added')
    return data_merged


def get_percentage(data_merged):
    # Creating Percentage column
    data_merged['Percentage'] = (data_merged['Quantity'] / data_merged['Quantity'].sum()) * 100
    data_merged["Percentage"] = data_merged["Percentage"].round(4).mul(100).astype(int).astype(str) + '%'
    print('Percentage column added')
    return data_merged

def merged_final_data(data_merged, countries_df):
    data_list2 = [data_merged, countries_df]
    data_merged = reduce(lambda left, right: pd.merge(left, right, on='country_code'), data_list2)
    data_merged = data_merged[['Country', 'Job Title', 'Gender', 'Quantity', 'Percentage']]
    print('table obtained')
    return data_merged


