import pandas as pd

#create dictionary to store data
data = {
    "id": [1, 2, 3, 4, 5],
    "name": ["John Doe", "Jane Smith", "Alice Johnson", "Bob Brown", "Charlie Davis"],
    "age": [28, 34, 22, 45, 30],
    "city": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
} 

#convert dictionary to dataframe
df = pd.DataFrame(data)

#"show data"
print(df)