from pyjstat import pyjstat
import requests
import os
import json
from datetime import datetime
import locale
import io
import pandas as pd
import pycountry
os.makedirs('data', exist_ok=True)

#Trade Union Density Rate Worldwide Latest Year
df = pd.read_csv('https://sdmx.ilo.org/rest/data/ILO,DF_ILR_TUMT_NOC_RT/?format=csv&startPeriod=2010&lastNObservations=1')
country_codes = {country.alpha_3: country.name for country in pycountry.countries}
df['country_name'] = df['REF_AREA'].map(country_codes)
df.to_csv('data/Trade_Union_Density_Rate_ILO_Latest.csv', index=True)

#Trade Union Density Rate Worldwide All Years
df = pd.read_csv('https://sdmx.ilo.org/rest/data/ILO,DF_ILR_TUMT_NOC_RT/?format=csv')
country_codes = {country.alpha_3: country.name for country in pycountry.countries}
df['country_name'] = df['REF_AREA'].map(country_codes)
df_new = df.pivot(index='country_name', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.to_csv('data/Trade_Union_Density_Rate_ILO_All_Years.csv', index=True)

#Collective Bargaining Coverage Rate Worldwide Latest Year
df = pd.read_csv('https://sdmx.ilo.org/rest/data/ILO,DF_ILR_CBCT_NOC_RT/?format=csv&startPeriod=2010-01-01&lastNObservations=1')
country_codes = {country.alpha_3: country.name for country in pycountry.countries}
df['country_name'] = df['REF_AREA'].map(country_codes)
df.to_csv('data/Collective_Bargaining_Rate_ILO_Latest.csv', index=True)

#Collective Bargaining Coverage Rate Worldwide All Years
df = pd.read_csv('https://sdmx.ilo.org/rest/data/ILO,DF_ILR_CBCT_NOC_RT/?format=csv')
country_codes = {country.alpha_3: country.name for country in pycountry.countries}
df['country_name'] = df['REF_AREA'].map(country_codes)
df_new = df.pivot(index='country_name', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.to_csv('data/Collective_Bargaining_Rate_ILO_All_Years.csv', index=True)