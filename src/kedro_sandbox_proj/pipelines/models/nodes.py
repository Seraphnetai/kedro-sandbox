
from typing import Tuple, Dict, Any
import pandas as pd
from sklearn.model_selection import RandomizedSearchCV
from sklearn.linear_model import LogisticRegression, RidgeClassifier
from sklearn import metrics


def random_cv(parameters: Dict[str,Any]):

    gs_lr = RandomizedSearchCV(estimator=LogisticRegression(random_state=parameters['random_state']),
                               param_distributions=parameters['grid_params_lr'],
                               scoring='roc_auc',
                               cv=10,
                               n_jobs=-1) 

    gs_ridge = RandomizedSearchCV(estimator=RidgeClassifier(random_state=parameters['random_state']),
                                  param_distributions=parameters['grid_params_ridge'],
                                  scoring='roc_auc',
                                  cv=10,
                                  n_jobs=-1)                    

    return gs_lr, gs_ridge


def find_best_model(X_train, y_train, X_test, y_test, parameters: Dict[str,Any]):

    gs_lr, gs_ridge = random_cv(parameters)

    grids = [gs_lr, gs_ridge]
    grid_dict = {0: 'Logistic Regression',
                 1: 'Ridge Classifier'}

    # Fit the grid search objects
    print('Performing model optimizations...')
    best_acc = 0.0
    best_reg = ''
    best_model = 0
    best_params = {}
    for idx, gs in enumerate(grids):
        print('\nEstimator: %s' % grid_dict[idx])
        # Fit grid search
        gs.fit(X_train, y_train)
        # Best params
        print('Best params: %s' % gs.best_params_)
        best_params = gs.best_params_
        # Predict on test data with best params
        y_pred = gs.predict(X_test)
        # Test data accuracy of model with best params
        print('Test set accuracy score for best params: %.3f ' % metrics.roc_auc_score(y_test, y_pred))
        # Track best (highest test accuracy) model
        print(metrics.roc_auc_score(y_test, y_pred))
        if metrics.roc_auc_score(y_test, y_pred) > best_acc:
            best_acc = metrics.roc_auc_score(y_test, y_pred)
            best_reg = gs
            best_model = idx
            
    print('\nRegression with best test set accuracy: %s' % grid_dict[best_model])

    best_params = pd.DataFrame.from_dict(best_params, orient='index')

    return best_reg, best_params
