from pymongo import MongoClient

client = MongoClient('localhost:27017')
db = client.EmployeeData1
def read():
    
     empCol = db.Employees.find({},{"_id":0})
     print ('\n All data from EmployeeData Database \n')
     for emp in empCol:
        print (emp)

    
read()
