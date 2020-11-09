# -*- coding: utf-8 -*-
"""EDA Black Friday.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SMj4m9CP25XcfdmSc_ClZEF7LgCoRlHJ

# **Black Friday Sales Prediction**
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

! pip install squarify
import squarify

df=pd.read_csv("/content/train.csv")
df.head()

df.info()

"""#### **Note**:
There is null data in Product Category 2 and Product_Category_3.
Of203281 values, Product Category 3 has only 62257 values. Which is just around 1/4 the of the dataset.
"""

df.describe()

"""## **Exploratory Data Analysis**

### **Univarate Analysis**

**Age Distribution**
"""

df['Age'].value_counts()

plt.style.available

plt.style.use('seaborn-whitegrid')
sns.countplot(df['Age'])
plt.title('Age group Distribution',fontdict={'fontsize':20})

age=df['Age'].value_counts()

plt.style.use('default')
squarify.plot(sizes=age.values,label=age.index,value=age.values)
plt.title('Age group wise Distribution',fontdict={'fontsize':20})
plt.show()

"""**Gender Distribution**"""

plt.figure(figsize=(10,8))
plt.style.use('seaborn-whitegrid')
sns.countplot(df['Gender'])
plt.title('Gender Distribution',fontdict={'fontsize':20})

"""**Occupation Distribution**"""

plt.figure(figsize=(14,7))
plt.style.use('seaborn-whitegrid')
sns.countplot(df['Occupation'])
plt.title('Occupation Distribution',fontdict={'fontsize':20})

"""**City_Category Distribution**"""

city=df['City_Category'].value_counts()

plt.style.use('seaborn')
plt.figure(figsize=(10,8))
plt.pie(city.values,labels=city.index,startangle=-30,explode=(0,0.20,0), shadow=True, autopct= '%1.1f%%')
plt.title('City_Category Distribution')
plt.legend()
plt.legend(prop={'size':15})
plt.axis('equal')
plt.show()

"""**Marital Status Distribution**"""

plt.figure(figsize=(10,8))
sns.countplot(df['Marital_Status'])
plt.title('Marital Status Distribution',fontdict={'fontsize':20})

#0: Unmarried
#1: Married

"""**Stay in City Distribution**"""

plt.style.use('seaborn-whitegrid')
sns.countplot(df['Stay_In_Current_City_Years'])
plt.title('Years in City wise Distribution',fontdict={'fontsize':20})

stay=df['Stay_In_Current_City_Years'].value_counts()

plt.style.use('default')
squarify.plot(sizes=stay.values,label=stay.index,value=stay.values)
plt.title('Years in City wise Distribution',fontdict={'fontsize':20})
plt.show()

purchase_prod=df.groupby(['Product_ID']).Purchase.agg('mean').to_frame('Mean_Purchase_Value').reset_index()
purchase_prod.sort_values('Mean_Purchase_Value',ascending=False)

df['User_ID'].nunique()

"""5891 Unique Customers did shopping during Black Friday"""

df['Product_ID'].nunique()

"""3631 Unique Products were sold during Black Friday

**Purchase Distribution**
"""

plt.figure(figsize=(14,7))
sns.distplot(df['Purchase'],bins=20)
plt.title('Distribution of Purchase amount',fontdict={'fontsize':20})
plt.xlabel('Amount')
plt.ylabel('Number of People')

"""### **Bivarate Analysis**

