import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
from utils.functionForFeatures import engagement_level,label,retention_label
from utils.constants import DATA_SET_PATH




ROOT_DIR=os.path.dirname(__file__)
data_set_path=os.path.join(ROOT_DIR,'data/edtech.csv')

def get_featured_df():
    
    df=pd.read_csv(DATA_SET_PATH)



#std_deviation=df['quiz_avg_score'].std()


    df['actual_engagement']=df['total_time_spent']*df['videos_watched']
    df['actual_engagement']=np.where(df['actual_engagement']>300,
                                     df['actual_engagement']*0.7,
                                     df['actual_engagement'])

    df['engagement_level']=df['actual_engagement'].apply(engagement_level)    
    df.groupby('engagement_level')['quiz_avg_score'].mean()
    df['label_student']=df.apply(label,axis=1)

    df['retention_factor']=np.where(
    df['videos_watched']==0,0,
     (df['quiz_avg_score']/100)*(df['actual_engagement']/df['videos_watched']))

    df['retention_level']=df['retention_factor'].apply(retention_label)

    return df


