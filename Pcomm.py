import pandas as pd
import numpy as nm

df=pd.read_csv('NF.csv')



movies= df[df["type"]=="Movie"].reset_index()
movies=movies.drop(['index','show_id','type','date_added','release_year','duration','description'],axis=1)
print(movies.head())

tv=df[df['type']=='TV Show'].reset_index()
tv=tv.drop(['index','show_id','type','date_added','release_year','duration','description'],axis=1)
print(tv.head())