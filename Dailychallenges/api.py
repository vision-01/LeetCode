import functions_framework
from flask import  jsonify

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus

uname="vellendula"
pwd="Abcd@1234"
encoded_username = quote_plus(uname)
encoded_password = quote_plus(pwd)

uri = "mongodb+srv://{encoded_username}:{encoded_password}@cluster0.lxibh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0".format(encoded_username=encoded_username, encoded_password=encoded_password)
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["MyPortfolio"]
try:
    client.admin.command('ping')
    print("Successfully connected to MongoDB!")
except Exception as e:
    print(e)

@functions_framework.http
def dataHandler(request):
    request_json = request.get_json(silent=True)
    path = request.path
    if path == '/userContactInfo' and request.method == 'POST':
        if request_json:
            return insert_user_contact_info(request_json)
        else:
            return jsonify({"status": "error", "message": "Invalid JSON data"}), 400
    else:
        return jsonify({"status": "error", "message": "Invalid route or method"}), 404

    # if request_json and 'name' in request_json:
    #     name = request_json['name']
    #     try:
    #         collection_name = "UserContactInfo"
    #         db[collection_name].insert_one(request_json)
    #         print("Sucessfully inserted")
    #     except Exception as e:
    #         print(e)
    # elif request_args and 'name' in request_args:
    #     name = request_args['name']
    # else:
    #     name = 'World'
    # return 'Hello {}!'.format(name)

def insert_user_contact_info(request_json):
    try:
        collection_name = "UserContactInfo"
        collection = db[collection_name]
        result = collection.insert_one(request_json)
        return jsonify({"status": "success", "inserted_id": str(result.inserted_id)}), 201
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
