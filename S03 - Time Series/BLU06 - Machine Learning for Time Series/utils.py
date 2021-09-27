import pandas as pd
import numpy as np
#from lightgbm import LGBMRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from tqdm import tqdm_notebook as tqdm

def get_stores_data():
    stores = pd.read_csv('data/stores.csv')
    stores = stores.sample(frac=1, random_state=9999)
    return stores

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

def get_store_data():
    stores = get_stores_data()
    store = stores.loc[stores.store_nbr==1].drop('store_nbr', axis=1)    
    #store.date = pd.to_datetime(store.date).dt.strftime('%Y/%m/%d')
    store = store.sample(frac=1, random_state=9999)
    return store

def build_exog_features(df_, leads):
    """ 
    takes a df with the exogenous data and creates lagged features so that the dataset is compatible with the ML formulation.
    use this as described in the google doc. If you mess with this function be careful.
    """
    
    for i in np.arange(1, leads+1):
        df_['exog_lead'+str(i)] = df_.exog.shift(-i)
    return df_

def build_target(df_, number_of_periods_ahead, target):
    """ 
    takes a series, turned it into a dataframe, and adds a new column called target
    This column is the input series, lagged number_of_periods_ahead into the future
    """
    
    # the target column will be the input series, lagged into the future
    df_ = df_.copy()
    df_['target'] = df_[target].shift(-number_of_periods_ahead)
    return df_

def separate_last_day(df_):
    
    """
    takes a dataset which has the target and features built 
    and separates it into the last day
    """
    # take the last period 
    last_period = df_.iloc[-1]
    
    # the last period is now a series, so it's name will be the timestamp
    training_data = df_.loc[df_.index < last_period.name]

    return last_period, training_data

def separate_train_and_test_set(last_period_, training_data_): 
    
    """ 
    separates training and test set (clue was in the name, really... )
    Ok, we were lazy and left the target hardcoded as 'target'. Shame on us. 
    """
    
    # anything that isn't a target is a feature 
    features = [feature for feature in training_data_.columns if feature != 'target']
    
    # adding a sneaky little dropna to avoid the missing data problem above 
    X_train = training_data_.dropna()[features]
    y_train = training_data_.dropna()['target']
    
    X_last_period = last_period_[features]
    
    return X_train, y_train, X_last_period

def prepare_for_prediction(series_, number_of_periods_ahead, num_periods_lagged, num_periods_diffed, weekday, month, rolling, holidays, target):
    
    """ 
    Wrapper to go from the original series to X_train, y_train, X_last_period 
    
    """
    
    # build the target 
    data_with_target = build_target(series_, 
                                    number_of_periods_ahead, target)
    
    # build the features 
    data_with_target_and_features = build_some_features(data_with_target, target,
                                                        num_periods_lagged=num_periods_lagged,
                                                       num_periods_diffed=num_periods_diffed,
                                                       weekday=weekday,
                                                       month=month,
                                                       rolling=rolling,
                                                       holidays=holidays)    
            
    # separate train and test data 
    last_period, training_data = separate_last_day(data_with_target_and_features)

    # separate X_train, y_train, and X_test 
    X_train, y_train, X_last_period = separate_train_and_test_set(last_period, 
                                                           training_data)
    
    # return ALL OF THE THINGS! (well, actually just the ones we need)
    return X_train, y_train, X_last_period 

def predict_period_n(series_, model, number_of_periods_ahead, num_periods_lagged, num_periods_diffed, weekday, month, rolling, holidays, target): 
    
        X_train, y_train, X_last_period = prepare_for_prediction(series_, 
                                                             number_of_periods_ahead, 
                                                             num_periods_lagged,
                                                             num_periods_diffed,
                                                             weekday,
                                                             month,
                                                             rolling,
                                                             holidays,
                                                             target
                                                             )
        
        model.fit(X_train, y_train)
        return model.predict(X_last_period.values.reshape(1, -1))
    
def predict_n_periods(series_, n_periods, model, num_periods_lagged, num_periods_diffed=0, weekday=False, month=False,rolling=[], holidays=False, target="customers"): 
    predictions = []

    for period_ahead in tqdm(range(1, n_periods+1)):
        pred = predict_period_n(series_=series_, 
                                model=model, 
                                number_of_periods_ahead=period_ahead, 
                                num_periods_lagged=num_periods_lagged,
                                num_periods_diffed=num_periods_diffed,
                                weekday=weekday,
                                month=month,
                                rolling=rolling,
                                holidays=holidays,
                                target=target)
        
        predictions.append(pred[0])
        
    return predictions 

def build_some_features(df_, target, num_periods_lagged=1, num_periods_diffed=0, weekday=False, month=False, rolling=[], holidays=False): 
    """
    Builds some features by calculating differences between periods  
    """
    # make a copy 
    df_ = df_.copy()
            
    # for a few values, get the lags  
    for i in range(1, num_periods_lagged+1):
        # make a new feature, with the lags in the observed values column
        df_['lagged_%s' % str(i)] = df_[target].shift(i)
        
    # for a few values, get the diffs  
    for i in range(1, num_periods_diffed+1):
        # make a new feature, with the lags in the observed values column
        df_['diff_%s' % str(i)] = df_[target].diff(i)
    
    for stat in rolling:
        df_['rolling_%s'%str(stat)] = df_[target].rolling('7D').aggregate(stat)
        
    if weekday == True:
        df_['sin_weekday'] = np.sin(2*np.pi*df_.index.weekday/7)
        df_['cos_weekday'] = np.cos(2*np.pi*df_.index.weekday/7)
        
    if month == True:
        df_['sin_month'] = np.sin(2*np.pi*df_.index.month/12)
        df_['cos_month'] = np.cos(2*np.pi*df_.index.month/12)
        
    if holidays == True:
        holidays = df_[((df_.index.month==12) & (df_.index.day==25))
              |((df_.index.month==1) & (df_.index.day==1))][target]
        df_['holidays'] = holidays + 1
        df_['holidays'] = df_['holidays'].fillna(0)
        
    return df_

def generate_submission_file(predictions_wf_1, predictions_wf_2, predictions_wf_3):
    test_1 = pd.DataFrame(predictions_wf_1)
    test_2 = pd.DataFrame(predictions_wf_2)
    test_3 = pd.DataFrame(predictions_wf_3)
    test = pd.concat([test_1,test_2,test_3])
    test.columns = ['value']
    test.to_csv('submission.csv', index=False)
    return test
