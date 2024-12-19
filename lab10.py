#a
#case1:
import pandas as pd
import plotly.express as px
dollar_conv = pd.read_csv('CUR_DLR_INR.csv')
fig = px.line(dollar_conv, x='DATE', y='RATE', title='Dollar vs Rupee')
print(dollar_conv.head())
fig.show()

#case2:
import pandas as pd
import plotly.express as px
runs_scored = pd.read_csv('AusVsInd.csv')
fig = px.line(runs_scored, x='Overs', y=['AUS', 'IND'], markers=True)
fig.update_layout(title='Australia vs India ODI Match', xaxis_title='OVERS',
yaxis_title='RUNS', legend_title='Country')
fig.show()

#case3:
import pandas as pd
import plotly.express as px
runs_scored = pd.read_csv('AusVsInd.csv')
fig = px.bar(runs_scored, x='Overs', y=['AUS_RPO', 'IND_RPO'], barmode='group')
fig.update_layout(title='Australia vs India ODI Match', xaxis_title='OVERS', yaxis_title='RUNS',
legend_title='Country')
fig.show()

#b
#case1:
import plotly.express as px
import pandas as pd
data=pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_with_codes.csv')
fig = px.choropleth(data, locations='iso_alpha', color='gdpPercap', hover_name='country',
projection='natural earth', title='GDP per Capita by Country')
fig.show()

#case2:
import json
import numpy as np
import pandas as pd
import plotly.express as px
india_states = json.load(open("states_india.geojson", "r"))
df = pd.read_csv("india_census.csv")
state_id_map = {}
for feature in india_states["features"]:
    feature["id"] = feature["properties"]["state_code"]
    state_id_map[feature["properties"]["st_nm"]] = feature["id"]
df = pd.read_csv("india_census.csv")
df["Density"] = df["Density[a]"].apply(lambda x:int(x.split("/")[0].replace(",", "")))
df["id"] = df["State or union territory"].apply(lambda x: state_id_map[x])
print(df.head())
fig = px.choropleth(
    df, locations="id",
    geojson=india_states,
    color="Population",
    hover_name="State or union territory",
    hover_data=["Density", "Sex ratio", "Population"],
    title="India Population Statewise",)
fig.update_geos(fitbounds="locations", visible=False)
fig.show()
