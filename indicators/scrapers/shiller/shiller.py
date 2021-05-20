'''
 @author:Christopher Wong
 @date: 07 Mar 2021

 This module returns metrics, developed by Yale economist Prof. Robert Shiller,
 from http://www.econ.yale.edu/~shiller/data.htm
'''

import pandas as pd

def get_cape_df() -> pd.DataFrame:
    '''
    Obtains the CAPE ratio data
    :return: pandas dataframe
    '''
    colname_dict = {'Date': str,
                'S&P Composite Price': float,
                'Dividend': float,
                'Earnings': float,
                'CPI': float,
                'Date Fraction': str,
                'Consant Maturity 10Yr Treasury': float,
                'Real Price': float,
                'Real Dividend': float,
                'Real TR Price': float,
                'Real Earnings': float,
                'Real TR Scaled Earnings': float,
                'Cyclically Adjusted CAPE': float,
                'EMPTY.13': str,
                'Cyclically Adjusted TR CAPE': float,
                'EMPTY.15': str,
                'Excess CAPE Yield': float,
                'Monthly TR Bond': float,
                'Monthly Real TR Bond': float,
                'Annualized 10Yr Real Stock Return': float,
                'Annualized 10Yr Real Bond Return': float,
                'Annualized 10Yr Real Excess Return': float}

    df = pd.read_excel(io='http://www.econ.yale.edu/~shiller/data/ie_data.xls',
                       sheet_name='Data', skiprows=8, skipfooter=1, header=None,
                       names=colname_dict.keys(), dtype=colname_dict,
                       usecols=range(len(colname_dict.keys())))

    return df
