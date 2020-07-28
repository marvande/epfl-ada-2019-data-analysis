# epfl-ada-2019-project-bubble582


## Tell me what you buy, and I will tell you who you are.
### Data Story:
The website works on most browsers (google chrome and safari for sure). There are two blog posts on the website: our data story and another with additionnal pre-processing information. Enjoy!  
- Our website: [link](https://projectadabubble582.netlify.com)
- Our second repo that creates the website: [link](https://github.com/marvande/website_ada_bubble582) 

### Abstract
*A 150-word description of the project idea, goals, dataset used. What story you would like to tell and why? What's the motivation behind your project? *

We would like to analyse the Dunnhumby dataset. Living in a time and age where every piece of our data is stored and analysed; and being active consumers ourselves, we would like to see what information retail chains can gather and infer about us knowing only our shopping habits. As transactions over two years of several households **and** their basic demographic profiles are provided, we want to see if there are any links and correlations between specific demographics (e.g. marital status, income, number of children, etc) and purchase patterns. Furthermore, if time permits it, we want to see if we can create a model predicting a consumer demographic profile from their shopping. Thus, we would like to see how "easy" and how precise it actually is for retailers to infer who their customers are by what they buy and target them with specific marketing strategies. Basically, we want to know how much of a target we actually are. 

### Research questions
*A list of research questions you would like to address during the project.*
- What are the main shopping trends that we can identify in this data? 
- Can we relate shopping trends to specific demographic parameters? 
- Can we predict some of these demographic parameters (age, marital status, etc) by knowing the households' habits? 
- In the opposite way, can we predict household’s consumption behaviour by knowing their characteristics?
- What accuracy in consumption prediction can the retailer obtain from a simple profile information? 

### Dataset
*List the dataset(s) you want to use, and some ideas on how you expect to get, manage, process and enrich it/them. Show us you've read the docs and some examples, and you've a clear idea on what to expect. Discuss data size and format if relevant. *
-  The complete journey from Dunnhumby company: this dataset is made of 8 tables and summarize the study of an unknown retailer. Our group is going to focus mostly on HH-demographic, Transactions and Product tables. Dunnhumby also provides tables about specific marketing campaigns and their results. However, our problem is not marketing, but demographic oriented. That is why we decided not to include those other tables in our analysis. We plan to extract households' habits in term of consumption patterns. That is to say, their choices of products, the money they sped in their groceries, their consumer behaviors (when, how much, how fast, how often they buy). 

- We expect to identify a few number (3 to 6) of shopping trend clusters that we can relate to some household profiles and vice versa. To enrich our results, we would to train a model to predict the consumption profile of a random household. 

### Understanding our git repo:
There is a README in each folder explaining its content in detail. What you need to know is the following: 
- doc: contains all documentaion
- source: contains all notebooks (including the main.py)
- data: should be empty on github but should contain the dunnhumby dataset locally on your computer. 
Everything else needed to understand how to run and get our results is in the README of source. 

The file which contains our analysis is the **main.py**. If you read only one, this must be the one for you to understand our analysis.
