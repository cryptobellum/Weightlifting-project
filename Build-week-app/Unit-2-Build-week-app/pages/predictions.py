import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_daq as daq
import dash_html_components as html
from dash.dependencies import Input, Output, State
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score
import pandas as pd
from joblib import load
#from pages import index, predictions, insights, process
import numpy as np

pipeline = load('assets/pipeline.joblib')

from app import app

column1 = dbc.Col(
    [
        dcc.Markdown('## Predictions', className='mb-5'), 
        dcc.Markdown('#### Age'), 
        
        #dcc.Input(
        #placeholder='Enter a value...',
        #type='text',
        #value=''
#),
        dcc.Slider(
            id='age', 
            min=18, 
            max=65, 
            step=2, 
            value=50, 
            #marks={n: str(n) for n in range(23,70,5)}, 
            marks={
                18: '18',
                30: '30',
                40: '40',
                50: '50',
                65: '65'
            },
            className='mb-5', 
        ), dcc.Markdown('', id='out1'),


        
        
        dcc.Markdown('#### Snatch'), 
        dcc.Slider(
            id='snatch', 
            min=35, 
            max=400, 
            step=5, 
            value=0, 
            marks={0:'0',
                    50:'50',
                    100:'100',
                    150:'150',
                    200:'200',
                    250:'250',
                    300:'300',
                    350:'350',
                    400:'400',
                    450:'450'},
            className='mb-5', 
        ), dcc.Markdown('', id='out2'),

  

        
        
        
        

        
        dcc.Markdown('#### Deadlift'), 
        
dcc.Slider(
            id='deadlift', 
            min=35, 
            max=400, 
            step=1, 
            value=0, 
            marks={0:'0',
                    50:'50',
                    100:'100',
                    150:'150',
                    200:'200',
                    250:'250',
                    300:'300',
                    350:'350',
                    400:'400',
                    450:'450'},
            className='mb-5'
        ), dcc.Markdown('', id='out3'),


        
        
    #dbc.Button('See if you can be competitive in Weightlifting', id='button', n_clicks=1, color='primary',
     #   style=dict(marginTop=1.75, marginBottom=10)
      #  ),  
    ],
    md=4, 
)

column2 = dbc.Col(
    [
        html.H2('Competitive Potential for Weightlifting', className='mb-5'), 
        html.Div(id='prediction-content', className='lead'),
        #dcc.Markdown("Here is your prediction", id='out1'),
        #html.Div(id='prediction-content', className='lead', style={'marginBottom': '10px'}),  

        
 #       daq.Gauge(
  #          id='my-daq-gauge',
   #         color={"gradient":True,"ranges":{"green":[0,6],"yellow":[6,8],"red":[8,10]}},
    #        max=10,
     #       value=5,
      #      min=0
       # )

        html.Img(src='assets/silhouette.png', className='img-fluid'),
        #html.H4(id='prediction-content', style={'fontWeight':'bold'}),
        #html.Div(
    	#dcc.Graph(id='shap-plot')
    	#)
    ]
)

layout = dbc.Row([column1, column2])


#@app.callback(

 #   [Output('prediction-content', 'children')],
  #  #Output('shap-plot', 'figure')],
   # [Input('button','n_clicks')],
    #[State('age', 'value'), State('snatch', 'value'),
    #State('deadlift', 'value')], 
    
#)


#def predict(clicked, age, snatch, deadlift):
 #   if clicked:
  #      df = pd.DataFrame(
   #     columns=['age', 'snatch', 'deadlift'],
    
    #    data=[[age, snatch, deadlift]]
        
     #   )
    

      #  y_pred = pipeline.predict(df)[0]
        
       # return [f'The prediction is: {y_pred}.']

    
@app.callback(

    [Output('prediction-content', 'children')], 
    #Output('shap-plot', 'figure')],
    #Output('shap-plot', 'figure')],
    #[Input('button','n_clicks')],
    #[State('age', 'value'), State('snatch', 'value'),
    #State('deadlift', 'value')], 
    [Input('age', 'value'),
    Input('snatch', 'value'),
    Input('deadlift', 'value'),]
)


def predict(age, snatch, deadlift):
    #if clicked:
        df = pd.DataFrame(
        columns=['age', 'snatch', 'deadlift'],
    
        data=[[age, snatch, deadlift]]
        
        )
    

        y_pred = pipeline.predict(df)[0]
        
        return [f'The prediction is: {y_pred}.']
        #pred_out = [f'The prediction is {y_pred}.']

@app.callback(
    Output(component_id='out1', component_property='children'),
    [Input(component_id='age', component_property='value')]
)
def update_output_div(input_value):
    return 'The age you\'ve entered is "{}"'.format(input_value)

@app.callback(
    Output(component_id='out2', component_property='children'),
    [Input(component_id='snatch', component_property='value')]
)
def update_output_div(input_value):
    return 'The weight for snatch you\'ve entered is "{}" pounds'.format(input_value)
        
			  
@app.callback(
    Output(component_id='out3', component_property='children'),
    [Input(component_id='deadlift', component_property='value')]
)
def update_output_div(input_value):
    return 'The weight for deadlift you\'ve entered is "{}" pounds'.format(input_value)