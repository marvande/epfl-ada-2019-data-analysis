# FUNCTIONS DOCUMENTATION

###  order_hh_dem
Renders a column in the demographic dataframe categorical according to a specific ordering. 
*  input: 
    -   *[pd.DataFrame]*    **hh_dem**: demographic dataframe
    -   *[string]* **label**:  column name
    -   *[list of string]* **ordered_label**: ordering for the categorical variables
    
*  output: 
    -   outputs a pd.Categorical ordered column. 
    
```python
def order_hh_dem(hh_dem, label, ordered_label):
 ordered_column = pd.Categorical(hh_dem[label],
                      ordered = True,
                      categories = ordered_label)
    return ordered_column 
```
-----------------------------
### descision_tree
Trains a decision tree model on data.
*   input:
    -   *[string]*  **target**: column name of data that is the target
    -   *[array of string]*  **features**: column names of data that correspond to the features
    
*   output: 
    -   returns the accuracy of the model and the AUC score.
   
 
```python 
def decision_tree(target, features, data):
   
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
    
    return tree
```
----------------------------------------------- 
### multiclass_roc_auc_score
Calculates an AUC score for a multiclass model as the score method from metrics does not work for multiclass. 
*   input: 
    -   *[array]*  **y_test**: true labels
    -   *[array]*  **y_pred**: predicted labels from model
    
*   output: 
    -   returns AUC score for the multiclass model

```python
def multiclass_roc_auc_score(y_test, y_pred, average="macro"):
   
    lb = preprocessing.LabelBinarizer()
    lb.fit(y_test)
    y_test = lb.transform(y_test)
    y_pred = lb.transform(y_pred)
    
    return metrics.roc_auc_score(y_test, y_pred, average=average)
```
-----------------------------------------

### random_forest
Trains a random forest model on data.
*   input:
    -   *[string]*  **target**: column name of data that is the target
    -   *[array of string]*  **features**: column names of data that correspond to the features
*   output: 
    -   returns the accuracy of the model and the AUC score.

```python
def random_forest(target, features, data):
    
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
    return model
```
---------------------------------
### cat_count_plot
Plots the number of occurences per category in to_be_plotted.
*   input: 
    -   *[pd.Series]*  **to_be_plotted**: categorical data (e.g. columns of incomes for all households)
    -   *[string]*  **title**: the title we want to give the plot
*   output: 
    -   plots the number of occurences per category

```python 
def cat_count_plot(to_be_plotted, title):
   
    fig, axs = plt.subplots(1,1, figsize = (18,6))

    sns.countplot(to_be_plotted, ax = axs)

    axs.set_xticklabels(axs.get_xticklabels(), rotation = 45, horizontalalignment = 'right')
    axs.set(title = title)
```
-------------------------
### corr_function_plot
Function used in pair_corr_plot. Calculates the correlation between 2 variables and adds it on the scatter plot. 
*   input: 
    -   [continuous variable] x: first variable
    -   [continuous variable] y: second variable
    -   **kwargs**: additional arguments for function plotting 
*   output: 
    -   show correlation on scatter plot. 

```python
def corr_function_plot(x, y, **kwargs):
    
    # Calculate the value: 
    coef = np.corrcoef(x, y)[0][1]
    # Make the label: 
    label = r'$\rho$ = ' + str(round(coef, 2))
    
    # Add the label to the plot: 
    ax = plt.gca()
    ax.annotate(label, xy = (0.2, 1), size = 10, xycoords = ax.transAxes)
```
------------------------------------
### double_categorical_scatter
Does a double categorical scatter plot. 
*   input: 
    -   *[pd.Series]*  **to_be_plotted1x, to_be_plotted1y**: x and y axis for first categorical scatter plot
    -   *[pd.Series]*  **to_be_plotted2x, to_be_plotted2y**: x and y axis  for second categorical scatter plot
    -   *[array of string]*  **titles**: array of titles for plots
    -   *[Boolean]*  **add_mean**:True if we want to add the mean on the plots

*   output: 
    -   double categorical scatter plot.  


