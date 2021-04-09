from pymongo import MongoClient

client = MongoClient('localhost:27017')
db = client.EmployeeData1
def update():
   
     criteria = input('\nEnter id to update\n')
     name = input('\nEnter name to update\n')
     age = input('\nEnter age to update\n')
     country = input('\nEnter country to update\n')

     db.Employees.update_one(
        {"name": name},
        {
        "$set": {
           
            "age":age,
            "country":country
        }
        }
    )
     print("\nRecords updated successfully\n")
update()
    
    
