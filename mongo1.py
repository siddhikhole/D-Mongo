import pymongo

myClient=pymongo.MongoClient("mongodb://localhost:27017/") 
# mongoclient is A NodeJs Module That Lets You Manipulate,Create,Connect To A Mongo Database.

mydb=myClient["mydatab"]
mycol=mydb["urll"]
for x in mycol.find():
 	print(x)
mycol.drop()