```python 
def double_categorical_scatter(to_be_plotted1x, to_be_plotted1y, to_be_plotted2x, to_be_plotted2y, titles, add_mean = False):
   
    fig, axs = plt.subplots(1,2, figsize = (18,6))
    
    sns.swarmplot(x = to_be_plotted1x, y = to_be_plotted1y, ax = axs[0])
    if add_mean: 
        axs[0].axhline(to_be_plotted1y.mean(), color = 'r', linestyle = '--')
    
    sns.swarmplot(x = to_be_plotted2x, y = to_be_plotted2y, ax = axs[1])
    if add_mean: 
        axs[1].axhline(to_be_plotted2y.mean(), color = 'r', linestyle = '--')
        plt.legend({'Mean': mean})
    
    #Rotate labels: 
    axs[0].set_xticklabels(axs[0].get_xticklabels(), rotation = 45, horizontalalignment = 'right')
    axs[1].set_xticklabels(axs[1].get_xticklabels(), rotation = 45, horizontalalignment = 'right')

    axs[0].set(title = titles[0])
    axs[1].set(title =  titles[1])
```
------------------------------------------------------
### double_plot_box_dist
Does a double box plot with distribution with a shared x axis. 
*   input:
    -   *[pd.Series]*  **to_be_plotted1, to_be_plotted2**: panda series from which we want to plot the distribution and boxplot
    -   *[list of string]*  **titles** = array of titles to give both plots
    -   *[list of string]*  **xlabels** = array of labels for both xaxis

*   output: 
    -   boxplot and distribution of to_be_plotted1 and to_be_plotted2
  
    
```python
def double_plot_box_dist(to_be_plotted1, to_be_plotted2, titles, xlabels):
   
    f, axes = plt.subplots(2, 2, sharex = 'col', gridspec_kw = {"height_ratios": (0.2, 2)}, figsize = (20,8))
    
    means = [to_be_plotted1.mean(), to_be_plotted2.mean()]
    medians = [to_be_plotted1.median(), to_be_plotted2.median()]
    
    sns.boxplot(to_be_plotted1, ax = axes[0,0])
    axes[0,0].axvline(means[0], color = 'r', linestyle = '--')
    axes[0,0].axvline(medians[0], color = 'g', linestyle = '-')

    sns.distplot(to_be_plotted1, ax = axes[1,0])
    axes[1,0].axvline(means[0], color = 'r', linestyle = '--')
    axes[1,0].axvline(medians[0], color = 'g', linestyle = '-')

    sns.boxplot(to_be_plotted2, ax =axes[0,1])
    axes[0,1].axvline(means[1], color = 'r', linestyle = '--')
    axes[0,1].axvline(medians[1], color = 'g', linestyle = '-')

    sns.distplot(to_be_plotted2, ax = axes[1,1])
    axes[1,1].axvline(means[1], color = 'r', linestyle = '--')
    axes[1,1].axvline(medians[1], color = 'g', linestyle = '-')

    plt.legend({'Mean':mean,'Median':median})

    axes[0,0].set(xlabel = '', title = titles[0])
    axes[0,1].set(xlabel = '', title = titles[1])

    axes[1,0].set(xlabel = xlabels[0])
    axes[1,1].set(xlabel = xlabels[1])

    plt.show()
```
-------------------------------------------------
### pair_corr_plot
Plots a pair plot with the scatter plots and correlation coefficients off diagonal, and histograms on the diagonal. 
*   input: 
    -   *[pd.DataFrame]*  **to_be_plotted**: the dataframe with each column being one variable. 
    -   *[function]*  **correlation_function**: the correlation function which is used 
*   output: 
    -   plot. 

```python
def pair_corr_plot(to_be_plotted, correlation_function = corr_function_plot, hue = None):
    
    fig = sns.pairplot(to_be_plotted, hue)
    fig = fig.map_offdiag(correlation_function)
```
--------------------------------------------------
### plot_box_dist
Plots the boxplot and distribution of an entered series with shared x axis. 
*   input: 
    -   *[pd.Series]*  **to_be_plotted**: series from which we want to plot the distribution and boxplot
    -   *[string]*  **title**: title we want to give the plot
    -   *[string]*  **xlabel**: label for x axis

*   output: 
    -   boxplot and distribution of to_be_plotted

```python
def plot_box_dist(to_be_plotted, title, xlabel):
    
    f, axes = plt.subplots(2, 1, sharex = 'col', gridspec_kw = {"height_ratios": (0.2, 2)}, figsize = (5,5))
    
    mean = to_be_plotted.mean()
    median = to_be_plotted.median()
    
    sns.boxplot(to_be_plotted, ax = axes[0])
    axes[0].axvline(mean, color = 'r', linestyle='--')
    axes[0].axvline(median, color = 'g', linestyle='-')

    sns.distplot(to_be_plotted, ax = axes[1])
    axes[1].axvline(mean, color = 'r', linestyle='--')
    axes[1].axvline(median, color = 'g', linestyle='-')

    plt.legend({'Mean':mean,'Median':median})

    axes[0].set(xlabel = '', title = title)
    axes[1].set(xlabel = xlabel)

    plt.show()    
```
-----------------------------------------------
### plot_demographics
Plots the number of households per category for the household dataframe.
*   input:
    -   *[pd.DataFrame]*  **hh_demographic_fxd**: dataframe with household data
    