**Age-Gender Distribution**
"""

plt.figure(figsize=(10,8))
sns.countplot(df['Age'],hue=df['Gender'])
plt.title('Gender wise - Age Distribution',fontdict={'fontsize':20})

"""**Age Group vs Purchase**"""

plt.style.use( 'seaborn-pastel')
sns.boxplot(df['Age'],df['Purchase'])
plt.title('Age group wise Purchase',fontdict={'fontsize':20})
plt.ylabel('Purchase Amount')
plt.show()

age = ('0-17','18-25','26-35','36-45','46-50','51-55','55+')
purchase = []
for g in age:
    purchase.append(df[df['Age'] == g]['Purchase'].sum())

print(purchase)

obj = ('0-17','18-25','26-35','36-45','46-50','51-55','55+')
y_pos = np.arange(len(obj))

plt.bar(y_pos, purchase, align='center', alpha=0.5)
plt.xticks(y_pos, obj)
plt.ylabel('Money spent')
plt.title('Age vs Purchase')

plt.show()

"""**Gender vs Purchase**"""

plt.style.use( 'seaborn-pastel')
sns.boxplot(df['Gender'],df['Purchase'])
plt.ylabel('Purchase Amount')
plt.title('Gender wise Purchase',fontdict={'fontsize':20})

gender = ('M','F')
purchase = []
for g in gender:
    purchase.append(df[df['Gender'] == g]['Purchase'].sum())

print(purchase)

obj = ('M','F')
y_pos = np.arange(len(obj))

plt.bar(y_pos, purchase, align='center', alpha=0.5)
plt.xticks(y_pos, obj)
plt.ylabel('Money spent')
plt.title('Gender vs Purchase')

plt.show()

"""**Occupation vs Purchase**"""

plt.style.use( 'seaborn-pastel')
sns.boxplot(df['Occupation'],df['Purchase'])
plt.ylabel('Purchase Amount')
plt.title('Occupation wise Purchase',fontdict={'fontsize':20})

occupations_id = list(range(0, 21))
purchase = []
for oid in occupations_id:
    purchase.append(df[df['Occupation'] == oid]['Purchase'].sum())

print(purchase)

obj = ('0', '1', '2', '3', '4', '5','6','7','8','9','10', '11','12', '13', '14', '15', '16', '17', '18', '19', '20')
y_pos = np.arange(len(obj))

plt.bar(y_pos, purchase, align='center', alpha=0.5)
plt.xticks(y_pos, obj)
plt.ylabel('Money spent')
plt.title('Occupation ID vs Purchase')

plt.show()

"""**City_Category vs Purchase**"""

plt.style.use( 'seaborn-pastel')
sns.boxplot(df['City_Category'],df['Purchase'])
plt.ylabel('Purchase Amount')
plt.title('City Category wise Purchase',fontdict={'fontsize':20})

status = ('A','B','C')
purchase = []
for g in status:
    purchase.append(df[df['City_Category'] == g]['Purchase'].sum())

print(purchase)

obj = ('A','B','C')
y_pos = np.arange(len(obj))

plt.bar(y_pos, purchase, align='center', alpha=0.5)
plt.xticks(y_pos, obj)
plt.ylabel('Money spent')
plt.title('City Category vs Purchase')

plt.show()

"""**Marital Status vs Purchase**"""

plt.style.use( 'seaborn-pastel')
sns.boxplot(df['Marital_Status'],df['Purchase'])
plt.ylabel('Purchase Amount')
plt.title('Marital Status wise Purchase',fontdict={'fontsize':20})

status = (0,1)
purchase = []
for g in status:
    purchase.append(df[df['Marital_Status'] == g]['Purchase'].sum())

print(purchase)

obj = (0,1)
y_pos = np.arange(len(obj))

plt.bar(y_pos, purchase, align='center', alpha=0.5)
plt.xticks(y_pos, obj)
plt.ylabel('Money spent')
plt.title('Marital Status vs Purchase')

plt.show()

"""**Stay in City  vs Purchase**"""

plt.style.use( 'seaborn-pastel')
sns.boxplot(df['Stay_In_Current_City_Years'],df['Purchase'])
plt.ylabel('Purchase Amount')
plt.title('Year wise Current Stay in City wise Purchase',fontdict={'fontsize':20})

status = ('0','1','2','3','4+')
purchase = []
for g in status:
    purchase.append(df[df['Stay_In_Current_City_Years'] == g]['Purchase'].sum())

print(purchase)

obj = ('0','1','2','3','4+')
y_pos = np.arange(len(obj))

plt.bar(y_pos, purchase, align='center', alpha=0.5)
plt.xticks(y_pos, obj)
plt.ylabel('Money spent')
plt.title('Stay in Current City vs Purchase')

plt.show()

"""### **Multivarate Analysis**"""

sns.heatmap(df.corr(), annot = True)
plt.title("HeatMap of Correlation Matrix")
plt.show()

"""## **Data Cleaning**

- Product Category 3 has values only for around 30% data. It would be wise to drop the column
- UserId means individual customer, it does not help us in predicting the value of Purchase
-ProductId means individual customer, it does not help us in predicting the value of Purchase
- In Product Category 2, null values can be adjusted my using the mean value.
- Removing '+' from 'Age' and 'Stay_In_Current_City_Years'
- We have to encode, Gender, Age group, City. 
- We have to convert data type of 'Stay in City' to int.

**Merging Datasets**
"""

test=pd.read_csv('/content/test.csv')

df['source']='train'
test['source']='test'

data=pd.concat([df,test])

"""**Dropping Features**"""

data.drop('Product_Category_3', axis = 1, inplace = True)

data.drop('User_ID', axis = 1, inplace = True)

data.drop('Product_ID', axis = 1, inplace = True)

"""**Adjusting value of Product_Category 2**"""

data['Product_Category_2'].fillna(data['Product_Category_2'].mean(), inplace = True)

"""**Replacing '+' in Age & 'Stay_In_Current_City_Years'**"""

data['Age']=data['Age'].apply(lambda x: str(x).replace('55+','55'))

data['Stay_In_Current_City_Years']=data['Stay_In_Current_City_Years'].apply(lambda x: str(x).replace('4+','4'))

"""**Encoding  Gender, Age group, City.**"""

from sklearn.preprocessing import LabelEncoder

label_encoder_gender=LabelEncoder()
data['Gender']=label_encoder_gender.fit_transform(data['Gender'])

label_encoder_age=LabelEncoder()
data['Age']=label_encoder_age.fit_transform(data['Age'])

label_encoder_city=LabelEncoder()
data['City_Category']=label_encoder_city.fit_transform(data['City_Category'])

"""**Converting Datatype to int**"""

data['Stay_In_Current_City_Years'] = data['Stay_In_Current_City_Years'].astype('int')

"""**Data Analysis**
-Most Populated Age Group is 26-25 years
- More Males than Females
- Occupation number 0 and 4 employ the most customers.
- Occupation number 8 and 9 employ the least customers.
- Most Customers are from City B
- Majority of Customers are Unmarried
- Most customers are living in the city for 1 years
- Age wise the mean purchase is of around 8000(currency)
- There is a direct correlation with number of customers and
amount spent .
"""



