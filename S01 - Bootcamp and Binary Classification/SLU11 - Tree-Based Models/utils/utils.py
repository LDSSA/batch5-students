import pandas as pd
import pydotplus
from sklearn.tree import (
    DecisionTreeClassifier,
    export_graphviz,
)


def make_data():

    data = {
        "Outlook": [
            "sunny",
            "sunny",
            "overcast",
            "rain",
            "rain",
            "rain",
            "overcast",
            "sunny",
            "sunny",
            "rain",
            "sunny",
            "overcast",
            "overcast",
            "rain",
        ],
        "Temperature": [
            "hot",
            "hot",
            "hot",
            "mild",
            "cool",
            "cool",
            "cool",
            "mild",
            "cool",
            "mild",
            "mild",
            "mild",
            "hot",
            "mild",
        ],
        "Humidity": [
            "high",
            "high",
            "high",
            "high",
            "normal",
            "normal",
            "normal",
            "high",
            "normal",
            "normal",
            "normal",
            "high",
            "normal",
            "high",
        ],
        "Windy": [
            "false",
            "true",
            "false",
            "false",
            "false",
            "false",
            "false",
            "false",
            "false",
            "false",
            "true",
            "true",
            "false",
            "true",
        ],
        "Class": [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0],
    }
    
    return pd.DataFrame.from_dict(data)

def make_exercise_data():

    data = {
        "sweet": [
            "n",
            "y",
            "y",
            "y",
            "n",
            "n",
            "y",
            "y",
            "n",
            "n",
            "n",
            "y",
            "y",
            "y",
            "y",
            "y",
            "y",
            "y",
            "n",
            "n",
        ],
        "fruit": [
            "oranges",
            "oranges",
            "oranges",
            "papaya",
            "oranges",
            "oranges",
            "oranges",
            "oranges",
            "oranges",
            "oranges",
            "papaya",
            "oranges",
            "oranges",
            "oranges",
            "oranges",
            "oranges",
            "oranges",
            "oranges",
            "oranges",
            "oranges",
        ],
        "Region": [
            "Central Asia",
            "Central America",
            "Central Asia",
            "Central Asia",
            "Central Asia",
            "Central Asia",
            "Central Asia",
            "Central Asia",
            "Central Asia",
            "Central Asia",
            "Central America",
            "Central America",
            "Central Asia",
            "Central America",
            "Central Asia",
            "Central Asia",
            "Central America",
            "Central America",
            "Central Asia",
            "Central America",
        ],
        "Class": [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
    }
    
    return pd.DataFrame.from_dict(data)

def separate_target_variable(data):
    X = data.copy()
    y = X.pop('Class')
    
    return X, y

def process_categorical_features(X):
    return pd.get_dummies(X)


def visualize_tree(clf, feature_names, class_names):
    dot_data = export_graphviz(
        clf,
        out_file=None,
        feature_names=feature_names,
        class_names=class_names,
    )

    graph = pydotplus.graph_from_dot_data(dot_data)
    return graph.create_png()
