import zipfile
print("This is a test file in python")
with zipfile.ZipFile("test/test_dataset.zip", 'r') as zip_ref:
    zip_ref.extractall(test)
