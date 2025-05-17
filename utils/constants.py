import os
import pandas as pd
import numpy as np

ROOT_DIR=os.path.dirname(os.path.dirname(__file__))
data_set_path=os.path.join(ROOT_DIR,'data/edtech.csv')
dataframe=pd.read_csv(data_set_path)


#quiz_mean

std_deviation=dataframe['quiz_mean'].std()

def quiz__mean():
    quiz_q1=df['quiz_avg_score'].quantile(0.33)
    quiz_q2=df['quiz_avg_score'].quantile(0.66)
    lower_quiz_df=df[df['quiz_avg_score']<=quiz_q1]
    upper_quiz_df=df[df['quiz_avg_score']>=quiz_q2]
    central_quiz_df=df[(df['quiz_avg_score']>quiz_q1)&(df['quiz_avg_score']<quiz_q2)]

#better quiz mean

    quiz_mean=(lower_quiz_df['quiz_avg_score'].mean()+
                 upper_quiz_df['quiz_avg_score'].mean()+
                  central_quiz_df['quiz_avg_score'].mean())/3
    return quiz_mean

quiz_mean=quiz__mean()

def engagement_mean(df):
    df['actual_engagement']=df['total_time_spent']*df['videos_watched']
    df['actual_engagement']=np.where(df['actual_engagement']>300,
                                     df['actual_engagement']*0.7,
                                     df['actual_engagement'])
    
    engagement_q1=df['actual_engagement'].quantile(0.33)
    engagement_q2=df['actual_engagement'].quantile(0.66)
    
    lower_engagement_df=df[df['actual_engagement']<=engagement_q1]
    upper_engagement_df=df[df['actual_engagement']>=engagement_q2]
    central_engagement_df=df[(df['actual_engagement']>engagement_q1)&
                             (df['actual_engagement']<engagement_q2)]

    better_engagement_mean=(lower_engagement_df['actual_engagement'].mean()+
                        upper_engagement_df['actual_engagement'].mean()+
                        central_engagement_df['actual_engagement'].mean())/3
    
    return better_engagement_mean,engagement_q1,engagement_q2

better_engagement_mean,engagement_q1,engagement_q2=engagement_mean(dataframe)

dataframe['quiz_deviation']=dataframe['quiz_avg_score']-quiz_mean

