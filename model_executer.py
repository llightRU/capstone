import joblib
from sklearn.linear_model import LogisticRegression

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report,f1_score
from xgboost import XGBClassifier
import data_executer as de
import warnings
warnings.filterwarnings('ignore')
import os
from sklearn.tree import _tree

def save_model(model, filename):
    joblib.dump(model, filename)

def load_model_to_use(name):
    model_files = {
        'Decision Tree': 'data/model/decisionTree_model.plk',
        'Random Forest': 'data/model/Random_Forest.sav',
        'XGBoost': 'data/model/XG_Boost.sav',
        'Logistic Regression': 'data/model/Logistic_Regression.sav'
    }

    model_file = model_files.get(name)
    if model_file and os.path.exists(model_file):
        try:
            with open(model_file, 'rb') as f:
                model = joblib.load(f)
            return model
        except Exception as e:

            return None
    elif os.path.exists(name):
        try:
            with open(name, 'rb') as f:
                model = joblib.load(f)
            return model
        except Exception as e:

            return None
    else:

        return None


def get_rules(tree, feature_names, class_names=None):
    tree_ = tree.tree_
    feature_name = [
        feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!"
        for i in tree_.feature
    ]

    paths = []
    path = []

    def recurse(node, path, paths):
        if tree_.feature[node] != _tree.TREE_UNDEFINED:
            name = feature_name[node]
            threshold = tree_.threshold[node]
            p1, p2 = list(path), list(path)
            p1 += [f"({name} <= {np.round(threshold, 3)})"]
            recurse(tree_.children_left[node], p1, paths)
            p2 += [f"({name} > {np.round(threshold, 3)})"]
            recurse(tree_.children_right[node], p2, paths)
        else:
            path += [(tree_.value[node], tree_.n_node_samples[node])]
            paths += [path]

    recurse(0, path, paths)

    # sort by samples count
    samples_count = [p[-1][1] for p in paths]
    ii = list(np.argsort(samples_count))
    paths = [paths[i] for i in reversed(ii)]

    rules = []
    for path in paths:
        rule = "if "
        for p in path[:-1]:
            if rule != "if ":
                rule += " and "
            rule += str(p)
        rule += " then "
        if class_names is None:
            rule += "response: " + str(np.round(path[-1][0][0][0], 3))
        else:
            classes = path[-1][0][0]
            l = np.argmax(classes)
            rule += f"class: {class_names[l]} (proba: {np.round(100.0 * classes[l] / np.sum(classes), 2)}%)"
        rule += f" | based on {path[-1][1]:,} samples"
        rules += [rule]

    return rules


def decision_tree_model(df,hold_out_score,criterion, max_depth, min_sample_split, min_sample_leaf, max_feature,check):
    X = df[:, :-1]
    y = df[:, -1]
    hold_out_score = 0.3 if hold_out_score > 0.3 else hold_out_score
    X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=hold_out_score, random_state=42)

    decision_tree_model = DecisionTreeClassifier(criterion=str(criterion), max_depth=int(max_depth),min_samples_split=int(min_sample_split),
                                                 min_samples_leaf=int(min_sample_leaf),max_features=int(max_feature),ccp_alpha=0.0001 if int(check) else 0,random_state=42)
    decision_tree_model.fit(X_train, y_train)

    y_predictions = decision_tree_model.predict(X_temp)
    y_accuracy = accuracy_score(y_temp, y_predictions)
    y_f1 = f1_score(y_temp, y_predictions)

    return decision_tree_model,y_accuracy,y_f1


