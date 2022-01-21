import numpy as np
import pandas as pd

import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output

import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

CHART_THEME = 'plotly_white'

def get_source(x):
    if x.startswith('SJ'): return 'St. Jude' 
    if x.startswith('TH'): return 'TreeHouse'
    if x.startswith('SRR'): return 'GTEx'
    if x.startswith('TCGA'): return 'TCGA'
    if x.startswith('TARG'): return 'TARGET'


""" Load data. """

tab = pd.read_hdf('./ref/df9sjn_table_211129.h5')
lab = pd.read_hdf('./ref/df9sjn_lab_201204.h5')
cli = pd.read_hdf('./ref/df9sjn_cli_201204.h5')

cli['source']= [get_source(x) for x in cli.index]

clusters_labels = [{'label': tab['Code'].iloc[i]+' '+tab['Short Name'].iloc[i],
                    'value': i} for i in range(tab.shape[0])] 

""" Set up the dashboard. """

app = dash.Dash()

app.layout = html.Div(id = 'parent', children = [

        html.H1(id = 'H1', children = 'OTTER Dashboard Mock-up', style = {'textAlign':'center',
                                                            'marginTop':40,'marginBottom':40, 
                                                            'font-family':'Helvetica'}, 
                                               className='text-center text-primary, mb-3'), 

        dcc.Dropdown( id = 'dropdown_class',
                options = clusters_labels,
                value = None,
                style={'font-family':'Helvetica'}),

        dcc.Graph(id = 'clinical_plots')
    ])

    
@app.callback(Output(component_id='clinical_plots', component_property= 'figure'),
              [Input(component_id='dropdown_class', component_property= 'value')])

#age distribution
#sex just a bar plot
#diagnosis either bar plot or doughnut
#sources doughnut

#also the opposite, given a diagnosis, where do they go
#see sunburst plot
#https://plotly.com/python/subplots/

def graph_update(dropdown_value, cli=cli, lab=lab):

    """ Set up selected data. """

    diagnoses = cli['disease'].loc[lab[lab[dropdown_value]==1].index].value_counts().to_dict()
    dx        = list(diagnoses.values())[::-1]
    dy        = list(diagnoses.keys())[::-1]
    
    sources = cli['source'].loc[lab[lab[dropdown_value]==1].index].value_counts().to_dict()
    sx        = list(sources.values())[::-1]
    sy        = list(sources.keys())[::-1]

    total=sum(dx)

    age = cli['age_at_dx'].loc[lab[lab[dropdown_value]==1].index].values
    sex = cli['gender'].loc[lab[lab[dropdown_value]==1].index].value_counts().to_dict()

    if 'male' not in sex:
        sex['male']   = 0
    if 'female' not in sex:
        sex['female'] = 0
    sex['unknown']    = total - sex['male'] - sex['female']

    
    """ Set up grid of plots. """

    fig = make_subplots(
                rows=3, cols=2, 
                #column_widths=500,
                specs=[[{"colspan": 2}, None],
                       [{"colspan": 2}, None],
                       [{"type": "domain"},{"type": "domain"}]],
                row_width=[.8, 0.1, 0.1],
                vertical_spacing = 0.1,
                horizontal_spacing = 0.1,
                subplot_titles=("Age (years)", "Sex (%)", 
                    "Composition by\ndiagnosis (%)", "Composition by\nsource (%)"))

    """ Age violin plot. """

    fig.add_trace(go.Violin(x=age, line_color='#6C5B7B', 
                            box_visible=True, meanline_visible=True,
                            orientation='h', side='positive', width=3, points=False,
                            name='', legendgroup = '1', showlegend=False), 
                            row=1, col=1)
    
    """ Sex stacked bar plot. """
    
    fig.add_trace(go.Bar(y           = [0], 
                         x           = [sex['male']*1.0/total], 
                         orientation = 'h',
                         hovertext   = '{:d} ({:d}%)'.format(sex['male'],int(sex['male']*100/total)),
                         name        = 'male', 
                         legendgroup = '2',
                         marker=dict(
                             color='#247ba0',
                             line=dict(color='#247ba0', width=0)),
                         ), row=2, col=1)

    fig.add_trace(go.Bar(y           = [0], 
                         x           = [sex['unknown']*1.0/total], 
                         orientation = 'h',
                         hovertext   = '{:d} ({:d}%)'.format(sex['unknown'],int(sex['unknown']*100/total)),
                         name        = 'unknown',
                         legendgroup = '2',                         
                         marker=dict(
                             color='#aaaaaa',
                             line=dict(color='#aaaaaa', width=0)),
                         ), row=2, col=1)

    fig.add_trace(go.Bar(y           = [0], 
                         x           = [sex['female']*1.0/total], 
                         orientation = 'h',
                         hovertext   = '{:d} ({:d}%)'.format(sex['female'],int(sex['female']*100/total)),
                         name        = 'female',
                         legendgroup = '2',                         
                         marker=dict(
                             color='#ff7149',
                             line=dict(color='#ff7149', width=0)),
                         ), row=2, col=1)

    """ Diagnoses donut plot. """

    fig.add_trace(go.Pie(labels = dy, values = dx, hole = .5,
                         textinfo = 'label+percent',
                         hovertext   = ['{:d} ({:d}%)'.format(i,int(i*100/total)) for i in dx],
                         name        = '',
                         legendgroup = '3', 
                         textposition='inside'), row=3, col=1)

    """ Sources donut plot. """
    
    fig.add_trace(go.Pie(labels = sy, values = sx, hole = .5,
                         textinfo = 'label+percent',
                         hovertext   = ['{:d} ({:d}%)'.format(i,int(i*100/total)) for i in sx],
                         name        = '',
                         legendgroup = '3', 
                         textposition='inside',), row=3, col=2)

    """ Plots configuration. """

    fig.update_layout(font_family="Helvetica",
                        autosize=False,
                        width=1000,
                        height=1000,
                        margin = dict(t=50, 
                                    b=50, 
                                    l=25, 
                                    r=25),
                        showlegend=False,
                        legend_tracegroupgap = 145,
                        template=CHART_THEME, 
                        barmode='stack',
                        uniformtext_minsize=12, uniformtext_mode='hide',
                        )

    """ Update xaxis properties. """
    
    fig.update_xaxes(title_text="", zeroline=False, range=[0, 100], row=1, col=1)
    fig.update_xaxes(title_text="", range=[0,1], row=2, col=1)
    
    """ Update yaxis properties. """

    fig.update_yaxes(title_text="Samples Density", showgrid=False, row=1, col=1)
    fig.update_yaxes(title_text="", showgrid=False, showticklabels=False, row=2, col=1)

    return fig  

if __name__ == '__main__': 
    app.run_server()