import plotly.express as px
import pandas as pd

df = pd.read_csv('../assets/countries.csv')

df['alpha3'] = df['alpha3'].str.upper()
df['color'] = None

# 4 coloring countries visited
# red
df.loc[df['alpha3'].isin(['CHN', 'POL', 'ITA', 'BIH', 'ROU', 'COL', 'MEX', 
    'BHS', 'THA', 'JPN', 'AZE', 'SVK', 'SVN', 'SRB', 'GTM', 'PRK', 'SGP', 
    'HUN', 'CZE', 'BGR', 'MNE', 'FRA', 'KOR', 'UKR', 'AUT', 'HRV', 'BEL', 
    'DNK', 'USA']), 'color'] = '#FF8360'

fig = px.choropleth(df, locations="alpha3", color="color")
fig.update_traces(showlegend=False, showscale=False)

fig.write_image("../assets/map.jpeg")
