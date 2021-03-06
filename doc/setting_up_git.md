# Small step by step to make sure you are ready to code ! 


## Repo structure: 
- **Code** : contains the notebook and all other code we need
- **Data** : contains data we create and the data we use (Attention you need to add the dataset yourself, see below in "Setting up your data)
- **Doc** : contains all documentation like the leaflet from dunnhumby and more if needed. 


## Ignoring outputs in jupyter notebook: 

### Automatically: 
Once you've activated your ada conda environment and you are in the git repo: 

- $ conda install -c conda-forge nbstripout 
- $ nbstripout --install --attributes .gitattributes


I'd advise you install the plugin to do it automatically just to be sure, but if that does not work there still is the manual method below. 

### Manually: 
In jupyter notebook, go to Kernel -> Restart & Clear Output \n
Do this everytime before pushing!


## Setting up your data:
Right now, no csv files are pushed to our repository. In case we need to push some small data we can still change that. Anyway, never ever push the dunnhumby data as they are too big for git (but this is included in the gitignore so you don't have to worry about it, but you never know. If you ever see an unwanted csv file in your "git status" don't push it ! Do a "git checkout"). So that you have it available and ready on your laptop you need to : 
- downlaod the whole dataset "complete journey" from : https://www.dunnhumby.com/careers/engineering/sourcefiles
- Copy only the **csv files** into **data/dunnhumby_complete_csv/** folder
