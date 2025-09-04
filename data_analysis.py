from statistics import correlation

import pandas as pd
import matplotlib.pyplot as plt
import seaborn  as sns
import numpy as np

df = pd.read_csv(r"C:\Users\Muthuvalli\Downloads\Banking.csv")
print(df.head(5))
print(df.shape)
print(df.info)
#Generate descripticve statistics for a dataframe
print(df.describe())
bins = [0,100000,300000,float('inf')]
labels = ['low','med','high']
df['Income Band'] = pd.cut(df['Estimated Income'], bins=bins, labels=labels, right=False)
print(df['Income Band'].value_counts().plot(kind = 'bar',color=['skyblue', 'orange', 'green'],edgecolor='black'))
plt.title('Distribution of Income Bands', fontsize=14)
plt.xlabel('Income Band', fontsize=12)
plt.ylabel('Number of People', fontsize=12)
plt.show()

#Examine the distribution of unique categories in categorical columns
categorial_cols = df[['BRId',"GenderId","IAId","Amount of Credit Cards","Nationality","Occupation","Fee Structure","Loyalty Classification","Properties Owned","Risk Weighting","Income Band"]].columns
for col in categorial_cols:
    print(f"Value Count  for '{col}':")
    print(df[col].value_counts())
'''
for i,predictor in enumerate(df[['BRId',"GenderId","IAId","Amount of Credit Cards","Nationality","Occupation","Fee Structure","Loyalty Classification","Properties Owned","Risk Weighting","Income Band"]].columns):
    plt.figure(i)
    sns.countplot(data=df,x=predictor,hue='Nationality')
    plt.show()

#Histplot of value counts for different occupation
for col in categorial_cols:
    if col == "Occupation":
        continue
    plt.figure(figsize=(8,4))
    sns.countplot(x=df[col])
    plt.title(f"Histogram of {col} count")
    plt.xlabel(col)
    plt.ylabel("Count")
    plt.show()
'''
#Numericsl analysis
numerical_cols = ['Estimated Income','Superannuation Savings','Credit Card Balance','Bank Loans','Bank Deposits','Checking Accounts','Saving Accounts','Foreign Currency Account','Business Lending']

plt.figure(figsize=(15,10))  # bigger canvas
for i, col in enumerate(numerical_cols):
    plt.subplot(4, 3, i+1)
    if col in df.columns:   # safe check to avoid KeyError
        sns.histplot(df[col], kde=True)
        plt.title(f"Distribution of {col}")
    else:
        plt.text(0.5, 0.5, f"Column '{col}' not found",
                 ha='center', va='center', fontsize=12, color='red')
plt.tight_layout()
plt.show()

#Heatmaps
correlation_matrix = df[numerical_cols].corr()
sns.heatmap(correlation_matrix,annot=True,cmap='crest',fmt='.2f')
plt.title("correlation Matrix")
plt.show()