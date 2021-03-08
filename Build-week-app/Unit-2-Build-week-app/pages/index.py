# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd


from joblib import load
pipeline = load('assets/pipeline.joblib')


# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Wondering who might be the toughest competition at your next meet?

            Figure out which Crossfit athlete has potential to be competitive in the sport of Olympic weightlifting.

            ✅  W8Lifter is a fitness app that relies on machine learning to identify an individual's potential to be competitive in the sport of Weightlifting.

            ✅ W8Lifter is an intelligent fitness app that uses XGBoost algorithm to hone in on your next toughest competitor because we believe in ML-driven sports intel.

            """
        ),
        dcc.Link(dbc.Button('See for Yourself', color='primary'), href='/predictions')
    ],
    md=4,
)


column2 = dbc.Col(
    [	
	html.Img(src='assets/imagefile.jpg', className='img-fluid'),
	
		     ]
)


layout = dbc.Row([column1, column2])

        


