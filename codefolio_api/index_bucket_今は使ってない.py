import json
from infrastructure.dynamodb import user_repository
from infrastructure.s3 import bucket_repository


# TODO サブドメイン作成はプレミアムプランとしておいおいリリースする
# def create(event, context):
#     body = json.loads(event["body"])
#     username = body["username"]
#     top_domain = body["topDomain"]
#     bucket_name = f"{top_domain}.hachipochi.net"
#     
#     bucketExists = bucket_repository.isBucketExists(bucket_name)
#     if bucketExists:
#         status = "alreadyCreated"
#     else:
#         try:
#             bucket_repository.create(bucket_name)
#             user_repository.update(username, "bucket_name", bucket_name)
#             status = "isSuccess"
#         except:
#             status = "alreadyCreated"
#     
#     return {
#         "statusCode": 200,
#         "headers": {
#             "Access-Control-Allow-Origin" : "*",
#             "Access-Control-Allow-Credentials": True,
#         },
#         "body": json.dumps({"status": status})
#     }


# def set_static_hosting(event, context):
#     top_domain = event['queryStringParameters']['top_domain']
#     bucket_name = f"{top_domain}.hachipochi.net"
#     bucket_repository.update_bucket_policy(bucket_name)
# 
#     files = [
#         {
#             "body": """
#                 Hello World !!
#             """,
#             "file_name": "index.html",
#             "content_type": "text/html"
#         },
#         {
#             "body": """
#                 This is Error ...
#             """,
#             "file_name": "error.html",
#             "content_type": "text/html"
#         }
#     ]
#     bucket_repository.upsert_bucket(bucket_name, files)


# def scan(event, context):
#     username = event['queryStringParameters']['username']
#     user = user_repository.get(username)
#     if user == {}:
#         message = {
#             "status": "no user"
#         }
#     else:
#         bucket_name = user["bucket_name"]
#         files = bucket_repository.scan(bucket_name)
#         # filesは少なくともindex.htmlとerror.htmlがいるので中身はチェックしない
#         message = {"files": files}
#     
#     return {
#         "statusCode": 200,
#         "headers": {
#             "Access-Control-Allow-Origin" : "*",
#             "Access-Control-Allow-Credentials": True,
#         },
#         "body": json.dumps(message)
#     }