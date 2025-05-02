import pandas as pd
import numpy as np
import os
import cv2
from faker import Faker

fake=Faker()

n=1000



student_ids=[fake.uuid4() for _ in range(n)]
total_time_spent=np.round(np.abs(np.random.normal(20,10,n)),2).tolist()
quiz_avg_score=np.clip(np.round(np.random.normal(75,15,n),2),0,100).tolist()
videos_watched=np.random.randint(0,50,n).tolist()
last_login_days_ago=np.random.randint(0,30,n).tolist()
completed=np.random.choice([0,1],size=n,p=[0.3,0.7]).tolist()








data={
    'student_id':student_ids,
    'total_time_spent':total_time_spent,
    'quiz_avg_score':quiz_avg_score,
    'videos_watched':videos_watched,
    'last_login_days_ago':last_login_days_ago,
    'completed':completed
}


df=pd.DataFrame(data)

df.to_csv('D:/CourseSaver AI/CourseSaver-ai/data/edtech.csv',index=False)


