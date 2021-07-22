#python -m pip install pandas --user

!pip install pandas
!pip install scanpy
!pip install tensorflow

import zipfile
import pandas as pd
import scanpy as sc
import tensorflow

print("Testing basic print function")
print("wanted to check if the update actuallly worked")

a = pd.DataFrame({"A":[1,2], "B":[3,4]})
print(a)
t = pd.read_csv("test_dataset.csv")
for i in t:
    print(i)
    
    
with zipfile.ZipFile("testzip.zip", 'r') as zip_ref:
    zip_ref.extractall()

f = open("myfile.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

f = open("myfile.txt", "r")
print(f.read())


