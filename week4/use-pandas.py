import pandas as pd

#a
data_url = "epldata_final.csv"
text = pd.read_csv(data_url)
print(text.head(5))

#b
text.rename(index = {0:'zero', 1:'one'}, inplace = True)
print(text.head(10))

#c
text2 = pd.read_csv(data_url, index_col = "name")
choice_columns = text2[5:9]
print(choice_columns)
print(type(choice_columns))

#d
print(text.columns)
text.rename(columns={'position':'pos','position_cat':'pos_cat'},inplace=True)
print(text.columns)
