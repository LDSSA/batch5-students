import sys
import os
import argparse

import pandas as pd
import ml_metrics as metrics


parser = argparse.ArgumentParser()
#parser.add_argument('y_true', help='Path to y_true')
parser.add_argument('y_pred', help='Path to y_pred')

def data_reader(y_file):
    """
    Import data from solution .csv file,
    """

    y_path = os.path.join('data', y_file)
    df_ = pd.read_csv(y_path, header=None)
    return df_


def validate_solution(df_true, df_pred):
    
    if df_true.shape[0] != df_pred.shape[0]:
        raise ValueError(
            f"Wrong number of users, expected {df_true.shape[0]} got {df_pred.shape[0]}"
        )

    users_set_true = set(df_true[0])
    users_set_pred = set(df_pred[0])
    
    if users_set_true != users_set_pred:
        raise ValueError(
            'Unexpected user ids, please check that you are providing '
            'recommendations for the correct users'
        )
    
    if df_pred.shape[1] < df_true.shape[1]:
        raise ValueError(
            f"Not enough recommendations were provided, "
            f"expected at least {df_true.shape[1]} got {df_pred.shape[1]}")

    
def evaluate_solution(y_pred_file, y_true_file=None):
    """
    Evaluate the solution.
    The number of recommendations used for evaluation (@k) is equal to the number of /
    recommendations on the test data.
    """
    
    #Actual recommendations.
    ###path_test_rec = os.path.join('data', 'test_recommendations.csv')
    ###df_true = pd.read_csv(path_test_rec, header=None)
    if y_true_file is None:
        df_true = data_reader("test_recommendations.csv")
    else:
        df_true = data_reader(f"{y_true_file}.csv")

    #Predicted recommendations depend on selected file
    df_pred = data_reader(f"{y_pred_file}.csv")
    
    #Validate solution format
    validate_solution(df_true, df_pred)
    
    df_true = df_true.sort_values(by=0).drop(columns=[0])
    y_true = df_true.values.tolist()

    df_pred = df_pred.sort_values(by=0).drop(columns=[0])
    y_pred = df_pred.values.tolist()
    
    return metrics.mapk(y_true, y_pred, k=df_true.shape[1]-1)


if __name__ == '__main__':

    args = parser.parse_args()
    print(evaluate_solution(args.y_pred))


