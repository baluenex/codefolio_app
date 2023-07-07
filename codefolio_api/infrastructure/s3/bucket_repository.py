import sys
import boto3
import json
import os
from ..dynamodb import file_transfer_history_repository


def scan(dir_name):
    s3 = boto3.client("s3")
    response = s3.list_objects_v2(
        Bucket=f"{os.environ['ENV']}.portfolio.codefolio.info",
        Prefix=f"{dir_name}/"
    )
    if "Contents" in response:
        return response["Contents"]
    else:
        return []


def is_bucket_exists(bucket_name):
    try:
        scan(bucket_name)
        bucket_exists = True
    except:
        bucket_exists = False
    
    return bucket_exists


def is_dir_exists(dir_name):
    result = scan(dir_name)
    if result:
        return True
    else:
        return False


def create(bucket_name):
    s3 = boto3.resource("s3")
    s3.create_bucket(
        Bucket=bucket_name, CreateBucketConfiguration={
        'LocationConstraint': 'ap-northeast-1'
    })


def update_bucket_policy(bucket_name):
    s3 = boto3.client("s3")
    bucket_policy = json.dumps({
     'Version': '2012-10-17',
     'Statement': [{
         'Sid': 'AddPerm',
         'Effect': 'Allow',
         'Principal': '*',
         'Action': ['s3:GetObject'],
         'Resource': f"arn:aws:s3:::{bucket_name}/*"
      }]
    })
    s3.put_bucket_policy(Bucket=bucket_name, Policy=bucket_policy)
    s3.put_bucket_website(
        Bucket=bucket_name,
        WebsiteConfiguration={
            'ErrorDocument': {'Key': 'error.html'},
            'IndexDocument': {'Suffix': 'index.html'},
        }
    )


def upsert(username, dir_name, fs):
    s3 = boto3.client("s3")
    file_size = 0
    file_list = []
    
    # 参考記事：https://qiita.com/ykarakita/items/8a9038597353f0615bbc#:~:text=FieldStorage%E3%81%AFPython%E6%A8%99%E6%BA%96%E3%83%A9%E3%82%A4%E3%83%96%E3%83%A9%E3%83%AA%E3%81%AB%E5%90%AB%E3%81%BE%E3%82%8C%E3%82%8B,cgi%20%E3%83%A2%E3%82%B8%E3%83%A5%E3%83%BC%E3%83%AB%E3%81%AE%E3%82%AF%E3%83%A9%E3%82%B9%E3%81%A7%E3%81%99%E3%80%82?msclkid=afbc2b33cec411ec9eedef8980f52c58
    for file in fs.list:
        file_size = file_size + len(file.value)
        file_list.append(file.filename)
        s3.put_object(
            Body=file.value,
            Bucket=f"{os.environ['ENV']}.portfolio.codefolio.info",
            Key=f"{dir_name}/{file.filename}",
            ContentType=file.type
        )
    
    file_transfer_history_repository.insert(username, "POST", file_list, file_size)


def first_upload(dir_name, files):
    s3 = boto3.client("s3")
    for file in files:
        s3.put_object(
            Body=file["body"],
            Bucket=f"{os.environ['ENV']}.portfolio.codefolio.info",
            Key=f"{dir_name}/{file['filename']}",
            ContentType=file["content_type"]
        )


def delete(username, dir_name, files):
    s3 = boto3.client("s3")
    for file in files:
        # index.htmlだけは削除してはいけない。おいおいギャラリーページを実装するときに、参照するため。
        if not file == "index.html":
            s3.delete_object(Bucket=f"{os.environ['ENV']}.portfolio.codefolio.info", Key=f"{dir_name}/{file}")
    
    file_transfer_history_repository.insert(username, "DELETE", files, 0)