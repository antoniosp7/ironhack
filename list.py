import pandas as pd
from pymongo import MongoClient
from pandas.io.json import json_normalize


client =  MongoClient("mongodb+srv://admin:admin@cluster0.lwcgs.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.Ironhack

input_data = db.Student
data = pd.DataFrame(list(input_data.find()))

print(data)