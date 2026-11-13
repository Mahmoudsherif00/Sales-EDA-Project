import pandas  as pd 
import seaborn as sns

data = pd.read_csv('Superstore.csv', encoding='windows-1252')
print('Data Shape:')
print(data.shape)
print('-------------------------------------------------------')

print('Data Types:')
print(data.dtypes)
print('--------------------------------------------------------')

print('Columns:')
print(data.columns)
print('--------------------------------------------------------')

print('Unique Values in Sales Column:')
print(data['Sales'].unique())
print('--------------------------------------------------------')

print('Unique Values in Ship Mode Column:')
print(data['Ship Mode'].unique())
print('--------------------------------------------------------')

print('Unique Values in Segment Column:')
print(data["Segment"].unique())
print('--------------------------------------------------------')

print('Unique Values in Country Column:')
print(data["Country"].unique())
print('--------------------------------------------------------')

print('Unique Values in City Column:')
print(data["City"].unique())
print('--------------------------------------------------------')

print('Unique Values in Region Column:')
print(data['Region'].unique())
print('--------------------------------------------------------')

print('Unique Values in Category Column:')
print(data['Category'].unique())
print('--------------------------------------------------------')

print('Unique Values in Sub-Category Column:')
print(data['Sub-Category'].unique())
print('--------------------------------------------------------')

print('Data Description:')
print(data.describe(include="all"))
print('--------------------------------------------------------')

print('Data After Dropping Columns:')
df = data.drop(
    ['Row ID', 'Order ID', 'Order Date', 'Customer ID',
     'Customer Name', 'Product ID' , 'Ship Date'],
    axis=1
)
print(df)
print('--------------------------------------------------------')

print('Data Shape:')
print(df.shape)
print('--------------------------------------------------------')


print('Data Types:')
print(df.dtypes)

print('--------------------------------------------------------')
dataframe = [
    ["Ship Mode" , "the type of shipping used" , df["Ship Mode"].dtype , " Categorical Feature "] , 
    ["Segment" , "the segment of the customer" , df["Segment"].dtype , " Categorical Feature "] ,
    ["Country" , "the country of the customer" , df["Country"].dtype , " Categorical Feature "] ,
    ["City" , "the city of the customer" , df["City"].dtype , " Categorical Feature "] ,
    ["Postal Code" , "the postal code of the customer" , df["Postal Code"].dtype , " Categorical Feature "] ,
    ["Region" , "the region of the customer" , df["Region"].dtype , " Categorical Feature "] ,
    ["Category" , "the category of the product" , df["Category"].dtype , " Categorical Feature "] ,
    ["Sub-Category" , "the sub-category of the product" , df["Sub-Category"].dtype , " Categorical Feature "] ,
    ["Product Name" , "the name of the product" , df["Product Name"].dtype , " Categorical Feature "] ,
    ["Sales" , "the sales of the product" , df["Sales"].dtype , " Numerical Feature "] ,
    ["Quantity" , "the quantity of the product" , df["Quantity"].dtype , " Numerical Feature "] ,
    ["Discount" , "the discount of the product" , df["Discount"].dtype , " Numerical Feature "] ,
    ["Profit" , "the profit of the product" , df["Profit"].dtype , " Numerical Feature "] ,
]
columns = ["Feature Name", "Description", "Data Type", "Feature Type"]

dataframe = pd.DataFrame(dataframe, columns=columns)

print('Dataframe:')
print(dataframe)
print('--------------------------------------------------------')

categorical_features = dataframe.loc[
    dataframe['Feature Type'].str.strip() == 'Categorical Feature',
    'Feature Name'
].tolist()

print('Categorical Features:')
print(categorical_features)
print('--------------------------------------------------------')
dataframe_categorical = [
    [categorical_features[0], "Ordinal Categorical Feature"] , 
    [categorical_features[1], "Nominal Categorical Feature"],
    [categorical_features[2], "Binary Categorical Feature"],
    [categorical_features[3], "Nominal Categorical Feature"],
    [categorical_features[4], "Ordinal Categorical Feature"],
    [categorical_features[5], "Nominal Categorical Feature"],
    [categorical_features[6], "Binary Categorical Feature"],
    [categorical_features[7], "Nominal Categorical Feature"],
    [categorical_features[8], "Ordinal Categorical Feature"],
]


print('Categorical Features with Types:')
print(dataframe_categorical)
print('--------------------------------------------------------')
columns = ["Feature Name", "Feature Type"]


dataframe_categorical = pd.DataFrame(dataframe_categorical, columns=columns)
print(dataframe_categorical)
print('--------------------------------------------------------')


Numerical_features = dataframe.loc[
    dataframe['Feature Type'].str.strip() == 'Numerical Feature',
    'Feature Name'
].tolist()
print('Numerical Features:')
print(Numerical_features)
print('--------------------------------------------------------')
print('Dataframe:')
dataframe_Numerical=[
    [Numerical_features[0], "Continuous Numerical Feature"],
    [Numerical_features[1], "Discrete Numerical Feature"],
    [Numerical_features[2], "Ratio Numerical Feature"],
    [Numerical_features[3], "Interval Numerical Feature"]
]
print('Numerical Features with Types:')
print(dataframe_Numerical)
print('--------------------------------------------------------')
