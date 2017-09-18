import pymongo
import pprint
import datetime
client = pymongo.MongoClient('mongodb://ykliu:*******@dbtest1-shard-00-00-lhy5s.mongodb.net:27017,dbtest1-shard-00-01-lhy5s.mongodb.net:27017,dbtest1-shard-00-02-lhy5s.mongodb.net:27017/test?ssl=true&replicaSet=dbtest1-shard-0&authSource=admin')


db = client.test_database
collection = db.test_collection

post = {"author": "yk-liu",
       "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo","test"],
        "date": datetime.datetime.utcnow()}
posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)

pprint.pprint(posts.find({"author": "ykliu"}))
pprint.pprint(posts.find_one({"author": "Hancock"}))
pprint.pprint(posts.find_one({"author": "ykliu"}))

posts.delete_many({"author": "ykliu"})
pprint.pprint(posts.find_one({"author": "ykliu"}))

item = db.posts.find({"author":'ykliu'})
for i in item:
    pprint.pprint(i)
result = db.posts.update_many({},{"$set":{"status":'working'}})
pprint.pprint(result.matched_count)
pprint.pprint(result.modified_count)
# db.posts.update({"_id" :ObjectId("4e93037bbf6f1dd3a0a9541a") },{$set : {"new_field":1}})
item = db.posts.find({})
for i in item:
    pprint.pprint(i)

pprint.pprint(db.posts.find_one({"author": "yk-liu"}))
