#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 16:41:46 2022

@author: omotaradele-johnson
"""

import pandas as pd
import matplotlib.pyplot as plot

df = pd.read_csv('/Users/omotaradele-johnson/Documents/Applied data Science/Dataset_NGA.csv',delim_whitespace=True)
print(df)
header = df.columns
print(header)

# represent Population_total as 'pol'
# ,, Rural_population as 'rur'
# ,, Urban_population as 'urb'
# ,, Population_female as 'poF'
# ,, Population_male as 'pom'
# ,, Death_rate_crude as 'drC'
# ,, infant_deaths as 'ID'
data = {
        "pol": df.loc['Population_total'],
        "rur": df.loc['Rural_population'],
        "urb": df.loc['Urban_population'],
        "poF": df.loc['Population_female'],
        "poM": df.loc['Population_male'],
        "drC": df.loc['Death_rate_crude'],
        "iD": df.loc['infant_deaths']
        }


df2 = pd.DataFrame(data = data,index=df.columns);

df2.plot.bar(rot = 0,title='Nigeria Population Estimate & projections');
plot.yticks([100000000,200000000,300000000])
plot.draw();
#plot.show();

pp = df.iloc[1]
print(pp)
