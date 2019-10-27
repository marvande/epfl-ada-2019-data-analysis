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
List the dataset(s) you want to use, and some ideas on how do you expect to get, manage, process and enrich it/them. Show us you've read the docs and some examples, and you've a clear idea on what to expect. Discuss data size and format if relevant.
-  The complete journey from Dunnhumby company: in this dataset 8 tables summarize the study of the company. We are going to focus mostly on HH-demographic, Transactions and Product tables. Dunnhumby also provides tables about specific marketing campains and their results. However our problematic is not marketing, but demographic oriented. That is why we decided not to include them in our analysis. We plan to extract households's habbits in term of consumption. That is to say their choices  of products, the budget they inject in their groceries, their consumer behaviors (when, how much, how fast, how often etc.). 

- We expect to identify a few number (3 to 6) of shopping trend clusters that we can relate to some household profiles and vice-versa. To enrich our results, we would like if time allows us, to try fitting a model to predict the consumption profile of a random household. 

- Format of the data and data size A COMPLETER : 307MB


### A list of internal milestones up until project milestone 2
*Add here a sketch of your planning for the next project milestone.*
General idea : analyze the dataset in general, i.e. find general trends
And for the milestone 3 : have done some ML analyses to identify big clusters of consumers depending on demographic data 
- Week 1 : Clean up the data and prepare the sets we want to keep
- Week 2 : Statistical analyses : identify the main trends and main household profiles. Define more in depth the possible relation in between shopping trends and household profiles.
- Week 3 : Prepare the dataset for the clustering + clean the code and comment everything

### Questions for TAa
Add here some questions you have for us, in general or project-specific.

