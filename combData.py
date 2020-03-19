import os
import json

def combineData():
    """
    Combines the individual test sets into one test set and combines the individual train sets into one train set.
    The whole test and train sets were divided into smaller sets n order to be able to upload the files to GitHub.
    
    You can use this function to create one train set and one test set from the individual sets before training 
    your models. 
    """
    
    if not os.path.exists('datasets'):
        os.makedirs('datasets')
    
    testData = []

    for index in range(5):
        with open("test/test" + str(index) + ".json") as infile:
            for line in infile:
                testData.extend(json.loads(line))
    with open('datasets/test.json', 'w') as fout:
        json.dump(testData, fout)
        
        
    trainData = []

    for index in range(18):
        with open("train/train" + str(index) + ".json") as infile:
            for line in infile:
                trainData.extend(json.loads(line))
    with open('datasets/train.json', 'w') as fout:
        json.dump(trainData, fout)

