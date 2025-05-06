import numpy as np
from features import engagement_q1,engagement_q2,final_quiz_mean,std_deviation,better_engagement_mean

def engagement_level(val):
    if val<= engagement_q1:
        return 'low'
    if val >=engagement_q2:
        return 'high'
    else:
        return 'medium'
    
    
def label(row):
    if row['quiz_avg_score']>final_quiz_mean+std_deviation:
        return 'star'
    elif row['quiz_avg_score']> final_quiz_mean:
        return 'Just avg'
    elif row['actual engagement']>better_engagement_mean & row['quiz_avg_score']> final_quiz_mean:
        return 'hardworking but needs help'
    else: 
        return 'At risk'    
    
    
def retention_label(val):
    if val <20:
        return 'poor'
    elif val<50:
        return 'average'
    else:
        return 'strong'
    