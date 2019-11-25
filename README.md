# epfl-ada-2019-project-bubble582

## Tell me what you buy and I will tell you who you are

### Abstract
*A 150 word description of the project idea, goals, dataset used. What story you would like to tell and why? What's the motivation behind your project?*

We would like to analyse the Dunnhumby dataset. Living in a time and age where every piece of our data is stored and analysed; and being active consumers ourselves, we would like to see what informations retail chains can gather and infer about us knowing only our shopping habits. As transactions over two years of several households **and** their basic demographic profiles are provided, we want to see if there are any links and correlations between specific demographics (e.g. marital status, income, number of children, etc) and purchase patterns. Furthermore, if time permits it, we want to see if we can create a model predicting a consumer demographic profile from their shopping. Thus, we would like to see how "easy" and how precise it actually is for retailers to infer who their customer is by what they buy and target them with specific marketing. Basically, we want to know how much of a target we actually are. 

### Research questions
*A list of research questions you would like to address during the project.*
- What are the main shopping trends that we can identify in this data ? 
- Can we relate shopping trends to specific demographic parameters ? 
- Can we predict some of these demographic parameters (age, marital statute etc) with knowing the household's habbits? 
- In the opposite way, can we predict household consumption behaviour with knowing its characteristics?
- What accuracy in consumption prediction can the retailer obtain from a simple profile information? 

### Dataset
*List the dataset(s) you want to use, and some ideas on how do you expect to get, manage, process and enrich it/them. Show us you've read the docs and some examples, and you've a clear idea on what to expect. Discuss data size and format if relevant.*
-  The complete journey from Dunnhumby company: this dataset is made of 8 tables summarize the study of the company. Our group is going to focus mostly on HH-demographic, Transactions and Product tables. Dunnhumby also provides tables about specific marketing campains and their results. However our problematic is not marketing, but demographic oriented. That is why we decided not to include them in our analysis. We plan to extract households's habbits in term of consumption. That is to say, their choices  of products, the budget they inject in their groceries, their consumer behaviors (when, how much, how fast, how often etc.). 

- We expect to identify a few number (3 to 6) of shopping trend clusters that we can relate to some household profiles and vice-versa. To enrich our results, we would like if time allows us, to try fitting a model to predict the consumption profile of a random household. 



### A list of internal milestones up until project milestone 2
*Add here a sketch of your planning for the next project milestone.*

Until milestone 2, we plan to have done the cleaning of the data, and the analyses of the trends. 
Thus we plan to follow the programme below:
- Until **07.11** : Clean up the data and prepare the sets we want to keep for the analysis
- Until **14.11** : Study the shopping trends in this dataset : identify the main trends and main household profiles. 
- Until **21.11** : Define more in depth the possible relation (correlations, causality, dependencies etc.) in between shopping trends and household profiles. 
- Until **25.11** : Clean the code 

If time permits it, we will prepare the dataset for the clustering and eventually begin it.
Between milestone 2 and 3, we will really concentrate on the prediction analysis.

### Understanding our git repo:
There is a README in each folder explaining its content in details. What you need to know is the following: 
- doc: contains all documentaion
- source: all notebooks (including the main.py)
-data: should be empty on github but should contain the dunnhumby dataset locally on your computer. 
Everything else needed to understand how to run and get our results is in the README of code. 

#### Next steps till milestone 3: 
A COMPLETER. 
