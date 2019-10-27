# Small step by step to make sure you are ready to code ! 

## Ignoring outputs in jupyter notebook: 


### Automatically: 
Once you've activated your ada conda environment and you are in the git repo: 

- $ conda install -c conda-forge nbstripout 
- (Ignore this for now as I've added it to the attributes already, I think it should work like this $ nbstripout --install --attributes .gitattributes)


I'd advise you install the plugin to do it automatically just to be sure, but if that does not work there still is the manual method below. 

### Manually: 
In jupyter notebook, go to Kernel -> Restart & Clear Output \n
Do this everytime before pushing!


## Setting up your data:
Right now, no csv files are pushed to our repository. In case we need to push some small data we can still change that. Anyway, never ever push the dunnhumby data as they are too big for git. So that you have it available and ready on your laptop you need to : 
- downlaod the whole dataset "complete journey" from : https://www.dunnhumby.com/careers/engineering/sourcefiles
- Copy only the **csv files** into **data/dunnhumby_complete_csv/** folder
