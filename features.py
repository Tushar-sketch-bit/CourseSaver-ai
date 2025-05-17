import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
from utils.functionForFeatures import engagement_level,label,retention_label





ROOT_DIR=os.path.dirname(__file__)
data_set_path=os.path.join(ROOT_DIR,'data/edtech.csv')
df=pd.read_csv(data_set_path)



print("maximum time spent: ",df['total_time_spent'].max())
print("mean time spent: ",df['total_time_spent'].mean())
print("minimum time spent: ",df['total_time_spent'].min())
print("average login duration: ", df['last_login_days_ago'].mean())
print("Average quiz score: ",df['quiz_avg_score'].mean())
print("Deviation of quiz score from it's mean: ",df['quiz_avg_score'].std())
std_deviation=df['quiz_avg_score'].std()

#derived features of quiz scores
#quiz_q1=df['quiz_avg_score'].quantile(0.33)
#quiz_q2=df['quiz_avg_score'].quantile(0.66)
#lower_quiz_df=df[df['quiz_avg_score']<=quiz_q1]
#upper_quiz_df=df[df['quiz_avg_score']>=quiz_q2]
#central_quiz_df=df[(df['quiz_avg_score']>quiz_q1)&(df['quiz_avg_score']<quiz_q2)]

#better quiz mean

#final_quiz_mean=(lower_quiz_df['quiz_avg_score'].mean()+
                 #upper_quiz_df['quiz_avg_score'].mean()+
                 # central_quiz_df['quiz_avg_score'].mean())/3

#df['quiz_deviation']=df['quiz_avg_score']-final_quiz_mean

#derived features of actual engagement
#df['actual_engagement']=df['total_time_spent']*df['videos_watched']
#df['actual_engagement']=np.where(df['actual_engagement']>300,df['actual_engagement']*0.7,df['actual_engagement'])
#engagement_q1=df['actual_engagement'].quantile(0.33)
#engagement_q2=df['actual_engagement'].quantile(0.66)
#lower_engagement_df=df[df['actual_engagement']<=engagement_q1]
#upper_engagement_df=df[df['actual_engagement']>=engagement_q2]
#central_engagement_df=df[(df['actual_engagement']>engagement_q1)&(df['actual_engagement']<engagement_q2)]

#better engagement mean

#better_engagement_mean=(lower_engagement_df['actual_engagement'].mean()+
                        #upper_engagement_df['actual_engagement'].mean()+
                        #central_engagement_df['actual_engagement'].mean())/3

df['actual_engagement']=df['total_time_spent']*df['videos_watched']
df['actual_engagement']=np.where(df['actual_engagement']>300,df['actual_engagement']*0.7,df['actual_engagement'])

df['engagement_level']=df['actual_engagement'].apply(engagement_level)    
df.groupby('engagement_level')['quiz_avg_score'].mean()
df['label_student']=df.apply(label,axis=1)

df['retention_factor']=np.where(
    df['videos_watched']==0,0,(df['quiz_avg_score']/100)*(df['actual_engagement']/df['videos_watched'])
)

df['retention_level']=df['retention_factor'].apply(retention_label)
#print("best mean: ",final_quiz_mean)
#print("Actual engagement time : ",df['actual_engagement'])
#print("Avg engagement time : ",better_engagement_mean)
#print("deviation of engagement time : ",df['actual_engagement'].std())
df['total_time_spent'].plot(kind='hist')
plt.title('Time spent')
plt.show()


