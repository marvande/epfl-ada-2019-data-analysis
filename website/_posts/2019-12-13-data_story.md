---
layout: post
title:  "Tell me what you buy, I will tell you who you are. A data story."
date:   2019-12-12
excerpt: "A story about shopping patterns."
image: "/images/pic07.jpg"
---

## Preface: 
Due to rumours about the troublesome ability of shopping centers to infer consumer information based on their shopping patterns, a private investigator, detective Duck, was hired by a consumer advocacy group to investigate the matter. Here are the details of his investigation. 

<style>
    .img-container{
        text-align: center;
    }
</style>
<body>
<div class = 'img-container'>
<img src="{{ "/images/pic08.png" | absolute_url }}"
    alt="Markdown Monster icon" width = "200" height = "300" />
</div>
</body>

Living in a time and age where every piece of our data is stored and analysed, the consumer advocacy group wonders what information retailers can gather and infer about consumers. To answer their question, detective Duck only gets information about a two year shopping spree of a group of 2500 clients of an unknown shopping center in the US. Based on this data, he seeks to identify possible links, if they exist, between demographic information (e.g. marital status, income, number of children, etc) and  purchase patterns. In other words, he would like to see how "easy" and how precise it is for retailers to infer a specific customer profile based on what their shopping habits as this could lead to easy targeted marketing. Luckily, detective Duck has followed the autumn 2019 Applied Data Analysis at the EPFL and counts on applying his newly aquired knowledge to this case. 

## Chapter 1. A rocky start to a rocky investigation. 

**A Dunnhumby dataset.**

The consumer advocacy group (also called G.A.C) provided the detective Duck  with a dataset owned by Dunhumby, an american data science company. This dataset includes the results of a two years long study, over 2500 voluntary households. Detective Duck knows that companies use harvested data to perform targeted marketing. Using his skills in data analysis, he plans to find out exactly what can be predicted out about the customer's personnal information. He expects to observe an relation in between the clients's consumption habits and their demographic characteristics. For example, he suspects that the income category will influence the amount and price range of groceries bought per week. 

**Preprocessing.**  
  When facing a huge amount of data, detective Duck has learned to start by preprocessing and cleaning the available information. For this, he keeps only households which portrayed coherent and sufficient demographic data. In a second time he labels the products with precise categories refering to grocery shopping.

*Demogrpahics*
 Detective Duck had to face a main issue when preprocessing his demographic data. Indeed, over the 2500 households studied by Dunhumby, only 780 provided their demographic information. Among these 780 families, around 750 were selected after cleaning. At this moment, suspicions started to arise in detective Duck's mind. This a too small amount of data might cause troubles. Nevertheless, after a long night of working and cursing, the data was finally usable and analysable. 

<style>
    .img-container{
        text-align: center;
    }
</style>
<body>
<div class = 'img-container'>
<img src="{{ "/images/pic09.png" | absolute_url }}"
    alt="Markdown Monster icon" width = "400" height = "300" />
</div>
</body>

*Products*   
After families selection, the detective Duck still needs to look at what they buy. The 750 selected families had access to a total of 92353 different products in their shopping center. These products are defined by their department (the place at which we find them) and by two different and non standard descriptive words sequences (commodity and sub-commodity). To be able to classify them the detective creates a function comparing both the commodity and the sub-commodity to a list of expressions from the lexical field of the grocery. He associates each expression to a certain grocery category. Since the products' descriptions are atypical, he give them a "score of similarity" with the expressions in the list. The highest score, above a certain threshold determines the label of the product. He uses the Fuzzywuzzy library to calculate this score. Fuzzywuzzy is based on Levenshtein Distance to calculate the differences and similarities between string sequences. 


## Chapter 2. Profiling is not a piece of cake. 

Now the data are ready for the analysis, the detective Duck is excited about facing the real challenge: profile prediction using machine learning. His goal is to extract the main consumption patterns of the shopping center's clients, and correlate them to their demographic features. For this purpose, he is already developping several clever strategies. Despite all his efforts, the investigation will turn out to be harder than he tought when venturing into this case. Looking at the data, he will quickly regret ever leaving his cozy pond...

*First round predc







