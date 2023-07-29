import pandas as pd
from helper import template_app as temp_app

# capstone case
case = 'Scotty Time Series'

# read data & data preparation
caps = pd.read_csv('data-input/ml_scotty_ts.csv')

# build app
temp_app.app(case, caps)