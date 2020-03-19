# Advertisement_Tagging
Predicting tags for job advertisements.

## AIM
Badly tagged job advertisements can fail to attract relevant jobseekers. This can result in a low number of applicants and the vacancies not being filled. The aim of this project is to predict three different tags for different ads.

## DATA
The dataset consists of 2 files, which are train and test sets. These are json files. They consist of the title, which is the title of the vacancy and the description, which descibes the vacancy. The tags are workplaces, subjects and positions. These tags are the labels for the supervised learning algorithms. 

The train and test sets were too large to be uploaded as single files so they were broken down into smaller pieces. They can be found in the train and test folders. These smaller pieces can be combined together by using the combineData function that is in the combData.py file. 

## ML MODELS
At the moment logistic regression, Naive Bayes and Neural Network models are trained for each tag seperately. For future work, a multi-task learning model will be implemened. Also LSTMs can be another approach that can give more promising results. The models were compared based on accuracy measured on hold-out validation dataset.  
