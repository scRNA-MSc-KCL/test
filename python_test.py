#python -m pip install pandas --user
import zipfile
import pandas as pd
print("Testing basic print function")
print("wanted to check if the update actuallly worked")

a = pd.DataFrame({"A":[1,2], "B":[3,4]})
print(a)
t = pd.read_csv("test_dataset.csv")
for i in t:
    print(i)
    
    
with zipfile.ZipFile("testzip.zip", 'r') as zip_ref:
    zip_ref.extractall()
    
    


