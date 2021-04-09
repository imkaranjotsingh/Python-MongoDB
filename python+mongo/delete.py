from pymongo import MongoClient

client = MongoClient('localhost:27017')
db = client.EmployeeData1
def delete():
    
      criteria =int(input('\nEnter employee id to delete\n'))
      db.Employees.delete_many({"id":criteria})
      print('\nDeletion successful\n')
    
delete()    
    
