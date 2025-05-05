import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
ROOT_DIR=os.path.dirname(__file__)
data_set_path=os.path.join(ROOT_DIR,'data/edtech.csv')
df=pd.read_csv(data_set_path)



#print(np.array(df.median()))

#df['log_time_spent'] = np.log1p(df['total_time_spent'])
#print(df.head(10))
#df=df.sort_values('total_time_spent',ascending=True)
print("maximum time spent: ",df['total_time_spent'].max())
print("mean time spent: ",df['total_time_spent'].mean())
print("minimum time spent: ",df['total_time_spent'].min())
print("average login duration: ", df['last_login_days_ago'].mean())
print("Average quiz score: ",df['quiz_avg_score'].mean())
print("Deviation of quiz score from it's mean: ",df['quiz_avg_score'].std())


q1=df['quiz_avg_score'].quantile(0.33)
q2=df['quiz_avg_score'].quantile(0.66)
lower_quiz_df=df[df['quiz_avg_score']<=q1]
upper_quiz_df=df[df['quiz_avg_score']>=q2]
central_quiz_df=df[(df['quiz_avg_score']>q1)&(df['quiz_avg_score']<q2)]

final_mean=(lower_quiz_df['quiz_avg_score'].mean()+upper_quiz_df['quiz_avg_score'].mean()+central_quiz_df['quiz_avg_score'].mean())/3
std_deviation=df['quiz_avg_score'].std()
#derived features
df['quiz_deviation']=df['quiz_avg_score']-final_mean
df['actual_engagement']=df['total_time_spent']*df['videos_watched']
df['actual_engagement']=np.where(df['actual_engagement']>300,df['actual_engagement']*0.7,df['actual_engagement'])
better_engagement_mean=(df.head(500)['actual_engagement'].mean()+df.tail(500)['actual_engagement'].mean())/2

def label(row):
    if row['quiz_avg_score']>final_mean+std_deviation:
        return 'star'
    elif row['quiz_avg_score']> final_mean & row['quiz_avg_score'] <final_mean+std_deviation:
        return 'Just avg'
    elif row['actual engagement']>better_engagement_mean & row['quiz_avg_score']> final_mean & row['quiz_avg_score'] <final_mean+std_deviation:
        return 'hardworking but needs help'
    else: 
        return 'At risk'
#df['label_student']=df.apply(label,axis=1)

print("best mean: ",final_mean)
#print(df['quiz_deviation'].head(10))

print("Actual engagement time : ",df['actual_engagement'])

print("Avg engagement time : ",better_engagement_mean)

print("deviation of engagement time : ",df['actual_engagement'].std())

df['total_time_spent'].plot(kind='hist')
plt.title('Time spent')
plt.show()


