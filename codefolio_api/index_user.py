from infrastructure.dynamodb import user_repository
from infrastructure.cognito import user_pool_repository
import json


# http: GET
def get(event, context):
    if "query" in event:
        access_token = event["query"]["cfat"]
    else:
        access_token = event["queryStringParameters"]["cfat"]
    username = user_pool_repository.get(access_token)
    user = user_repository.get(username)
    if user == {}:
        messageBody = {
            "user": "error"
        }
    else:
        # check directory
        if "dirName" not in user:
            user["isDirectoryRegistered"] = False
        else:
            user["isDirectoryRegistered"] = True
        # check payjp
        if "payjpToken" not in user:
            user["isPayjpRegistered"] = False
        else:
            user["isPayjpRegistered"] = True
            del user["payjpToken"]
        
        messageBody = {
            "user": user
        }
    
    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin" : "*",
            "Access-Control-Allow-Credentials": True,
        },
        "body": json.dumps(messageBody)
    }


# http: POST
# 初回作成のためaccess_tokenは存在しない
def create(event, context):
    body = json.loads(event["body"])
    username = body["username"]
    email = body["email"]
    user_repository.create(username, email)
    
    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin" : "*",
            "Access-Control-Allow-Credentials": True,
        },
        "body": json.dumps({"status": "success"})
    }


# http: POST
def register_payjp(event, context):
    if "query" in event:
        access_token = event["query"]["cfat"]
    else:
        access_token = event["queryStringParameters"]["cfat"]
    username = user_pool_repository.get(access_token)
    body = event["body"]
    payjp_token = body["token"]
    user_repository.update(username, "payjpToken", payjp_token)

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin" : "*",
            "Access-Control-Allow-Credentials": True
        },
        "body": json.dumps({"status": "success"})
    }