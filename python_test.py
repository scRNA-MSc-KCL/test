import pandas as pd

print("Testing basic print function")

t = pd.read_csv("test/test_dataset.csv")
for i in t:
    print(i)
    

