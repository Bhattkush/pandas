#A Series is like a single column of data with labels (index).

import pandas as pd

data = [10,20,30,40]
series = pd.Series(data , index=["a","b","c","d"])
print(series)
