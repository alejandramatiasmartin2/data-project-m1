import argparse
from p_acquisition import m_acquisition as mac
from p_wrangling import m_wrangling as mwr
from p_analysis import m_analysis as man
from p_reporting import m_reporting as mre

def argument_parser() :


    parser = argparse.ArgumentParser(description='indicate path...')
    
    return args


def main(path,country):

    print('starting pipeline...')
    data_base = mac.get_data()
    unique_jobs = mac.get_jobs_id(data_base)
    jobs_api = mac.get_jobs_api(data_base,unique_jobs)
    gender_c_cleaned = mwr.clean_gender(jobs_api)
    quantity_addition = man.get_quantity(gender_c_cleaned)
    data_merged = man.get_percentage(quantity_addition)
    countries_df = mac.get_country_codes()
    final_data_merged = man.merged_final_data(data_merged, countries_df)
    exported =  mre.export(data_merged, country)
    print('pipeline is complete!')


if __name__ == '__main__':

    arguments = argument_parser()
    main(arguments.path,arguments.country)
