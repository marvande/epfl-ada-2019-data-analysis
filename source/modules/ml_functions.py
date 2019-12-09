from sklearn import model_selection
from sklearn import preprocessing
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

#imports: 
from pylab import *
import os
import pandas as pd


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
    #print(f"The training data has shape: " + str(shape(X_train)))

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
    
    return tree 

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

#Looks at the products in the clusters: 
def observe_clusers(label, clustered_households, labelled_prod, quantities):
    cluster = clustered_households[clustered_households.labels ==
                                   label].set_index('household_key')
    cluster = quantities.join(cluster,
                              on='household_key').dropna().drop('labels',
                                                                axis=1)
    products_cluster = []
    for i in cluster.index:
        products_cluster.append(
            cluster.loc[i][cluster.loc[i].apply(lambda x: x > 0.0)])
    products_cluster = pd.DataFrame(data=products_cluster, index=cluster.index)
    products_cluster = products_cluster.fillna(0.0)

    #Columns with products bought by at least 2/3 of the households in this cluster ?
    #Count the number of non zero values for each column:
    non_zero_products = products_cluster.astype(bool).sum(axis=0)

    #At least half of the households bought the same product ?
    number_households = len(products_cluster.index)
    print('Cluster ' + str(label) + ':')
    print('')
    print("There are %d households in this cluster" % number_households)
    non_zero_products = non_zero_products[non_zero_products.apply(
        lambda x: x > number_households / 3)]
    print('')
    #See only one product: which one ?
    product_id = non_zero_products.index

    print(labelled_prod.loc[product_id])
    print('')

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
    X = data[tot_columns]

    y = np.array(X[target])

    X = np.array(X.drop(target, axis=1))
    
    # Set random seed to ensure reproducible runs
    RSEED = 50
    
    X_train, X_test, y_train, y_test = model_selection.train_test_split(
        X, y, test_size=0.25, random_state= RSEED)

    #Don't remove too much for testing as we don't have that many datapoints:
    #print(f"The training data has shape: " + str(shape(X_train)))

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
    return model

