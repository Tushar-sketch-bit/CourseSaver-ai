#import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import pandas as pd
import os
from utils.features import get_featured_df
ROOT_DIR=os.path.dirname(__file__)
features_path=os.path.join(ROOT_DIR,'features.py')

le=LabelEncoder()

df=get_featured_df()

X=df[['total_time_spent','videos_watched','actual_engagement','quiz_avg_score']]
y=df['label_student']

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

model=RandomForestClassifier()
model.fit(X_train,y_train)


y_pred=model.predict(X_test)
print(classification_report(y_test,y_pred=y_pred))


