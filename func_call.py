import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv("covid_19_india.csv")
class Call:

    def total_cases(self):
        final_casses = df.tail(36)
        return final_casses.Confirmed.sum()
    def active(self):
        final_cases = df.tail(36)
        return (final_cases['Confirmed']-final_cases['Deaths']-final_cases['Cured']).sum()
    def deaths(self):
        final_cases = df.tail(36)
        return final_cases['Deaths'].sum()
    def recover(self):
        final_cases = df.tail(36)
        return final_cases['Cured'].sum()
    def graph_create(self,case_type='Confirmed'):
        final_casses = df.tail(36)
        y_column = {
            'Total cases':'Confirmed',
            'Cured cases':'Cured',
            'Deaths':'Deaths',
        }.get(case_type,'Confirmed')
        print("val:",case_type)
        fig = px.bar(final_casses,x='State/UnionTerritory',y=y_column,barmode='group')
        fig.update_layout(title='Total Cases in India',xaxis_title='State/Union Territory',yaxis_title=y_column)
        print("val_last:",case_type)     
        return fig
    def states(self):
        df = pd.read_csv('covid_vaccine_statewise.csv')
        rd = df.loc[df['Updated On']=='09/08/2021',['Updated On','State','Male (Doses Administered)','Female (Doses Administered)','Transgender (Doses Administered)']]
        return rd['State']
    def pie_create(self,selected_state='India'):
        df = pd.read_csv('covid_vaccine_statewise.csv')
        rd = df.loc[df['Updated On']=='09/08/2021',['Updated On','State','Male (Doses Administered)','Female (Doses Administered)','Transgender (Doses Administered)']]
        trial = rd[rd['State']==selected_state]
        dose_data = trial.loc[df['State']==selected_state,['Male (Doses Administered)', 'Female (Doses Administered)', 'Transgender (Doses Administered)']]
        column_df = dose_data.squeeze().reset_index()
        column_df.columns = ['Category', 'Doses Administered']
        column_df = dose_data.squeeze().reset_index()
        column_df.columns = ['Category', 'Doses Administered']
        fig = px.pie(column_df,values='Doses Administered',names='Category',title='Gender Ratio')
        return fig
    def plot_sample(self):
        df = pd.read_csv('StatewiseTestingDetails.csv')
        rd = df.set_index('Date')
        trial = rd.loc['2021-08-10',['State','TotalSamples']]
        fig = px.scatter(trial,x='State',y='TotalSamples',title='State wise samples')
        return fig


     
