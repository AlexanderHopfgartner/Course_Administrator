import pandas as pd
from tabulate import tabulate

# create a sample DataFrame
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
        'age': [25, 30, 35, 40, 45],
        'salary': [50000, 60000, 70000, 80000, 90000]}
df = pd.DataFrame(data)

# convert the first five rows of the DataFrame to a list of lists
table = df.head(0).values.tolist()

# display the table centered in the terminal
print(tabulate(table, headers=df.columns, tablefmt='plain', numalign='center', stralign='center'))
