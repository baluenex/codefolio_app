import json
import base64
import io
import cgi
from infrastructure.dynamodb import user_repository
from infrastructure.s3 import bucket_repository
from infrastructure.cognito import user_pool_repository
from domain import directory_name


# http: GET
def exists(event, context):
    dir_name = event['query']['dirName']
    files = bucket_repository.scan(dir_name)
    if not files:
        is_exists = False
    else:
        is_exists = True
    
    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin" : "*",
            "Access-Control-Allow-Credentials": True,
        },
        "body": json.dumps({"isExists": is_exists})
    }


# http: GET
def scan(event, context):
    dir_name = event['query']['dirName']
    if "query" in event:
        dir_name = event['query']['dirName']
    else:
        dir_name = event['queryStringParameters']['dirName']
    files = bucket_repository.scan(dir_name)
    return_files = []
    for file in files:
        return_files.append({
            "Key": file["Key"].replace(f"{dir_name}/", ""),
            "Size": file["Size"],
            "LastModified": file["LastModified"].strftime('%Y-%m-%d %H:%M:%S')
        })

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin" : "*",
            "Access-Control-Allow-Credentials": True,
        },
        "body": json.dumps({"files": return_files})
    }


# http: POST
def create(event, context):
    if "query" in event:
        access_token = event["query"]["cfat"]
    else:
        access_token = event["queryStringParameters"]["cfat"]
    username = user_pool_repository.get(access_token)
    body = event["body"]
    dir_name = body["dirName"]
    is_ok_dir_name = directory_name.validate(dir_name)
    if not is_ok_dir_name:
        message = {"result": "failure"}
    else:
        files = [
            {
                "body": f"""
                    <!DOCTYPE html>
                    <html lang="ja">
                    <head>
                        <meta charset="UTF-8">
                        <meta http-equiv="X-UA-Compatible" content="IE=edge">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <title>My Page</title>
                    </head>
                    <body>
                        <h1>Hello {username}</h1>
                    </body>
                    </html>
                """,
                "filename": "index.html",
                "content_type": "text/html"
            }
        ]
        bucket_repository.first_upload(dir_name, files)
        user_repository.update(username, "dirName", dir_name)
        message = {"result": "success"}

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin" : "*",
            "Access-Control-Allow-Credentials": True,
        },
        "body": json.dumps(message)
    }


# http: POST
def upsert(event, context):
    if "query" in event:
        access_token = event["query"]["cfat"]
    else:
        access_token = event["queryStringParameters"]["cfat"]
    username = user_pool_repository.get(access_token)
    user = user_repository.get(username)
    directory_name = user["dirName"]

    body = base64.b64decode(event['body'])
    fp = io.BytesIO(body)
    
    environ = {'REQUEST_METHOD': 'POST'}
    headers = {
        'content-type': event['headers']['content-type'], 
        'content-length': len(body)
    }

    fs = cgi.FieldStorage(fp=fp, environ=environ, headers=headers)
    bucket_repository.upsert(username, directory_name, fs)
    
    return {
        'statusCode': 200,
        "headers": {
            "Access-Control-Allow-Origin" : "*",
            "Access-Control-Allow-Credentials": True,
        },
        'body': json.dumps('アップロード完了')
    }


# http: DELETE
def delete(event, context):
    if "query" in event:
        access_token = event["query"]["cfat"]
    else:
        access_token = event["queryStringParameters"]["cfat"]
    username = user_pool_repository.get(access_token)
    user = user_repository.get(username)
    directory_name = user["dirName"]

    # TODO filesの中身はbodyに入っているので取得方法を確認する
    body = json.loads(event["body"])
    files = body["files"]
    bucket_repository.delete(username, directory_name, files)
    
    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin" : "*",
            "Access-Control-Allow-Credentials": True,
        },
        "body": json.dumps("success")
    }


if __name__ == '__main__':
    event = {
        "body": json.dumps({
            "dirName": "hachipochi"
        })
    }
    context = {}
    create(event, context)