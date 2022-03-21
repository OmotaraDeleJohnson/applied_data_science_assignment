#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 16:41:46 2022

@author: omotaradele-johnson
"""

import pandas as pd
import matplotlib.pyplot as plot


NGA = pd.read_csv('/Users/omotaradele-johnson/Documents/Applied data Science/Dataset_NGA.csv',delim_whitespace=True)
print(NGA)
header = NGA.columns
print(header)
print(NGA.loc['Rural_population'])

# represent Population_total as 'pol'
# ,, Rural_population as 'rur'
# ,, Urban_population as 'urb'
# ,, Population_female as 'poF'
# ,, Population_male as 'pom'
# ,, Death_rate_crude as 'drC'
# ,, infant_deaths as 'ID'
data = {
        "pol": NGA.loc['Population_total'],
        "rur": NGA.loc['Rural_population'],
        "urb": NGA.loc['Urban_population'],
        "poF": NGA.loc['Population_female'],
        "poM": NGA.loc['Population_male'],
        "drC": NGA.loc['Death_rate_crude'],
        "iD": NGA.loc['infant_deaths']
        }

# For Bar Chart
NGA2 = pd.DataFrame(data = data,index=NGA.columns);

NGA2.plot.bar(rot = 0,title='Nigeria Population Estimate & projections');
plot.yticks([100000000,200000000,300000000])
plot.draw();


# For Pie Chart

pieNGA = pd.DataFrame({'population': NGA.columns,
                      'rural population': NGA.loc['Rural_population']})
Ruralplot = plot.subplot(121, aspect='equal')
print(pieNGA)
pieNGA.groupby(['population']).sum().plot(kind='pie',y='rural population',labels=pieNGA['population'],ax=Ruralplot, autopct='%1.1f%%', 
 startangle=90, shadow=False,fontsize=8,legend = False)

pieNGA2 = pd.DataFrame({'population_year': NGA.columns,
                      'urban population': NGA.loc['Urban_population']})
Urbanplot = plot.subplot(121, aspect='equal')
print(pieNGA2)
pieNGA2.groupby(['population_year']).sum().plot(kind='pie',y='urban population',labels=pieNGA2['population_year'],ax=Urbanplot, autopct='%1.1f%%', 
 startangle=90, shadow=False,fontsize=8,legend = False)



# For LINE Graph
Year = NGA.columns
female_pop = NGA.loc['Population_female']


plot.plot(Year, female_pop,label="female population")

plot.xlabel('Year')
plot.ylabel('Population')
plot.title('NGA Female population projections')
plot.xticks(Year)
plot.yticks([90000000,100000000,110000000])
#plot.show()


male_pop = NGA.loc['Population_male']
print(male_pop)

plot.plot(Year, male_pop,label='male projections')

plot.xlabel('Year')
plot.ylabel('Population')
plot.title('NGA population projections')
plot.xticks(Year)
plot.yticks([90000000,100000000,110000000])
plot.legend()
plot.show()