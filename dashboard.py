import pandas as pd
import numpy as np

import plotly.graph_objects as go
import dash
from dash import html,dcc
import dash_bootstrap_components as dbc
from func_call import Call
from dash.dependencies import Input, Output
call=Call()

external_stylesheets = [
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-MCw98/5FnGE8JT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin': 'anonymous'
    }
]

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout=html.Div([
    html.H1('Corona Virus Pandemic',style={'color':'white','textAlign':'center'}),
    html.Div([html.Div([
        html.Div([
            html.Div([
                html.H3('Total case',className='text-light'),
                html.H4(call.total_cases(),className='text-light')
            ],className='card-body')
         ],className='card',style={'backgroundColor': 'red', 'color': 'black'})
    ],className='col-md-3 mb-3'),
              html.Div([html.Div([
            html.Div([
                html.H3('Active',className='text-light'),
                html.H4(call.active(),className='text-light')
            ],className='card-body')
         ],className='card bg-info')],className='col-md-3 mb-3'),
         html.Div([html.Div([
             html.Div([
                 html.H3('Recover',className='text-light'),
                 html.H4(call.recover(),className='text-light')
             ],className='card-body')
         ],className='card bg-warning')],className='col-md-3'),
          html.Div([html.Div([
             html.Div([
                 html.H3('Deaths',className='text-light'),
                 html.H4(call.deaths(),className='text-light')
             ],className='card-body')
         ],className='card bg-success')],className='col-md-3')
         ],className='row'),
         html.Div([
              html.Div([html.H2("Gender wise Vaccination",style={'color':'white'}),
                   dcc.Dropdown(
                         id='state',
                         options=[{'label': i, 'value': i} for i in call.states()],
                         value='India',
                         placeholder='Select the state',
                         clearable=True,
                         searchable=True
                   ),
                   dcc.Graph(id='pie',style={'height':'400px'})
                   ],className='col-md-6'),
                   html.Div([
                    html.H3('Statewise Sample Taken',style={'color':'white'}),
                    dcc.Graph(figure = call.plot_sample(),style={'height':'400px'})
                   ],className='col-md-6')
                   ],className='row'),
         html.Div([html.H2("Pandemic Data Graph",style={'color':'white'}),
                   dcc.Dropdown(
                       id='dropdown',
                       options=[
                           {'label': 'Total Cases', 'value': 'Confirmed'},
                           {'label': 'Deaths', 'value': 'Deaths'},
                           {'label': 'Recover', 'value': 'Cured'},
                       ],
                       value='type',
                       placeholder='Choose the type',
                       clearable=True,
                       searchable=True,
                   ),
                   dcc.Graph(id='bar',className='col-md-12')
                   ],className='row')
],className='container',style={'backgroundColor': 'black', 'padding': '20px'})


@app.callback(Output('bar','figure'),[Input('dropdown','value')])
def update_graph(selected_value):
        print(selected_value)
        return call.graph_create(selected_value or 'Confirmed')
@app.callback(Output('pie','figure'),[Input('state','value')])
def state_wise(selected_option):
      return call.pie_create(selected_option or 'India')
if __name__=='__main__':
    app.run(debug=True)