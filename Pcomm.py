import pandas as pd
import numpy as nm
import re

import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.tokenize import word_tokenize

df=pd.read_csv('NF.csv')

a=df.groupby('type').count()
print(a)


df = df.dropna(subset=['cast', 'country', 'rating'])

movies= df[df["type"]=="Movie"].reset_index()
movies=movies.drop(['index','show_id','type','date_added','release_year','duration','description'],axis=1)


tv=df[df['type']=='TV Show'].reset_index()
tv=tv.drop(['index','show_id','type','date_added','release_year','duration','description'],axis=1)

actors = []

for i in movies['cast']:
    actor = re.split(r', \s*', i)
    actors.append(actor)

flat_list=[]
for sublist in actors:
    for item in sublist:
        flat_list.append(item)
actors_list = sorted(set(flat_list))
a= len(set(flat_list))
print(a)