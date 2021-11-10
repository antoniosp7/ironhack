# Imports
import pandas as pd
from pymongo import MongoClient
from datetime import datetime
import sched, time

s = sched.scheduler(time.time, time.sleep)

def loadData(sc): 
    print("Ejecutando carga de datos cada 60 segundos")

    # Load csv dataset
    data = pd.read_csv('students.csv', sep=';')

    created_date = []
    update_date = []

    for i in range(len(data)):
        dateTimeObj = datetime.now()
        created_date.append(dateTimeObj)
        update_date.append(dateTimeObj)


    data['created_date'] = created_date
    data['update_date'] = update_date

    print(data)

    # Connect to MongoDB
    client =  MongoClient("mongodb+srv://admin:admin@cluster0.lwcgs.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client['Ironhack']
    collection = db['Student']

    data.reset_index(inplace=True)
    data_dict = data.to_dict("records")

    # Insert collection
    collection.insert_many(data_dict)
    
    s.enter(60, 1, loadData, (sc,))

s.enter(60, 1, loadData, (s,))
s.run()
