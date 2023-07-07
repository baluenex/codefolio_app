import boto3
import os
import uuid
import datetime

def insert(username, http_method, files, file_size):
    file_transfer_history_table = boto3.resource("dynamodb").Table(f"{os.environ['ENV']}_codefolio_file_transfer_history")
    file_transfer_history_table.put_item(Item={
        "id": username,
        "uid": str(uuid.uuid4()),
        "method": http_method,
        "file_size": file_size,
        "detail": ",".join(files),
        "created_at": datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    })