*   output: 
    -   categorical histograms for each category

```python
def plot_demographics(hh_demographic_fxd):
    
    fig, axs = plt.subplots(2, 3, figsize=(18, 13))

    sns.countplot(hh_demographic_fxd['AGE_DESC'], ax=axs[0, 0])

    sns.countplot(hh_demographic_fxd['MARITAL_STATUS_CODE'], ax=axs[0, 1])

    sns.countplot(hh_demographic_fxd['INCOME_DESC'], ax=axs[1, 0])
    axs[1, 0].set_xticklabels(axs[1, 0].get_xticklabels(),
                              rotation=45,
                              horizontalalignment='right')

    sns.countplot(hh_demographic_fxd['HOMEOWNER_DESC'], ax=axs[1, 1])
    axs[1, 1].set_xticklabels(axs[1, 1].get_xticklabels(),
                              rotation=45,
                              horizontalalignment='right')

    sns.countplot(hh_demographic_fxd['KIDS_DESC'], ax=axs[1, 2])
    axs[1, 2].set_xticklabels(axs[1, 2].get_xticklabels(),
                              rotation=45,
                              horizontalalignment='right')

    sns.countplot(hh_demographic_fxd['HOUSEHOLD_SIZE_DESC'], ax=axs[0, 2])


    plt.show()
```
--------------------------------------------
### total_per_year
Calculates the total amount spent per household over a year (year 1 or 2)
*   input: 
    -   *[pd.DataFrame]*  **grouped_trans_spent**: df with transactions per family and information about those transactions. 
    -   *[pandas.core.indexes]*  **trans_clean_hous_ind**: household keys for the households participating that year

*   output: 
    -   pandas dataframe with the total amount spent by each household in year i (1 or 2)

```python
def bud_total_per_year(grouped_trans_spent, trans_clean_hous_ind):
   
    bud_total = [grouped_trans_spent.loc[i]['SALES_VALUE'].sum() for i in trans_clean_hous_ind]
    
    df = pd.DataFrame(index = trans_clean_hous_ind, data = {'yearly spending': bud_total})
    
    df.index.name = 'household_key'
    
    return df
```
-----------------------
### correlation_ratio
Calculates a correlation coefficient between a categorical variable and a continuous variable. 
*   input: 
    -   *[array of categorical variables]*  **categories**: categorical array
    -   *[array of continous variables]*  **measurements**: continuous array

*   output: 
    -   correlation coefficient between 0 and 1

```python
def correlation_ratio(categories, measurements):
  
    fcat, _ = pd.factorize(categories)
    cat_num = np.max(fcat) + 1
    y_avg_array = np.zeros(cat_num)
    n_array = np.zeros(cat_num)
    for i in range(0, cat_num):
        cat_measures = measurements.iloc[np.argwhere(fcat == i).flatten()]
        n_array[i] = len(cat_measures)
        y_avg_array[i] = np.average(cat_measures)

    y_total_avg = np.sum(np.multiply(y_avg_array, n_array)) / np.sum(n_array)
    numerator = np.sum(
        np.multiply(n_array, np.power(np.subtract(y_avg_array, y_total_avg),
                                      2)))
    denominator = np.sum(np.power(np.subtract(measurements, y_total_avg), 2))
    if numerator == 0:
        eta = 0.0
    else:
        eta = np.sqrt(numerator / denominator)
    return eta
```
-----------------------
### cramers_v
Calculates a correlation coefficient between two categorical variables x and y. 
*   input: 
    -   *[categorical variable array]*  **x,y**
    
*   output: 
    -   correlation coefficient between 0 and 1

```python
def cramers_v(x, y):
   
    confusion_matrix = pd.crosstab(x,y)
    chi2 = stats.chi2_contingency(confusion_matrix)[0]
    n = confusion_matrix.sum().sum()
    phi2 = chi2/n
    r,k = confusion_matrix.shape
    phi2corr = max(0, phi2-((k-1)*(r-1))/(n-1))
    rcorr = r-((r-1)**2)/(n-1)
    kcorr = k-((k-1)**2)/(n-1)
    return np.sqrt(phi2corr/min((kcorr-1),(rcorr-1)))
```
-----------------------------------
### create_weekly_cart_df
Creates a dataframe with average weekly quantities of each label for each household
*   input: 
    -   *[pd.DataFrame]*  **trans_clean**: a dataframe with all the transactions per household. Ideally the labels should have been cleaned before.
    
