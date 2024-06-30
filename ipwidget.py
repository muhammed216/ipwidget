import ipywidgets as widgets

import pandas as pd
import numpy as np
from io import StringIO
#import matplotlib as plt
#%matplotlib inline

tab = widgets.Tab()
placeholder = widgets.Label()
tab.children = [placeholder,placeholder,placeholder]
tab.set_title(0, "Upload")
tab.set_title(1, "Describer")
tab.set_title(2, "Plotter")
tab


up = widgets.FileUpload(accept="", multiple=False)
up

out = widgets.Output(layout={'border': 'lpx solid black'})
tab.children = [up,out,out]
tab

eraser = widgets.SelectMultiple(
    options=['tab', '"'],
    value=['tab'],
    #rows=10
    description='Eraser: ',
    disabled=False
)
eraser

delim = widgets.RadioButtons(
    options=[':', ',', ' '],
    description='Separator: ',
    disabled=False
)
delim

rows = widgets.IntSlider(
    value=0,
    step=1,
    desscription='# of lines:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='d'
)
rows

accordion = widgets.Accordion()
accordion.children = [
    up,
    delim,
    rows
]
accordion.set_title(0, 'File Selection')
accordion.set_title(1, 'Delimiter')
accordion.set_title(2, 'Skip Rows')
print(accordion)


button_upload = widgets.Button(
    description='Upload',
    disabled='False',
    button_style='warning',
    tooltip='Click to Upload',
    icon='check'
)
print(button_upload)


button_prewiew = widgets.Button(
    description='Prewiew',
    disabled='False',
    button_style='info',
    tooltip='Click to Prewiew',
    icon='search'
)
print(button_prewiew)

button_plot = widgets.Button(
    description='plot',
    disabled='False',
    button_style='danger',
    tooltip='Click to plot',
    icon='pencil'
)
print(button_plot)

vb = widgets.VBox([delim, eraser])
print(vb)

hb = widgets.HBox([delim, eraser])
print(hb)

accordion.children(
    up,
    widgets.VBox([delim, eraser]),
    rows
)

accordion_box = widgets.VBox([
    accordion,
    widgets.HBox([button_prewiew, button_upload]),
    out
])
print(accordion_box)

toggle = widgets.ToggleButtons(
    options=['prewiew', 'info', 'stats'],
    description='Options',
    diabled=False,
    button_style='warning',
    icons=['search', 'info', 'tachometer']
)
print(toggle)


x_axis = widgets.Dropdown(
    options=[''],
    value='',
    description='X-Axis:',
    disabled=False,
)


y_axis = widgets.Dropdown(
    options=[''],
    value='',
    description='Y-Axis:',
    disabled=False,
)


graph_type = widgets.Dropdown(
options=['Bar Chart', 'Line Chart'],
    value='Bar Chart',
    description='Chart Type:',
    disabled=False,
)
print(graph_type)

color_picker = widgets.ColorPicker(
    concise=False,
    description='Color Picker ',
    value='lightblue',
    disabled=False
)
print(color_picker)













