import pymongo


client = pymongo.MongoClient("mongodb+srv://SRIPAD-MONGODB:Sripad1992@sripadpc.2w74vlu.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

# To dump a record, We need to create a dictionary

d = {
    "name":"sripad",
    "email":"sripad.kulkarni@gmail.com",
    "surname":"Kulkarni"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)