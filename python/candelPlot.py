import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

import plotly.graph_objects as go
import glob 
import pandas as pd
from datetime import datetime



f = open("PumpSymbols.csv","r")
Lines = f.readlines()
for line in Lines:
    Symbol=line[:-1]
    print('Processing ', Symbol)
    Path=(r"../data/"+Symbol+".csv")
    df = pd.read_csv(Path)
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Candlestick(x=df['Date'],open=df['Open'],high=df['High'],low=df['Low'],close=df['Close']),secondary_y=True)
    fig.add_trace(go.Bar(x=df['Date'], y=df['Volume']),secondary_y=False)
    fig.layout.yaxis2.showgrid=False
    fig.show()
print("..Over!!!")


