from pymongo import MongoClient

client = MongoClient('localhost:27017')
db = client.EmployeeData1
db.Employees.insert_one(
        {
        "id": 1,
            "name":"aaa",
        "age":12,
        "country":"india"
        })
