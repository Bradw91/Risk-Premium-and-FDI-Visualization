import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from plotly import __version__
import cufflinks as cf
from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot
import plotly.graph_objs as go


init_notebook_mode(connected=True) ##connect notebook


#define function to convert percent sign to a float (needed to convert data in csv to readable values)
def p2f(x):
    return float(x.strip('%'))

Ctryprem = pd.read_csv(r"C:\Users\Admin\Desktop\Programming\IFC poverty project\ctryprem.csv",converters={'Equity Risk Premium':p2f}) # Data related to Country risk premium and Moody's rating (risk)
FDI = pd.read_csv(r"C:\Users\Admin\Desktop\Programming\IFC poverty project\API_BX.KLT.DINV.CD.WD_DS2_en_csv_v2_10399842.csv") #Foreign direct investment per country
Ctryprem.head()


#Chroropleth maps of market risk by Country
data = dict(
        type = 'choropleth',
        colorscale='Viridis',
        reversescale = True,
        locations = Ctryprem['Country'],
        locationmode = "country names",
        z = Ctryprem['Equity Risk Premium'],
        text = Ctryprem['Country'],
        colorbar = {'title' : 'Equity Risk Premium (%)'},
      )

layout = dict(
    title = 'Equity Risk Premiums Worldwide',
    geo = dict(
        showframe = True,
        projection = {'type':'mercator'}
    )
)

choromap = go.Figure(data = [data],layout = layout)
iplot(choromap,validate=False)


#Regression/coeff/correlation of Market risk to FDI amount
