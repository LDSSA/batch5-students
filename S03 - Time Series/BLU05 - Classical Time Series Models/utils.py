import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def load_airlines_series():
    airlines = pd.read_csv('data/AirPassengers.csv')[:-1]
    airlines.Month = pd.to_datetime(airlines.Month)
    airlines = airlines.set_index('Month')
    airlines.columns = ['thousands of passengers']
    airlines = airlines['thousands of passengers']
    return airlines

def load_electricity_consumption_series():
    data = pd.read_csv('data/monthly-av-residential-electrici.csv')
    data = data[:-1]
    data.Month = pd.to_datetime(data.Month)
    data.columns = ['month', 'consumption']
    data = data.set_index('month')
    return data

def load_airline_data():
    airlines = pd.read_csv('data/AirPassengers.csv',
                           index_col='Month')

    airlines.columns = ['passengers_thousands']
    airlines = airlines['passengers_thousands']
    airlines.index = pd.to_datetime(airlines.index)

    return airlines.asfreq('MS', method='ffill')