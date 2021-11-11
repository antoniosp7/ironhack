# Imports
import pandas as pd
from pymongo import MongoClient
from datetime import datetime
import sched, time

s = sched.scheduler(time.time, time.sleep)

def loadData(sc): 
    print("Ejecutando carga de datos cada 60 segundos")

    # Connect to MongoDB
    client =  MongoClient("mongodb+srv://admin:admin@cluster0.lwcgs.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.Ironhack

    print(db.Student)

    source = db.StudentDataset
    collection = db.Student

    data = pd.DataFrame(list(source.find()))

    print(data)

    data.reset_index(inplace=True)
    data_dict = data.to_dict("records")

    collection.insert_many(data_dict)
    
    s.enter(20, 1, loadData, (sc,))

s.enter(20, 1, loadData, (s,))
s.run()
