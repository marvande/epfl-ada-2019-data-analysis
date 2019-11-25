from sklearn import model_selection
from sklearn import preprocessing
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

#imports: 
from pylab import *
import os


def decision_tree(target, features, data):
    """
    Trains a deicsion tree model on data.
    @input:
        - [string] target: column name of data that is the target
        - [array of string] features: column names of data that correspond to the features
    @output: returns the accuracy of the model and the AUC score.
    """
    tot_columns = np.append(features, target)

    X = data[tot_columns]
    
    y = np.array(X[target])

    X = np.array(X.drop(target, axis=1))

    # Set random seed to ensure reproducible runs
    RSEED = 50
    
    X_train, X_test, y_train, y_test = model_selection.train_test_split(
        X, y, test_size=0.25, random_state=RSEED)

    #Don't remove too much for testing as we don't have that many datapoints: 
    print(f"The training data has shape: " + str(shape(X_train)))

    # We normalize the data, since it is good practice:
    scaler = preprocessing.StandardScaler().fit(X_train)

    X_train = scaler.transform(X_train)

    #Normalize the test set with the same normalizer as the training: 
    X_test = scaler.transform(
        X_test)

    # Set random seed to ensure reproducible runs
    RSEED = 50

    # Make a decision tree and train:
    tree = DecisionTreeClassifier(random_state=RSEED)

    tree.fit(X_train, y_train)
    print(
        f'Decision tree has {tree.tree_.node_count} nodes with maximum depth {tree.tree_.max_depth}.'
    )
    print(f'Model Accuracy on training set: {tree.score(X_train, y_train)}')
    print(f'Model Accuracy on test set: {metrics.accuracy_score(y_test, tree.predict(X_test))}')
    print('')
    print(f'Train ROC AUC Score: {multiclass_roc_auc_score(y_train, tree.predict(X_train))}')
    print(f'Test ROC AUC Score: {multiclass_roc_auc_score(y_test, tree.predict(X_test))}')
    print(f'Baseline ROC AUC: {multiclass_roc_auc_score(y_test, [1 for _ in range(len(y_test))])}')
    
    
def multiclass_roc_auc_score(y_test, y_pred, average="macro"):
    """
    Calculates an AUC score for a multiclass model as the score method from metrics does not work for multiclass. 
    @input: 
    - [array] y_test: true labels
    - [array] y_pred: predicted labels from model
    """
    lb = preprocessing.LabelBinarizer()
    lb.fit(y_test)
    y_test = lb.transform(y_test)
    y_pred = lb.transform(y_pred)
    
    return metrics.roc_auc_score(y_test, y_pred, average=average)


#Random forest:
def random_forest(target, features, data):
    """
    Trains a random forest model on data.
    @input:
        - [string] target: column name of data that is the target
        - [array of string] features: column names of data that correspond to the features
    @output: returns the accuracy of the model and the AUC score.
    """
    tot_columns = np.append(features, target)
    print(tot_columns)
    X = data[tot_columns]

    y = np.array(X[target])

    X = np.array(X.drop(target, axis=1))
    
    # Set random seed to ensure reproducible runs
    RSEED = 50
    
    X_train, X_test, y_train, y_test = model_selection.train_test_split(
        X, y, test_size=0.25, random_state= RSEED)

    #Don't remove too much for testing as we don't have that many datapoints:
    print(f"The training data has shape: " + str(shape(X_train)))

    # We normalize the data, since it is good practice:
    scaler = preprocessing.StandardScaler().fit(X_train)

    X_train = scaler.transform(X_train)

    #Normalize the test set with the same normalizer as the training:
    X_test = scaler.transform(X_test)

    # Create the model with 100 trees
    model = RandomForestClassifier(n_estimators=100,
                                   random_state=RSEED,
                                   max_features='sqrt',
                                   n_jobs=-1,
                                   verbose=1)
    # Fit on training data
    model.fit(X_train, y_train)

    n_nodes = []
    max_depths = []

    for ind_tree in model.estimators_:
        n_nodes.append(ind_tree.tree_.node_count)
        max_depths.append(ind_tree.tree_.max_depth)

    print(f'Average number of nodes {int(np.mean(n_nodes))}')
    print(f'Average maximum depth {int(np.mean(max_depths))}')

    print(f'Model Accuracy on training set: {model.score(X_train, y_train)}')
    print(
        f'Model Accuracy on test set: {metrics.accuracy_score(y_test, model.predict(X_test))}'
    )
    print('')
    print(
        f'Train ROC AUC Score: {multiclass_roc_auc_score(y_train, model.predict(X_train))}'
    )
    print(
        f'Test ROC AUC Score: {multiclass_roc_auc_score(y_test, model.predict(X_test))}'
    )
    print(
        f'Baseline ROC AUC: {multiclass_roc_auc_score(y_test, [1 for _ in range(len(y_test))])}'
    )