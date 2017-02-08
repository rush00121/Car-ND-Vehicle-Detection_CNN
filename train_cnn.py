import pandas as pd
import path
import os
directories = ["../object-detection-crowdai","../object-dataset"]

for directory in directories:
    df = pd.read_csv(directory + os.path.sep + "labels.csv")
    print (df.head())