*   output: 
    -   dataframe with average weekly quantities of each label for each household
   
```python
def create_weekly_cart_df(trans_clean, participation_per_hh):
   
    grouped_per_label = pd.DataFrame(trans_clean.groupby(['LABEL','household_key']).sum())
    
    index = trans_clean['household_key'].sort_values().unique()

    weekly_cart_df = pd.DataFrame(index = index)
    weekly_cart_df.index.name = 'household_key'

    for label in trans_clean['LABEL'].unique(): 
        data = [grouped_per_label.loc[label, i]['QUANTITY']/(participation_per_hh['participation_length'][i])  for i in grouped_per_label.loc[label].index]
        
        intermediary_df = pd.DataFrame(index = grouped_per_label.loc[label].index, data = {label +'_QUANT': data})

        weekly_cart_df = weekly_cart_df.join(intermediary_df)

    #Fill NaN values with 0.0:
    weekly_cart_df = weekly_cart_df.fillna(0.0)
    
    return weekly_cart_df
```
-------------------------------------------------------------
### df_weekly_spending
Creates a dataframe with the mean weekly spending for each household
*   input: 
    -   *[pd.DataFrame]*  **df_trans**: dataframe with all transactions per household. 

*   output:
    -   pandas dataframe with mean weekly spending per household

```python
def df_weekly_spending(df_trans):
    
    index = df_trans['household_key'].sort_values().unique()
    
    grouped_per_hh = spending_per_household_per_trans(df_trans)
    
    mean_per_fam = [grouped_per_hh.loc[i]['SALES_VALUE'].sum() / len(grouped_per_hh.loc[i]['WEEK_NO'].unique()) for i in index]
    
    mean_budget_week = pd.DataFrame(index = index, data = {'mean weekly spending': mean_per_fam})
    
    mean_budget_week.index.name = 'household_key'
    
    return mean_budget_week 
```
-------------------------
### mean_yearly_spending
Calculates the mean of yearly spending per household
*   input: 
    -   *[pd.Series]*  **budget_first_year, budget_second_year**: spending per household for year 1 and 2
    
*   output: 
    -   mean of the yearly spending per household
    
```python
def mean_yearly_spending(budget_first_year, budget_second_year):
   
    mean_yearly_spend = budget_first_year.join(budget_second_year, lsuffix='_1')
    
    mean_yearly_spend['mean yearly spending'] = mean_yearly_spend.mean(axis=1)
    
    mean_yearly_spend = mean_yearly_spend.drop(
        ['yearly spending', 'yearly spending_1'], axis=1)
    return mean_yearly_spend
```
------------------------------------
### spending_per_household_per_trans
Creates a new dataframe with the spending per household 
*   input: 
    -   *[pd.DataFrame]*  **trans_clean**: df with total transactions that have clean labels

*   output: 
    -   pandas dataframe that groups the spending per households and adds columns 
    of "WEEK_NO", "TRANS_TIME", "DAY" for when these transactions occured. 

```python
def spending_per_household_per_trans(trans_clean):
    
    grouped = trans_clean.groupby(['household_key', 'BASKET_ID']).sum()
    grouped_count = trans_clean.groupby(['household_key', 'BASKET_ID']).size()

    grouped_trans_spent = pd.DataFrame(grouped[['SALES_VALUE','QUANTITY']])

    grouped_trans_spent['WEEK_NO'] = grouped['WEEK_NO']/grouped_count
    grouped_trans_spent['TRANS_TIME'] = grouped['TRANS_TIME']/grouped_count
    grouped_trans_spent['DAY'] = grouped['DAY']/grouped_count

    return grouped_trans_spent
```
------------------------------------------------
### trans_per_year
Creates a dataframe with the total number of transactions per year for each household.
*   input:
    -   *[pd.DataFrame]*  **trans_clean_year_i*: datframe with all transactions and cleaned labels for year i (1 or 2)
    -   *[pandas.core.indexes]*  **trans_clean_hous_ind_i**: household keys for all households in the cleaned transaction df for year i (1 or 2)

*   output: 
    -   dataframe with total number of transactions per year per household. 

```python
def trans_per_year(trans_clean_year_i, trans_clean_hous_ind_i):
   
    grouped_trans_yeari = trans_clean_year_i.groupby(['household_key','BASKET_ID']).size()
    
    purch_per_hous_yeari = pd.DataFrame(index = trans_clean_hous_ind_i)
    
    total_transactioni = [len(grouped_trans_yeari.loc[i]) for i in trans_clean_hous_ind_i]
    
    purch_per_hous_yeari['total purchase per year'] = total_transactioni
    
    return purch_per_hous_yeari
```
-----------------