def random_forest_model(df, n_estimators, criterion, max_depth, min_samples_split, min_samples_leaf, max_features,
                        hold_out_score):
    # Split data into features (X) and target (y)
    X = df[:, :-1]
    y = df[:, -1]

    # Ensure the hold-out score is at least 0.3
    hold_out_score = min(hold_out_score, 0.3)

    # Split data into training and a temporary set
    X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=hold_out_score, random_state=42)


    # Create a Random Forest classifier with specified parameters
    rf_model = RandomForestClassifier(
        n_estimators=int(n_estimators),
        criterion=str(criterion),
        max_depth=int(max_depth),
        min_samples_split=int(min_samples_split),
        min_samples_leaf=int(min_samples_leaf),
        max_features=int(max_features),
        random_state=42
    )

    # Train the model on the training set
    rf_model.fit(X_train, y_train)

    # Make predictions on the validation set (if using cross-validation)
    y_predictions = rf_model.predict(X_temp)
    y_accuracy = accuracy_score(y_temp, y_predictions)
    y_f1 = f1_score(y_temp, y_predictions)
    # Return the trained model
    return rf_model,y_accuracy,y_f1


def logistic_regression_model(df, hold_out=0.1,penalty='l2', C=1.0, max_iter=100, solver='lbfgs', tol=1e-4):
    # Split data into features (X) and target (y)
    X = df[:, :-1]
    y = df[:, -1]
    hold_out = min(hold_out, 0.3)
    # Split the data into training and test sets
    X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=hold_out, random_state=42)

    # Create a logistic regression model with the specified parameters
    if penalty == 'none':
        penalty = None
    logreg_model = LogisticRegression(
        penalty=penalty,  # Regularization type ('l1', 'l2', 'elasticnet', 'none')
        C=float(C),  # Inverse of regularization strength; smaller values imply stronger regularization
        max_iter=int(max_iter),  # Maximum number of iterations
        solver=str(solver),  # Solver to use for optimization (e.g., 'lbfgs', 'liblinear', 'saga')
        tol=tol,  # Tolerance for stopping criteria
        random_state=42
    )

    # Train the model on the training set
    logreg_model.fit(X_train, y_train)

    y_predictions = logreg_model.predict(X_temp)
    y_accuracy = accuracy_score(y_temp, y_predictions)
    y_f1 = f1_score(y_temp, y_predictions)

    # Return the trained logistic regression model
    return logreg_model,y_accuracy,y_f1


def xgboost_model(df, hold_out_score, n_estimators, learning_rate, max_depth, subsample, min_child_weight, objective):
    # Ensure df is not empty
    if df.size == 0:
        raise ValueError("Input data is empty. Please provide valid data.")

    # Split data into features and target
    X = df[:, :-1]
    y = df[:, -1]

    # Validate the hold_out_score
    hold_out_score = min(max(0, hold_out_score), 0.3)

    # Split data into training and validation sets
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=hold_out_score, random_state=42)

    # Create XGBClassifier with specified parameters
    xgb_model = XGBClassifier(
        n_estimators=int(n_estimators),
        learning_rate=float(learning_rate),
        max_depth=int(max_depth),
        subsample=float(subsample),
        min_child_weight=float(min_child_weight),
        objective=str(objective),
        gamma=1.5764684532828115,
        reg_alpha=0.868849518999903,
        reg_lambda=0.08699844342243063,
        colsample_bytree=1.0,
        random_state=42
    )

    # Train the model
    xgb_model.fit(X_train, y_train)

    # Verify the number of features in the validation set matches the trained model
    if X_val.shape[1] != xgb_model.n_features_in_:
        raise ValueError(f"The number of features in the validation set ({X_val.shape[1]}) does not match the number of features in the trained model ({xgb_model.n_features_in_}).")

    # Make predictions
    y_pred = xgb_model.predict(X_val)

    # Calculate accuracy and F1 score
    accuracy = accuracy_score(y_val, y_pred)
    f1 = f1_score(y_val, y_pred, average='binary' if len(set(y_val)) == 2 else 'weighted')

    # Return the trained model and metrics
    return xgb_model, accuracy, f1

if __name__ == "__main__":
    # Đọc dữ liệu từ tệp CSV
    
    pass


